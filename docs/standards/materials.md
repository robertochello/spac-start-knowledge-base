# Standard materiali

## Obiettivo

Definire regole operative per gestire materiali, archivi custom e associazioni ai simboli.

## Regole principali

- Ogni materiale deve avere un codice identificativo chiaro.
- La descrizione deve essere sintetica ma utile.
- Il costruttore deve essere compilato quando noto.
- La categoria deve essere coerente con la funzione del materiale.
- Ogni record deve avere uno stato.
- I materiali non verificati non devono essere trattati come standard.
- I codici catalogo devono essere reali e verificabili.
- Non usare codici fittizi o iniziali personali nei codici catalogo.

## Stati ammessi

| Stato | Uso |
|---|---|
| Bozza | Record iniziale non ancora revisionato |
| Da verificare | Record plausibile ma non validato |
| Validato | Record testato e utilizzabile |
| Deprecato | Record da non usare per nuovi progetti |

## Associazione ai simboli

Associare il materiale al simbolo più coerente con il componente reale.

Linee guida:

- componente principale: materiale sul simbolo principale;
- accessorio separato: materiale sul simbolo dedicato;
- pura grafica: evitare associazione materiale stabile;
- casi ambigui: documentare la scelta nel decision log.

## Archivio, associazione e report

Distinguere sempre:

| Livello | Verifica |
|---|---|
| Archivio materiali | Record ricercabile e normalizzato |
| Associazione simbolo | Materiale collegato a simbolo coerente |
| Distinta o report | Materiale presente senza duplicazioni |
| File pubblicato | Archivio tracciato, sanitizzato e versionato |

## Import archivi

Ogni import deve passare da:

1. backup;
2. normalizzazione;
3. controllo duplicati;
4. ambiente di prova;
5. validazione;
6. verifica distinta o report;
7. promozione a standard.

## Regola finale

Un materiale è davvero utile solo se può essere ricercato, associato, riportato e mantenuto senza ambiguità.
