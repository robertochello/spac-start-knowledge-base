# Guida pratica: dove andare

Usa questa pagina come indice operativo. Parti da **quello che devi fare**, non dal nome delle sezioni del sito.

## Scegli il tuo caso

### 1. Sto preparando o modificando un progetto

| Obiettivo | Pagina da aprire |
|---|---|
| installare o verificare `_CUSTOM` | [Libreria custom](15-custom-library.md) |
| creare la base di un nuovo progetto | [Template progetto](16-project-template.md) |
| orientarmi nell'interfaccia | [Interfaccia e menu](01-interface-and-menu.md) |
| gestire pagine, cartigli o immagini | [Pagine, cartigli e immagini](05-pages-titleblocks-images.md) |
| lavorare con geometria CAD | [Workflow CAD 2D](02-cad-workflow.md) |

### 2. Sto disegnando lo schema

| Obiettivo | Pagina da aprire |
|---|---|
| schema unifilare | [Schema unifilare](17-unifilare.md) |
| numerazione e identificazione fili | [Numerazione fili](18-wire-numbering.md) |
| schema multifilare | [Multifilare](09-multifilare.md) |
| morsetti, morsettiere e cross-reference | [Rimandi e morsetti](06-cross-references-terminals.md) |

### 3. Sto lavorando sui simboli

| Obiettivo | Pagina da aprire |
|---|---|
| creare un simbolo nuovo | [Playbook: creare un simbolo custom](playbooks/create-custom-symbol.md) |
| capire la struttura dei simboli custom | [Simboli custom](03-custom-symbols.md) |
| configurare `PRES`, `PINA`, `PINB` | [Attributi e pinatura](04-attributes-and-pinning.md) |
| scegliere il nome corretto | [Nomenclatura simboli](19-symbol-naming.md) |
| verificare un simbolo prima del riuso | [Checklist validazione simbolo](10-symbol-validation-checklist.md) |

### 4. Sto gestendo materiali, cavi o download

| Obiettivo | Pagina da aprire |
|---|---|
| archivi materiali custom | [Archivi materiali](21-material-archives.md) |
| regole per i materiali | [Standard materiali](standards/materials.md) |
| archivio cavi | [Archivio Cavi DbCables](25-cable-archive-dbcables.md) |
| controlli dopo un aggiornamento | [Back-check e controlli incrociati](26-back-check-controls.md) |
| scaricare file pubblicati | [Download](downloads.md) |

### 5. Qualcosa non funziona

Apri prima **[Diagnosi rapida](07-troubleshooting.md)**.

Se riconosci già il sintomo, usa direttamente il riferimento seguente.

| Sintomo | Vai a |
|---|---|
| pin che non aggancia | [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| oggetti o layer che non riesci a eliminare | [Pulire oggetti residui](playbooks/clean-residual-objects.md) |
| rimando alimentazione errato o obsoleto | [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md) |
| morsetto rappresentato in modo inatteso | [Verificare rappresentazione morsetti](playbooks/terminal-representation.md) |
| immagine non più visualizzata | [Known issue: riferimento immagine mancante](known-issues/missing-image-reference.md) |
| DbCables con versione non congruente | [Known issue: DbCables](known-issues/dbcables-version-mismatch.md) |

## Quale tipo di pagina usare

| Tipo | Quando usarlo |
|---|---|
| **Pagina operativa** | devi capire un'area di lavoro e le sue regole principali |
| **Playbook** | devi eseguire una procedura passo-passo |
| **Troubleshooting** | hai un sintomo ma non conosci ancora la causa |
| **Known issue** | il problema è già noto e ricorrente |
| **Standard** | devi sapere quale regola è stata adottata |
| **Quality gate** | devi verificare che il lavoro sia pronto |
| **Decision log** | devi capire perché è stata presa una certa decisione |

## Manuale completo: quando usarlo

La pagina **[Guida operativa completa](guida-operativa-completa.md)** raccoglie molti argomenti in un unico documento.

Usala quando:

- vuoi fare una ricerca testuale su tutto il manuale;
- vuoi scorrere più argomenti consecutivamente;
- ti serve un riferimento unico da consultare.

Per una singola attività è normalmente più chiaro usare le pagine operative o i playbook collegati sopra.

## Se devi aggiungere nuova documentazione

Prima di creare una nuova pagina, verifica se l'informazione appartiene già a una pagina esistente.

1. **Procedura pratica** → aggiungi o aggiorna un playbook.
2. **Problema ricorrente** → known issue.
3. **Regola stabile** → standard.
4. **Scelta progettuale/documentale** → decision log.
5. **Controllo prima del rilascio** → quality gate.

!!! note "Regola editoriale"

    Una pagina deve aiutare almeno a **decidere, configurare, verificare, diagnosticare o standardizzare**. Se non fa nessuna di queste cose, va semplificata o collegata meglio.
