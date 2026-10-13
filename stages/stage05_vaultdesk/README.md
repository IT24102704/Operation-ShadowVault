\# Stage 05 - VaultDesk Breach



\## Challenge ID

SV-05



\## Domain

Web Technologies / Web Security



\## Difficulty

Moderate-Hard



\## Scenario

Players access the internal Asteria Dynamics VaultDesk incident-response portal using credentials recovered from Stage 4.



The portal correctly requires authentication, but the application contains an intentional insecure direct object reference (IDOR) / broken object-level authorization flaw.



Authenticated users can manually request incident records that are not assigned to their account.



\## Player Objective

Authenticate to VaultDesk, identify the access-control weakness, access the restricted ShadowVault incident record, and recover the Stage 5 flag together with the Stage 6 SSH connection details.



\## Credentials

Recovered from Stage 4:



\- Username: `analyst`

\- Password: `vaultdesk2026`



\## Player Entry Point

`http://localhost:8080/vaultdesk/`



\## Intended Investigation Path

1\. Log in using the Stage 4 credentials.

2\. Review the analyst dashboard.

3\. Observe the visible incident record identifiers.

4\. Notice that incident records are accessed using numeric IDs.

5\. Manually change the incident ID in the URL.

6\. Access the restricted incident record.

7\. Recover the Stage 5 flag and Stage 6 SSH connection information.



\## Intended Vulnerability

The route:



`/vaultdesk/incident/<incident\_id>`



checks whether the user is authenticated, but does not verify whether the requested incident belongs to the authenticated user.



This intentionally creates an IDOR / broken authorization condition for the CTF.



\## Restricted Record

Incident ID:



`900`



\## Flag

`SHADOW{vaultdesk\_access\_control\_broken}`



\## Stage 6 Connection Details

\- Host: `localhost`

\- Port: `2222`

\- Username: `investigator`

\- Password: `nightwatch2026`



\## Challenge Application

The VaultDesk Flask application is implemented in:



`app.py`



\## Containerization

The application is packaged using:



\- `Dockerfile`

\- `requirements.txt`



The service runs internally on port `5000` and is exposed to players through the Nginx reverse proxy at `/vaultdesk/`.



\## Isolation

VaultDesk uses only synthetic users, incidents, credentials, and investigation records created specifically for Operation ShadowVault.



The application is isolated inside the Docker challenge environment.

