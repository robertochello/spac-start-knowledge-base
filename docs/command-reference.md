# Comandi e click esatti

Questa è la pagina da tenere aperta mentre lavori in **SPAC Start 26**.

Regola: quando il percorso è verificato viene riportato letteralmente. Dove manca una verifica reale viene scritto **Da verificare**.

## Riferimento rapidissimo

| Devo fare | Comando / percorso |
|---|---|
| Aprire libreria simboli | `SP_XML_MENU` |
| Personalizzare shortcut | `CUI` / `_CUI` |
| Snap e griglia | `_DSETTINGS` → **Snap e griglia** |
| Inserire pagina standard | **Modifica/Inserisci → Riferimento DWG → Tipo di percorso: Percorso completo → OK** |
| Legenda fogli | **Fogli → Legenda Fogli → Disegna → foglio vuoto → OK** |
| Aprire unifilare | **UNIFILARE → Disegno Unifilare** |
| Materiale in Disegno Unifilare | tasto destro tabella → **Avvio DbCenter** |
| Numerare fili | **SPAC → Numera Fili** |
| Numeri/rimandi usati | **Numerazione fili → Lista numeri usati** |
| Solo rimandi | **Vedi solo i Rimandi → Scansiona i Multifogli** |
| Eliminare numerazione | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Cross-reference | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** |
| Inserire morsetti | **Inser Morsetti** / `SPINSMOR` |
| Nuova morsettiera | **Elenco Quadri → tasto destro → Nuova morsettiera** |
| Nuovo morsetto | morsettiera → tipo → **Anteprima → Ok - Nuovo → clic filo → Invio** |
| Associare materiale a simbolo | doppio click → **Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)** |
| Inserire DWG/blocco | `_INSER` |
| Esplodere | `ESPLODI` |
| Creare attributo | `ATTDEF` |
| Proprietà | `PROPRIETA` / `CTRL+1` |
| Copiare proprietà | `CORRISPROP` |
| Modificare attributi | `EDITATT` |
| Salvare simbolo DWG | `MBLOCCO` |
| Anteprima simbolo | `_MSLIDE` |
| Gestire immagini | `IMMAGINI` |
| Ripristinare immagine | **Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso** |
| Togliere bordo immagine | `IMAGEFRAME` → `0` |
| Layer non eliminabile | `PURGE` → **Trova elementi non eliminabili** |
| Oggetti su layer | `QSELECT` → filtro **Layer** |
| Residuo dentro blocco | `BEDIT` → modifica → salva → `PURGE` |

---

## Interfaccia e libreria

### Libreria simboli

```text
SP_XML_MENU
```

Esito atteso: apertura della libreria simboli SPAC.

### Shortcut per la libreria

1. `CUI` oppure `_CUI`.
2. Finestra **Personalizza interfaccia utente**.
3. **Elenco comandi** → tasto destro → **Nuovo comando**.
4. Nome, ad esempio `Libreria simboli`.
5. Campo **Macro**:

   ```text
   ^C^CSP_XML_MENU;
   ```

6. **Tasti di scelta rapida → Tasti di scelta rapida**.
7. Trascina il comando.
8. Campo **Accesso-Tasto/i** → ad esempio `CTRL+SHIFT+L`.
9. **Applica → OK**.

### Menu CAD/SPAC

```text
_MENU
```

Il menu/file specifico da ricaricare dipende dalla configurazione installata.

---

## Progetto, pagine e cartigli

### Pagina standard come Riferimento DWG

1. foglio libero;
2. **Modifica/Inserisci → Riferimento DWG**;
3. seleziona il DWG;
4. **Tipo di percorso → Percorso completo**;
5. **OK**;
6. posiziona il riferimento.

Non usare **Inserisci Blocco** per le pagine standard che devono restare collegate al sorgente.

### Legenda fogli

```text
Fogli → Legenda Fogli → Disegna
```

Poi seleziona un foglio vuoto e premi **OK**.

### Immagini

```text
IMMAGINI
```

- **Attacca** → collega immagine;
- **Stacca** → scollega immagine.

Se il path non è più valido:

```text
Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso
```

Bordo immagini:

```text
IMAGEFRAME
0
```

---

## Snap e griglia

```text
_DSETTINGS
```

Tab:

```text
Snap e griglia
```

Esempio usato:

```text
Intervallo snap X = 2,5
Intervallo snap Y = 2,5
```

---

## Schema unifilare

### Aprire Disegno Unifilare

```text
UNIFILARE → Disegno Unifilare
```

Campi principali della finestra:

- **Scelta Circuiti memorizzati**;
- **Tipo quadro**;
- **Monofase / Trifase**;
- **Composizione/Tipologia**;
- **Anteprima**;
- **Scelta del quadro**.

### Materiale su un livello

1. seleziona livello;
2. seleziona tipo dispositivo;
3. tasto destro sulla tabella materiali;
4. **Avvio DbCenter**;
5. scegli materiale.

### Ingresso linea

1. **Ingresso linea**;
2. compila livelli;
3. associa materiali;
4. verifica **Composizione/Tipologia**;
5. **Disegna**.

Nuova linea singola: togli spunta **Ingresso linea** → configura → **Disegna** → scegli posizione.

---

## Numerazione fili

### Fili non di alimentazione

```text
SPAC → Numera Fili
```

Poi:

1. tipo cavo;
2. **Modalita' di Numerazione**;
3. clic immagine modalità;
4. finestra **Configurazione Numerazione Conduttori**;
5. tab **Numerazione Conduttori**;
6. scegli modalità;
7. se **Foglio Numero**, scegli separatore;
8. **OK**;
9. **OK** nella finestra precedente;
10. interseca il cavo nello schema.

