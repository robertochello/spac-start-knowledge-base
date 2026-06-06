# Schema unifilare

Questa sezione raccoglie le procedure operative per impostare e sviluppare uno schema unifilare in SPAC Start.

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
