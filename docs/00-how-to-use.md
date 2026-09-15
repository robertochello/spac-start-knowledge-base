# Guida pratica: dove andare

Usa questa pagina come indice operativo. Parti da **quello che devi fare**, non dal nome delle sezioni del sito.

## Se vuoi sapere esattamente cosa cliccare

Apri subito:

**[Comandi e click esatti](command-reference.md)**

Quella pagina raccoglie i nomi verificati di:

- comandi da digitare nella riga comando;
- menu e sottomenu;
- finestre/dialog;
- pulsanti;
- campi e valori da impostare.

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
```

oppure percorsi come:

```text
SPAC → Utility Fili → Elimina numerazione
Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera
Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso
```

!!! important

    Se un percorso non è stato ancora verificato direttamente in SPAC Start 26, la guida deve scrivere **Da verificare**. Non deve inventare il nome di un comando o di un pulsante.

## Scegli il tuo caso

### 1. Sto preparando o modificando un progetto

| Obiettivo | Pagina da aprire |
|---|---|
| installare/verificare `_CUSTOM` e aprire la libreria | [Libreria custom](15-custom-library.md) |
| creare la base di un nuovo progetto | [Template progetto](16-project-template.md) |
| menu, `SP_XML_MENU`, `CUI`, shortcut | [Interfaccia e menu](01-interface-and-menu.md) |
| immagini, `IMMAGINI`, `IMAGEFRAME` | [Pagine, cartigli e immagini](05-pages-titleblocks-images.md) |
| `_INSER`, `ESPLODI`, `MBLOCCO`, `_MSLIDE` | [Workflow CAD 2D](02-cad-workflow.md) |

### 2. Sto disegnando lo schema

| Obiettivo | Pagina da aprire |
|---|---|
| schema unifilare, `_DSETTINGS`, **Disegna**, **Identificatore Linee** | [Schema unifilare](17-unifilare.md) |
| **SPAC → Numera Fili**, modalità e alimentazioni | [Numerazione fili](18-wire-numbering.md) |
| `DEL_NUMF`, `SPINSMOR`, Madre/Figlio | [Multifilare](09-multifilare.md) |
| **Inser Morsetti**, `NumI/NumO/NumM`, cross-reference | [Rimandi e morsetti](06-cross-references-terminals.md) |

### 3. Sto lavorando sui simboli

| Obiettivo | Pagina da aprire |
|---|---|
| creare un simbolo dall'inizio | [Creare un simbolo custom](playbooks/create-custom-symbol.md) |
| workflow `ATTDEF → MBLOCCO → _MSLIDE → EDITATT` | [Simboli custom](03-custom-symbols.md) |
| creare `PRES`, `PINA`, `PINB` | [Attributi e pinatura](04-attributes-and-pinning.md) |
| diagnosticare pin che non aggancia | [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| validare un simbolo prima del riuso | [Validare un simbolo](playbooks/validate-custom-symbol.md) |
| scegliere il nome corretto | [Nomenclatura simboli](19-symbol-naming.md) |

### 4. Sto gestendo materiali, cavi o download

| Obiettivo | Pagina da aprire |
|---|---|
| associare materiale tramite **Avvio Archivio Materiali (DbCenter)** | [Associare materiali](playbooks/material-association.md) |
| archivi materiali custom | [Archivi materiali](21-material-archives.md) |
| regole per i materiali | [Standard materiali](standards/materials.md) |
| archivio cavi | [Archivio Cavi DbCables](25-cable-archive-dbcables.md) |
| controlli dopo un aggiornamento | [Back-check e controlli incrociati](26-back-check-controls.md) |
| scaricare file pubblicati | [Download](downloads.md) |

### 5. Qualcosa non funziona

Apri prima **[Diagnosi rapida](07-troubleshooting.md)**.

| Sintomo | Vai a |
|---|---|
| pin non aggancia | [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| layer non si elimina / oggetto residuo | [PURGE, QSELECT, BEDIT](playbooks/clean-residual-objects.md) |
| rimando alimentazione errato/obsoleto | [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md) |
| morsetto mostra numero sbagliato | [Verificare rappresentazione morsetti](playbooks/terminal-representation.md) |
| immagine non visualizzata | [Pagine, cartigli e immagini](05-pages-titleblocks-images.md) |
| DbCables con versione non congruente | [Known issue: DbCables](known-issues/dbcables-version-mismatch.md) |

## Manuale completo: quando usarlo

La **[Guida operativa completa](guida-operativa-completa.md)** resta il riferimento esteso e contiene la storia consolidata delle procedure.

Per lavorare sul campo, preferisci però le pagine operative e i playbook sopra: devono contenere localmente i comandi necessari senza costringerti a cercarli nel manuale monolitico.

## Regola editoriale

Ogni procedura deve rispondere, quando applicabile, a queste domande:

1. **Cosa devo digitare?**
2. **Cosa devo cliccare?**
3. **Come si chiama la finestra che si apre?**
4. **Quale campo devo modificare?**
5. **Che valore devo mettere?**
6. **Cosa devo vedere se ha funzionato?**
7. **Quali prerequisiti servono?**

Se una di queste informazioni non è ancora nota, scrivere `Da verificare` nel punto preciso invece di sostituirla con una descrizione generica.
