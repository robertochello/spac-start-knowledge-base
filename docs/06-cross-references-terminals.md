# Rimandi, cross-reference e morsetti

Questa pagina contiene le procedure operative verificate per rimandi, cross-reference, morsetti e morsettiere in **SPAC Start 26**.

## Lista dei soli rimandi usati

Percorso:

```text
Numerazione fili → Lista numeri usati
```

Nella finestra **Lista numeri usati**:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli da analizzare, ad esempio `SCHEMA`;
3. clicca **Scansiona i Multifogli**;
4. controlla l'elenco generato.

I numeri con **asterisco** sono ripetuti e devono essere verificati.

## Creare un rimando

Il collegamento deve essere un oggetto SPAC, non una semplice linea CAD.

Per il primo rimando:

1. seleziona **Dynamic Coll** oppure **Dynamic Alim**;
2. seleziona il numero di fili;
3. traccia il cavo/collegamento;
4. premi **Invio**;
5. scegli uno dei tipi:
   - **Rimandi di arrivo**;
   - **Rimandi di partenza**;
   - **Rimandi di arrivo e partenza**;
6. scegli il numero/nome del filo;
7. se necessario scegli il tipo di cavo;
8. clicca **Ok** per posizionare il filo.

Per il secondo rimando usa lo **stesso nome** del primo.

Regola direzionale:

- primo **partenza** → secondo **arrivo** oppure **arrivo e partenza**;
- primo **arrivo** → secondo **partenza** oppure **arrivo e partenza**.

## Aggiornare il cross-reference

Percorso verificato:

```text
UTIL → Cross Reference
```

Poi:

1. scegli il tipo di elaborazione **Rimandi**;
2. clicca **Cross**;
3. scegli se visualizzare l'output del cross-reference, cioè il file Excel generato;
4. clicca **Ok - Aggiorna**;
5. torna allo schema e controlla i riferimenti generati;
6. verifica eventuali duplicati con **Numerazione fili → Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli**.

### Esito atteso

- i due rimandi con lo stesso nome vengono collegati logicamente;
- il riferimento punta al foglio/posizione corretti;
- non restano rimandi duplicati inattesi.

## Quando il rimando restituisce selezione non valida

Controlla nell'ordine:

1. stai selezionando **Dynamic Coll/Dynamic Alim** o una linea CAD?
2. l'oggetto è stato esploso o alterato?
3. esistono linee/oggetti sovrapposti?
4. il collegamento è ancora un oggetto SPAC riconosciuto?
5. il problema si ripete su un foglio pulito?

Non disegnare una seconda linea CAD sopra quella esistente per simulare il collegamento.

## Cross-reference che punta a una vecchia posizione

1. Controlla i rimandi con **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli**.
2. Cerca oggetti residui o sovrapposti.
3. Se necessario usa `PURGE`, `QSELECT` e `BEDIT` seguendo il playbook dedicato.
4. Torna in **UTIL → Cross Reference**.
5. Seleziona **Rimandi**.
6. Clicca **Cross**.
7. Clicca **Ok - Aggiorna**.
8. Verifica nuovamente i riferimenti sul foglio.

## Eliminare la numerazione fili

Percorso:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente:

```text
DEL_NUMF
```

La funzione elimina i numeri, non i fili.

## Aprire Inser Morsetti

Funzione:

```text
Inser Morsetti
```

Comando equivalente:

```text
SPINSMOR
```

!!! warning "Prerequisito"

    Prima di usare `SPINSMOR` deve essere aperto un database materiali contenente almeno una morsettiera.

## Creare una nuova morsettiera

Nella finestra **Inser Morsetti**:

1. individua **Elenco Quadri** in alto a sinistra;
2. tasto destro su **Elenco Quadri**, sul nome del quadro oppure su una morsettiera esistente;
3. clicca **Nuova morsettiera**;
4. completa i dati;
5. verifica che compaia sotto il quadro corretto.

Per modificare/eliminare una morsettiera già esistente usa la relativa voce del menu contestuale aperto con il tasto destro.

## Inserire un morsetto sul filo

Nella finestra **Inser Morsetti**:

1. seleziona la morsettiera da utilizzare;
2. scegli il **tipo di morsetto**;
3. nel riquadro **Anteprima** seleziona il modello grafico desiderato;
4. se vuoi visualizzare il numero morsetto, scegli una rappresentazione basata su `NumM`, preferibilmente insieme al nome morsettiera;
5. clicca **Ok - Nuovo** in basso a destra;
6. torna al disegno e clicca il filo nel punto in cui deve essere inserito il morsetto;
7. premi **Invio**.

Il punto cliccato sul filo determina la posizione del morsetto.

### Significato campi rappresentazione

| Sigla | Significato |
|---|---|
| `NumI` | numero filo in ingresso |
| `NumO` | numero filo in uscita |
| `NumM` | numero morsetto |

Se vedi il numero filo quando vuoi il numero morsetto, verifica il modello selezionato nel riquadro **Anteprima**: deve mostrare `NumM`, non `NumI`/`NumO`.

## Diagnostica rapida

| Sintomo | Azione concreta |
|---|---|
| Rimandi duplicati | **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli** |
| Cross-reference da aggiornare | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** |
| Rimando non accetta la selezione | verifica `Dynamic Coll` / `Dynamic Alim` vs linea CAD |
| Devo eliminare numeri filo | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Devo aprire gestione morsetti | **Inser Morsetti** / `SPINSMOR` |
| Devo creare morsettiera | **Elenco Quadri → tasto destro → Nuova morsettiera** |
| Devo inserire morsetto | scegli morsettiera/tipo → **Anteprima** → **Ok - Nuovo** → clic filo → **Invio** |
| Vedo numero filo invece del morsetto | seleziona modello **Anteprima** che visualizza `NumM` |

## Verifica finale

Prima di chiudere il lavoro:

- rimandi con nomi coerenti;
- direzione arrivo/partenza corretta;
- cross-reference aggiornato con **Ok - Aggiorna**;
- lista rimandi scansionata senza duplicati inattesi;
- morsettiera corretta;
- morsetto inserito sul filo corretto;
- rappresentazione coerente (`NumM` se richiesto).

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Schema multifilare](09-multifilare.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Verificare rappresentazione morsetti](playbooks/terminal-representation.md)
- [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md)
- [Pulire oggetti residui](playbooks/clean-residual-objects.md)
