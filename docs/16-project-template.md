# Template progetto

Questa sezione definisce la base operativa per creare un progetto SPAC riutilizzabile per schemi unifilari e multifilari.

## Obiettivo

Creare una struttura progetto ordinata prima di iniziare lo sviluppo degli schemi.

## Pagine standard previste

| Foglio | Riferimento DWG | Contenuto |
|---|---|---|
| 1 | `01_BLOCCO_DATI` | dati cliente e dati aziendali |
| 2 | `02_BLOCCO_DISPOSIZIONI_SICUREZZA` | disposizioni/informazioni di sicurezza |
| 3 | `03_BLOCCO_TARGA_QUADRO` | targa quadro e marcatura CE |

Questi file non devono essere inseriti con **Inserisci Blocco**: devono essere collegati come **Riferimento DWG**.

## Inserire una pagina standard come Riferimento DWG

1. Apri un foglio libero.
2. Clicca:

   ```text
   Modifica/Inserisci → Riferimento DWG
   ```

3. Naviga nella cartella che contiene il DWG della pagina standard.
4. Seleziona il file, ad esempio:

   ```text
   01_BLOCCO_DATI
   ```

5. Nella finestra successiva individua, sulla destra, la sezione **Tipo di percorso**.
6. Seleziona:

   ```text
   Percorso completo
   ```

7. Premi **OK**.
8. Posiziona il riferimento DWG nel foglio.
9. Salva il progetto.
10. Chiudi e riapri per verificare che il riferimento resti valido.

Ripeti la stessa procedura per:

```text
02_BLOCCO_DISPOSIZIONI_SICUREZZA
03_BLOCCO_TARGA_QUADRO
```

## Inserire la legenda fogli

Percorso verificato:

1. Apri il menu **Fogli**.
2. Clicca **Legenda Fogli**.
3. Premi **Disegna**.
4. Seleziona un foglio vuoto.
5. Premi **OK** per confermare.

Quando la struttura dei fogli cambia, rigenera la tabella e inseriscila sempre nello stesso foglio dedicato.

## Creazione iniziale progetto

La sequenza logica è:

1. creare il nuovo progetto;
2. compilare le informazioni principali della commessa;
3. scegliere il cartiglio master;
4. predisporre il numero di fogli necessario;
5. lasciare fogli liberi per pagine standard e legenda;
6. inserire le pagine standard con **Modifica/Inserisci → Riferimento DWG**;
7. generare la legenda con **Fogli → Legenda Fogli**.

!!! warning "Creazione progetto/cartiglio: percorso UI da verificare"

    I nomi esatti dei pulsanti iniziali per **Nuovo progetto**, selezione del **cartiglio master** e impostazione del numero di fogli non sono ancora consolidati nella knowledge base. La sequenza funzionale è verificata, ma i singoli click devono essere documentati solo dopo verifica diretta in SPAC Start 26.

## Checklist template

Prima di usare un template come base:

- cartiglio verificato;
- `01_BLOCCO_DATI` inserito come **Riferimento DWG**;
- `02_BLOCCO_DISPOSIZIONI_SICUREZZA` inserito come **Riferimento DWG**;
- `03_BLOCCO_TARGA_QUADRO` inserito come **Riferimento DWG**;
- **Tipo di percorso = Percorso completo** verificato;
- **Fogli → Legenda Fogli → Disegna** completato;
- immagini e riferimenti validi dopo riapertura;
- fogli liberi disponibili;
- progetto salvato come base pulita.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Pagine, cartigli e immagini](05-pages-titleblocks-images.md)
- [Workflow CAD 2D](02-cad-workflow.md)
