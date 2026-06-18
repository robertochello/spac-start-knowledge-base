# Playbook — Gestire cartiglio e logo

## Obiettivo

Gestire loghi e immagini nei cartigli riducendo problemi di riferimenti mancanti o non caricati.

## Quando usarlo

Usare questo playbook quando:

- un logo non viene visualizzato;
- nel multifoglio compare un riquadro al posto dell'immagine;
- una pagina standard deve essere riutilizzata;
- un cartiglio master contiene immagini collegate.

## Flusso operativo

```mermaid
flowchart TD
    A[Cartiglio con logo]:::data --> B[Percorso stabile]:::warn
    B --> C[Test master]:::process
    C --> D[Test multifoglio]:::process
    D --> E{Logo visibile?}:::warn
    E -->|Sì| F[Standardizzabile]:::ok
    E -->|No| G[Verifica riferimento]:::danger
    G --> B

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef danger fill:#fdecea,stroke:#c62828,color:#7f1d1d;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

## Procedura

### 1. Usare asset controllati

- Mantenere il logo in una posizione stabile.
- Evitare riferimenti casuali o temporanei.
- Non dipendere da file locali non documentati.

### 2. Testare il cartiglio master

- Aprire il file master.
- Verificare che il logo sia visibile.
- Salvare.
- Chiudere e riaprire.

### 3. Testare nel multifoglio

- Applicare il cartiglio a un progetto prova.
- Verificare la visibilità del logo.
- Controllare eventuali riquadri o riferimenti non risolti.

### 4. Risolvere riferimenti non caricati

Se compare un riquadro al posto dell'immagine:

- controllare il nome del file;
- controllare il riferimento;
- ricaricare l'immagine;
- ripetere il test dopo riapertura.

## Verifica finale

Il cartiglio è stabile quando:

- il logo è visibile nel master;
- il logo è visibile nel multifoglio;
- la visibilità resta corretta dopo riapertura;
- la procedura è ripetibile.

## Collegamenti

- [Pagine, cartigli e immagini](../05-pages-titleblocks-images.md)
- [Troubleshooting](../07-troubleshooting.md)
