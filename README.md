# SPAC Start Knowledge Base

Knowledge base operativa per **SPAC Start 26 / SPAC Start Impianti**.

> Consulta il sito: [SPAC Start Knowledge Base](https://robertochello.github.io/spac-start-knowledge-base/)

## Da dove partire

| Se devi... | Apri |
|---|---|
| sapere **esattamente cosa digitare/cliccare** | [Comandi e click esatti](https://robertochello.github.io/spac-start-knowledge-base/command-reference/) |
| preparare un progetto | [Template progetto](https://robertochello.github.io/spac-start-knowledge-base/16-project-template/) |
| lavorare in unifilare | [Schema unifilare](https://robertochello.github.io/spac-start-knowledge-base/17-unifilare/) |
| lavorare in multifilare | [Schema multifilare](https://robertochello.github.io/spac-start-knowledge-base/09-multifilare/) |
| creare un simbolo | [Playbook simbolo custom](https://robertochello.github.io/spac-start-knowledge-base/playbooks/create-custom-symbol/) |
| scaricare archivi materiali/cavi | [Download](https://robertochello.github.io/spac-start-knowledge-base/downloads/) |
| partire da un problema | [Troubleshooting](https://robertochello.github.io/spac-start-knowledge-base/07-troubleshooting/) |

## Standard della documentazione

Una procedura SPAC deve essere scritta, quando le informazioni sono note, nel formato:

```text
Dove cliccare / cosa digitare
→ cosa impostare
→ risultato atteso
→ cosa verificare se non funziona
```

Non usare descrizioni generiche se il nome reale del comando o del pulsante è già noto.

Se un click non è stato ancora verificato direttamente in SPAC Start 26, indicare **Da verificare** nel punto preciso.

## Download pubblici

Le aree pubbliche sono:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

Attualmente la sezione materiali contiene:

```text
ABB_Materials.db
archivio-materiali-custom-r01.db
```

La cartella cavi è predisposta per un futuro archivio `DbCables.db` sanitizzato e versionato.

Prima del deploy il workflow esegue:

```bash
python scripts/audit_public_content.py
```

L'audit controlla file testuali e database SQLite per pattern sensibili e calcola SHA256 degli archivi pubblici.

## Privacy e pubblicazione

Non pubblicare nella repository:

- nomi cliente o dati di commessa;
- codici ordine/elaborato reali;
- email o credenziali;
- IP/MAC reali di impianti;
- percorsi personali `C:\Users\...`;
- screenshot o file con dati identificativi;
- database non sanitizzati;
- file vendor senza diritto di redistribuzione.

Gli esempi della knowledge base devono restare generici.

## Esempi consolidati

```text
UNIFILARE → Disegno Unifilare

Modifica/Inserisci → Riferimento DWG
→ Tipo di percorso: Percorso completo
→ OK

Numerazione fili → Lista numeri usati
→ Vedi solo i Rimandi
→ Scansiona i Multifogli

UTIL → Cross Reference
→ Rimandi
→ Cross
→ Ok - Aggiorna

Inser Morsetti / SPINSMOR
→ morsettiera
→ tipo morsetto
→ Anteprima
→ Ok - Nuovo
→ clic filo
→ Invio

MBLOCCO
→ Origine: Oggetti
→ punto base
→ Destinazione: Nome e percorso del file
→ Unità inser.: Senza unità
```

## Struttura

- `docs/command-reference.md` — cheat sheet comandi/click;
- `docs/downloads.md` — archivi pubblici;
- `docs/17-unifilare.md` — unifilare;
- `docs/09-multifilare.md` — multifilare;
- `docs/06-cross-references-terminals.md` — rimandi, cross-reference, morsetti;
- `docs/playbooks/` — procedure passo-passo;
- `docs/known-issues/` — problemi ricorrenti;
- `docs/standards/` — standard stabili;
- `scripts/audit_public_content.py` — audit privacy/pubblicazione.

## Validazione

```bash
pip install -r requirements.txt
python scripts/audit_public_content.py
mkdocs build --strict
npx --yes markdownlint-cli2
yamllint mkdocs.yml .github/workflows
```

## Pubblicazione

```text
push su master → audit privacy → build MkDocs → deploy GitHub Pages
```

Non modificare manualmente `gh-pages`.

## Versione documentale

Ultima revisione strutturale: **0.8.0 — Public downloads & visual refresh**.
