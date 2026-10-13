$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
if (-not (Test-Path ".env")) {
  Copy-Item ".env.example" ".env"
  Write-Host "Created .env from .env.example. Change the development secrets before a shared demo." -ForegroundColor Yellow
}
Write-Host "Starting Operation ShadowVault control plane..."
docker compose up -d
Write-Host ""
Write-Host "CTFd:   http://localhost:8080" -ForegroundColor Green
Write-Host "SV-01:  http://localhost:8080/osint/" -ForegroundColor Green
Write-Host "First run: open CTFd and complete its administrator setup page."
