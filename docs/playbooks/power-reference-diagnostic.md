# Playbook — Diagnosticare rimandi alimentazione

## Obiettivo

Capire perché un rimando/alimentazione non viene accettato oppure punta a una posizione non coerente, senza inventare comandi non ancora verificati.

## Prima verifica: oggetto SPAC o linea CAD?

Prima di qualsiasi rigenerazione:

1. seleziona il tratto interessato;
2. verifica se è un collegamento/alimentazione SPAC o semplice geometria CAD;
3. controlla se ci sono oggetti sovrapposti o residui;
4. verifica nome e direzione del rimando.

Un rimando deve appoggiarsi a un oggetto riconosciuto, non a una semplice linea disegnata.

## Verificare duplicati e numeri usati

Percorso verificato:

```text
Numerazione fili → Lista numeri usati
```

Controlla:

- numeri ripetuti;
- rimandi duplicati;
- riferimenti ancora presenti ma non più coerenti.

I numeri con **asterisco** richiedono verifica.

## Regole direzionali dei rimandi

- partenza ↔ arrivo;
- partenza ↔ arrivo/partenza;
- arrivo ↔ partenza;
- arrivo ↔ arrivo/partenza.

I rimandi che rappresentano lo stesso collegamento devono usare un nome coerente.

## Aggiornare il cross-reference

Sequenza logica:

1. verifica oggetti SPAC e nomi dei rimandi;
2. verifica la direzione;
3. apri la funzione di cross-reference;
4. seleziona l'elaborazione dedicata ai rimandi;
5. avvia l'aggiornamento;
6. verifica il riferimento generato;
7. ricontrolla **Numerazione fili → Lista numeri usati**.

!!! warning "Nome comando cross-reference da verificare"

    Il nome esatto del comando/percorso menu che avvia l'elaborazione cross-reference non è ancora consolidato nella knowledge base per SPAC Start 26. Non usare un nome ipotetico. Quando viene verificato direttamente va sostituito qui.

## Se il comando segnala selezione non valida

Controlla nell'ordine:

1. stai selezionando la linea CAD o il collegamento SPAC?
2. l'oggetto è stato esploso o alterato?
3. esistono vecchi oggetti sovrapposti?
4. il collegamento è stato cancellato solo graficamente?
5. lo stesso caso funziona su un foglio pulito?

Non risolvere disegnando una seconda linea grafica sopra quella esistente.

## Se il riferimento punta a una vecchia posizione

1. Cerca oggetti residui nella zona originaria.
2. Cerca rimandi non più utilizzati.
3. Controlla eventuali alimentazioni duplicate.
4. Verifica la lista numeri/rimandi usati.
5. Rigenera il cross-reference con la funzione corretta dell'installazione.
6. Controlla di nuovo il foglio.

## Se devi pulire residui

Usa il playbook [Pulire oggetti residui](clean-residual-objects.md) prima di rigenerare i riferimenti.

## Verifica finale

Il rimando è corretto quando:

- la selezione viene accettata su un oggetto SPAC reale;
- nome e direzione sono coerenti;
- **Lista numeri usati** non evidenzia duplicati inattesi;
- il cross-reference punta alla posizione corretta;
- non rimangono riferimenti a celle/oggetti vecchi;
- il comportamento resta corretto dopo salvataggio e riapertura.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Cross-reference obsoleto](../known-issues/obsolete-cross-reference.md)
- [Pulire oggetti residui](clean-residual-objects.md)
