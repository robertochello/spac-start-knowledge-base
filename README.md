# SPAC Start Knowledge Base

Knowledge base operativa per **SPAC Start 26 / SPAC Start Impianti**.

Il contenuto è pensato per il lavoro reale: setup progetto, schemi unifilari e multifilari, simboli custom, attributi e pinatura, materiali, cavi, rimandi, morsetti e troubleshooting.

> **Il modo consigliato per consultare la repository è il sito GitHub Pages:**
> [Apri SPAC Start Knowledge Base](https://robertochello.github.io/spac-start-knowledge-base/)

## Da dove partire

Non è necessario leggere tutta la documentazione in ordine.

| Se devi... | Apri |
|---|---|
| capire dove trovare una procedura | [Guida pratica](https://robertochello.github.io/spac-start-knowledge-base/00-how-to-use/) |
| iniziare un lavoro o configurare SPAC | [Lavoro in SPAC](https://robertochello.github.io/spac-start-knowledge-base/15-custom-library/) |
| risolvere un problema | [Problemi e diagnosi](https://robertochello.github.io/spac-start-knowledge-base/07-troubleshooting/) |
| scaricare archivi pubblicati | [Download](https://robertochello.github.io/spac-start-knowledge-base/downloads/) |
| consultare tutto il materiale in una sola pagina | [Manuale completo](https://robertochello.github.io/spac-start-knowledge-base/guida-operativa-completa/) |

Il **Manuale completo** è una pagina di consultazione estesa: non è il punto di ingresso consigliato per il sito.

## Come è organizzata

La documentazione pubblicata è divisa per utilizzo:

- **Guida pratica**: orientamento, concetti, FAQ e manuale completo;
- **Lavoro in SPAC**: setup, schemi, simboli e archivi;
- **Procedure**: playbook passo-passo e checklist;
- **Problemi e diagnosi**: troubleshooting, known issue e casi pratici;
- **Riferimenti**: standard, decisioni, quality gate e manutenzione della knowledge base.

La fonte dei contenuti pubblicati è la cartella `docs/`; la navigazione del sito è definita in `mkdocs.yml`.

## Aree tecniche principali

| Area | Riferimento principale |
|---|---|
| Libreria custom `_CUSTOM` | `docs/15-custom-library.md` |
| Template progetto | `docs/16-project-template.md` |
| Schema unifilare | `docs/17-unifilare.md` |
| Schema multifilare | `docs/09-multifilare.md` |
| Rimandi e morsetti | `docs/06-cross-references-terminals.md` |
| Simboli custom | `docs/03-custom-symbols.md` |
| Attributi e pinatura | `docs/04-attributes-and-pinning.md` |
| Archivi materiali | `docs/21-material-archives.md` |
| Archivio cavi `DbCables.db` | `docs/25-cable-archive-dbcables.md` |
| Download pubblici | `docs/downloads.md` |
| Troubleshooting | `docs/07-troubleshooting.md` |

## Regole della knowledge base

- Documentare procedure realmente verificate o marcare chiaramente ciò che è **Da verificare**.
- Non inventare comandi, menu o comportamenti SPAC.
- Separare oggetti CAD grafici e oggetti intelligenti SPAC.
- Mantenere distinti unifilare e multifilare quando il comportamento cambia.
- Non pubblicare dati cliente, commessa, credenziali o file riservati.
- Preferire procedure, checklist e tabelle a testo generico.

## Sviluppo e preview locale

Installazione dipendenze:

```bash
pip install -r requirements.txt
```

Preview:

```bash
mkdocs serve
```

Verifica prima del push:

```bash
mkdocs build --strict
```

## Pubblicazione

Il sito usa **MkDocs Material** e viene pubblicato automaticamente tramite GitHub Actions.

```text
push su master -> mkdocs build --strict -> deploy GitHub Pages
```

Non modificare manualmente il contenuto generato nel branch `gh-pages`.

## Ownership

Roberto Chello
