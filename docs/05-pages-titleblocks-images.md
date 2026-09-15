# Pagine standard, cartigli e immagini

Questa sezione raccoglie le procedure operative per pagine standard, cartigli, immagini e loghi in SPAC Start.

## Gestire le immagini collegate

Il comando verificato è:

```text
IMMAGINI
```

Dalla finestra di gestione immagini:

- **Attacca** → collega una nuova immagine;
- **Stacca** → rimuove il riferimento dell'immagine selezionata.

### Inserire una nuova immagine

1. Digita `IMMAGINI` nella riga comando.
2. Clicca **Attacca**.
3. Seleziona il file immagine.
4. Posiziona l'immagine nel disegno.
5. Salva il progetto.
6. Chiudi e riapri il progetto per verificare che il riferimento resti valido.

## Ripristinare un'immagine non visualizzata

Percorso verificato da menu:

```text
Modifica/Inserisci → Gestioni immagini
```

Procedura:

1. Apri **Modifica/Inserisci**.
2. Clicca **Gestioni immagini**.
3. Individua l'immagine interessata nella lista.
4. Clicca **Sfoglia**.
5. Seleziona nuovamente il file corretto sul PC.
6. Clicca **Salva percorso**.
7. Salva il progetto.
8. Chiudi e riapri per verificare il collegamento.

## Eliminare il bordo delle immagini

Nella riga comando digita:

```text
IMAGEFRAME
```

Quando viene richiesto il valore, imposta:

```text
0
```

Risultato atteso: il bordo/frame delle immagini non viene visualizzato.

!!! important "Da ripetere nei nuovi progetti"

    Anche se `IMAGEFRAME = 0` è già stato impostato nel cartiglio master o in un DWG sorgente, in un nuovo progetto può essere necessario eseguire nuovamente `IMAGEFRAME` e impostare `0`.

## Cartella immagini consigliata

Per loghi e immagini ricorrenti usa una cartella stabile:

```text
97_RISORSE\IMMAGINI
```

Evita di spostare o rinominare i file dopo averli collegati.

## Cartiglio master con logo

Procedura:

1. Apri il DWG master del cartiglio.
2. Inserisci/collega il logo con `IMMAGINI` → **Attacca**.
3. Usa un file presente in `97_RISORSE\IMMAGINI` o in un altro percorso stabile controllato.
4. Digita `IMAGEFRAME` e imposta `0` se non vuoi visualizzare il bordo.
5. Salva il DWG master.
6. Chiudi e riapri il file.
7. Verifica che il logo sia ancora visibile.
8. Testa il cartiglio in un progetto/multifoglio di prova.

## Inserimento di un DWG come riferimento

La knowledge base stabilisce che una pagina standard che deve restare collegata al file sorgente non va trattata come semplice blocco.

!!! warning "Percorso menu da verificare"

    Il nome esatto del comando/percorso SPAC Start 26 per inserire la pagina come **riferimento DWG** non è ancora consolidato. Finché non viene verificato direttamente non deve essere sostituito con un nome ipotetico.

Una volta aperta la funzione corretta, la verifica minima è:

1. selezionare il DWG sorgente;
2. usare un percorso stabile;
3. posizionare il riferimento;
4. salvare;
5. chiudere e riaprire il progetto;
6. verificare che il riferimento sia ancora risolto.

## Problema: riquadro al posto dell'immagine

Se compare un riquadro invece del logo/immagine:

1. apri **Modifica/Inserisci → Gestioni immagini**;
2. seleziona l'immagine;
3. controlla il percorso;
4. clicca **Sfoglia** se il file non viene trovato;
5. riseleziona il file;
6. clicca **Salva percorso**;
7. verifica `IMAGEFRAME` se il problema riguarda solo il bordo.

## Checklist finale

Prima di considerare stabile una pagina o un cartiglio:

- `IMMAGINI` mostra riferimenti validi;
- il logo è collegato al file corretto;
- **Sfoglia → Salva percorso** è stato usato se il path era errato;
- `IMAGEFRAME = 0` se il bordo non deve comparire;
- salvataggio, chiusura e riapertura completati senza perdita degli asset;
- test eseguito su progetto prova.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Gestire cartiglio e logo](playbooks/titleblock-logo-workflow.md)
- [Known Issue - Riferimento immagine mancante](known-issues/missing-image-reference.md)
