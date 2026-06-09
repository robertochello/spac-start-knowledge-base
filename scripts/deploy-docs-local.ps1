param(
    [switch]$SkipInstall
)

$ErrorActionPreference = "Stop"

Write-Host "== SPAC Start Knowledge Base - deploy manuale MkDocs ==" -ForegroundColor Cyan

if (-not (Test-Path "mkdocs.yml")) {
    throw "Eseguire lo script dalla root della repository. File mkdocs.yml non trovato."
}

if (-not $SkipInstall) {
    Write-Host "Installazione dipendenze..." -ForegroundColor Yellow
    python -m pip install -r requirements.txt
}

Write-Host "Build documentazione..." -ForegroundColor Yellow
mkdocs build

Write-Host "Deploy su branch gh-pages..." -ForegroundColor Yellow
mkdocs gh-deploy --force --no-history

Write-Host "Deploy completato." -ForegroundColor Green
Write-Host "Verificare: https://robertochello.github.io/spac-start-knowledge-base/" -ForegroundColor Green
