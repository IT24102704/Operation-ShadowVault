# Operation ShadowVault

Operation ShadowVault is a local, isolated Capture The Flag (CTF) play box developed for the IE3132 Penetration Testing assignment.

The platform contains six connected challenge stages covering multiple cybersecurity domains. Each stage provides information required to progress to the next stage.

## Challenge Structure

1. **SV-01 - Open Source Footprints**
   - Domain: OSINT
   - Difficulty: Easy
   - Flag: `SHADOW{mhale_shadowvault}`

2. **SV-02 - Pixel Whisper**
   - Domain: Steganography
   - Difficulty: Easy
   - Flag: `SHADOW{pixels_hide_secrets}`

3. **SV-03 - Cipher Relay**
   - Domain: Cryptography
   - Difficulty: Moderate
   - Flag: `SHADOW{relay_layers_unlocked}`

4. **SV-04 - Ghost Traffic**
   - Domain: Network / Digital Forensics
   - Difficulty: Moderate
   - Flag: `SHADOW{ghost_traffic_found}`

5. **SV-05 - VaultDesk Breach**
   - Domain: Web Security
   - Difficulty: Moderate-Hard
   - Flag: `SHADOW{vaultdesk_access_control_broken}`

6. **SV-06 - Root of the Shadow**
   - Domain: Linux / System Security
   - Difficulty: Hard
   - Flag: `SHADOW{root_of_the_shadow}`

## Platform Components

The environment uses Docker Compose and includes:

- CTFd
- MariaDB
- Redis
- Nginx reverse proxy
- VaultDesk Flask application
- Linux SSH challenge container
- SSH gateway
- Separate control, backend, and challenge Docker networks

## Player Entry Points

### CTF Portal
`http://localhost:8080`

### Stage 1 OSINT Site
`http://localhost:8080/osint/`

### VaultDesk
`http://localhost:8080/vaultdesk/`

### Stage 6 SSH
Host: `localhost`

Port: `2222`

## Docker Network Design

The platform uses three Docker networks:

### control
Used by externally reachable services such as CTFd, Nginx, VaultDesk, and the SSH gateway.

### backend
Internal-only network used by CTFd, MariaDB, and Redis.

### challenge
Internal-only network used by challenge services including VaultDesk and the Stage 6 Linux container.

The Stage 6 container is not directly exposed to the host. SSH access is provided through a dedicated gateway container that forwards host port `2222` to the internal Linux challenge service.

## Windows 11 Quick Start

Open PowerShell in the project directory.

Start the environment:

```powershell
docker compose up -d