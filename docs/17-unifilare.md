# Schema unifilare

Questa sezione raccoglie le procedure operative per impostare e sviluppare uno schema unifilare in SPAC Start.

## In questa pagina impari

- come impostare il flusso unifilare senza confonderlo con il multifilare;
- quali controlli fare su linee, identificazione, numerazione e materiali;
- quando passare a rimandi, numerazione fili o back-check;
- quali verifiche fare prima di considerare stabile la pagina.

## Flusso unifilare

Il flusso unifilare deve mantenere separati disegno, riconoscimento SPAC,
identificazione delle linee e verifica finale.

```mermaid
graph LR
    A[Preparazione pagina] --> B[Linee e simboli]
    B --> C[Identificazione linee]
    C --> D[Numerazione fili]
    D --> E[Materiali]
    E --> F[Report e controlli]
```

| Fase | Verifica minima | Rimando |
|---|---|---|
| preparazione pagina | griglia, snap e scala coerenti | [Workflow CAD 2D](02-cad-workflow.md) |
| linee e simboli | elementi riconosciuti quando serve logica SPAC | [Concetti SPAC](concepts.md) |
| identificazione linee | alimentazioni e collegamenti nominati in modo coerente | [Rimandi e morsetti](06-cross-references-terminals.md) |
| numerazione fili | numeri leggibili e rigenerabili | [Numerazione e identificazione fili](18-wire-numbering.md) |
| materiali e report | materiali associati e distinta verificata | [Associare materiali](playbooks/material-association.md) |

!!! note "Differenza dal multifilare"

    In unifilare l'obiettivo è rappresentare linee, livelli e materiali in
    modo sintetico. Per componenti associati, morsetti dettagliati e rimandi
    tra fogli, verificare anche [Multifilare](09-multifilare.md) e
    [Rimandi e morsetti](06-cross-references-terminals.md).

## Preparazione

Prima di iniziare:

1. verificare che il progetto sia stato creato correttamente;
2. verificare cartiglio e pagine standard;
3. selezionare l'ambiente unifilare;
4. usare la simbologia unifilare;
5. configurare griglia e snap.

## Snap e griglia

Per lavorare in modo ordinato, configurare snap e griglia in modo coerente.

Esempio operativo:

- griglia principale con passo 10;
- snap con passo 2,5;
- ogni quadrato principale viene così suddiviso in 4 parti per lato.

Questo consente un posizionamento più preciso dei simboli.

## Disegno unifilare

La finestra di disegno unifilare permette di configurare circuiti, livelli, materiali e tipologia della linea.

Campi da verificare:

| Campo | Scopo |
|---|---|
| Circuiti memorizzati | Selezione di circuiti predisposti |
| Tipo quadro | Filtro o selezione del quadro |
| Monofase / Trifase | Tipo di alimentazione |
| Composizione / Tipologia | Composizione della linea e fine circuito |
| Anteprima | Controllo grafico prima del disegno |
| Scelta quadro | Associazione al quadro corretto |

## Ingresso linea

È consigliato disegnare prima l'ingresso linea.

Procedura:

1. selezionare la voce dedicata all'ingresso linea;
2. configurare i livelli necessari;
3. associare materiali ai componenti;
4. disegnare la linea;
5. verificare tabella e dati generati.

## Nuove linee

Per inserire una nuova linea:

1. disattivare l'opzione ingresso linea;
2. configurare la linea;
3. disegnare;
4. selezionare la posizione nello schema.

## Materiali in unifilare

Per ogni livello della linea è possibile associare un materiale.

Regole operative:

- associare il materiale al livello corretto;
- evitare duplicazioni;
- verificare la tabella generata;
- controllare distinta o report se richiesti.

## Identificazione linee di alimentazione

I fili di alimentazione devono essere identificati come fasi, neutro o altri conduttori coerenti.

Se l'identificatore non è presente:

1. usare la funzione di identificazione linee;
2. selezionare il tipo di linea;
3. applicare l'identificatore alla linea interessata;
4. verificare che il simbolo identificatore sia visibile.

## Numerazione fili

I fili non di alimentazione possono essere numerati con le funzioni di numerazione dedicate.

Regola pratica:

- i fili di alimentazione seguono una logica di identificazione;
- i fili non di alimentazione possono seguire una numerazione progressiva o per foglio.

## Checklist unifilare

Prima di chiudere uno schema unifilare:

- ingresso linea presente;
- linee configurate correttamente;
- materiali associati;
- identificatori alimentazione presenti;
- numerazione fili verificata;
- tabelle generate coerenti;
- layout leggibile.

## Collegamenti

- [Template progetto](16-project-template.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Associazione materiali](playbooks/material-association.md)
