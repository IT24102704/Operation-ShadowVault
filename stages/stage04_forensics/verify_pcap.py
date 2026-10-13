from scapy.all import rdpcap, Raw
from pathlib import Path
import base64
import re

PCAP_FILE = Path(__file__).with_name("ghost_traffic.pcap")

pcap = rdpcap(str(PCAP_FILE))

print("Packets:", len(pcap))

for packet in pcap:
    if packet.haslayer(Raw):
        data = bytes(packet[Raw].load).decode("latin1", errors="ignore")

        if "archive-gw.asteria.local" in data or "X-Archive-Encoding: base64" in data:
            print("\n--- Relevant Traffic ---")
            print(data)

            match = re.search(r"\r\n\r\n([A-Za-z0-9+/=]+)$", data)

            if match:
                decoded = base64.b64decode(match.group(1)).decode()
                print("\n--- Decoded Evidence ---")
                print(decoded)