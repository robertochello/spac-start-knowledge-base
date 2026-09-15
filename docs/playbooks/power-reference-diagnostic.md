# Playbook — Diagnosticare rimandi alimentazione

## Obiettivo

Capire perché un rimando/alimentazione non viene accettato oppure punta a una posizione non coerente usando i comandi verificati in SPAC Start 26.

## Creare correttamente il rimando

Per un nuovo collegamento usa:

- **Dynamic Coll**;
- oppure **Dynamic Alim**.

Procedura:

1. scegli **Dynamic Coll** o **Dynamic Alim**;
2. seleziona il numero di fili;
3. traccia il collegamento;
4. premi **Invio**;
5. scegli **Rimandi di arrivo**, **Rimandi di partenza** oppure **Rimandi di arrivo e partenza**;
6. scegli numero/nome del filo;
7. se necessario scegli il tipo di cavo;
8. clicca **Ok**.

Il secondo rimando deve usare lo stesso nome e una direzione coerente.

## Controllare i rimandi esistenti

Apri:

```text
Numerazione fili → Lista numeri usati
```

Poi:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli, ad esempio `SCHEMA`;
3. clicca **Scansiona i Multifogli**.

I numeri con **asterisco** sono ripetuti.

## Aggiornare il cross-reference

Percorso verificato:

```text
UTIL → Cross Reference
```

Poi:

1. tipo elaborazione → **Rimandi**;
2. clicca **Cross**;
3. scegli se visualizzare il file Excel di output;
4. clicca **Ok - Aggiorna**;
5. controlla i riferimenti sul foglio.

## Se il rimando restituisce selezione non valida

Verifica nell'ordine:

1. il collegamento è stato creato con **Dynamic Coll/Dynamic Alim** oppure è una linea CAD?
2. l'oggetto è stato esploso/alterato?
3. esistono geometrie sovrapposte?
4. stai cliccando l'oggetto SPAC reale?
5. il problema si ripete su foglio pulito?

Non aggiungere una seconda linea CAD sopra il collegamento.

## Se il cross-reference punta alla vecchia posizione

1. **Numerazione fili → Lista numeri usati**.
2. **Vedi solo i Rimandi**.
3. **Scansiona i Multifogli**.
4. Controlla duplicati/rimandi residui.
5. Se sospetti oggetti residui usa `PURGE → Trova elementi non eliminabili`, poi `QSELECT`/`BEDIT` se necessario.
6. Torna in **UTIL → Cross Reference**.
7. **Rimandi → Cross → Ok - Aggiorna**.
8. Controlla nuovamente il riferimento.

## Regole direzionali

- partenza ↔ arrivo;
- partenza ↔ arrivo/partenza;
- arrivo ↔ partenza;
- arrivo ↔ arrivo/partenza.

I rimandi della stessa connessione devono usare lo stesso nome.

## Verifica finale

- collegamento creato come oggetto SPAC;
- nomi rimandi uguali;
- direzioni coerenti;
- nessun duplicato inatteso nella scansione;
- **Ok - Aggiorna** eseguito;
- riferimento corretto dopo salvataggio e riapertura.

## Collegamenti

- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Pulire oggetti residui](clean-residual-objects.md)
- [Comandi e click esatti](../command-reference.md)
