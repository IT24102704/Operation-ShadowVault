# Operation ShadowVault - Implementation Plan

This build follows the approved report design:

1. **Foundation / control plane** - Docker Compose, CTFd, MariaDB, Redis, Nginx, isolated networks.
2. **SV-01 Open Source Footprints** - synthetic Asteria Dynamics website, staff directory, archived announcement, first flag and Stage 2 filename clue.
3. **SV-02 Pixel Whisper** - generated PNG with metadata/trailing hidden payload, Stage 2 flag, Stage 3 keyword.
4. **SV-03 Cipher Relay** - deterministic layered encoding + classical cipher, Stage 3 flag, Stage 4 hostname indicator.
5. **SV-04 Ghost Traffic** - synthetic PCAP and reconstructed artefact, Stage 4 flag, VaultDesk low-privilege credentials.
6. **SV-05 VaultDesk Breach** - isolated Flask app with deliberately vulnerable object-level authorization, Stage 5 flag and final SSH clue.
7. **SV-06 Root of the Shadow** - disposable Linux/SSH target with a deliberately engineered local privilege-boundary challenge and final flag.
8. **CTFd integration** - challenge descriptions, flags, attachments, dependencies, scoring and hints.
9. **Testing and reset automation** - health checks, checksums, intended-solution tests, negative tests, isolation checks and reset scripts.
10. **Submission evidence** - screenshots, test records, Git history/contribution evidence, updated report and viva notes.

## Safety boundary

All vulnerable components are for this local CTF only. Do not expose the lab to the public Internet. Use only the synthetic assets created in this repository.
