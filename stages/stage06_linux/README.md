\# Stage 06 - Root of the Shadow



\## Challenge ID

SV-06



\## Domain

Linux / System Security



\## Difficulty

Hard



\## Scenario

Players connect to a dedicated Linux challenge container using SSH credentials recovered from Stage 5.



The user account has limited privileges, but it is allowed to run a privileged maintenance wrapper through `sudo`.



The wrapper executes a helper program using a PATH configuration that includes a user-controlled directory before trusted system paths.



This intentionally creates a controlled privilege-escalation opportunity for the CTF.



\## Player Objective

Enumerate the Linux environment, identify the unsafe privileged maintenance configuration, and use it to access the final protected ShadowVault evidence.



\## SSH Connection

\- Host: `localhost`

\- Port: `2222`

\- Username: `investigator`

\- Password: `nightwatch2026`



\## Intended Investigation Path

1\. Connect to the Linux challenge environment using SSH.

2\. Enumerate the current user and available permissions.

3\. Run `sudo -l`.

4\. Identify that the user can execute `/usr/local/sbin/shadow-maintenance` as root without a password.

5\. Inspect the maintenance wrapper.

6\. Notice that `/home/investigator/bin` appears before trusted system directories in the wrapper PATH.

7\. Create a controlled replacement for the expected `backup-helper`.

8\. Run the maintenance wrapper with `sudo`.

9\. Use the privileged helper execution to copy the protected final evidence to a readable location.

10\. Read the final flag.



\## Privileged Maintenance Wrapper

`/usr/local/sbin/shadow-maintenance`



\## Protected Evidence

`/opt/shadowvault/evidence/final\_flag.txt`



The protected evidence file is owned by root and configured with restricted permissions.



\## Final Flag

`SHADOW{root\_of\_the\_shadow}`



\## Synthetic Logs

The challenge environment includes synthetic operational logs in:



`/var/log/shadowvault/maintenance.log`



These records support the investigation scenario and contain no real system data.



\## Container Components

\- `Dockerfile`

\- `entrypoint.sh`

\- `maintenance.sh`



\## Flag Injection

The final flag is injected into the container at startup through the environment variable:



`SHADOWVAULT\_FINAL\_FLAG`



The entrypoint writes the value to the protected evidence file and applies root-only permissions.



\## Isolation

The Linux challenge runs inside a dedicated Docker container connected only to the internal challenge network.



External SSH access is provided through a separate controlled SSH gateway on host port `2222`.



The environment contains only synthetic users, credentials, logs, and evidence created for Operation ShadowVault.



The intended goal is controlled evidence access inside the isolated CTF environment, not persistence or activity outside the challenge container.

