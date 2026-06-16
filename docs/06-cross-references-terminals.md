# Rimandi, cross-reference e morsetti

Questa sezione raccoglie note operative su rimandi, alimentazioni, cross-reference e rappresentazione dei morsetti in SPAC Start.

## Cross-reference

Il cross-reference dei rimandi è una procedura comune sia allo schema unifilare sia allo schema multifilare.

Principio operativo:

- i collegamenti da mettere in relazione devono usare lo stesso nome;
- un rimando di partenza deve essere coerente con un rimando di arrivo;
- dopo la creazione dei rimandi è necessario aggiornare il cross-reference.

## Direzione dei rimandi

Regole:

- se il primo rimando è di partenza, il secondo deve essere di arrivo oppure arrivo/partenza;
- se il primo rimando è di arrivo, il secondo deve essere di partenza oppure arrivo/partenza;
- la direzione deve essere coerente con il flusso logico dello schema.

## Aggiornamento cross-reference

Dopo aver creato o modificato rimandi:

1. aprire la funzione cross-reference;
2. selezionare l'elaborazione dedicata ai rimandi;
3. avviare l'aggiornamento;
4. verificare eventuale output generato;
5. controllare che i riferimenti puntino alle posizioni corrette.

## Rimandi per alimentazioni

I rimandi permettono di collegare graficamente e logicamente alimentazioni o segnali tra fogli diversi.

Prima di inserire un rimando:

- verificare che la linea sia riconosciuta come alimentazione o collegamento corretto;
- selezionare l'oggetto intelligente, non una semplice linea CAD;
- evitare entità grafiche duplicate o residue;
- rigenerare/verificare i riferimenti dopo modifiche importanti.

## Lista rimandi usati

Per controllare i rimandi presenti nello schema, usare la funzione che mostra la lista dei numeri usati e filtrare i soli rimandi.

Questa lista è utile per:

- individuare rimandi duplicati;
- verificare nomi usati;
- trovare ripetizioni;
- controllare riferimenti non più coerenti.

Nota: i numeri segnalati come ripetuti devono essere verificati prima di procedere con ulteriori modifiche.

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

## Eliminare numerazione fili

La funzione di eliminazione numerazione fili rimuove i numeri filo, ma non cancella i fili dallo schema.

Usarla quando è necessario pulire una numerazione errata prima di rigenerarla.

## Morsetti

Per i morsetti, distinguere sempre tra:

- nome morsettiera;
- numero morsetto;
- numero filo;
- riferimento funzionale;
- rappresentazione grafica selezionata.

Prima di inserire morsetti è consigliato nominare i fili presenti nella pagina.

## Morsettiere

Durante la gestione morsettiere, verificare:

- quadro di appartenenza;
- morsettiera selezionata;
- tipo morsetto;
- progressione dei morsetti;
- rappresentazione scelta.

Per creare una nuova morsettiera, usare il menu contestuale della gestione morsettiere e assegnare un nome coerente.

## Inserimento morsetto

Workflow generale:

1. selezionare la morsettiera;
2. scegliere il tipo morsetto;
3. creare un nuovo morsetto;
4. selezionare il filo interessato;
5. verificare il punto di inserimento;
6. controllare rappresentazione e dati.

Il punto in cui viene selezionato il filo determina il punto di inserimento del morsetto.

## Rappresentazione morsetti

Sigle operative:

| Sigla | Significato |
|---|---|
| `NumI` | Numero filo di ingresso nel morsetto |
| `NumO` | Numero filo di uscita dal morsetto |
| `NumM` | Numero di morsetto |

Per una lettura più chiara dello schema, preferire rappresentazioni che mostrino `NumM` insieme al nome della morsettiera.

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

## Baseline sezione

La sezione rimandi e morsetti è completa come riferimento operativo quando copre:

- principio del cross-reference tra rimandi;
- direzione coerente arrivo/partenza;
- aggiornamento dei riferimenti;
- controllo lista rimandi usati;
- diagnosi di selezioni non valide;
- pulizia numerazione fili;
- gestione morsettiere e inserimento morsetti;
- differenza tra `NumI`, `NumO` e `NumM`;
- verifica finale della rappresentazione morsetti.

Nuove anomalie ricorrenti vanno documentate come known issue o playbook dedicato.
