# Nomenclatura simboli

Questa sezione definisce la convenzione di nomenclatura per i simboli custom.

## Obiettivo

I nomi dei simboli devono essere:

- sintetici;
- leggibili;
- coerenti;
- facilmente ricercabili;
- compatibili con il limite massimo di 32 caratteri per il nome base.

## Nome base

Il nome base è il nome del file senza estensione.

Esempio:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

Nome base:

```text
NOME_SIMBOLO
```

Il file DWG e il file SLD devono avere lo stesso nome base.

## Formato consigliato

Formato logico:

```text
FAMIGLIA_TIPO_POLI_ESECUZIONE_AZIONAMENTO_ACCESSORI
```

Non tutti i campi sono obbligatori. Inserire solo i campi necessari a distinguere correttamente il simbolo.

## Significato dei campi

| Campo | Significato | Esempi |
|---|---|---|
| FAMIGLIA | Classe principale del simbolo | INT, TOR, MULT, ATT, SPIA |
| TIPO | Tipo funzionale principale | MT, MTD, SEZ, MAN, RELE, FUS |
| POLI | Numero poli se utile | 1P, 3P, 4P |
| ESECUZIONE | Caratteristica meccanica o costruttiva | ESTR, FUS |
| AZIONAMENTO | Modalità di comando | MOT, MAN |
| ACCESSORI | Accessori o funzioni aggiuntive | SGL, AUS, SCAMBIO |

## Regole formali

- Usare lettere maiuscole.
- Non usare spazi.
- Non usare accenti.
- Non usare caratteri speciali.
- Usare underscore come separatore.
- Non superare 32 caratteri nel nome base.
- Demandare la descrizione estesa all'inventario, non al nome file.

## Priorità dei campi

Ordine consigliato:

```text
FAMIGLIA → TIPO → POLI → ESECUZIONE → AZIONAMENTO → ACCESSORI
```

## Esempi

| Caso | Nome consigliato |
|---|---|
| Interruttore magnetotermico estraibile con ausiliari | INT_MT_ESTR_AUS |
| Interruttore magnetotermico estraibile motorizzato con ausiliari | INT_MT_ESTR_MOT_AUS |
| Interruttore magnetotermico differenziale con ausiliari | INT_MTD_AUS |
| Interruttore sezionatore manuale unipolare fusibilato | INT_SEZ_MAN_1P_FUS |
| Interruttore manuale con contatto di scambio | INT_MAN_SCAMBIO |

## Nota su SCAMBIO

Per i nuovi simboli usare `SCAMBIO` come termine esplicito. Evitare abbreviazioni ambigue se il nome resta entro il limite massimo.

## Collegamenti

- [Libreria custom](15-custom-library.md)
- [Standard simboli](standards/symbols.md)
