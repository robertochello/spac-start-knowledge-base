# Multifilare

Questa pagina raccoglie le operazioni multifilari verificate in SPAC Start 26 con i nomi esatti di comandi, finestre e pulsanti.

## Lista dei soli rimandi

Apri:

```text
Numerazione fili → Lista numeri usati
```

Nella finestra **Lista numeri usati**:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli da analizzare, ad esempio `SCHEMA`;
3. clicca **Scansiona i Multifogli**.

I numeri con **asterisco** sono ripetuti.

## Eliminare numerazione fili

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

La funzione rimuove i numeri ma non cancella i fili.

## Creare e aggiornare rimandi

Per creare il rimando usa **Dynamic Coll** oppure **Dynamic Alim** e scegli il tipo:

- **Rimandi di arrivo**;
- **Rimandi di partenza**;
- **Rimandi di arrivo e partenza**.

I due rimandi collegati devono usare lo stesso nome e direzioni coerenti.

Per aggiornare il cross-reference:

```text
UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna
```

## Inserire morsetti

Apri:

```text
SPINSMOR
```

oppure la funzione **Inser Morsetti**.

!!! warning "Prerequisito"

    Deve essere aperto un database materiali che contenga almeno una morsettiera.

### Creare una morsettiera

Nella finestra **Inser Morsetti**:

1. tasto destro su **Elenco Quadri**, sul nome del quadro o su una morsettiera esistente;
2. clicca **Nuova morsettiera**;
3. completa i dati;
4. verifica l'appartenenza al quadro corretto.

### Inserire un morsetto

1. seleziona la morsettiera;
2. scegli il tipo di morsetto;
3. nel riquadro **Anteprima** scegli la rappresentazione corretta;
4. se vuoi mostrare il numero morsetto, scegli il modello che visualizza `NumM`;
5. clicca **Ok - Nuovo** in basso a destra;
6. clicca il filo nel punto di inserimento;
7. premi **Invio**.

Il punto cliccato sul filo determina la posizione del morsetto.

| Campo | Significato |
|---|---|
| `NumI` | numero filo ingresso |
| `NumO` | numero filo uscita |
| `NumM` | numero morsetto |

## Madre, Figlio e accessori

Regola:

```text
Madre  → PRES = M
Figlio → PRES = F
Figlio → NOME uguale alla Madre
```

Per modificare un simbolo già inserito usa:

```text
EDITATT
```

Se SPAC segnala un nome già esistente, conferma quando l'uguaglianza è intenzionale per associare il Figlio alla Madre.

## Associare materiale

1. doppio click sul simbolo;
2. riquadro **Materiali**;
3. tasto destro;
4. **Avvio Archivio Materiali (DbCenter)**;
5. seleziona il materiale;
6. conferma;
7. verifica distinta/report.

## Sequenza operativa consigliata

1. Verifica componente Madre con `EDITATT`.
2. Verifica eventuali Figli/accessori.
3. Numera/identifica i fili.
4. Controlla rimandi con **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli**.
5. Aggiorna cross-reference con **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna**.
6. Inserisci morsetti con `SPINSMOR`.
7. Per ogni morsetto usa **Anteprima → Ok - Nuovo → clic filo → Invio**.
8. Associa materiali tramite DbCenter.
9. Verifica distinta/report.

## Diagnostica rapida

| Sintomo | Prima azione |
|---|---|
| rimando duplicato | **Vedi solo i Rimandi → Scansiona i Multifogli** |
| cross-reference vecchio | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** |
| numerazione da cancellare | `DEL_NUMF` |
| morsettiera da creare | **Elenco Quadri → tasto destro → Nuova morsettiera** |
| morsetto da inserire | **Anteprima → Ok - Nuovo → clic filo → Invio** |
| compare numero filo anziché morsetto | scegli in **Anteprima** un modello con `NumM` |
| accessorio non associato | `EDITATT` → `PRES = F`, stesso `NOME` della Madre |
| materiale mancante | doppio click → **Materiali → Avvio Archivio Materiali (DbCenter)** |

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Rimandi e morsetti](06-cross-references-terminals.md)
- [Numerazione fili](18-wire-numbering.md)
- [Gestire accessori e bobine](playbooks/manage-accessories-and-coils.md)
