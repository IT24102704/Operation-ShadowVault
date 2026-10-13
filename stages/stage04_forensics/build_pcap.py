from scapy.all import *
import base64
from pathlib import Path

OUTPUT = Path(__file__).with_name("ghost_traffic.pcap")

CLIENT = "10.20.0.25"
DNS_SERVER = "10.20.0.53"
ARCHIVE_SERVER = "10.20.0.80"

HOSTNAME = "archive-gw.asteria.local"

evidence = """ASTERIA DYNAMICS - ARCHIVE TRANSFER

FLAG: SHADOW{ghost_traffic_found}

VAULTDESK_USER: analyst
VAULTDESK_PASS: vaultdesk2026
"""

encoded_evidence = base64.b64encode(evidence.encode()).decode()

packets = []


def add_dns_query(src, sport, dns_id, hostname):
    packets.append(
        IP(src=src, dst=DNS_SERVER) /
        UDP(sport=sport, dport=53) /
        DNS(
            id=dns_id,
            rd=1,
            qd=DNSQR(qname=hostname)
        )
    )


def add_dns_response(dst, dport, dns_id, hostname, ip):
    packets.append(
        IP(src=DNS_SERVER, dst=dst) /
        UDP(sport=53, dport=dport) /
        DNS(
            id=dns_id,
            qr=1,
            aa=1,
            qd=DNSQR(qname=hostname),
            an=DNSRR(
                rrname=hostname,
                type="A",
                ttl=300,
                rdata=ip
            )
        )
    )


def add_http_request(src, dst, sport, host, path, user_agent):
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: {user_agent}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    packets.append(
        IP(src=src, dst=dst) /
        TCP(sport=sport, dport=80, flags="PA", seq=1, ack=1) /
        Raw(load=request)
    )


def add_http_response(src, dst, dport, body):
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
        f"{body}"
    )

    packets.append(
        IP(src=src, dst=dst) /
        TCP(sport=80, dport=dport, flags="PA", seq=1, ack=1) /
        Raw(load=response)
    )


# -------------------------------------------------
# Background DNS traffic
# -------------------------------------------------

background_dns = [
    ("10.20.0.21", 53101, 201, "intranet.asteria.local", "10.20.0.70"),
    ("10.20.0.22", 53102, 202, "updates.asteria.local", "10.20.0.71"),
    ("10.20.0.23", 53103, 203, "mail.asteria.local", "10.20.0.72"),
    ("10.20.0.24", 53104, 204, "files.asteria.local", "10.20.0.73"),
    ("10.20.0.30", 53105, 205, "helpdesk.asteria.local", "10.20.0.74"),
    ("10.20.0.31", 53106, 206, "monitor.asteria.local", "10.20.0.75"),
    ("10.20.0.32", 53107, 207, "backup.asteria.local", "10.20.0.76"),
    ("10.20.0.33", 53108, 208, "wiki.asteria.local", "10.20.0.77"),
]

for src, sport, dns_id, hostname, result_ip in background_dns:
    add_dns_query(src, sport, dns_id, hostname)
    add_dns_response(src, sport, dns_id, hostname, result_ip)


# -------------------------------------------------
# Relevant DNS traffic
# -------------------------------------------------

add_dns_query(
    CLIENT,
    53002,
    301,
    HOSTNAME
)

add_dns_response(
    CLIENT,
    53002,
    301,
    HOSTNAME,
    ARCHIVE_SERVER
)


# -------------------------------------------------
# More background traffic
# -------------------------------------------------

add_http_request(
    "10.20.0.30",
    "10.20.0.70",
    41000,
    "intranet.asteria.local",
    "/status",
    "AsteriaMonitor/1.0"
)

add_http_response(
    "10.20.0.70",
    "10.20.0.30",
    41000,
    "SYSTEM STATUS: OK"
)

add_http_request(
    "10.20.0.22",
    "10.20.0.71",
    41001,
    "updates.asteria.local",
    "/packages/check",
    "AsteriaUpdater/3.2"
)

add_http_response(
    "10.20.0.71",
    "10.20.0.22",
    41001,
    "NO UPDATES AVAILABLE"
)

add_http_request(
    "10.20.0.23",
    "10.20.0.74",
    41002,
    "helpdesk.asteria.local",
    "/tickets/open",
    "AsteriaHelpdesk/2.0"
)

add_http_response(
    "10.20.0.74",
    "10.20.0.23",
    41002,
    "OPEN TICKETS: 4"
)

add_http_request(
    "10.20.0.31",
    "10.20.0.75",
    41003,
    "monitor.asteria.local",
    "/health",
    "AsteriaHealth/1.4"
)

add_http_response(
    "10.20.0.75",
    "10.20.0.31",
    41003,
    "CPU=18%;MEMORY=42%;STATUS=HEALTHY"
)


# -------------------------------------------------
# Relevant ShadowVault HTTP request
# -------------------------------------------------

http_request = (
    "GET /archive/shadowvault-transfer.txt HTTP/1.1\r\n"
    f"Host: {HOSTNAME}\r\n"
    "User-Agent: AsteriaArchiveClient/2.1\r\n"
    "Connection: close\r\n"
    "\r\n"
)

packets.append(
    IP(src=CLIENT, dst=ARCHIVE_SERVER) /
    TCP(sport=42000, dport=80, flags="PA", seq=1, ack=1) /
    Raw(load=http_request)
)


# -------------------------------------------------
# Relevant HTTP response containing evidence
# -------------------------------------------------

http_response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    f"Content-Length: {len(encoded_evidence)}\r\n"
    "X-Archive-Encoding: base64\r\n"
    "Server: AsteriaArchive/2.1\r\n"
    "\r\n"
    f"{encoded_evidence}"
)

packets.append(
    IP(src=ARCHIVE_SERVER, dst=CLIENT) /
    TCP(sport=80, dport=42000, flags="PA", seq=1, ack=1) /
    Raw(load=http_response)
)


# -------------------------------------------------
# Extra harmless traffic after the evidence
# -------------------------------------------------

for i in range(5):
    packets.append(
        IP(src=f"10.20.0.{40 + i}", dst="10.20.0.1") /
        ICMP(type=8, id=400 + i, seq=1) /
        Raw(load=f"Asteria diagnostic ping {i + 1}")
    )

    packets.append(
        IP(src="10.20.0.1", dst=f"10.20.0.{40 + i}") /
        ICMP(type=0, id=400 + i, seq=1) /
        Raw(load=f"Asteria diagnostic reply {i + 1}")
    )


# Give packets realistic sequential timestamps
base_time = 1789300000.0

for index, packet in enumerate(packets):
    packet.time = base_time + (index * 0.35)


wrpcap(str(OUTPUT), packets)

print("Done!")
print(f"Created: {OUTPUT}")
print(f"Stage 4 indicator: {HOSTNAME}")
print(f"Packets written: {len(packets)}")