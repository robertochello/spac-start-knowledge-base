# Schema unifilare

Questa pagina raccoglie le procedure operative già consolidate per sviluppare uno schema unifilare in SPAC Start 26.

## Preparazione: snap e griglia

Nella riga comando digita:

```text
_DSETTINGS
```

Nella finestra che si apre seleziona il tab:

```text
Snap e griglia
```

Esempio operativo:

- griglia principale: `10`;
- snap: `2.5`.

Verifica finale: simboli e punti di inserimento devono agganciarsi ai passi impostati.

## Disegno unifilare

Nella finestra di disegno unifilare controlla i campi:

- **Circuiti memorizzati**;
- **Tipo quadro**;
- **Monofase / Trifase**;
- **Composizione / Tipologia**;
- **Anteprima**;
- **Scelta quadro**.

## Ingresso linea

Per la linea iniziale:

1. attiva/seleziona **Ingresso linea**;
2. configura i livelli necessari;
3. associa i materiali ai componenti previsti;
4. verifica **Composizione / Tipologia**;
5. premi **Disegna**;
6. scegli nello schema la posizione della linea;
7. verifica i dati generati.

## Inserire una nuova linea

1. Togli la spunta da **Ingresso linea**.
2. Configura la linea come necessario.
3. Premi **Disegna**.
4. Scegli nello schema la posizione della nuova linea.

## Numerare fili non di alimentazione

1. Apri il menu **SPAC**.
2. Clicca **Numera Fili**.
3. Nella finestra aperta seleziona il tipo di cavo dalla lista.
4. A destra individua **Modalita' di Numerazione**.
5. Clicca sull'immagine della modalità.
6. Nella finestra **Configurazione Numerazione Conduttori**, apri il tab **Numerazione Conduttori**.
7. Seleziona la **Modalita' di Numerazione**.
8. Se scegli **Foglio Numero**, seleziona anche il separatore.
9. Torna allo schema.
10. Evidenzia il cavo da numerare tracciando una linea che lo interseca.

!!! note

    Questa procedura è per fili **non di alimentazione**.

## Identificare una linea di alimentazione

La linea di partenza può avere già l'identificatore se la composizione è stata definita correttamente in **Composizione / Tipologia**.

Se il simbolo identificatore non è presente:

1. dalla barra dei menu seleziona **Identificatore Linee**;
2. seleziona il tipo di linea;
3. premi **OK**;
4. torna allo schema;
5. evidenzia la linea interessata tracciando una linea che la interseca.

## Numerare/identificare i conduttori di alimentazione

1. Seleziona **Numerazione Fili**.
2. Nella finestra **Numerazione Fili Unifilare**, scegli il tipo di fase/neutro, per esempio:

   ```text
   L1 L2 L3 N
   ```

3. Nel campo accanto a **Numero**, imposta il numero di partenza, per esempio `1`.
4. Configura l'uso del progressivo numerico.
5. Se vuoi solo l'identificatore (`L1`, `N`, ecc.), disattiva il progressivo numerico.

## Verificare i numeri già usati

Percorso:

```text
Numerazione fili → Lista numeri usati
```

I numeri con asterisco indicano ripetizioni.

## Eliminare la numerazione

Percorso:

```text
SPAC → Utility Fili → Elimina numerazione
```

Oppure da riga comando:

```text
DEL_NUMF
```

La funzione elimina i numeri ma non cancella i fili.

## Materiali

Per associare materiale a un simbolo intelligente:

1. fai **doppio click sul simbolo**;
2. nel riquadro **Materiali** fai **tasto destro**;
3. clicca **Avvio Archivio Materiali (DbCenter)**;
4. scegli il materiale corretto;
5. verifica distinta/report.

## Checklist unifilare

Prima di considerare stabile lo schema:

- `_DSETTINGS` configurato;
- ingresso linea disegnato;
- **Composizione / Tipologia** coerente;
- nuove linee inserite con **Disegna**;
- fili non alimentazione numerati con **SPAC → Numera Fili**;
- alimentazioni dotate di **Identificatore Linee**;
- fasi/neutro configurati in **Numerazione Fili Unifilare**;
- duplicati verificati con **Lista numeri usati**;
- materiali verificati in DbCenter;
- layout e tabelle coerenti.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Associare materiali](playbooks/material-association.md)
