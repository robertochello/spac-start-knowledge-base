# Simboli custom

Questa sezione definisce il workflow operativo per creare e gestire simboli custom in SPAC Start.

## Concetto generale

In SPAC è importante distinguere tra:

- **grafica CAD**: semplice disegno, non intelligente;
- **blocco CAD**: insieme di entità raggruppate;
- **simbolo SPAC intelligente**: oggetto riconosciuto da SPAC, con attributi e logiche applicative.

Un simbolo custom utile deve essere riconoscibile e gestibile come componente SPAC, non solo come geometria grafica.

## Simbolo Madre

Un simbolo Madre rappresenta il componente principale.

Convenzione operativa:

```text
PRES = M
```

Esempi di simboli che possono essere gestiti come Madre:

- selettori;
- attuatori a chiave;
- dispositivi modulari;
- componenti senza pin ma con materiale associabile.

## Simbolo Figlia

Un simbolo Figlia rappresenta un elemento collegato a un componente Madre, ad esempio:

- contatti ausiliari;
- bobine;
- accessori;
- elementi funzionali associati.

La relazione Madre/Figlia deve essere chiara e verificabile nel progetto.

## Simboli senza pin

Un simbolo può essere utile anche senza pin se rappresenta un componente riconosciuto e associabile a materiali.

Esempio: attuatore a chiave rappresentato come simbolo Madre senza pin.

Prefisso consigliato per attuatori/selettori:

```text
SA
```

## Simboli cablati

Per simboli cablati, la pinatura deve essere gestita con attributi coerenti.

Gli attributi di pin principali sono documentati in:

```text
04-attributes-and-pinning.md
```

## Simboli complessi

Per simboli complessi, evitare un unico oggetto ingestibile.

Workflow consigliato:

- creare simboli semplici e coerenti;
- usare macro per raggruppare insiemi ricorrenti;
- mantenere chiara la relazione tra elementi;
- testare ogni simbolo singolarmente prima di inserirlo in macro.

## Inventario simboli

L'inventario completo dei simboli custom non deve stare nel README.

Convenzione consigliata:

```text
SPAC_Custom_Simboli_Convenzione.xlsx
```

Il file Excel può contenere:

- nome simbolo;
- descrizione;
- categoria;
- attributi principali;
- presenza pin;
- materiale associabile;
- stato di validazione;
- note operative.

## Checklist simbolo custom

Prima di considerare un simbolo custom riutilizzabile:

- verificare attributi principali;
- verificare eventuale PRES;
- verificare pinatura se presente;
- testare modifica attributi con editor attributi;
- testare inserimento in progetto prova;
- testare associazione materiale se richiesta;
- documentare nome e convenzione nell'inventario.
