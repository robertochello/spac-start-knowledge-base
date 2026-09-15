# Schema unifilare

Questa pagina raccoglie le procedure operative per impostare e sviluppare uno schema unifilare in SPAC Start. I comandi verificati sono riportati con il nome esatto; dove il percorso non è ancora confermato viene indicato `Da verificare`.

## Preparazione

Prima di iniziare:

1. verifica che il progetto sia stato creato correttamente;
2. verifica cartiglio e pagine standard;
3. seleziona l'ambiente unifilare;
4. usa la simbologia unifilare;
5. configura griglia e snap con il comando indicato sotto.

## Snap e griglia

Nella riga comando digita:

```text
_DSETTINGS
```

Nella finestra che si apre seleziona il tab:

```text
Snap e griglia
```

Imposta gli intervalli di snap sugli assi X e Y e la griglia secondo lo standard del progetto.

Esempio operativo già adottato:

- griglia principale: `10`;
- snap: `2.5`;
- ogni quadrato principale viene suddiviso in 4 parti per lato.

Verifica finale: spostando o inserendo un simbolo, il punto di inserimento deve agganciarsi ai passi impostati.

## Disegno unifilare

Nella finestra di disegno unifilare controlla i campi disponibili prima di confermare il disegno:

| Campo | Cosa controllare |
|---|---|
| **Circuiti memorizzati** | circuito predisposto da utilizzare |
| **Tipo quadro** | quadro corretto |
| **Monofase / Trifase** | tipo di alimentazione |
| **Composizione / Tipologia** | composizione linea e fine circuito |
| **Anteprima** | risultato grafico prima dell'inserimento |
| **Scelta quadro** | associazione al quadro corretto |

## Ingresso linea

È consigliato disegnare prima l'ingresso linea.

Procedura attuale:

1. seleziona la voce dedicata all'ingresso linea nella finestra unifilare;
2. configura i livelli necessari;
3. associa i materiali ai componenti;
4. disegna la linea;
5. verifica la tabella e i dati generati.

!!! warning "Percorso menu da verificare"

    Il nome esatto della voce/ribbon che apre la finestra di disegno unifilare non è ancora consolidato nella knowledge base. Finché non viene verificato direttamente in SPAC Start 26 non deve essere inventato.

## Nuove linee

1. disattiva l'opzione **Ingresso linea**;
2. configura la nuova linea;
3. conferma il disegno;
4. seleziona la posizione nello schema;
5. verifica l'anteprima e i dati generati.

## Materiali in unifilare

Per ogni livello della linea associa il materiale al livello corretto e controlla che non venga duplicato.

Per la gestione dettagliata usa [Associare materiali](playbooks/material-association.md).

## Identificazione linee di alimentazione

I fili di alimentazione devono essere identificati come fasi, neutro o altri conduttori coerenti.

Procedura concettualmente verificata:

1. usa la funzione di identificazione linee;
2. seleziona il tipo di linea;
3. applica l'identificatore alla linea interessata;
4. verifica che il simbolo identificatore sia visibile.

!!! warning "Comando esatto da verificare"

    Il nome esatto del comando/percorso menu per **Identificazione linee** deve ancora essere consolidato. Non sostituirlo con un nome ipotetico.

## Numerazione fili

I fili non di alimentazione possono essere numerati con le funzioni di numerazione dedicate.

Per consultare i numeri già usati nel progetto è verificato il percorso:

```text
Numerazione fili → Lista numeri usati
```

Per eliminare la numerazione esistente è verificato:

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure da riga comando:

```text
DEL_NUMF
```

## Checklist unifilare

Prima di chiudere uno schema unifilare:

- `_DSETTINGS` verificato con snap/griglia corretti;
- ingresso linea presente;
- linee configurate correttamente;
- materiali associati;
- identificatori alimentazione presenti;
- numerazione fili verificata;
- tabelle generate coerenti;
- layout leggibile.

## Collegamenti

- [Comandi e percorsi esatti](command-reference.md)
- [Template progetto](16-project-template.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Associazione materiali](playbooks/material-association.md)
