#!/usr/bin/env bash
set -euo pipefail

echo "== SPAC Start Knowledge Base - deploy manuale MkDocs =="

if [ ! -f "mkdocs.yml" ]; then
  echo "Eseguire lo script dalla root della repository. File mkdocs.yml non trovato." >&2
  exit 1
fi

python -m pip install -r requirements.txt
mkdocs build
mkdocs gh-deploy --force --no-history

echo "Deploy completato."
echo "Verificare: https://robertochello.github.io/spac-start-knowledge-base/"
