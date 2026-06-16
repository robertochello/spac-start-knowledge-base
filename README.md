# SPAC Start Knowledge Base

Guida operativa tecnica per **SPAC Start 26**: libreria custom, template progetto, schemi unifilari e multifilari, simboli, attributi, pinatura, materiali, cavi e troubleshooting.

La repository è pensata per essere pubblicata come sito documentale su **GitHub Pages** tramite MkDocs Material.

## Scopo

Raccogliere procedure pratiche e standard riutilizzabili per:

- installare e mantenere la libreria custom `_CUSTOM`;
- preparare progetti SPAC con pagine standard e cartigli;
- gestire schema unifilare, multifilare, rimandi e morsetti;
- creare simboli grafici e simboli intelligenti SPAC;
- mantenere nomenclatura, abbreviazioni e inventario simboli;
- documentare problemi ricorrenti, decisioni operative e quality gate.

## Struttura sito

| Area | Contenuto |
|---|---|
| `docs/index.md` | Home della guida pubblicata |
| `docs/README.md` | Guida operativa completa SPAC Start 26 |
| `docs/00-how-to-use.md` | Percorsi di lettura |
| `docs/15-custom-library.md` | Libreria custom `_CUSTOM` |
| `docs/16-project-template.md` | Template progetto e pagine standard |
| `docs/17-unifilare.md` | Schema unifilare |
| `docs/09-multifilare.md` | Base operativa multifilare |
| `docs/06-cross-references-terminals.md` | Rimandi, cross-reference e morsetti |
| `docs/03-custom-symbols.md` | Creazione simboli custom |
| `docs/04-attributes-and-pinning.md` | Attributi, `PRES`, `PINA`, `PINB` |
| `docs/19-symbol-naming.md` | Nomenclatura simboli |
| `docs/20-abbreviations.md` | Dizionario abbreviazioni |
| `docs/21-material-archives.md` | Archivi materiali custom |
| `docs/25-cable-archive-dbcables.md` | Archivio Cavi `DbCables.db` |
| `docs/26-back-check-controls.md` | Back-check e controlli incrociati |
| `docs/07-troubleshooting.md` | Troubleshooting generale |
| `docs/known-issues/` | Problemi noti |
| `docs/playbooks/` | Procedure guidate |
| `docs/standards/` | Standard operativi |

## Regole editoriali

- Scrivere in modo tecnico, sintetico e operativo.
- Preferire procedure, checklist e tabelle a testo teorico.
- Separare guida, standard, decisioni, troubleshooting e casi pratici.
- Non inserire dati sensibili, nomi cliente o dettagli di commessa.
- Usare immagini solo se chiariscono una procedura o un controllo.
- Mantenere grafica e diagrammi minimal, leggibili e non decorativi.
- Aggiornare il decision log quando una scelta diventa standard.

## Pubblicazione

La configurazione principale è in `mkdocs.yml`.

Caratteristiche abilitate:

- navigazione laterale e tab;
- ricerca interna;
- tema chiaro/scuro;
- diagrammi e tabelle;
- copia rapida dei blocchi codice;
- deploy automatico su branch `gh-pages` tramite GitHub Actions.

Workflow:

```text
push su master -> build MkDocs -> deploy gh-pages
```

## Preview locale

Installazione dipendenze:

```bash
pip install -r requirements.txt
```

Avvio sito locale:

```bash
mkdocs serve
```

Build di verifica:

```bash
mkdocs build --strict
```

## Stato

| Area | Stato |
|---|---|
| Sito MkDocs | Configurato |
| Guida operativa completa | Presente |
| Libreria custom | Standard documentato |
| Template progetto | Base operativa presente |
| Unifilare | Base operativa presente |
| Multifilare | Base operativa presente, da consolidare |
| Simboli custom | Workflow e checklist presenti |
| Materiali e cavi | Procedure e back-check presenti |
| Troubleshooting | Avviato |
| Governance | Decision log, manutenzione e quality gate presenti |

## Ownership

Roberto Chello
