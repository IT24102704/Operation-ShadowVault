\# SV-04 - Ghost Traffic



\## Domain

Networking / Digital Forensics



\## Difficulty

Moderate



\## Challenge File

`ghost\_traffic.pcap`



\## Scenario

Asteria Dynamics captured suspicious internal network traffic during the ShadowVault investigation.



The participant must analyze the packet capture, identify the important internal host, and recover transferred evidence hidden inside HTTP traffic.



\## Player Task

Analyze the PCAP and recover:



\- the Stage 4 flag

\- VaultDesk username

\- VaultDesk password



These credentials are required for Stage 5.



\## Important Indicator

`archive-gw.asteria.local`



This hostname is provided by the previous stage and helps the player focus on the relevant traffic.



\## Intended Investigation Path

1\. Open `ghost\_traffic.pcap` in Wireshark or an equivalent packet-analysis tool.

2\. Review DNS traffic and locate `archive-gw.asteria.local`.

3\. Identify the server IP associated with the hostname.

4\. Inspect HTTP traffic involving that server.

5\. Locate the request for `/archive/shadowvault-transfer.txt`.

6\. Inspect the HTTP response.

7\. Notice the `X-Archive-Encoding: base64` header.

8\. Decode the Base64 body.

9\. Recover the Stage 4 flag and VaultDesk credentials.



\## Background Traffic

The capture contains synthetic DNS, HTTP, and ICMP traffic to make the analysis more realistic.



The intended evidence traffic is mixed with harmless internal activity.



\## Validation

CTFd validates the Stage 4 flag using exact-match validation.



A local verification script is included:



`verify\_pcap.py`



\## Reset / Recovery

This is a static PCAP challenge.



If the file is modified, regenerate it using:



`build\_pcap.py`



\## Notes

All hosts, traffic, credentials, and evidence are synthetic and exist only for the Operation ShadowVault CTF lab.

