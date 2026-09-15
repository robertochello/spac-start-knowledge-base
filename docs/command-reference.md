# Comandi e percorsi esatti

Questa pagina raccoglie i **nomi esatti dei comandi**, delle finestre e delle voci da cliccare già verificati nella guida SPAC Start 26.

!!! important "Regola della knowledge base"

    Quando il percorso è noto, una procedura deve riportare: **comando da digitare**, **finestra che si apre**, **voce da cliccare**, **campo da impostare** e **risultato atteso**.

    Se il nome esatto non è stato ancora verificato in SPAC Start 26, va scritto `Da verificare`. Non inventare nomi plausibili di menu o pulsanti.

## Interfaccia e libreria simboli

### Ripristino/gestione menu

```text
_MENU
```

Il file/menu specifico da ricaricare dipende dalla configurazione installata.

### Aprire la libreria simboli

```text
SP_XML_MENU
```

Risultato atteso: apertura della libreria simboli SPAC.

### Creare una scorciatoia da tastiera per la libreria

1. Digita `CUI` oppure `_CUI`.
2. Nella finestra **Personalizza interfaccia utente**, vai in **Elenco comandi**.
3. Tasto destro → **Nuovo comando**.
4. Nome consigliato: `Libreria simboli`.
5. Nel campo **Macro** inserisci:

   ```text
   ^C^CSP_XML_MENU;
   ```

6. Nell'albero apri:

   ```text
   Tasti di scelta rapida → Tasti di scelta rapida
   ```

7. Trascina il comando dentro **Tasti di scelta rapida**.
8. Nel campo **Accesso-Tasto/i** imposta la combinazione, ad esempio `CTRL+SHIFT+L`.
9. Clicca **Applica** → **OK**.

## Snap e griglia

```text
_DSETTINGS
```

Nella finestra aperta seleziona il tab **Snap e griglia**.

## Immagini

### Gestione immagini

```text
IMMAGINI
```

Pulsanti verificati:

- **Attacca** → collega una nuova immagine;
- **Stacca** → rimuove il riferimento selezionato.

### Ripristinare il percorso di un'immagine

```text
Modifica/Inserisci → Gestioni immagini
```

Poi:

1. seleziona l'immagine;
2. **Sfoglia**;
3. riseleziona il file;
4. **Salva percorso**.

### Nascondere il bordo immagini

```text
IMAGEFRAME
```

Valore:

```text
0
```

## CAD e creazione simboli

### Inserire DWG/blocco

```text
_INSER
```

### Esplodere geometria

```text
ESPLODI
```

### Riempimento pieno

```text
Disegna → Tratteggio
```

Poi:

1. nella barra dei comandi usa **I**;
2. finestra **Tratteggio e sfumatura**;
3. campo **Modello** → `SOLID`;
4. scegli il colore;
5. seleziona l'area da riempire.

### Creare il DWG del simbolo

1. Seleziona gli oggetti.
2. Digita:

   ```text
   MBLOCCO
   ```

3. In **Origine** seleziona `Oggetti`.
4. Seleziona il **punto base**.
5. Salva nella categoria corretta sotto:

   ```text
   C:\SPAC Start 26\Librerie\Blk\_CUSTOM
   ```

### Creare l'anteprima SLD

1. Apri il DWG.
2. Centra il disegno e regola lo zoom.
3. Digita:

   ```text
   _MSLIDE
   ```

4. Salva nella stessa cartella del DWG.
5. Usa lo stesso nome base per `.dwg` e `.sld`.

## Attributi

### Creare un attributo

```text
ATTDEF
```

Per `NOME`:

| Campo | Valore |
|---|---|
| **Etichetta** | `NOME` |
| **Messaggio** | `Sigla componente` |

Per `PRES` di una Madre:

| Campo | Valore |
|---|---|
| **Etichetta** | `PRES` |
| **Default** | `M` |

Per `PINA1`:

| Campo | Valore |
|---|---|
| **Etichetta** | `PINA1` |
| **Default** | `1` |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

Per il pin di uscita corrispondente usa `PINB1` mantenendo la stessa numerazione della coppia.

### Proprietà

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

### Copiare proprietà

```text
CORRISPROP
```

### Modificare attributi di un'istanza

```text
EDITATT
```

## Numerazione fili non di alimentazione

### Avviare la numerazione

```text
SPAC → Numera Fili
```

Poi:

1. seleziona il tipo di cavo;
2. a destra individua **Modalita' di Numerazione**;
3. clicca sull'immagine della modalità;
4. nella finestra **Configurazione Numerazione Conduttori** apri il tab **Numerazione Conduttori**;
5. seleziona la **Modalita' di Numerazione**;
6. se scegli **Foglio Numero**, seleziona anche il separatore;
7. torna allo schema;
8. evidenzia il cavo tracciando una linea che lo interseca.

### Lista dei numeri usati

```text
Numerazione fili → Lista numeri usati
```

I numeri con asterisco sono ripetuti.

### Eliminare numerazione

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

La funzione elimina i numeri, non i fili.

## Fili di alimentazione

### Aggiungere l'identificatore alla linea

