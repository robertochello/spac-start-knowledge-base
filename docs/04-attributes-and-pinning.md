# Attributi e pinatura

Questa sezione raccoglie le convenzioni operative sugli attributi principali dei simboli custom SPAC e sulla gestione della pinatura.

## Attributi principali

Attributi ricorrenti da considerare nei simboli custom:

| Attributo | Uso operativo |
|---|---|
| `NOME` | Identificativo del componente |
| `PRES` | Presenza/tipo simbolo, ad esempio Madre |
| `DESCRIZIONE` | Descrizione funzionale |
| `TIPO` | Tipo componente |
| `COSTRUTTORE` | Costruttore o marca |
| `QUADRO` | Quadro o area di appartenenza |

## Simbolo Madre

Per indicare un simbolo Madre:

```text
PRES = M
```

Questa convenzione aiuta a distinguere il componente principale dagli eventuali elementi collegati.

## Pinatura standard

Per i simboli SPAC custom, lo standard adottato è:

```text
PINA1
PINA2
PINA3
...
```

La presenza di `PINB`, con lo stesso numero incrementale, indica che il segnale presente su `PINA<n>` viene riportato in uscita su `PINB<n>`.

Esempio:

| Ingresso | Uscita collegata | Significato |
|---|---|---|
| `PINA1` | `PINB1` | Il segnale entra su PINA1 e viene riportato su PINB1 |
| `PINA2` | `PINB2` | Il segnale entra su PINA2 e viene riportato su PINB2 |

## Quando usare solo PINA

Usare solo `PINA<n>` quando il simbolo rappresenta un punto di connessione singolo o non deve riportare il segnale in uscita.

## Quando usare PINA e PINB

Usare `PINA<n>` + `PINB<n>` quando il simbolo è attraversato da un collegamento o quando il segnale deve essere rappresentato in ingresso e uscita.

## Posizione dei pin

La posizione dei pin deve essere coerente con la griglia di disegno.

Linee guida:

- allineare i pin alla griglia;
- evitare posizioni arbitrarie;
- verificare aggancio fili dopo l'inserimento;
- testare il simbolo in un progetto prova;
- mantenere coerenza tra orientamento grafico e significato del pin.

## Test consigliati

Dopo aver creato o modificato un simbolo:

1. inserirlo in un progetto di prova;
2. verificare modifica attributi;
3. collegare fili ai pin;
4. controllare aggancio e continuità grafica;
5. verificare eventuali report o associazioni materiali;
6. aggiornare l'inventario simboli custom.

## Nota su PINB

Non usare `PINB` se non serve realmente riportare il segnale. Una pinatura eccessiva o non coerente rende il simbolo più difficile da mantenere.