### Alimentazioni

Se manca l'identificatore:

```text
Identificatore Linee → tipo linea → OK
```

Poi interseca la linea nello schema.

Per fasi/neutro:

1. **Numerazione Fili**;
2. finestra **Numerazione Fili Unifilare**;
3. scegli, ad esempio, **L1 L2 L3 N**;
4. campo **Numero** → valore iniziale;
5. configura progressivo.

Per soli identificatori usa **Non utilizzare numero incrementale**.

Prefissi/suffissi:

```text
Prefissi o Suffissi Locali → Abilita
```

Funzionano solo se è attivo un numero incrementale.

### Lista numeri e rimandi

```text
Numerazione fili → Lista numeri usati
```

Per soli rimandi:

1. **Vedi solo i Rimandi**;
2. seleziona multifogli;
3. **Scansiona i Multifogli**.

Asterisco = numero ripetuto.

---

## Rimandi e cross-reference

### Creare un rimando

1. **Dynamic Coll** oppure **Dynamic Alim**;
2. numero fili;
3. traccia collegamento;
4. **Invio**;
5. scegli:
   - **Rimandi di arrivo**;
   - **Rimandi di partenza**;
   - **Rimandi di arrivo e partenza**;
6. scegli numero/nome filo;
7. eventuale tipo cavo;
8. **Ok**.

Secondo rimando: stesso nome e direzione coerente.

### Aggiornare cross-reference

```text
UTIL → Cross Reference
```

Poi:

1. **Rimandi**;
2. **Cross**;
3. scegli se mostrare il file Excel di output;
4. **Ok - Aggiorna**.

---

## Morsetti e morsettiere

### Aprire

```text
SPINSMOR
```

oppure **Inser Morsetti**.

Prerequisito: database materiali con almeno una morsettiera.

### Nuova morsettiera

**Inser Morsetti** → **Elenco Quadri** → tasto destro → **Nuova morsettiera**.

### Nuovo morsetto

1. seleziona morsettiera;
2. scegli tipo morsetto;
3. riquadro **Anteprima** → scegli rappresentazione;
4. per numero morsetto usa modello con `NumM`;
5. **Ok - Nuovo**;
6. clic sul filo nel punto di inserimento;
7. **Invio**.

| Campo | Significato |
|---|---|
| `NumI` | numero filo ingresso |
| `NumO` | numero filo uscita |
| `NumM` | numero morsetto |

---

## Simboli custom

### Importare DWG

```text
_INSER
```

Nella finestra puoi usare le tab **Disegno corrente**, **Recenti**, **Preferiti**, **Librerie**, oppure ricerca/sfoglia.

### Esplodere

```text
ESPLODI
```

Poi normalizza su:

- Layer `0`;
- Colore `DaBlocco`;
- Tipo linea `DaBlocco`;
- Spessore `DaBlocco`.

### Salvare DWG simbolo

```text
MBLOCCO
```

Impostazioni:

1. **Origine → Oggetti**;
2. seleziona punto base;
3. **Destinazione → Nome e percorso del file** → cartella `_CUSTOM` corretta;
4. **Unità inser. → Senza unità**;
5. salva.

### Creare SLD

1. apri DWG;
2. centra/zoom;
3. `_MSLIDE`;
4. salva nella stessa cartella e con lo stesso nome base.

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

---

## Attributi

### NOME

`ATTDEF`:

| Campo | Valore |
|---|---|
| Etichetta | `NOME` |
| Messaggio | `Sigla componente` |
| Default | vuoto |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

### PRES Madre

| Campo | Valore |
|---|---|
| Etichetta | `PRES` |
| Default | `M` |
| Invisibile | Sì |
| Costante | Sì |
| Blocca posizione | Sì |

### PINA1

| Campo | Valore |
|---|---|
| Etichetta | `PINA1` |
| Default | `1` |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

### PINB1

| Campo | Valore |
|---|---|
| Etichetta | `PINB1` |
| Default | `2` |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

Testo pin standard BLK custom: `1.5`.

Altri comandi:

```text
PROPRIETA / CTRL+1
CORRISPROP
EDITATT
```

`CORRISPROP`: sorgente → destinazione → **Invio**.

---

## Materiali

Su simbolo intelligente:

1. doppio click;
2. riquadro **Materiali**;
3. tasto destro;
4. **Avvio Archivio Materiali (DbCenter)**;
5. scegli materiale;
6. conferma;
7. verifica distinta/report.

---

## Tratteggio pieno

```text
Disegna → Tratteggio
```

Poi **I** → finestra **Tratteggio e sfumatura** → **Modello: SOLID** → colore → area.

---

## Layer e oggetti residui

### Layer non eliminabile

```text
PURGE
```

Se non eliminabile:

```text
Trova elementi non eliminabili
```

### Oggetto diretto sul layer

```text
QSELECT
```

Finestra **Selezione rapida** → filtro **Layer** → scegli layer → elimina/sposta oggetto → `PURGE`.

### Residuo dentro blocco

```text
BEDIT
```

Apri il blocco indicato da `PURGE` → elimina/sposta residuo → salva → `PURGE`.

Se annidato, modifica il blocco interno reale.

!!! danger "Non disponibili nell'ambiente verificato"

    Non proporre `LAYISO` o `LAYWALK` come soluzione SPAC Start 26.

---

## Ancora da verificare

Restano da consolidare solo i click che non sono stati ancora osservati direttamente, ad esempio alcuni pulsanti iniziali della creazione di un nuovo progetto/cartiglio. In quei casi la pagina specifica deve riportare **Da verificare** nel punto preciso.
