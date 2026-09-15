# Numerazione e identificazione fili

Questa pagina separa le procedure per **fili non di alimentazione** e **conduttori di alimentazione**, riportando i nomi esatti già verificati in SPAC Start 26.

## Fili non di alimentazione

1. Apri **SPAC → Numera Fili**.
2. Seleziona il **tipo di cavo** dalla lista.
3. A destra individua **Modalita' di Numerazione**.
4. Clicca sull'immagine della modalità.
5. Nella finestra **Configurazione Numerazione Conduttori**, apri il tab **Numerazione Conduttori**.
6. Scegli la **Modalita' di Numerazione**.
7. Se usi **Foglio Numero**, scegli il separatore.
8. Clicca **OK** nella finestra **Configurazione Numerazione Conduttori**.
9. Clicca **OK** nella finestra precedente.
10. Torna allo schema.
11. Evidenzia il cavo tracciando una linea che lo interseca.

### Esito atteso

Con **Foglio Numero** l'identificativo segue una forma del tipo:

```text
numeroPagina.numeroIncrementale
```

La procedura descritta sopra vale per fili **non di alimentazione**.

## Lista dei numeri/rimandi usati

Apri:

```text
Numerazione fili → Lista numeri usati
```

Per filtrare solo i rimandi:

1. attiva **Vedi solo i Rimandi**;
2. seleziona i multifogli da analizzare, ad esempio `SCHEMA`;
3. clicca **Scansiona i Multifogli**.

I numeri con **asterisco** sono ripetuti.

## Eliminare una numerazione esistente

Percorso:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente:

```text
DEL_NUMF
```

La funzione elimina i numeri ma non i fili.

## Fili di alimentazione: aggiungere l'identificatore

Se manca il simbolo identificatore:

1. barra dei menu → **Identificatore Linee**;
2. seleziona il tipo di linea;
3. clicca **OK**;
4. torna allo schema;
5. traccia una linea che interseca il conduttore interessato.

## Numerare/identificare i fili di alimentazione

1. seleziona **Numerazione Fili**;
2. nella finestra **Numerazione Fili Unifilare** scegli il tipo, ad esempio:

   ```text
   L1 L2 L3 N
   ```

3. nel campo accanto a **Numero** imposta il numero iniziale, ad esempio `1`;
4. configura il numero incrementale in base al risultato desiderato.

Se vuoi soltanto l'identificatore (`L1`, `L2`, `L3`, `N`), usa l'opzione **Non utilizzare numero incrementale**.

## Prefissi o Suffissi Locali

Nella sezione **Prefissi o Suffissi Locali**:

1. attiva **Abilita**;
2. configura il prefisso/suffisso richiesto.

!!! warning "Vincolo"

    Prefissi e suffissi locali funzionano solo insieme a un numero incrementale. Se **Non utilizzare numero incrementale** è attivo, non vengono applicati.

## Cross-reference dei rimandi

Dopo aver creato rimandi con lo stesso nome e direzione coerente:

```text
UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna
```

Se vuoi vedere il file Excel prodotto, abilita la visualizzazione dell'output prima di **Ok - Aggiorna**.

## Riferimento rapido

| Operazione | Percorso esatto |
|---|---|
| Numerare fili normali | **SPAC → Numera Fili** |
| Configurare modalità | **Configurazione Numerazione Conduttori → Numerazione Conduttori** |
| Confermare modalità | **OK** → **OK** → selezione cavo nello schema |
| Lista numeri/rimandi | **Numerazione fili → Lista numeri usati** |
| Solo rimandi | **Vedi solo i Rimandi → Scansiona i Multifogli** |
| Eliminare numerazione | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Identificatore alimentazione | **Identificatore Linee → tipo linea → OK** |
| Fasi/neutro | **Numerazione Fili → Numerazione Fili Unifilare** |
| Prefissi/suffissi | **Prefissi o Suffissi Locali → Abilita** |
| Cross-reference | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** |

## Checklist

- modalità numerazione confermata con i due **OK**;
- selezione cavo eseguita nello schema;
- rimandi controllati con filtro **Vedi solo i Rimandi**;
- alimentazioni dotate di identificatore;
- progressivo/prefisso/suffisso coerenti;
- cross-reference aggiornato quando vengono modificati i rimandi.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Schema unifilare](17-unifilare.md)
- [Schema multifilare](09-multifilare.md)
- [Rimandi e morsetti](06-cross-references-terminals.md)
