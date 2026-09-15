# SPAC Start Knowledge Base

Questa è una guida operativa per **SPAC Start Impianti**. Non va letta come un manuale lineare: scegli cosa devi fare e apri direttamente la procedura utile.

<div class="home-grid" markdown>

[**Sto iniziando un lavoro**<br>Setup libreria, template, interfaccia e pagine.](15-custom-library.md){ .home-card }

[**Sto disegnando uno schema**<br>Unifilare, multifilare, fili, morsetti e rimandi.](17-unifilare.md){ .home-card }

[**Sto creando o correggendo un simbolo**<br>Simboli custom, attributi, pinatura e naming.](03-custom-symbols.md){ .home-card }

[**Sto gestendo materiali o cavi**<br>Archivi materiali, DbCables, download e back-check.](21-material-archives.md){ .home-card }

[**Ho un problema da risolvere**<br>Diagnosi rapida, known issue e playbook.](07-troubleshooting.md){ .home-card }

[**Non so dove cercare**<br>Apri la guida pratica e scegli il caso più vicino al tuo.](00-how-to-use.md){ .home-card }

</div>

!!! info "Prima volta qui?"

    Apri **[Guida pratica](00-how-to-use.md)**. In pochi passaggi ti porta alla pagina corretta senza costringerti a leggere tutta la knowledge base.

!!! note "Manuale completo"

    La **[Guida operativa completa](guida-operativa-completa.md)** raccoglie molte procedure in un'unica pagina ed è utile come riferimento esteso. Per il lavoro quotidiano è più rapido usare le sezioni e i playbook del sito.

## Scelta rapida per attività

| Devo... | Vai qui |
|---|---|
| installare o aggiornare la libreria `_CUSTOM` | [Libreria custom](15-custom-library.md) |
| preparare la struttura di un nuovo progetto | [Template progetto](16-project-template.md) |
| lavorare in unifilare | [Schema unifilare](17-unifilare.md) |
| lavorare in multifilare | [Schema multifilare](09-multifilare.md) |
| sistemare fili, morsetti o cross-reference | [Rimandi e morsetti](06-cross-references-terminals.md) |
| creare un simbolo custom | [Creare un simbolo custom](playbooks/create-custom-symbol.md) |
| capire `PRES`, `PINA` e `PINB` | [Attributi e pinatura](04-attributes-and-pinning.md) |
| associare o controllare materiali | [Archivi materiali custom](21-material-archives.md) |
| gestire l'archivio cavi | [Archivio Cavi DbCables](25-cable-archive-dbcables.md) |
| scaricare file pubblicati | [Download](downloads.md) |
| capire perché qualcosa non funziona | [Diagnosi rapida](07-troubleshooting.md) |
| verificare un problema già noto | [Known Issues](known-issues/index.md) |

## Se il problema è già davanti a te

Parti dal **sintomo**, non dalla struttura della documentazione.

| Sintomo | Prima verifica | Procedura collegata |
|---|---|---|
| il pin di un simbolo non aggancia il filo | attributi e punto di inserimento | [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| un rimando punta alla posizione sbagliata | tipo oggetto, nome e aggiornamento riferimenti | [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md) |
| un morsetto visualizza dati inattesi | rappresentazione e dato sorgente | [Verificare rappresentazione morsetti](playbooks/terminal-representation.md) |
| un accessorio non risulta associato al dispositivo | relazione Madre/Figlio | [Gestire accessori e bobine](playbooks/manage-accessories-and-coils.md) |
| un materiale manca o compare duplicato | associazione e archivio sorgente | [Associare materiali](playbooks/material-association.md) |
| SPAC segnala una versione DbCables non congruente | versione archivio e ambiente | [Known Issue DbCables](known-issues/dbcables-version-mismatch.md) |
| restano oggetti/layer apparentemente vuoti | riferimenti residui, blocchi e oggetti nascosti | [Pulire oggetti residui](playbooks/clean-residual-objects.md) |

## Percorso consigliato per un progetto

1. **Setup** — verifica libreria `_CUSTOM`, template e pagine standard.
2. **Disegno** — lavora in unifilare o multifilare usando simboli coerenti.
3. **Dati** — completa pinatura, morsetti, rimandi, materiali e cavi.
4. **Verifica** — esegui checklist e quality gate prima di riutilizzare o pubblicare il risultato.

```mermaid
flowchart LR
    A[Setup]:::process --> B[Schema]:::process
    B --> C[Simboli e collegamenti]:::data
    C --> D[Morsetti, rimandi e materiali]:::warn
    D --> E[Verifica finale]:::ok

    classDef ok fill:#e6f4ea,stroke:#2e7d32,color:#1b5e20;
    classDef warn fill:#fff4e5,stroke:#ef6c00,color:#5d4037;
    classDef data fill:#e0f7fa,stroke:#00838f,color:#004d40;
    classDef process fill:#f5f5f5,stroke:#757575,color:#212121;
```

## Come leggere le pagine

Nel sito trovi tipi di contenuto diversi:

- **pagina operativa**: spiega un'area di lavoro stabile;
- **playbook**: procedura passo-passo per fare una cosa precisa;
- **known issue**: diagnosi di un problema ricorrente;
- **standard**: regola adottata e riutilizzabile;
- **quality gate**: controlli da superare prima di considerare il lavoro pronto.

Quando devi **fare qualcosa**, preferisci un playbook. Quando devi **capire perché non funziona**, parti dalla diagnosi. Quando devi **sapere qual è la regola corretta**, apri gli standard.

## Principio di diagnosi

!!! warning "Non correggere solo l'effetto visibile"

    Prima distingui se il problema è **grafico CAD**, **attributivo**, **logico SPAC**, **di rappresentazione** oppure **nel dato sorgente**. La correzione dipende dal livello in cui nasce il problema.