Se manca il simbolo identificatore:

1. barra dei menu → **Identificatore Linee**;
2. seleziona il tipo di linea;
3. **OK**;
4. torna allo schema;
5. evidenzia la linea tracciando una linea che la interseca.

### Numerare/identificare fasi e neutro

1. Seleziona **Numerazione Fili**.
2. Nella finestra **Numerazione Fili Unifilare**, scegli il tipo di fase/neutro, ad esempio `L1 L2 L3 N`.
3. Nel campo accanto a **Numero** imposta il numero di partenza, ad esempio `1`.
4. Configura il progressivo numerico.
5. Se vuoi solo `L1`, `L2`, `L3`, `N`, disattiva il progressivo.

## Morsetti e morsettiere

### Aprire Inser Morsetti

Nome funzione:

```text
Inser Morsetti
```

Comando equivalente da riga comando:

```text
SPINSMOR
```

Prerequisito: deve essere aperto un database materiali contenente almeno una morsettiera.

### Creare una nuova morsettiera

Nella finestra **Inser Morsetti**:

1. individua il riquadro in alto a sinistra **Elenco Quadri**;
2. tasto destro su **Elenco Quadri**, sul nome del quadro oppure su una morsettiera esistente;
3. clicca **Nuova morsettiera**.

## Associazione materiali

Sul simbolo:

1. **doppio click sul simbolo**;
2. riquadro **Materiali**;
3. **tasto destro**;
4. clicca **Avvio Archivio Materiali (DbCenter)**;
5. seleziona il materiale corretto;
6. verifica distinta/report.

## Layer e oggetti residui

### Verificare perché un layer non si elimina

Digita:

```text
PURGE
```

Nella finestra controlla:

```text
Elementi eliminabili → Layer
```

Se il layer non è eliminabile, usa:

```text
Trova elementi non eliminabili
```

Seleziona il layer interessato e verifica quale oggetto o blocco lo referenzia.

### Se il riferimento è un oggetto diretto

Digita:

```text
QSELECT
```

Nella finestra **Selezione rapida**:

1. filtra per proprietà **Layer**;
2. scegli il layer problematico;
3. conferma;
4. elimina l'oggetto inutile oppure spostalo sul layer corretto;
5. riesegui `PURGE`.

### Se il riferimento è dentro un blocco

Digita:

```text
BEDIT
```

Poi:

1. seleziona il blocco indicato da `PURGE`;
2. individua la geometria sul layer problematico;
3. elimina o sposta la geometria correttamente;
4. salva e chiudi il Block Editor;
5. riesegui `PURGE`.

Se l'oggetto è dentro un blocco annidato, modifica con `BEDIT` il blocco interno che possiede realmente la geometria.

!!! danger "Non disponibili in SPAC Start 26"

    `LAYISO` e `LAYWALK` risultano non disponibili nell'ambiente SPAC Start 26 verificato e non devono essere proposti come procedura.

## Riferimento rapido

| Operazione | Comando / percorso esatto |
|---|---|
| Ripristino/gestione menu | `_MENU` |
| Libreria simboli | `SP_XML_MENU` |
| Shortcut interfaccia | `CUI` / `_CUI` |
| Snap e griglia | `_DSETTINGS` → **Snap e griglia** |
| Gestire immagini | `IMMAGINI` |
| Ripristinare immagine | **Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso** |
| Togliere bordo immagini | `IMAGEFRAME` → `0` |
| Inserire DWG/blocco | `_INSER` |
| Esplodere geometria | `ESPLODI` |
| Tratteggio pieno | **Disegna → Tratteggio → I → Tratteggio e sfumatura → Modello: SOLID** |
| Salvare DWG simbolo | `MBLOCCO` → **Origine: Oggetti** |
| Creare SLD | `_MSLIDE` |
| Creare attributo | `ATTDEF` |
| Proprietà | `PROPRIETA` / `CTRL+1` |
| Copiare proprietà | `CORRISPROP` |
| Modificare attributi istanza | `EDITATT` |
| Numerare fili normali | **SPAC → Numera Fili** |
| Configurare numerazione | **Configurazione Numerazione Conduttori → Numerazione Conduttori** |
| Lista numeri usati | **Numerazione fili → Lista numeri usati** |
| Eliminare numerazione | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Identificare alimentazione | **Identificatore Linee** → tipo linea → **OK** |
| Numerare alimentazione | **Numerazione Fili** → **Numerazione Fili Unifilare** |
| Inserire morsetti | **Inser Morsetti** / `SPINSMOR` |
| Creare morsettiera | **Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera** |
| Associare materiale | **doppio click simbolo → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)** |
| Layer non eliminabile | `PURGE` → **Trova elementi non eliminabili** |
| Selezionare oggetti di un layer | `QSELECT` → **Layer** |
| Residuo dentro un blocco | `BEDIT` → modifica blocco → salva → `PURGE` |

## Ancora da verificare

Sezioni per cui la knowledge base conosce la logica ma non ha ancora consolidato il nome esatto di ogni comando/percorso devono restare marcate `Da verificare`, in particolare dove indicato nelle relative pagine operative.
