# Playbook — Verificare rappresentazione morsetti

## Obiettivo

Capire perché un morsetto mostra un'informazione diversa da quella attesa e verificare il dato sorgente prima di modificare la grafica.

## Aprire la gestione morsetti

Usa la funzione:

```text
Inser Morsetti
```

oppure da riga comando:

```text
SPINSMOR
```

!!! warning "Prerequisito"

    Deve essere aperto un database materiali che contenga almeno una morsettiera.

## Se devi creare una morsettiera di prova

Nella finestra **Inser Morsetti**:

1. individua **Elenco Quadri** in alto a sinistra;
2. fai **tasto destro** su **Elenco Quadri**, sul nome del quadro oppure su una morsettiera esistente;
3. clicca **Nuova morsettiera**;
4. completa i dati;
5. verifica che la morsettiera compaia sotto il quadro corretto.

## Capire cosa sta mostrando il morsetto

Sigle documentate:

| Sigla | Significato |
|---|---|
| `NumI` | numero filo in ingresso |
| `NumO` | numero filo in uscita |
| `NumM` | numero morsetto |

Se sul morsetto compare il numero filo invece del numero morsetto, verifica se la rappresentazione sta mostrando `NumI` o `NumO` invece di `NumM`.

## Procedura diagnostica

### 1. Apri il morsetto nella gestione corretta

1. Avvia **Inser Morsetti** / `SPINSMOR`.
2. Seleziona il quadro corretto.
3. Seleziona la morsettiera corretta.
4. Individua il morsetto interessato.

### 2. Verifica i dati sorgente

Controlla separatamente:

- nome morsettiera;
- numero morsetto;
- numero filo in ingresso;
- numero filo in uscita;
- riferimento funzionale.

### 3. Verifica la rappresentazione

Controlla quale campo la rappresentazione del morsetto sta mostrando:

- `NumM` se vuoi il numero morsetto;
- `NumI` se vuoi il numero filo in ingresso;
- `NumO` se vuoi il numero filo in uscita.

!!! warning "Percorso della rappresentazione da verificare"

    Il nome esatto del pulsante/menu interno con cui si cambia la rappresentazione grafica del morsetto non è ancora consolidato nella knowledge base. Non inventarlo. Quando viene verificato su SPAC Start 26 va aggiunto qui.

### 4. Non correggere il testo manualmente

Se il dato visualizzato è sbagliato:

- non spostare o riscrivere il testo a mano;
- correggi il dato sorgente oppure la rappresentazione che richiama il campo sbagliato.

### 5. Crea un morsetto di prova

1. Usa **Inser Morsetti**.
2. Se necessario crea una **Nuova morsettiera**.
3. Inserisci un morsetto nuovo su un filo noto.
4. Verifica quale campo viene mostrato.
5. Confronta il comportamento con il morsetto problematico.

## Diagnostica rapida

| Sintomo | Controllo |
|---|---|
| compare numero filo al posto del numero morsetto | verifica `NumI`/`NumO` vs `NumM` |
| morsettiera inattesa | apri `SPINSMOR` e verifica appartenenza sotto **Elenco Quadri** |
| numero morsetto corretto nei dati ma non a video | verifica campo usato dalla rappresentazione |
| problema presente solo su un morsetto | confronta con un morsetto nuovo |
| problema presente su tutti i morsetti | verifica configurazione/rappresentazione generale |

## Verifica finale

Il problema è risolto quando:

- il morsetto appartiene alla morsettiera corretta;
- `NumM`, `NumI` e `NumO` sono coerenti con i dati reali;
- la rappresentazione mostra il campo previsto;
- non è stato corretto solo il testo grafico;
- un morsetto nuovo mostra lo stesso comportamento corretto.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Multifilare](../09-multifilare.md)
- [Numerazione e identificazione fili](../18-wire-numbering.md)
