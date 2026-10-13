#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [ ! -f .env ]; then cp .env.example .env; fi
docker compose up -d
echo "CTFd:  http://localhost:8080"
echo "SV-01: http://localhost:8080/osint/"
