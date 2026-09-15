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

Comandi ricorrenti:

```text
SP_XML_MENU
_DSETTINGS
ATTDEF
EDITATT
PROPRIETA
CORRISPROP
MBLOCCO
_MSLIDE
SPINSMOR
DEL_NUMF
IMMAGINI
IMAGEFRAME
PURGE
QSELECT
BEDIT
```

## Struttura

- `docs/command-reference.md` — cheat sheet comandi/click;
- `docs/00-how-to-use.md` — indice per attività;
- `docs/17-unifilare.md` — unifilare;
- `docs/09-multifilare.md` — multifilare;
- `docs/06-cross-references-terminals.md` — rimandi, cross-reference, morsetti;
- `docs/03-custom-symbols.md` — panoramica simboli;
- `docs/playbooks/` — procedure passo-passo;
- `docs/known-issues/` — problemi ricorrenti;
- `docs/standards/` — standard stabili.

Il sito è configurato in `mkdocs.yml`.

## Validazione

```bash
pip install -r requirements.txt
mkdocs build --strict
npx --yes markdownlint-cli2
yamllint mkdocs.yml .github/workflows
```

## Pubblicazione

```text
push su master → validazione → deploy GitHub Pages
```

Non modificare manualmente `gh-pages`.

## Versione documentale

Ultima revisione strutturale: **0.7.0 — Procedure fidelity pass**.

## Ownership

Roberto Chello
