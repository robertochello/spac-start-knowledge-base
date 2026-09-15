# Numerazione e identificazione fili

Questa pagina separa le procedure per **fili non di alimentazione** e **conduttori di alimentazione**, riportando i nomi esatti delle funzioni già verificati in SPAC Start 26.

## Fili non di alimentazione

Per numerare i fili:

1. Apri il menu **SPAC**.
2. Clicca **Numera Fili**.
3. Nella finestra che si apre seleziona il **tipo di cavo** dalla lista.
4. A destra individua la sezione **Modalita' di Numerazione**.
5. Clicca sull'immagine della modalità di numerazione.
6. Nella finestra **Configurazione Numerazione Conduttori**, apri il tab **Numerazione Conduttori**.
7. Seleziona la **Modalita' di Numerazione** desiderata.
8. Se usi **Foglio Numero**, scegli anche il separatore.
9. Torna allo schema.
10. Evidenzia il cavo da numerare tracciando una linea che interseca il cavo.

!!! note "Limite"

    La funzione di numerazione descritta sopra si usa per i fili **non di alimentazione**.

## Consultare i numeri già usati

Percorso:

```text
Numerazione fili → Lista numeri usati
```

I numeri segnalati con **asterisco** sono numeri ripetuti e vanno verificati.

## Eliminare una numerazione esistente

Percorso da menu:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente:

```text
DEL_NUMF
```

Questa funzione rimuove i numeri filo ma **non cancella i fili dallo schema**.

## Fili di alimentazione: verificare l'identificatore linea

I conduttori di alimentazione devono avere un identificatore che permetta a SPAC di distinguere fase, neutro o altro conduttore.

Se il simbolo identificatore non è presente sulla linea:

1. dalla barra dei menu seleziona **Identificatore Linee**;
2. seleziona il tipo di linea;
3. premi **OK**;
4. torna allo schema;
5. evidenzia la linea interessata tracciando una linea che la interseca.

## Numerare/identificare i fili di alimentazione

Dopo aver verificato l'identificatore linea:

1. seleziona **Numerazione Fili**;
2. nella finestra **Numerazione Fili Unifilare**, seleziona il tipo di fase/neutro, per esempio:

   ```text
   L1 L2 L3 N
   ```

3. nel campo accanto a **Numero**, imposta il numero di partenza, per esempio:

   ```text
   1
   ```

4. configura l'uso del numero incrementale in base al risultato desiderato;
5. se vuoi visualizzare solo l'identificatore (`L1`, `N`, ecc.), disattiva l'uso del progressivo numerico.

Esempio senza progressivo:

```text
L1
N
```

## Differenza pratica

| Caso | Funzione |
|---|---|
| Filo non di alimentazione | **SPAC → Numera Fili** |
| Configurazione modalità | **Configurazione Numerazione Conduttori** → **Numerazione Conduttori** |
| Verifica duplicati | **Numerazione fili → Lista numeri usati** |
| Rimozione numerazione | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Alimentazione senza identificatore | **Identificatore Linee** → tipo linea → **OK** |
| Numerazione/identificazione alimentazione | **Numerazione Fili** → finestra **Numerazione Fili Unifilare** |

## Checklist

Prima di validare:

- fili non di alimentazione numerati con **SPAC → Numera Fili**;
- modalità scelta in **Configurazione Numerazione Conduttori**;
- alimentazioni con identificatore linea presente;
- fasi/neutro scelti nella finestra **Numerazione Fili Unifilare**;
- duplicati verificati con **Lista numeri usati**;
- numerazione vecchia eliminata con `DEL_NUMF` se necessario.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Schema unifilare](17-unifilare.md)
- [Schema multifilare](09-multifilare.md)
- [Rimandi e morsetti](06-cross-references-terminals.md)
