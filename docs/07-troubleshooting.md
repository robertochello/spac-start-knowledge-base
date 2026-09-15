# Troubleshooting

Questa pagina parte dal sintomo e indica il **primo comando concreto** da usare.

## Diagnosi rapida

| Sintomo | Prima azione concreta | Procedura |
|---|---|---|
| libreria simboli non si apre | `SP_XML_MENU` | [Interfaccia e menu](01-interface-and-menu.md) |
| menu alterati/mancanti | `_MENU` | [Interfaccia e menu](01-interface-and-menu.md) |
| pin non aggancia | `EDITATT` → verifica `PINA/PINB`; `_DSETTINGS → Snap e griglia` | [Pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| layer non si elimina | `PURGE → Trova elementi non eliminabili` | [Oggetti residui](playbooks/clean-residual-objects.md) |
| oggetto diretto mantiene layer | `QSELECT` → filtro **Layer** | [Oggetti residui](playbooks/clean-residual-objects.md) |
| residuo dentro blocco | `BEDIT` → modifica → salva → `PURGE` | [Oggetti residui](playbooks/clean-residual-objects.md) |
| rimando duplicato | **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli** | [Rimandi](06-cross-references-terminals.md) |
| cross-reference vecchio | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** | [Rimandi](06-cross-references-terminals.md) |
| morsetto mostra dato sbagliato | `SPINSMOR` → **Anteprima** → verifica `NumM/NumI/NumO` | [Morsetti](playbooks/terminal-representation.md) |
| devo inserire morsetto | **Anteprima → Ok - Nuovo → clic filo → Invio** | [Morsetti](06-cross-references-terminals.md) |
| numerazione errata | **Numerazione fili → Lista numeri usati** | [Numerazione](18-wire-numbering.md) |
| eliminare numerazione | `DEL_NUMF` | [Numerazione](18-wire-numbering.md) |
| materiale manca/duplicato | doppio click → **Materiali → Avvio Archivio Materiali (DbCenter)** | [Materiali](playbooks/material-association.md) |
| immagine non visibile | **Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso** | [Immagini](05-pages-titleblocks-images.md) |
| bordo immagine visibile | `IMAGEFRAME → 0` | [Immagini](05-pages-titleblocks-images.md) |

## Rimando non accetta la selezione

1. verifica se il collegamento è **Dynamic Coll/Dynamic Alim** o semplice linea CAD;
2. controlla sovrapposizioni/residui;
3. verifica nome e direzione;
4. controlla i rimandi:

   ```text
   Numerazione fili → Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli
   ```

5. se necessario ricrea il rimando con **Dynamic Coll/Dynamic Alim**.

## Cross-reference obsoleto

1. controlla rimandi e duplicati;
2. pulisci eventuali residui;
3. apri:

   ```text
   UTIL → Cross Reference
   ```

4. seleziona **Rimandi**;
5. clicca **Cross**;
6. clicca **Ok - Aggiorna**;
7. verifica il riferimento generato.

## Morsetto mostra numero filo invece del numero morsetto

1. `SPINSMOR`;
2. seleziona morsettiera/tipo;
3. nel riquadro **Anteprima** scegli un modello che mostri `NumM`;
4. **Ok - Nuovo**;
5. clic sul filo;
6. **Invio**;
7. confronta il morsetto nuovo con quello problematico.

## Pin non aggancia

1. `EDITATT` → `PINA<n>/PINB<n>`;
2. `_DSETTINGS → Snap e griglia`;
3. verifica collegamento SPAC vs linea CAD;
4. se necessario `ATTDEF` nel sorgente;
5. rigenera con `MBLOCCO` e `_MSLIDE`;
6. reinserisci e testa.

## Layer non eliminabile

1. `PURGE`;
2. **Trova elementi non eliminabili**;
3. oggetto diretto → `QSELECT` → **Layer**;
4. blocco → `BEDIT`;
5. salva;
6. `PURGE` di nuovo.

!!! danger

    Non proporre `LAYISO` o `LAYWALK`: non sono disponibili nell'ambiente SPAC Start 26 verificato.

## Logo/immagine non visibile

```text
Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso
```

Per il bordo:

```text
IMAGEFRAME → 0
```

## Materiale non presente o duplicato

```text
doppio click simbolo → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)
```

Poi verifica distinta/report e il punto di associazione Madre/Figlio.

## Regola diagnostica

Prima individua il livello del problema:

- grafica CAD;
- attributi;
- oggetto SPAC;
- rappresentazione;
- riferimento esterno;
- archivio dati.

Poi correggi la causa, non il solo effetto visibile.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Guida pratica](00-how-to-use.md)
