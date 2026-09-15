# SPAC Start Knowledge Base

Knowledge base operativa per **SPAC Start 26 / SPAC Start Impianti**.

Il contenuto è pensato per il lavoro reale: setup progetto, schemi unifilari e multifilari, simboli custom, attributi e pinatura, materiali, cavi, rimandi, morsetti e troubleshooting.

> **Il modo consigliato per consultare la repository è il sito GitHub Pages:**
> [Apri SPAC Start Knowledge Base](https://robertochello.github.io/spac-start-knowledge-base/)

## Da dove partire

| Se devi... | Apri |
|---|---|
| sapere **esattamente cosa digitare o cliccare** | [Comandi e click esatti](https://robertochello.github.io/spac-start-knowledge-base/command-reference/) |
| capire dove trovare una procedura | [Guida pratica](https://robertochello.github.io/spac-start-knowledge-base/00-how-to-use/) |
| iniziare un lavoro o configurare SPAC | [Libreria custom](https://robertochello.github.io/spac-start-knowledge-base/15-custom-library/) |
| risolvere un problema | [Problemi e diagnosi](https://robertochello.github.io/spac-start-knowledge-base/07-troubleshooting/) |
| scaricare archivi pubblicati | [Download](https://robertochello.github.io/spac-start-knowledge-base/downloads/) |
| consultare tutto il materiale in una sola pagina | [Manuale completo](https://robertochello.github.io/spac-start-knowledge-base/guida-operativa-completa/) |

## Regola fondamentale della guida

Le procedure operative devono riportare i **nomi reali** dell'interfaccia quando sono stati verificati.

Esempi:

```text
SP_XML_MENU
_DSETTINGS
ATTDEF
MBLOCCO
_MSLIDE
EDITATT
SPINSMOR
DEL_NUMF
PURGE
QSELECT
BEDIT
```

e percorsi come:

```text
SPAC → Numera Fili
SPAC → Utility Fili → Elimina numerazione
Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera
Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso
```

Se il nome esatto di un comando, pulsante o percorso non è ancora stato verificato in **SPAC Start 26**, viene indicato **Da verificare** invece di inventarlo.

## Come è organizzata

- **Guida pratica**: orientamento e accesso immediato ai comandi esatti;
- **Lavoro in SPAC**: setup, schemi, simboli e archivi;
- **Procedure**: playbook passo-passo;
- **Problemi e diagnosi**: troubleshooting e known issue;
- **Riferimenti**: standard, decisioni e quality gate.

La fonte dei contenuti pubblicati è `docs/`; la navigazione del sito è definita in `mkdocs.yml`.

## Aree tecniche principali

| Area | Riferimento principale |
|---|---|
| Comandi e percorsi esatti | `docs/command-reference.md` |
| Libreria custom `_CUSTOM` | `docs/15-custom-library.md` |
| Schema unifilare | `docs/17-unifilare.md` |
| Numerazione fili | `docs/18-wire-numbering.md` |
| Schema multifilare | `docs/09-multifilare.md` |
| Rimandi e morsetti | `docs/06-cross-references-terminals.md` |
| Simboli custom | `docs/03-custom-symbols.md` |
| Attributi e pinatura | `docs/04-attributes-and-pinning.md` |
| Archivi materiali | `docs/21-material-archives.md` |
| Archivio cavi `DbCables.db` | `docs/25-cable-archive-dbcables.md` |
| Troubleshooting | `docs/07-troubleshooting.md` |

## Regole della knowledge base

- Documentare procedure realmente verificate.
- Riportare comando, menu, finestra, pulsante e valore esatti quando noti.
- Marcare **Da verificare** il punto preciso che non è ancora confermato.
- Non inventare comandi, menu o comportamenti SPAC.
- Separare oggetti CAD e oggetti intelligenti SPAC.
- Non pubblicare dati cliente, commessa, credenziali o file riservati.

## Preview locale

```bash
pip install -r requirements.txt
mkdocs serve
```

Verifica:

```bash
mkdocs build --strict
```

## Pubblicazione

```text
push su master -> mkdocs build --strict -> deploy GitHub Pages
```

Non modificare manualmente il branch `gh-pages`.

## Ownership

Roberto Chello
