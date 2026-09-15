# Playbook — Verificare rappresentazione morsetti

## Obiettivo

Capire perché un morsetto mostra un'informazione diversa da quella attesa e correggere la rappresentazione usando i controlli realmente presenti in **Inser Morsetti**.

## Aprire Inser Morsetti

```text
SPINSMOR
```

oppure usa la funzione **Inser Morsetti**.

!!! warning "Prerequisito"

    Deve essere aperto un database materiali contenente almeno una morsettiera.

## Creare una morsettiera di prova

1. Apri **Inser Morsetti**.
2. Nel riquadro in alto a sinistra individua **Elenco Quadri**.
3. Tasto destro su **Elenco Quadri**, sul quadro o su una morsettiera esistente.
4. Clicca **Nuova morsettiera**.
5. Completa i dati.

## Inserire un morsetto nuovo

1. seleziona la morsettiera;
2. scegli il tipo di morsetto;
3. nel riquadro **Anteprima** scegli il modello grafico;
4. clicca **Ok - Nuovo** in basso a destra;
5. torna al disegno;
6. clicca il filo esattamente nel punto dove vuoi inserire il morsetto;
7. premi **Invio**.

Il punto cliccato sul filo determina la posizione del morsetto.

## Scegliere cosa visualizzare

Nel riquadro **Anteprima** verifica quale dato mostra il modello:

| Sigla | Significato |
|---|---|
| `NumI` | numero filo in ingresso |
| `NumO` | numero filo in uscita |
| `NumM` | numero morsetto |

Se vuoi vedere il numero morsetto, scegli un modello che mostri **`NumM`**, preferibilmente insieme al nome della morsettiera.

## Diagnosi: compare il numero filo anziché il numero morsetto

1. Apri `SPINSMOR`.
2. Seleziona la morsettiera corretta.
3. Inserisci un morsetto di prova.
4. Nel riquadro **Anteprima** scegli un modello con `NumM`.
5. Clicca **Ok - Nuovo**.
6. Inseriscilo su un filo noto.
7. Premi **Invio**.
8. Confronta il risultato con il morsetto problematico.

Se il nuovo morsetto è corretto e quello vecchio no, il problema è locale alla rappresentazione/dato del morsetto esistente.

## Cosa non fare

- non riscrivere manualmente il testo;
- non confondere `NumI`/`NumO` con `NumM`;
- non spostare il testo per nascondere un dato sorgente errato.

## Verifica finale

Il risultato è corretto quando:

- morsettiera corretta;
- morsetto inserito sul filo corretto;
- **Anteprima** scelta coerentemente;
- `NumM` visualizzato quando serve il numero morsetto;
- comportamento ripetibile su un morsetto nuovo.

## Collegamenti

- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Multifilare](../09-multifilare.md)
- [Comandi e click esatti](../command-reference.md)
