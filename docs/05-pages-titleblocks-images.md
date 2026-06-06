# Pagine standard, cartigli e immagini

Questa sezione raccoglie note operative per gestire pagine standard, cartigli, immagini e loghi in SPAC Start.

## Pagine standard

Le pagine standard possono includere:

- pagina iniziale;
- pagina sicurezza;
- pagine documentali;
- pagine con dati committente;
- pagine con attributi editabili.

Queste pagine devono essere mantenute come contenuti generici e riutilizzabili.

## Pagine DWG senza cartiglio

Una pagina DWG può essere usata come pagina standard anche se non contiene un cartiglio completo.

Linee guida:

- mantenere il file pulito;
- verificare eventuali attributi editabili;
- evitare riferimenti non controllati;
- testare l'inserimento in un progetto prova;
- conservare una copia standard separata dalle commesse.

## Inserimento come riferimento DWG

Le pagine standard non devono essere inserite come blocco semplice quando devono restare collegate al file sorgente.

Workflow consigliato:

1. aprire un foglio libero;
2. usare la funzione riferimento DWG;
3. selezionare il file della pagina standard;
4. usare un percorso controllato;
5. posizionare il riferimento nel foglio;
6. verificare il comportamento dopo salvataggio e riapertura.

## Immagini e loghi

Quando un logo o un'immagine non viene visualizzato, il problema è spesso legato a un riferimento esterno non risolto.

Approccio pratico consigliato:

- mantenere le immagini in una cartella stabile;
- usare riferimenti coerenti e verificabili;
- controllare i riferimenti dopo riapertura del disegno;
- includere sempre gli asset necessari quando si sposta una commessa.

## Gestione immagini

La gestione immagini permette di vedere i riferimenti presenti nel progetto e di scollegare o ricollegare asset esterni.

Procedure tipiche:

- verificare quali immagini sono collegate;
- ricollegare un'immagine non trovata;
- scollegare un'immagine non più utilizzata;
- salvare il nuovo percorso;
- verificare dopo riapertura.

## Cartiglio master con logo

Workflow consigliato:

1. aprire il file master del cartiglio;
2. inserire il logo come immagine collegata;
3. usare un percorso stabile;
4. salvare il file;
5. chiudere e riaprire per verificare che il logo resti visibile;
6. testare il cartiglio in un multifoglio di prova.

## Problema: riquadro al posto dell'immagine

Se nel multifoglio compare un riquadro o un riferimento testuale al posto dell'immagine, il collegamento non è stato risolto correttamente.

Checklist:

- verificare se il frame immagine è visibile;
- controllare il nome del file immagine;
- controllare il percorso del riferimento;
- rigenerare la visualizzazione;
- ricaricare o correggere il collegamento;
- ripetere il test chiudendo e riaprendo il progetto.

## Bordo immagini

Le immagini possono essere visualizzate con un bordo o frame.

Regola operativa:

- il frame va gestito nel progetto corrente;
- anche se il cartiglio master è già stato configurato, un nuovo progetto può richiedere una verifica dedicata;
- controllare sempre la visualizzazione dopo inserimento cartiglio o pagina standard.

## Cartella immagini consigliata

Per loghi e immagini ricorrenti usare una cartella risorse stabile, ad esempio:

```text
97_RISORSE/IMMAGINI
```

Regole:

- non spostare immagini dopo l'inserimento;
- non rinominare file già referenziati;
- non eliminare file sorgente usati da cartigli o pagine standard;
- verificare sempre salvataggio e riapertura.

## Raster vs vettoriale

Per loghi ricorrenti esistono due approcci:

- immagine raster con riferimento controllato;
- geometria vettoriale integrata nel DWG.

La scelta dipende da robustezza richiesta, semplicità del workflow e frequenza di riutilizzo.

## Checklist finale

Prima di considerare stabile una pagina o un cartiglio:

- verificare attributi editabili;
- verificare immagini collegate;
- testare in un progetto prova;
- chiudere e riaprire;
- verificare su una copia della commessa.
