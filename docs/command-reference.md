# Comandi e percorsi esatti

Questa pagina raccoglie i **nomi esatti dei comandi**, delle finestre e delle voci da cliccare già verificati nella guida SPAC Start 26.

!!! important "Regola della knowledge base"

    Una procedura operativa non deve limitarsi a dire "aprire la libreria", "creare un blocco" o "inserire un morsetto". Quando il percorso è noto deve riportare, nell'ordine: **comando da digitare**, **finestra che si apre**, **voce da cliccare**, **campo da impostare** e **risultato atteso**.

    Se il nome esatto non è stato ancora verificato in SPAC Start 26, va scritto esplicitamente `Da verificare` invece di inventare il percorso.

## Libreria simboli

### Aprire direttamente la libreria simboli

Nella riga comando digitare:

```text
SP_XML_MENU
```

Risultato atteso: apertura della libreria simboli SPAC.

### Creare una scorciatoia da tastiera per la libreria

1. Nella riga comando digitare:

   ```text
   CUI
   ```

   oppure:

   ```text
   _CUI
   ```

2. Nella finestra **Personalizza interfaccia utente**, andare nel riquadro **Elenco comandi**.
3. Tasto destro in **Elenco comandi** → **Nuovo comando**.
4. Assegnare un nome, ad esempio `Libreria simboli`.
5. Nel campo **Macro** inserire:

   ```text
   ^C^CSP_XML_MENU;
   ```

6. Nell'albero di personalizzazione aprire:

   ```text
   Tasti di scelta rapida → Tasti di scelta rapida
   ```

7. Trascinare il nuovo comando dentro **Tasti di scelta rapida**.
8. Selezionare il comando e compilare **Accesso-Tasto/i**, ad esempio `CTRL+SHIFT+L`.
9. Cliccare **Applica** → **OK**.

## Snap e griglia

Nella riga comando digitare:

```text
_DSETTINGS
```

Nella finestra aperta selezionare il tab **Snap e griglia**.

Qui si impostano gli intervalli di snap X/Y e della griglia.

## Immagini

### Gestione immagini collegate

Nella riga comando digitare:

```text
IMMAGINI
```

Nella finestra:

- **Attacca** → inserisce una nuova immagine;
- **Stacca** → rimuove il riferimento dell'immagine selezionata.

### Ripristinare il percorso di un'immagine non trovata

Percorso verificato:

```text
Modifica/Inserisci → Gestioni immagini
```

Poi:

1. selezionare l'immagine interessata;
2. cliccare **Sfoglia**;
3. selezionare nuovamente il file;
4. cliccare **Salva percorso**.

### Nascondere il bordo delle immagini

Nella riga comando digitare:

```text
IMAGEFRAME
```

Impostare:

```text
0
```

Il comando deve essere eseguito anche nei nuovi progetti se il bordo torna visibile.

## Creazione simboli custom

### Inserire un DWG o blocco di partenza

Comando da riga comando:

```text
_INSER
```

### Esplodere la geometria importata

Comando:

```text
ESPLODI
```

Usarlo solo quando serve realmente modificare le singole entità.

### Creare il file DWG del simbolo

1. Selezionare tutta la geometria del simbolo.
2. Nella riga comando digitare:

   ```text
   MBLOCCO
   ```

3. Nella finestra del comando, in **Origine**, selezionare `Oggetti`.
4. Indicare il **punto base** del simbolo.
5. Salvare il `.dwg` nella categoria corretta sotto:

   ```text
   C:\SPAC Start 26\Librerie\Blk\_CUSTOM
   ```

### Creare l'anteprima SLD

1. Aprire direttamente il DWG del simbolo.
2. Centrare il disegno e regolare lo zoom.
3. Nella riga comando digitare:

   ```text
   _MSLIDE
   ```

4. Salvare il file `.sld` nella stessa cartella del `.dwg`.
5. Il nome base deve essere identico:

   ```text
   NOME_SIMBOLO.dwg
   NOME_SIMBOLO.sld
   ```

## Attributi dei simboli

### Creare un attributo

Comando:

```text
ATTDEF
```

Per `NOME` usare almeno:

| Campo | Valore |
|---|---|
| **Etichetta** | `NOME` |
| **Messaggio** | `Sigla componente` |

Per un simbolo Madre, `PRES` deve avere:

| Campo | Valore |
|---|---|
| **Etichetta** | `PRES` |
| **Default** | `M` |

Per il primo pin di ingresso:

| Campo | Valore |
|---|---|
| **Etichetta** | `PINA1` |
| **Default** | `1` |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

Per il pin corrispondente di uscita usare `PINB1`; la numerazione deve restare coerente con `PINA1`.

### Modificare le proprietà

Comando:

```text
PROPRIETA
```

Scorciatoia equivalente:

```text
CTRL+1
```

### Copiare proprietà da un oggetto a un altro

Comando:

```text
CORRISPROP
```

### Modificare gli attributi di un'istanza

Comando:

```text
EDITATT
```

## Multifilare: fili e numerazioni

### Visualizzare la lista dei numeri usati

Percorso verificato:

```text
Numerazione fili → Lista numeri usati
```

I numeri marcati con asterisco indicano numerazioni ripetute.

### Eliminare la numerazione fili

Percorso verificato:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente da riga comando:

```text
DEL_NUMF
```

## Multifilare: morsetti e morsettiere

### Aprire Inser Morsetti

Comando da riga comando:

```text
SPINSMOR
```

Prerequisito: deve essere aperto un database materiali contenente almeno una morsettiera.

### Creare una nuova morsettiera

Nella finestra **Inser Morsetti**:

1. individuare il riquadro in alto a sinistra **Elenco Quadri**;
2. tasto destro su **Elenco Quadri**, sul nome del quadro oppure su una morsettiera esistente;
3. cliccare **Nuova morsettiera**.

## Riferimento rapido

| Cosa devi fare | Comando / percorso esatto |
|---|---|
| Aprire libreria simboli | `SP_XML_MENU` |
| Personalizzare shortcut | `CUI` / `_CUI` |
| Snap e griglia | `_DSETTINGS` → **Snap e griglia** |
| Gestire immagini | `IMMAGINI` |
| Ripristinare immagine | **Modifica/Inserisci** → **Gestioni immagini** → **Sfoglia** → **Salva percorso** |
| Togliere bordo immagini | `IMAGEFRAME` → `0` |
| Inserire DWG/blocco | `_INSER` |
| Esplodere geometria | `ESPLODI` |
| Salvare simbolo DWG | `MBLOCCO` → **Origine: Oggetti** |
| Creare anteprima | `_MSLIDE` |
| Creare attributo | `ATTDEF` |
| Proprietà | `PROPRIETA` / `CTRL+1` |
| Copiare proprietà | `CORRISPROP` |
| Modificare attributi istanza | `EDITATT` |
| Lista numeri usati | **Numerazione fili** → **Lista numeri usati** |
| Eliminare numerazione | **SPAC** → **Utility Fili** → **Elimina numerazione** oppure `DEL_NUMF` |
| Inserire morsetti | `SPINSMOR` |
| Creare morsettiera | **Inser Morsetti** → tasto destro in **Elenco Quadri** → **Nuova morsettiera** |

## Regola per i prossimi aggiornamenti

Ogni nuovo comando consolidato deve riportare:

1. nome esatto del comando;
2. percorso esatto da cliccare, se disponibile;
3. nome della finestra che si apre;
4. campi o pulsanti da usare;
5. valore da impostare;
6. esito atteso;
7. eventuale prerequisito o errore noto.
