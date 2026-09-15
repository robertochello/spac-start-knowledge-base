# Playbook — Gestire cartiglio e logo

## Obiettivo

Gestire loghi e immagini nei cartigli usando i comandi effettivi di SPAC/CAD, evitando riferimenti mancanti dopo lo spostamento del progetto.

## Cartella consigliata

Per asset ricorrenti usa un percorso stabile, ad esempio:

```text
97_RISORSE\IMMAGINI
```

Non rinominare o spostare il file dopo averlo collegato.

## Inserire/collegare il logo

1. Apri il DWG master del cartiglio.
2. Digita:

   ```text
   IMMAGINI
   ```

3. Nella finestra di gestione immagini clicca **Attacca**.
4. Seleziona il file del logo.
5. Posiziona il logo nel cartiglio.
6. Salva il DWG.
7. Chiudi e riapri per verificare il riferimento.

## Eliminare il bordo del logo

Digita:

```text
IMAGEFRAME
```

Imposta:

```text
0
```

!!! note

    `IMAGEFRAME = 0` può dover essere impostato nuovamente in ogni nuovo progetto anche se era già presente nel DWG master.

## Se il logo non viene più trovato

Percorso verificato:

```text
Modifica/Inserisci → Gestioni immagini
```

Poi:

1. individua il logo nella lista;
2. clicca **Sfoglia**;
3. seleziona nuovamente il file corretto;
4. clicca **Salva percorso**;
5. salva;
6. chiudi e riapri il progetto.

## Se devi scollegare un logo/immagine

1. Digita `IMMAGINI`.
2. Seleziona l'immagine nella lista.
3. Clicca **Stacca**.

## Test del cartiglio master

1. Apri il master.
2. Verifica che il logo sia visibile.
3. Digita `IMMAGINI` e controlla che il riferimento punti al file corretto.
4. Digita `IMAGEFRAME` e verifica `0` se non vuoi il bordo.
5. Salva.
6. Chiudi e riapri.

## Test nel progetto/multifoglio

1. Applica il cartiglio a un progetto di prova.
2. Verifica la visibilità del logo.
3. Se appare un riquadro o il logo manca, apri **Modifica/Inserisci → Gestioni immagini**.
4. Usa **Sfoglia → Salva percorso** se il path non è più valido.
5. Esegui `IMAGEFRAME → 0` se il problema è solo il bordo.
6. Salva, chiudi e riapri.

## Verifica finale

Il cartiglio è stabile quando:

- `IMMAGINI` mostra il riferimento corretto;
- il file del logo esiste nel percorso previsto;
- il logo è visibile nel master e nel progetto;
- `IMAGEFRAME = 0` se richiesto;
- il riferimento resta valido dopo salvataggio e riapertura.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Pagine, cartigli e immagini](../05-pages-titleblocks-images.md)
- [Riferimento immagine mancante](../known-issues/missing-image-reference.md)
