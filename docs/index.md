# SPAC Start Knowledge Base

Knowledge base operativa per **SPAC Start Impianti**. Serve per trovare rapidamente procedure, standard, playbook e soluzioni ricorrenti senza dover leggere tutta la guida in ordine.

!!! tip "Non sai da dove partire?"

    Parti da [Come usare questa guida](00-how-to-use.md). Se hai già un
    problema pratico, vai direttamente a [Troubleshooting](07-troubleshooting.md)
    o ai [Playbook](playbooks/index.md).

## Percorsi principali

<div class="home-grid" markdown>

[**Inizia qui**<br>Orientamento, scopo e concetti base.](00-how-to-use.md){ .home-card }

[**Setup progetto**<br>Libreria custom, template, interfaccia, cartigli.](15-custom-library.md){ .home-card }

[**Schemi**<br>Unifilare, multifilare, fili, rimandi e morsetti.](17-unifilare.md){ .home-card }

[**Simboli custom**<br>Creazione, attributi, pinatura e nomenclatura.](03-custom-symbols.md){ .home-card }

[**Archivi**<br>Materiali custom, cavi `DbCables.db` e back-check.](21-material-archives.md){ .home-card }

[**Download**<br>File scaricabili: materiali, cavi e archivi verificati.](downloads.md){ .home-card }

[**Playbook**<br>Procedure guidate per casi operativi specifici.](playbooks/index.md){ .home-card }

[**Diagnosi**<br>Troubleshooting, known issues e casi pratici.](07-troubleshooting.md){ .home-card }

[**Governance**<br>Standard, decisioni, quality gates e manutenzione.](08-standards.md){ .home-card }

</div>

## Mappa logica

![SPAC Start Knowledge Base map](assets/diagrams/site-structure-map.svg)

| Area | Cosa contiene |
|---|---|
| Start | orientamento, overview, concetti, FAQ, glossario |
| Operativo | setup, schemi, simboli, archivi |
| Playbook | procedure guidate e checklist |
| Diagnosi | troubleshooting, known issues, casi pratici |
| Governance | standard, decisioni, quality gates, roadmap |

## Flusso operativo

Il sito segue il flusso reale di lavoro: prima si prepara il progetto, poi si
modellano simboli e collegamenti, quindi si verificano morsetti, rimandi,
materiali e report.

```mermaid
flowchart LR
    A[Progetto] --> B[Simboli]
    B --> C[Collegamenti]
    C --> D[Morsetti e rimandi]
    B --> E[Materiali]
    E --> F[Report e distinte]
    D --> G[Verifica]
    F --> G
    G --> H[Standard e quality gate]
```

| Se stai lavorando su... | Vai a |
|---|---|
| impostazione del progetto | [Libreria custom](15-custom-library.md) e [Template progetto](16-project-template.md) |
| schema unifilare o multifilare | [Schema unifilare](17-unifilare.md) o [Multifilare](09-multifilare.md) |
| morsetti, fili o rimandi | [Rimandi e morsetti](06-cross-references-terminals.md) |
| simboli custom e attributi | [Simboli custom](03-custom-symbols.md) e [Attributi e pinatura](04-attributes-and-pinning.md) |
| materiali, cavi o file scaricabili | [Archivi materiali custom](21-material-archives.md), [Archivio Cavi DbCables](25-cable-archive-dbcables.md) e [Download](downloads.md) |
| anomalie ricorrenti | [Troubleshooting](07-troubleshooting.md) e [Known Issues](known-issues/index.md) |
| rilascio o manutenzione | [Quality gates](14-quality-gates.md) e [Decision log](11-decision-log.md) |

## Uso consigliato

1. Parti dal problema operativo.
2. Apri la sezione dedicata.
3. Segui il playbook, la procedura o la checklist.
4. Verifica il risultato in un progetto di prova.
5. Aggiorna standard, decision log o casi pratici se emerge una regola riutilizzabile.

!!! warning "Regola operativa"

    Non correggere solo l'effetto visibile: prima verifica se il problema è
    grafico, attributivo, logico, di rappresentazione o di dato sorgente.

## Stato attuale

| Area | Stato |
|---|---|
| Base documentale | Baseline completata |
| Simboli custom | Baseline completata |
| Attributi e pinatura | Baseline completata |
| Workflow CAD | Baseline completata |
| Rimandi e morsetti | Baseline completata |
| Materiali custom | Baseline completata |
| Archivio Cavi DbCables | Verificato su SPAC Automazione e SPAC Start |
| Multifilare | Baseline operativa completata |
| Governance documentale | Baseline completata |

## Estensioni future

1. Aggiungere casi pratici multifilare quando emergono esempi riutilizzabili.
2. Aggiungere screenshot sanitizzati solo dove servono.
3. Collegare ogni caso pratico a una decisione o a uno standard.
4. Mantenere navigazione e Home pulite.
