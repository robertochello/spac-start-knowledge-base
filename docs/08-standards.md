# Standard operativi

Questa sezione raccoglie convenzioni generali per mantenere la knowledge base e i workflow SPAC ordinati e riutilizzabili.

## Standard generali

- Usare nomi chiari e descrittivi.
- Evitare abbreviazioni non documentate.
- Separare guida, template, troubleshooting e inventari.
- Non inserire dati riservati o specifici di commessa.
- Documentare sempre cosa è testato e cosa è da verificare.

## Layer CAD

Per file CAD/DXF/DWG destinati a SPAC:

```text
Layer 0
```

Questa convenzione riduce problemi di importazione, visibilità e gestione grafica.

## Simboli custom

Ogni simbolo custom dovrebbe avere:

- nome coerente;
- attributi principali;
- eventuale `PRES` se simbolo Madre;
- pinatura coerente se cablato;
- test in progetto prova;
- voce nell'inventario simboli.

## Pinatura

Standard adottato:

```text
PINA<n>
PINB<n>
```

`PINB<n>` si usa solo quando serve riportare in uscita il segnale associato a `PINA<n>`.

## Contatti di scambio

Per indicare un contatto di scambio, usare l'abbreviazione documentata:

```text
SCB
```

Non introdurre abbreviazioni alternative.

## Inventario simboli

L'inventario completo dei simboli custom deve stare in un file separato, non nel README.

Nome consigliato:

```text
SPAC_Custom_Simboli_Convenzione.xlsx
```

## Documentazione

Ogni file Markdown deve essere:

- breve;
- specifico;
- facilmente aggiornabile;
- collegato ad altri file quando necessario;
- privo di dati non pubblicabili.

## Stato delle sezioni

Usare una delle seguenti etichette quando necessario:

| Stato | Significato |
|---|---|
| `Testato` | Procedura verificata praticamente |
| `Da verificare` | Nota plausibile ma non ancora consolidata |
| `In revisione` | Contenuto da completare o correggere |
| `Deprecato` | Procedura superata o non consigliata |

## Regola editoriale

La knowledge base deve restare operativa. Evitare testi troppo teorici se non portano a una procedura, una scelta tecnica o una checklist.
