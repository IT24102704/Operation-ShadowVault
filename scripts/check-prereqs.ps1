$ErrorActionPreference = "Stop"
Write-Host "[ShadowVault] Checking Docker..."
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
  Write-Host "Docker command was not found." -ForegroundColor Red
  Write-Host "Install Docker Desktop and enable WSL 2 integration, then reopen the terminal."
  exit 1
}
docker --version
docker compose version
Write-Host "[OK] Docker and Docker Compose are available." -ForegroundColor Green
