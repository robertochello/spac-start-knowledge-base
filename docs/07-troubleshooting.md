# Troubleshooting

Questa sezione raccoglie problemi ricorrenti e indica **il primo comando concreto da usare** prima di passare alla diagnosi dettagliata.

## Diagnosi rapida

| Sintomo | Prima azione concreta | Procedura |
|---|---|---|
| libreria simboli non si apre | digita `SP_XML_MENU` | [Interfaccia e menu](01-interface-and-menu.md) |
| menu SPAC/CAD alterati o mancanti | digita `_MENU` | [Interfaccia e menu](01-interface-and-menu.md) |
| pin non aggancia | `EDITATT` → verifica `PINA/PINB`; poi `_DSETTINGS` → **Snap e griglia** | [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| layer apparentemente vuoto non si elimina | `PURGE` → **Trova elementi non eliminabili** | [Pulire oggetti residui](playbooks/clean-residual-objects.md) |
| oggetto diretto mantiene un layer | `QSELECT` → filtro **Layer** | [Pulire oggetti residui](playbooks/clean-residual-objects.md) |
| residuo dentro un blocco | `BEDIT` → modifica blocco reale → salva → `PURGE` | [Pulire oggetti residui](playbooks/clean-residual-objects.md) |
| morsetto mostra numero sbagliato | `SPINSMOR` → verifica `NumI`/`NumO`/`NumM` | [Verificare rappresentazione morsetti](playbooks/terminal-representation.md) |
| devo creare una morsettiera | **Inser Morsetti** → tasto destro **Elenco Quadri** → **Nuova morsettiera** | [Rimandi e morsetti](06-cross-references-terminals.md) |
| numerazione fili errata | **Numerazione fili → Lista numeri usati** | [Numerazione fili](18-wire-numbering.md) |
| devo eliminare numerazione fili | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` | [Numerazione fili](18-wire-numbering.md) |
| materiale manca/è duplicato | doppio click simbolo → **Materiali** → tasto destro → **Avvio Archivio Materiali (DbCenter)** | [Associare materiali](playbooks/material-association.md) |
| logo/immagine non visibile | **Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso** | [Pagine, cartigli e immagini](05-pages-titleblocks-images.md) |
| bordo immagine visibile | `IMAGEFRAME` → `0` | [Pagine, cartigli e immagini](05-pages-titleblocks-images.md) |
| rimando non accetta la selezione | verifica oggetto SPAC vs linea CAD; poi **Lista numeri usati** | [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md) |
| cross-reference punta a posizione vecchia | `PURGE`/controllo residui + lista numeri; comando cross-reference esatto `Da verificare` | [Cross-reference obsoleto](known-issues/obsolete-cross-reference.md) |
| `DbCables.db` non allineato | verifica versione archivio/ambiente e segui known issue | [Known Issue DbCables](known-issues/dbcables-version-mismatch.md) |

## Menu o libreria simboli non visibili

### Libreria

Digita:

```text
SP_XML_MENU
```

Se non si apre, verifica che la cartella custom esista in:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM
```

### Menu

Digita:

```text
_MENU
```

Il file/menu specifico da ricaricare dipende dall'installazione e non va inventato se non verificato.

## Simbolo custom non riconosciuto

1. Inserisci il simbolo in un progetto prova.
2. Usa:

   ```text
   EDITATT
   ```

3. Verifica `NOME`, `PRES`, `PINA/PINB`.
4. Se un attributo manca nel sorgente, correggi con `ATTDEF`.
5. Controlla proprietà con `PROPRIETA` / `CTRL+1`.
6. Se modifichi il DWG, rigenera con `MBLOCCO` e `_MSLIDE`.

## Pin non aggancia

1. `EDITATT` → controlla `PINA<n>`/`PINB<n>`.
2. `_DSETTINGS` → **Snap e griglia**.
3. Verifica collegamento SPAC vs linea CAD.
4. Se necessario modifica il sorgente con `ATTDEF`.
5. Reinserisci/testa il simbolo.

## Layer non eliminabile / residui

Procedura verificata:

```text
PURGE
```

Se non eliminabile:

```text
Trova elementi non eliminabili
```

Poi:

- oggetto diretto → `QSELECT` → filtro **Layer**;
- residuo in blocco → `BEDIT`;
- blocco annidato → `BEDIT` sul blocco interno;
- infine riesegui `PURGE`.

!!! danger

    `LAYISO` e `LAYWALK` non sono disponibili in SPAC Start 26: non usarli come soluzione in questa knowledge base.

## Logo o immagine non visibile

1. **Modifica/Inserisci → Gestioni immagini**.
2. Seleziona l'immagine.
3. **Sfoglia**.
4. Riseleziona il file.
5. **Salva percorso**.
6. Per il bordo: `IMAGEFRAME` → `0`.

## Morsetti

Apri:

```text
SPINSMOR
```

oppure **Inser Morsetti**.

Per nuova morsettiera:

```text
Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera
```

Se il testo è sbagliato, verifica:

- `NumI` = numero filo ingresso;
- `NumO` = numero filo uscita;
- `NumM` = numero morsetto.

## Numerazione fili

Per fili non di alimentazione:

```text
SPAC → Numera Fili
```

Per duplicati:

```text
Numerazione fili → Lista numeri usati
```

Per eliminare numeri:

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

## Materiali

Percorso:

```text
doppio click simbolo → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)
```

Controlla poi distinta/report.

## Cross-reference

La procedura logica è consolidata, ma il **nome esatto del comando/menu di rigenerazione cross-reference** non è ancora verificato nella knowledge base.

Quindi:

- verifica oggetto SPAC;
- verifica nome/direzione rimando;
- verifica **Numerazione fili → Lista numeri usati**;
- pulisci residui se necessario;
- usa la funzione cross-reference dell'installazione;
- fino alla verifica del nome esatto, il comando resta `Da verificare`.

## Regola generale

Quando qualcosa non funziona, individua prima il livello:

- grafica CAD;
- attributi;
- oggetto intelligente;
- rappresentazione;
- riferimento esterno;
- archivio dati.

Poi usa il comando pertinente. Non correggere solo l'effetto visibile.

## Riferimenti

- [Comandi e click esatti](command-reference.md)
- [Guida pratica](00-how-to-use.md)
