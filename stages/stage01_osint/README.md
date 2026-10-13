\# Stage 01 - Open Source Footprints



\## Challenge ID

SV-01



\## Domain

OSINT / Open Source Intelligence



\## Difficulty

Easy



\## Scenario

Players investigate the public-facing Asteria Dynamics website to identify information connected to the ShadowVault research project.



The synthetic website contains staff information and historical archive records. Players must correlate publicly available details to identify the correct project owner alias and codename.



\## Player Objective

Discover the flag by reviewing the Asteria Dynamics public website.



\## Intended Investigation Path

1\. Open the Asteria Dynamics website.

2\. Review the Staff Directory.

3\. Identify Marcus Hale and his internal alias.

4\. Review the News Archive.

5\. Identify the ShadowVault project codename.

6\. Combine the discovered information to determine the challenge flag.



\## Important Evidence

\- Employee: Marcus Hale

\- Internal alias: `mhale`

\- Project codename: `ShadowVault`

\- Evidence package reference: `office\_photo.png`



\## Flag

`SHADOW{mhale\_shadowvault}`



\## Player Entry Point

`http://localhost:8080/osint/`



\## Challenge Assets

The public OSINT website is stored in:



`site/`



Main pages:

\- `index.html`

\- `staff.html`

\- `archive.html`



\## Isolation

All company names, employees, projects, and records used in this challenge are fictional and created specifically for the Operation ShadowVault training environment.

