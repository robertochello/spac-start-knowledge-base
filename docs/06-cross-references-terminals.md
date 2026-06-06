# Rimandi, cross-reference e morsetti

Questa sezione raccoglie note operative su rimandi, alimentazioni, cross-reference e rappresentazione dei morsetti in SPAC Start.

## Rimandi per alimentazioni

I rimandi permettono di collegare graficamente e logicamente alimentazioni o segnali tra fogli diversi.

Prima di inserire un rimando:

- verificare che la linea sia riconosciuta come alimentazione o collegamento corretto;
- selezionare l'oggetto intelligente, non una semplice linea CAD;
- evitare entità grafiche duplicate o residue;
- rigenerare/verificare i riferimenti dopo modifiche importanti.

## Quando la selezione risulta non valida

Se selezionando una linea il comando segnala selezione non valida, possibili cause:

- la linea è solo geometria CAD;
- l'alimentazione non è stata creata con il comando SPAC corretto;
- l'oggetto intelligente è stato esploso o alterato;
- esistono vecchi oggetti sovrapposti;
- la selezione avviene su un elemento grafico e non sul collegamento riconosciuto.

## Cross-reference non aggiornati

Se un cross-reference punta a una posizione dove prima esisteva un collegamento ma ora non più, controllare:

- vecchi oggetti intelligenti rimasti nel foglio;
- rimandi non più utilizzati;
- riferimenti non rigenerati;
- alimentazioni duplicate;
- oggetti cancellati graficamente ma non rimossi logicamente.

## Morsetti

Per i morsetti, distinguere sempre tra:

- nome morsettiera;
- numero morsetto;
- numero filo;
- riferimento funzionale;
- rappresentazione grafica selezionata.

Se sul morsetto compare il numero filo invece del numero morsetto, il problema è probabilmente nella configurazione della rappresentazione grafica o nei dati visualizzati dal simbolo morsetto.

## Checklist morsetti

Quando la rappresentazione del morsetto non è corretta:

1. verificare proprietà del morsetto;
2. controllare dati morsettiera;
3. verificare campi visualizzati dal simbolo;
4. controllare impostazioni grafiche della rappresentazione;
5. aggiornare o rigenerare i riferimenti;
6. testare su un morsetto nuovo in progetto prova.

## Regola pratica

Non correggere solo il testo visibile se l'oggetto è intelligente. Verificare sempre il dato sorgente e la configurazione grafica che lo mostra.
