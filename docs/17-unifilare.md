# Schema unifilare

## Parti da qui

Se devi fare un unifilare, segui questo ordine:

1. **UNIFILARE → Disegno Unifilare**.
2. Seleziona il tipo di linea.
3. Associa i materiali con **Avvio DbCenter**.
4. Premi **Disegna**.
5. Inserisci eventuali nuove linee.
6. Numera i fili.
7. Controlla i rimandi.

Il resto della pagina spiega questi passaggi uno per uno.

## Aprire Disegno Unifilare

Clicca:

```text
UNIFILARE → Disegno Unifilare
```

Si apre la finestra **Disegno Unifilare**.

## Impostare snap e griglia

Digita:

```text
_DSETTINGS
```

Poi apri **Snap e griglia**.

Esempio usato:

```text
Intervallo snap X = 2,5
Intervallo snap Y = 2,5
```

## Creare l'ingresso linea

Nella finestra **Disegno Unifilare**:

1. seleziona **Ingresso linea**;
2. scegli **Monofase** o **Trifase**;
3. compila i livelli necessari;
4. per ogni materiale fai tasto destro sulla tabella;
5. clicca **Avvio DbCenter**;
6. scegli il materiale;
7. controlla **Composizione/Tipologia**;
8. premi **Disegna**.

SPAC inserisce la linea nello schema.

## Aggiungere una nuova linea

1. Togli la spunta da **Ingresso linea**.
2. Configura la linea.
3. Premi **Disegna**.
4. Clicca nello schema dove vuoi inserirla.

## Numerare i fili normali

1. Clicca **SPAC → Numera Fili**.
2. Seleziona il tipo di cavo.
3. Vai a **Modalita' di Numerazione**.
4. Clicca sull'immagine della modalità.
5. Si apre **Configurazione Numerazione Conduttori**.
6. Apri **Numerazione Conduttori**.
7. Scegli la modalità.
8. Se usi **Foglio Numero**, scegli il separatore.
9. Premi **OK**.
10. Premi ancora **OK**.
11. Torna allo schema.
12. Traccia una linea che attraversa il cavo da numerare.

## Fili di alimentazione

Se manca l'identificatore:

1. clicca **Identificatore Linee**;
2. scegli il tipo di linea;
3. premi **OK**;
4. attraversa con una linea il filo interessato.

Per fasi e neutro:

1. apri **Numerazione Fili**;
2. nella finestra **Numerazione Fili Unifilare** scegli, per esempio, **L1 L2 L3 N**;
3. nel campo vicino a **Numero** inserisci il valore iniziale;
4. imposta il progressivo.

Se vuoi vedere solo `L1`, `L2`, `L3`, `N`, usa **Non utilizzare numero incrementale**.

## Prefisso o suffisso

Vai a **Prefissi o Suffissi Locali** e attiva **Abilita**.

Funziona solo quando è attivo un numero incrementale.

## Controllare i rimandi

Apri:

```text
Numerazione fili → Lista numeri usati
```

Poi:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli;
3. premi **Scansiona i Multifogli**.

Un asterisco indica un numero ripetuto.

## Eliminare la numerazione

Usa:

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

## Aggiornare i cross-reference

Clicca:

```text
UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna
```

Poi controlla il rimando sul foglio.

## Controllo finale

Prima di chiudere verifica:

- ingresso linea presente;
- materiali corretti;
- linee inserite;
- fili numerati;
- identificatori di alimentazione presenti;
- rimandi controllati;
- cross-reference aggiornati.

## Se qualcosa non funziona

Vai a [Problemi e soluzioni](07-troubleshooting.md).
