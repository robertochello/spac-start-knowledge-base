# Concetti SPAC

Questa pagina raccoglie i concetti fondamentali usati nella knowledge base.

## In questa pagina impari

- la differenza tra geometria CAD e oggetto SPAC intelligente;
- perché attributi, pinatura e dati sorgente non sono semplice testo;
- quando un problema va cercato nella rappresentazione e non nel disegno;
- quali pagine usare per approfondire simboli, morsetti, rimandi e materiali.

## Mappa concettuale

```mermaid
flowchart LR
    A[Grafica CAD]:::process --> B[Blocco CAD]:::process
    B --> C[Oggetto SPAC]:::data
    C --> D[Attributi]:::data
    C --> E[Pinatura]:::data
    C --> F[Materiali]:::data
    C --> G[Rimandi]:::warn
    D --> H[Madre/Figlia]:::data
    E --> I[PINA/PINB]:::data

    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

## Distinzione operativa

Molti problemi nascono quando un elemento visibile viene scambiato per un dato
logico SPAC. Usare questa tabella prima di correggere graficamente un oggetto.

| Elemento | È | Non è | Dove approfondire |
|---|---|---|---|
| Grafica CAD | geometria visibile nel disegno | un collegamento logico SPAC | [Workflow CAD 2D](02-cad-workflow.md) |
| Blocco CAD | gruppo riutilizzabile di entità | garanzia di comportamento elettrico | [Simboli custom](03-custom-symbols.md) |
| Simbolo SPAC intelligente | oggetto riconosciuto con dati e relazioni | solo una forma grafica | [Attributi e pinatura](04-attributes-and-pinning.md) |
| Attributi | dati associati al simbolo | testo libero senza effetto operativo | [Checklist validazione simbolo](10-symbol-validation-checklist.md) |
| Dati sorgente | informazione usata da report, rimandi o rappresentazioni | necessariamente il testo visibile nel foglio | [Rimandi e morsetti](06-cross-references-terminals.md) |
| Rappresentazione | modo in cui un dato viene mostrato | prova che il dato sorgente sia corretto | [Verificare rappresentazione morsetti](playbooks/terminal-representation.md) |

Il percorso corretto di diagnosi è questo.

```mermaid
flowchart LR
    A[Elemento visibile]:::info --> B{Solo grafica?}:::warn
    B -->|Sì| C[Controllare disegno]:::process
    B -->|No| D[Oggetto SPAC]:::data
    D --> E[Dati sorgente]:::data
    E --> F[Rappresentazione]:::process
    F --> G[Report o rimandi]:::ok

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef info fill:#e8f0fe,stroke:#1565c0,color:#0d47a1;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

!!! warning "Errore tipico"

    Se il testo visibile è sbagliato, non modificarlo manualmente prima di
    avere controllato oggetto, attributi, dato sorgente e rappresentazione.

## Grafica CAD

È semplice geometria. Può essere utile per disegno 2D, layout, cornici o elementi non elettrici, ma non ha automaticamente logica SPAC.

## Blocco CAD

È un insieme di entità raggruppate. Può essere comodo per il riuso grafico, ma non garantisce che SPAC lo riconosca come componente.

## Simbolo SPAC intelligente

È un oggetto riconosciuto da SPAC e gestibile tramite attributi, pinatura, relazioni e associazioni.

## Attributi

Gli attributi sono il livello informativo del simbolo. Permettono di gestire nome, descrizione, tipo, costruttore, quadro e ruolo del simbolo.

## Pinatura

La pinatura definisce i punti di connessione. In questa knowledge base si usa lo standard PINA/PINB.

## Madre/Figlia

La Madre è il componente principale. La Figlia è un elemento associato. La relazione deve essere chiara, documentata e testata.

## Rimandi e cross-reference

I rimandi servono a mantenere coerenza tra fogli, collegamenti e riferimenti. Non devono essere trattati come pura grafica.

## Regola chiave

Prima di correggere un problema visivo, capire se il problema è:

- grafico;
- attributivo;
- logico;
- di configurazione;
- di riferimento.
