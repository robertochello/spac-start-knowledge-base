# Esempi operativi

Questa sezione raccoglie esempi generici, non legati a commesse reali, utili per spiegare procedure e standard della knowledge base.

## Obiettivo

Fornire riferimenti visuali semplici per chiarire concetti ricorrenti:

- simbolo Madre;
- simbolo cablato;
- rappresentazione morsetto;
- record materiale.

## Esempio 1 — Simbolo Madre

```mermaid
flowchart LR
    A[Simbolo Madre]:::data --> B[Attributi]:::data
    A --> C[Materiale]:::process
    A --> D[Inventario]:::process
    B --> E[Test progetto]:::warn
    C --> E
    E -->|OK| F[Riutilizzabile]:::ok

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

Un simbolo Madre rappresenta il componente principale. Può avere materiale associabile anche quando non ha pin.

Verifiche minime:

- ruolo del simbolo chiaro;
- attributi principali presenti;
- eventuale materiale associato al componente corretto;
- inventario aggiornato.

## Esempio 2 — Simbolo cablato

```mermaid
flowchart LR
    A[PINA]:::data --> B[Simbolo cablato]:::data
    B --> C[PINB]:::data
    B --> D[Test aggancio]:::warn
    D -->|OK| E[Pinatura valida]:::ok
    D -->|KO| F[Correggere pin]:::todo

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef todo fill:#f3e8ff,stroke:#7b1fa2,color:#4a148c;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
```

Un simbolo cablato deve avere punti di connessione coerenti. Se il segnale deve attraversare il simbolo, la relazione tra ingresso e uscita deve essere chiara.

Verifiche minime:

- pin allineati;
- numerazione coerente;
- aggancio filo testato;
- simbolo validato in progetto prova.

## Esempio 3 — Morsetto

```mermaid
flowchart LR
    A[Oggetto morsetto]:::data --> B[Dati sorgente]:::data
    B --> C[Rappresentazione]:::process
    C --> D[Testo visibile]:::process
    D --> E{Dato corretto?}:::warn
    E -->|Sì| F[OK]:::ok
    E -->|No| G[Verificare campo]:::danger

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef danger fill:#fdecea,stroke:#c62828,color:#7f1d1d;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

La rappresentazione del morsetto deve mostrare il dato corretto. Non correggere manualmente il testo visibile senza verificare il campo sorgente.

Verifiche minime:

- morsettiera corretta;
- numero morsetto corretto;
- dato visualizzato coerente;
- rappresentazione testata su morsetto nuovo.

## Esempio 4 — Record materiale

```mermaid
flowchart LR
    A[Codice reale]:::data --> B[Descrizione]:::data
    B --> C[Categoria]:::process
    C --> D[Stato]:::warn
    D --> E[Associazione simbolo]:::process
    E -->|Verificata| F[Record valido]:::ok
    E -->|Non verificata| G[Da verificare]:::todo

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef todo fill:#f3e8ff,stroke:#7b1fa2,color:#4a148c;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

Un materiale è pronto per il riuso solo quando i dati minimi sono coerenti e lo stato è documentato.

Verifiche minime:

- codice coerente;
- descrizione chiara;
- categoria assegnata;
- stato definito;
- associazione a simbolo verificata.

## Collegamenti

- [Simboli custom](03-custom-symbols.md)
- [Attributi e pinatura](04-attributes-and-pinning.md)
- [Rimandi, cross-reference e morsetti](06-cross-references-terminals.md)
- [Archivi materiali custom](21-material-archives.md)
- [Quality gates](14-quality-gates.md)
