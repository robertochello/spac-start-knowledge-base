# Schema unifilare

Questa pagina raccoglie le procedure operative già consolidate per sviluppare uno schema unifilare in **SPAC Start 26**.

## Aprire l'ambiente unifilare

Dalla barra superiore:

```text
UNIFILARE → Disegno Unifilare
```

Risultato atteso: apertura della finestra **Disegno Unifilare**.

## Preparazione: snap e griglia

Digita:

```text
_DSETTINGS
```

Apri il tab **Snap e griglia**.

Esempio verificato:

```text
Intervallo snap X = 2,5
Intervallo snap Y = 2,5
```

Con griglia principale `10`, ogni quadrato viene suddiviso in quattro passi per lato.

## Finestra Disegno Unifilare

Controlla i campi:

- **Scelta Circuiti memorizzati**;
- **Tipo quadro**;
- **Monofase / Trifase**;
- **Composizione/Tipologia**;
- **Anteprima**;
- **Scelta del quadro**.

A destra è presente la tabella dei componenti/materiali per ogni livello.

## Associare un materiale a un livello

Nella finestra **Disegno Unifilare**:

1. seleziona il livello interessato;
2. seleziona il tipo di dispositivo;
3. fai **tasto destro** sulla tabella materiali;
4. clicca **Avvio DbCenter**;
5. scegli il materiale;
6. verifica che il record compaia sul livello corretto.

## Disegnare l'ingresso linea

1. seleziona la voce dedicata a **Ingresso linea**;
2. compila i livelli necessari;
3. associa i materiali;
4. verifica **Composizione/Tipologia**;
5. clicca **Disegna**.

SPAC disegna automaticamente la linea e genera la tabella con i dati dei materiali e del cavo.

La finestra resta in primo piano per consentire l'inserimento di ulteriori linee.

## Disegnare una nuova linea singola

1. togli la spunta da **Ingresso linea**;
2. configura la linea;
3. clicca **Disegna**;
4. clicca nello schema la posizione della nuova linea.

## Numerare fili non di alimentazione

1. **SPAC → Numera Fili**;
2. seleziona il tipo di cavo;
3. individua **Modalita' di Numerazione**;
4. clicca sull'immagine della modalità;
5. nella finestra **Configurazione Numerazione Conduttori** apri **Numerazione Conduttori**;
6. scegli la **Modalita' di Numerazione**;
7. se usi **Foglio Numero**, scegli il separatore;
8. clicca **OK** nella finestra **Configurazione Numerazione Conduttori**;
9. clicca **OK** nella finestra precedente;
10. torna allo schema;
11. traccia una linea che interseca il cavo da numerare.

Questa procedura vale per fili **non di alimentazione**.

## Identificare una linea di alimentazione

Se manca il simbolo identificatore:

1. barra dei menu → **Identificatore Linee**;
2. seleziona il tipo di linea;
3. clicca **OK**;
4. torna allo schema;
5. traccia una linea che interseca la linea interessata.

## Numerare/identificare fasi e neutro

1. seleziona **Numerazione Fili**;
2. nella finestra **Numerazione Fili Unifilare** scegli il tipo, ad esempio **L1 L2 L3 N**;
3. nel campo accanto a **Numero** imposta il valore iniziale, ad esempio `1`;
4. configura il progressivo numerico.

Se vuoi solo `L1`, `L2`, `L3`, `N`, attiva l'opzione equivalente a **Non utilizzare numero incrementale**.

### Prefissi o suffissi locali

Nella sezione **Prefissi o Suffissi Locali**:

1. attiva **Abilita** se vuoi aggiungere un prefisso/suffisso;
2. configura il testo desiderato.

!!! note

    Prefissi e suffissi locali funzionano solo se viene utilizzato un numero incrementale. Se **Non utilizzare numero incrementale** è attivo, non vengono applicati.

## Lista dei rimandi/numeri usati

Percorso:

```text
Numerazione fili → Lista numeri usati
```

Per vedere solo i rimandi:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli;
3. clicca **Scansiona i Multifogli**.

I numeri con asterisco indicano ripetizioni.

## Eliminare la numerazione

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

## Cross-reference

Dopo aver creato i rimandi con nome e direzione coerenti:

```text
UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna
```

Verifica poi il riferimento generato sul foglio.

## Checklist unifilare

- **UNIFILARE → Disegno Unifilare** usato per aprire l'ambiente;
- `_DSETTINGS` configurato;
- ingresso linea disegnato;
- materiali associati con **Avvio DbCenter**;
- nuove linee inserite con **Disegna**;
- fili non alimentazione numerati con **SPAC → Numera Fili**;
- alimentazioni con **Identificatore Linee**;
- fasi/neutro configurati in **Numerazione Fili Unifilare**;
- eventuali prefissi/suffissi compatibili con il progressivo;
- rimandi verificati con **Lista numeri usati**;
- cross-reference aggiornato con **UTIL → Cross Reference**.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Rimandi e morsetti](06-cross-references-terminals.md)
