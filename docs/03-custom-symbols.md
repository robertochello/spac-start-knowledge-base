# Simboli custom

Questa sezione definisce il workflow operativo per creare e gestire simboli custom in SPAC Start.

## Concetto generale

In SPAC è importante distinguere tra:

- **grafica CAD**: semplice disegno, non intelligente;
- **blocco CAD**: insieme di entità raggruppate;
- **simbolo SPAC intelligente**: oggetto riconosciuto da SPAC, con attributi e logiche applicative.

Un simbolo custom utile deve essere riconoscibile e gestibile come componente SPAC, non solo come geometria grafica.

## Workflow generale

```mermaid
flowchart LR
    A[Disegno sorgente] --> B[Pulizia]
    B --> C[Normalizzazione]
    C --> D[Blocco DWG]
    D --> E[Anteprima SLD]
    E --> F[Attributi]
    F --> G[Test]
    G --> H[Inventario]
```

## Creazione elemento grafico

Questa procedura serve quando si parte da:

- DWG esterno;
- simbolo SPAC esistente;
- geometria disegnata manualmente.

Regole iniziali:

- lavorare in un foglio o progetto di prova;
- non usare una commessa reale come laboratorio;
- pulire il disegno da testi o linee non necessarie;
- normalizzare layer, colore, tipo linea e spessore.

## Importazione da DWG esterno

Dopo aver importato un DWG esterno:

1. verificare scala;
2. verificare layer;
3. eliminare attributi o testi non necessari;
4. esplodere solo se serve realmente;
5. normalizzare il disegno;
6. trasformarlo in blocco riutilizzabile.

## Importazione da simbolo SPAC esistente

Un simbolo esistente può essere usato come base, ma va sempre ripulito.

Checklist:

- rimuovere attributi non pertinenti;
- verificare logica Madre/Figlio;
- controllare pinatura;
- rinominare secondo convenzione;
- testare il nuovo simbolo come entità autonoma.

## Pulizia e normalizzazione

Per i simboli custom:

- usare Layer 0;
- colore DaBlocco;
- tipo linea DaBlocco;
- spessore linea DaBlocco;
- eliminare elementi non necessari;
- mantenere il disegno leggibile e scalato.

## Creazione blocco DWG

Quando la geometria è pronta:

1. selezionare gli oggetti del simbolo;
2. creare il blocco DWG;
3. scegliere un punto base coerente;
4. salvare nella categoria corretta della libreria custom;
5. usare il nome secondo la convenzione;
6. lasciare l'unità senza forzature se il simbolo deve restare generico.

Per simboli puramente grafici, il punto base può essere il centro grafico. Per simboli con pin, il punto base deve aiutare l'inserimento coerente nello schema.

## Creazione anteprima SLD

Ogni blocco DWG custom deve avere un'anteprima coerente.

Regole:

- aprire il DWG del simbolo;
- centrare il disegno;
- regolare lo zoom;
- creare la slide SLD;
- salvare la slide nella stessa cartella del DWG;
- usare lo stesso nome base.

Regola obbligatoria:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

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

## Simbolo Figlio

Un simbolo Figlio rappresenta un elemento collegato a un componente Madre, ad esempio:

- contatti ausiliari;
- bobine;
- accessori;
- elementi funzionali associati.

La relazione Madre/Figlio deve essere chiara e verificabile nel progetto.

Regola operativa:

- Madre con `PRES = M`;
- Figlio con `PRES = F`;
- Figlio con lo stesso `NOME` della Madre quando deve essere associato logicamente.

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

## Associazione materiale

Un simbolo intelligente può avere materiali associati se deve contribuire alla distinta.

Regole:

- associare materiali solo a simboli riconosciuti;
- evitare materiali su pura grafica;
- verificare report o distinta;
- documentare eccezioni.

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
