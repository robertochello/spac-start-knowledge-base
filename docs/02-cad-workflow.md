# Workflow CAD 2D

SPAC Start può essere usato anche per disegno CAD 2D quando il contenuto non è direttamente elettrico.

In questi casi il disegno planimetrico/CAD è più coerente rispetto a un ambiente unifilare o multifilare, che sono orientati alla rappresentazione elettrica intelligente.

## Quando usare il disegno CAD/planimetrico

Usare il workflow CAD/planimetrico quando serve:

- disegnare strutture 2D;
- preparare viste dall'alto;
- creare quote e ingombri;
- importare o adattare geometrie DWG;
- produrre elementi grafici non elettrici.

## Layer

Per file CAD/DXF/DWG destinati a SPAC, mantenere le entità sul:

```text
Layer 0
```

Questo riduce problemi di importazione, visibilità e gestione grafica.

## Rettangoli e geometrie

Per disegnare rettangoli o cornici:

- definire sempre unità di misura e quote;
- verificare se il rettangolo è solo contorno o pieno;
- evitare tratteggi o riempimenti se non sono necessari;
- usare offset controllati per rettangoli interni.

## Rettangoli pieni e tratteggi

Per indicare in vista dall'alto un elemento pieno o una zona non vuota, usare un tratteggio coerente e leggibile.

Linee guida:

- evitare riempimenti troppo scuri se coprono quote o riferimenti;
- usare tratteggi semplici per sezioni o parti piene;
- mantenere lo stile coerente in tutto il disegno;
- aggiungere legenda se il significato non è evidente.

## Scala e disegni copiati

Quando un disegno copiato da un altro DWG risulta troppo piccolo o fuori scala:

1. identificare una quota reale nota;
2. misurare la quota attuale nel disegno importato;
3. calcolare il fattore di scala;
4. applicare la scala all'insieme selezionato;
5. verificare nuovamente una quota nota.

## Blocchi CAD

Per creare blocchi DWG da elementi esistenti:

1. partire da geometria pulita;
2. esplodere eventuali oggetti complessi solo se necessario;
3. rimuovere entità inutili;
4. portare tutto su Layer 0;
5. creare il blocco;
6. testare inserimento, scala e visibilità.

## Test minimi

Prima di riutilizzare una geometria CAD in una commessa:

- aprire il file in un progetto di prova;
- verificare scala;
- verificare layer;
- verificare eventuali riferimenti esterni;
- controllare che non ci siano entità invisibili o inutili.
