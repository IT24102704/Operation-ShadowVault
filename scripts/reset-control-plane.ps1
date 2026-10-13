$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
Write-Host "WARNING: this deletes CTFd/database data for the LOCAL ShadowVault lab." -ForegroundColor Yellow
$confirm = Read-Host "Type RESET to continue"
if ($confirm -ne "RESET") { Write-Host "Cancelled."; exit 0 }
docker compose down -v
docker compose up -d
Write-Host "Local control plane reset complete." -ForegroundColor Green
