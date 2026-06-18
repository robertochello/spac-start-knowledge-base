# Back-check e controlli incrociati

Questa pagina definisce i controlli minimi da eseguire prima di considerare riutilizzabile una modifica agli archivi SPAC, in particolare `DbCables.db`.

## Obiettivo

Evitare che una modifica funzioni solo nell'ambiente di test ma fallisca nell'ambiente reale di destinazione.

Il back-check deve verificare:

- integrità del file modificato;
- presenza del backup;
- visibilità dei dati da interfaccia SPAC;
- coerenza dei dati tecnici;
- reversibilità tramite rollback.

## Quando usarlo

Usare questa checklist quando:

- si sostituisce `DbCables.db`;
- si importano o aggiornano archivi materiali;
- si porta una libreria custom da un PC a un altro;
- una procedura deve valere sia in SPAC Automazione sia in SPAC Start;
- un archivio deve essere usato in commessa reale.

## Flusso di controllo

```mermaid
flowchart LR
    A[Backup]:::warn --> B[File modificato]:::data
    B --> C[Controllo dati]:::warn
    C --> D[Test in SPAC]:::process
    D --> E[Report o uso]:::process
    E --> F[Rollback]:::warn
    F --> G[Rilascio o verifica]:::ok

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

!!! warning "Da verificare"
    Il rilascio è possibile solo se ogni passaggio ha un esito documentabile.
    In caso contrario lo stato resta `Da verificare`.

## Controlli prima dell'avvio

| Controllo | Esito atteso |
|---|---|
| Backup originale | File presente e ripristinabile |
| File modificato | Nome e percorso corretti |
| Integrità database | Nessun errore rilevato |
| Record custom | Marcatura o release riconoscibile |
| Dati collegati | Nessun record orfano evidente |
| Codici catalogo | Nessun codice fittizio o con iniziali personali |
| Materiale reale di test | Codice, costruttore e descrizione identificati |
| Cavo reale di test | Costruttore e codice produttore identificati |
| Ambiente test | Identificato prima della prova |

## Controlli in SPAC

| Controllo | Esito atteso |
|---|---|
| Avvio software | Nessun blocco |
| Allineamento librerie | Completato se richiesto |
| Archivio consultabile | Finestra aperta correttamente |
| Record custom visibile | Ricerca positiva |
| Dettaglio tecnico | Campi popolati e coerenti |
| Conduttori | Dettaglio conduttori visibile e coerente |
| Associazione simbolo | Materiale associabile a un simbolo riconosciuto |
| Distinta o report | Nessuna duplicazione o omissione evidente |
| Uso operativo | Il dato è selezionabile nella funzione prevista |

## Controllo incrociato ambienti

Quando la modifica deve essere valida su più installazioni, ripetere gli stessi check su ogni ambiente.

| Check | SPAC Automazione | SPAC Start |
|---|---|---|
| Avvio software | OK / KO | OK / KO |
| Archivio consultabile | OK / KO | OK / KO |
| Record custom ricercabile | OK / KO | OK / KO |
| Dati tecnici visibili | OK / KO | OK / KO |
| Conduttori coerenti | OK / KO | OK / KO |
| Uso operativo testato | OK / KO | OK / KO |
| Rollback verificato | OK / KO | OK / KO |

## Criterio di rilascio

Una modifica può essere considerata pronta solo se:

- passa i controlli minimi nell'ambiente di destinazione;
- il rollback è stato verificato;
- eventuali dati tecnici sono stati validati su fonte attendibile;
- almeno un materiale reale è stato associato e verificato in distinta/report;
- almeno un cavo reale è stato testato in uso operativo;
- non sono presenti codici catalogo fittizi o con iniziali personali;
- la procedura è documentata nel playbook o nel decision log.

## Collegamenti

- [Archivio Cavi DbCables](25-cable-archive-dbcables.md)
- [Aggiornare Archivio Cavi DbCables](playbooks/update-dbcables-archive.md)
- [Quality gates](14-quality-gates.md)
- [Decision log](11-decision-log.md)
