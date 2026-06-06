# Pagine standard, cartigli e immagini

Questa sezione raccoglie note operative per gestire pagine standard, cartigli e loghi in SPAC Start.

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

## Immagini e loghi

Quando un logo o un'immagine non viene visualizzato, il problema è spesso legato a un riferimento esterno non risolto.

Approccio pratico consigliato:

- mantenere le immagini in una cartella stabile;
- usare riferimenti coerenti e verificabili;
- controllare i riferimenti dopo riapertura del disegno;
- includere sempre gli asset necessari quando si sposta una commessa.

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
