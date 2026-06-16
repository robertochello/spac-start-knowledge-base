# Guida operativa SPAC Start 26

## Indice

- [Guida operativa SPAC Start 26](#guida-operativa-spac-start-26)
  - [Indice](#indice)
  - [Scopo](#scopo)
  - [Come usare questa guida](#come-usare-questa-guida)
  - [Download e file pubblici](#download-e-file-pubblici)
  - [Installazione e impostazioni](#installazione-e-impostazioni)
    - [Installazione cartella libreria custom](#installazione-cartella-libreria-custom)
    - [Categorie libreria custom](#categorie-libreria-custom)
    - [Creazione shortcut da tastiera personalizzati](#creazione-shortcut-da-tastiera-personalizzati)
      - [Esempio: shortcut per aprire la libreria simboli](#esempio-shortcut-per-aprire-la-libreria-simboli)
      - [Procedura](#procedura)
    - [Operazioni grafiche comuni](#operazioni-grafiche-comuni)
      - [Colorare o riempire una forma](#colorare-o-riempire-una-forma)
    - [Come inserire immagini](#come-inserire-immagini)
      - [Ripristinare immagini non visualizzate](#ripristinare-immagini-non-visualizzate)
      - [Eliminare il bordo delle immagini](#eliminare-il-bordo-delle-immagini)
  - [Preparazione progetto](#preparazione-progetto)
    - [Template progetto generico](#template-progetto-generico)
      - [Procedura](#procedura-1)
      - [Legenda fogli](#legenda-fogli)
  - [Procedure comuni di schema](#procedure-comuni-di-schema)
    - [Cross reference](#cross-reference)
  - [Schema unifilare](#schema-unifilare)
    - [Preparazione](#preparazione)
    - [Impostazione snap e griglia](#impostazione-snap-e-griglia)
    - [Disegno unifilare](#disegno-unifilare)
    - [Ingresso linea e nuove linee](#ingresso-linea-e-nuove-linee)
    - [Numerazione fili non di alimentazione](#numerazione-fili-non-di-alimentazione)
    - [Identificazione fili di alimentazione](#identificazione-fili-di-alimentazione)
  - [Schema multifilare](#schema-multifilare)
    - [Lista completa dei rimandi](#lista-completa-dei-rimandi)
    - [Eliminare numerazione fili](#eliminare-numerazione-fili)
    - [Inserimento e utilizzo di morsetti e morsettiere](#inserimento-e-utilizzo-di-morsetti-e-morsettiere)
    - [Associazione accessorio a dispositivo Madre](#associazione-accessorio-a-dispositivo-madre)
  - [Creazione e manutenzione simboli custom](#creazione-e-manutenzione-simboli-custom)
    - [Creazione elemento grafico](#creazione-elemento-grafico)
      - [Procedura](#procedura-2)
      - [Importazione da DWG esterno](#importazione-da-dwg-esterno)
      - [Importazione da simbolo SPAC esistente](#importazione-da-simbolo-spac-esistente)
      - [Pulizia e normalizzazione](#pulizia-e-normalizzazione)
      - [Creazione del blocco DWG](#creazione-del-blocco-dwg)
      - [Creazione della slide SLD](#creazione-della-slide-sld)
    - [Differenza tra Simbolo Madre e Simbolo Figlio in SPAC](#differenza-tra-simbolo-madre-e-simbolo-figlio-in-spac)
      - [Sintesi rapida](#sintesi-rapida)
      - [Simbolo Madre](#simbolo-madre)
      - [Simbolo Figlio](#simbolo-figlio)
    - [Creazione elemento intelligente](#creazione-elemento-intelligente)
      - [Preparazione](#preparazione-1)
      - [Attributo `NOME`](#attributo-nome)
      - [Attributo `PRES`](#attributo-pres)
      - [Attributi `PINA1` e `PINB1`](#attributi-pina1-e-pinb1)
      - [Modifica stile attributi](#modifica-stile-attributi)
      - [Salvataggio simbolo intelligente](#salvataggio-simbolo-intelligente)
    - [Associazione materiale al simbolo intelligente](#associazione-materiale-al-simbolo-intelligente)
  - [Convenzioni e catalogo libreria](#convenzioni-e-catalogo-libreria)
    - [Convenzione di nomenclatura simboli](#convenzione-di-nomenclatura-simboli)
      - [Obiettivo](#obiettivo)
      - [Formato standard](#formato-standard)
      - [Significato dei campi](#significato-dei-campi)
      - [Regole formali](#regole-formali)
      - [Regola di priorità](#regola-di-priorità)
    - [Dizionario abbreviazioni](#dizionario-abbreviazioni)
      - [Note sulle abbreviazioni](#note-sulle-abbreviazioni)
    - [Simboli realizzati](#simboli-realizzati)

## Scopo

Questo documento definisce il workflow operativo per usare SPAC Start 26 con la libreria custom `_CUSTOM`, creare progetti unifilari e multifilari, gestire rimandi/cross reference e mantenere ordinata la libreria dei simboli BLK.

La guida copre:

- installazione e struttura della cartella libreria `_CUSTOM`;
- impostazioni operative comuni, shortcut, immagini e operazioni grafiche;
- preparazione del template progetto;
- procedure comuni agli schemi, inclusi i cross reference;
- procedure specifiche per schema unifilare e schema multifilare;
- creazione di simboli grafici e simboli intelligenti;
- gestione degli attributi principali, dei materiali e dei rapporti Madre/Figlio;
- convenzione di nomenclatura, abbreviazioni e catalogo dei simboli realizzati.

> Nota operativa: i path completi delle categorie e la relativa descrizione master sono mantenuti nel file Excel dedicato alla libreria. In questo README vengono riportati solo i criteri operativi e i simboli realizzati.

---

## Come usare questa guida

La guida e' organizzata in ordine operativo.

1. Usare **Installazione e impostazioni** per preparare la libreria, l'ambiente di lavoro e le risorse comuni.
2. Usare **Preparazione progetto** per creare la base della commessa e inserire i fogli standard.
3. Usare **Procedure comuni di schema** per le funzioni valide sia in unifilare sia in multifilare.
4. Usare **Schema unifilare** o **Schema multifilare** in base al tipo di elaborato.
5. Usare **Creazione e manutenzione simboli custom** quando bisogna creare o correggere simboli della libreria.
6. Usare **Convenzioni e catalogo libreria** per verificare nomi, abbreviazioni e simboli gia' realizzati.

---

## Download e file pubblici

Il sito può pubblicare file scaricabili, ad esempio archivi materiali o archivi cavi.

La pagina di riferimento è:

```text
downloads.md
```

Le cartelle pubbliche predisposte sono:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

Regole operative:

- pubblicare solo file generici o sanitizzati;
- non inserire dati cliente, commessa o contenuti non pubblicabili;
- usare nomi file chiari, senza spazi e con release;
- aggiornare la pagina Download dopo aver aggiunto o sostituito un file;
- verificare il link dopo la build del sito.

File materiali attualmente collegati:

- `ABB_Materials.db`;
- `archivio-materiali-custom-r01.db`.

---

## Installazione e impostazioni

Questa parte raccoglie le operazioni da completare prima di lavorare su una commessa o sulla libreria.

### Installazione cartella libreria custom

Assicurarsi che la cartella di installazione del software sia:

`C:\SPAC Start 26`

La libreria viene distribuita già completa della cartella `_CUSTOM` e delle relative sottocartelle.

Non è necessario creare manualmente le cartelle o eseguire script PowerShell.

La cartella `_CUSTOM` deve essere copiata dentro:

```text
C:\SPAC Start 26\Librerie\Blk
```

Il risultato finale deve essere:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM
```

Procedura:

1. Chiudere SPAC Start 26, se aperto.
2. Copiare la cartella `_CUSTOM` fornita con la libreria.
3. Incollarla nella cartella `C:\SPAC Start 26\Librerie\Blk`.
4. Verificare che dentro `_CUSTOM` siano presenti le categorie della libreria e la cartella `Documentazione`.
5. Riavviare SPAC Start 26 e verificare la visibilità dei simboli nella libreria BLK.

Se la cartella `_CUSTOM` è già presente, verificare il contenuto prima di sovrascrivere file esistenti.

### Categorie libreria custom

La classificazione dei simboli deve rimanere stabile nel tempo.

| Categoria | Utilizzo |
|---|---|
| `00_SIMBOLI_GRAFICI` | Simboli grafici generici, elementi di comando, segnalazione o rappresentazioni senza logica elettrica complessa. |
| `01_ALIMENTATORI` | Alimentatori, trasformatori, UPS, sorgenti e dispositivi di alimentazione. |
| `02_PROTEZIONI` | Protezioni dedicate non classificate come interruttori/sezionatori. |
| `03_RELE_INTERFACCE` | Relè, interfacce, moduli di isolamento e dispositivi di appoggio ai comandi. |
| `04_MODULI_IO_PLC` | PLC, moduli I/O, moduli remoti e dispositivi di automazione. |
| `05_SENSORI` | Sensori, finecorsa, proximity, pressostati, termostati e dispositivi di rilevamento. |
| `06_ATTUATORI_DRIVE` | Attuatori, motori, inverter, drive, elettrovalvole e dispositivi di movimento. |
| `07_COMUNICAZIONE` | Switch, gateway, router, convertitori, dispositivi di rete e comunicazione industriale. |
| `08_MORSETTI_CONNETTORI` | Morsetti, connettori, spine, prese e punti di connessione. |
| `09_STRUMENTAZIONE` | Multimetri, strumenti di misura, analizzatori, amperometri, voltmetri e strumenti da pannello. |
| `10_INTERRUTTORI` | Interruttori, magnetotermici, differenziali, sezionatori, manuali, fusibilati, motorizzati ed estraibili. |
| `99_GENERICI` | Simboli provvisori, generici o non ancora classificati. Da usare solo come area temporanea. |
| `Documentazione` | Documentazione con `README.md` e file Excel contenente la lista dei simboli realizzati. |

Regola operativa:

- tutto ciò che inizia con `INT_` deve stare in `10_INTERRUTTORI`;
- tutto ciò che è strumentazione deve stare in `09_STRUMENTAZIONE`;
- tutto ciò che è protezione non riconducibile a interruttori/sezionatori può stare in `02_PROTEZIONI`;
- `99_GENERICI` non deve diventare una cartella definitiva di lavoro.

### Creazione shortcut da tastiera personalizzati

In SPAC Start 26 è possibile associare una combinazione da tastiera a un comando tramite la personalizzazione CUI.

#### Esempio: shortcut per aprire la libreria simboli

Comando SPAC da richiamare:

```text
SP_XML_MENU
```

#### Procedura

1. Digitare nella riga comando:

   ```text
   CUI
   ```

   oppure:

   ```text
   _CUI
   ```

2. Nella finestra **Personalizza interfaccia utente**, creare un nuovo comando nella sezione **Elenco comandi** con tasto destro → **Nuovo comando**.
3. Assegnare al comando un nome chiaro, ad esempio `Libreria simboli`.
4. Inserire nel campo **Macro**:

   ```text
   ^C^CSP_XML_MENU;
   ```

5. Nell'albero di personalizzazione andare in:

   ```text
   Tasti di scelta rapida → Tasti di scelta rapida
   ```

6. Trascinare il comando appena creato dentro **Tasti di scelta rapida**.
7. Selezionare il comando e impostare la combinazione nel campo **Accesso-Tasto/i**, ad esempio:

   ```text
   CTRL+SHIFT+L
   ```

8. Confermare con **Applica** e poi **OK**.

### Operazioni grafiche comuni

Queste procedure valgono sia per lo schema unifilare sia per lo schema multifilare.

#### Colorare o riempire una forma

Per colorare o riempire una forma:

1. Aprire il menu **Disegna**.
2. Cliccare **Tratteggio**.
3. Nella barra dei comandi cliccare **I** per aprire le impostazioni.
4. Nella finestra **Tratteggio e sfumatura**, alla voce **Modello**, selezionare `SOLID`.
5. Scegliere il colore da applicare.
6. Confermare e selezionare l'area o la forma da riempire.

### Come inserire immagini

Nella barra dei comandi utilizzare il comando:

```text
IMMAGINI
```

Se nella pagina sono già presenti immagini, il relativo path comparirà nella lista.

Per eliminare immagini:

1. Selezionare l'immagine nella lista.
2. Premere **Stacca**.

Per inserire nuove immagini:

1. Premere **Attacca**.
2. Selezionare il file immagine.
3. Verificare che il riferimento rimanga valido dopo il salvataggio e la riapertura del progetto.

#### Ripristinare immagini non visualizzate

Se un progetto viene spostato da un PC a un altro, puo' capitare che le immagini inserite non vengano piu' visualizzate correttamente.

Per risolvere:

1. Verificare prima che il file immagine sia presente nel path indicato nel riquadro in cui dovrebbe comparire l'immagine.
2. Aprire il menu **Modifica/Inserisci**.
3. Selezionare **Gestioni immagini**.
4. Nella finestra che si apre, individuare l'immagine interessata tra quelle presenti nel progetto.
5. Cliccare **Sfoglia**.
6. Cercare nuovamente l'immagine all'interno del PC.
7. Cliccare **Salva percorso**.

#### Eliminare il bordo delle immagini

Di default le immagini inserite possono essere visualizzate con il bordo.

Per eliminare il bordo da tutte le immagini del disegno, digitare nella riga comando:

```text
IMAGEFRAME
```

Impostare quindi il valore:

```text
0
```

> Importante: anche se nel cartiglio master, o in qualsiasi `.dwg` creato e poi importato nel progetto, e' gia' stato impostato `IMAGEFRAME = 0`, in ogni nuovo progetto bisogna eseguire di nuovo lo stesso comando per non visualizzare il bordo delle immagini.

Nota operativa:

- per loghi e immagini ricorrenti, usare la cartella stabile `97_RISORSE\IMMAGINI`;
- preferire percorsi controllati e riutilizzabili;
- dopo aver inserito un'immagine in un foglio o nel cartiglio master, non spostare, rinominare o eliminare il file sorgente;
- verificare sempre il comportamento dopo chiusura e riapertura del progetto.

Le immagini inserite mantengono un riferimento al file esterno. Se il file viene spostato rispetto al percorso usato al momento dell'inserimento, SPAC potrebbe non riuscire piu' a caricarlo correttamente nei fogli o nei progetti basati sul cartiglio master.

---

## Preparazione progetto

Questa parte descrive la base comune da usare prima di sviluppare gli schemi.

### Template progetto generico

Questa sezione descrive la creazione di un template riutilizzabile per progetti **UNIFILARI** e **MULTIFILARI**.

Il template e' una base comune. Le differenze operative tra schema unifilare e schema multifilare devono essere documentate in sezioni dedicate.

#### Procedura

1. Creare un nuovo progetto con le informazioni principali della commessa.
2. Scegliere il cartiglio master.
3. Inserire il numero di fogli necessario, lasciando fogli liberi per le pagine standard.
4. Sul foglio 1 inserire come **riferimento DWG** il file:

   ```text
   01_BLOCCO_DATI
   ```

   Il blocco rappresenta il foglio iniziale con i dati del cliente e dell'azienda.

5. Sul foglio 2 inserire come **riferimento DWG** il file:

   ```text
   02_BLOCCO_DISPOSIZIONI_SICUREZZA
   ```

   Il blocco rappresenta il foglio con le informazioni di sicurezza del quadro.

6. Sul foglio 3 inserire come **riferimento DWG** il file:

   ```text
   03_BLOCCO_TARGA_QUADRO
   ```

   Il blocco rappresenta il foglio per la targa quadro e la marcatura CE.

I blocchi delle pagine standard non devono essere inseriti con **Inserisci Blocco**.
Devono essere collegati come riferimento DWG.

Procedura corretta:

1. Aprire un foglio libero.
2. Cliccare il menu **Modifica/Inserisci**.
3. Cliccare **Riferimento DWG**.
4. Navigare fino alla cartella in cui si trova il DWG della pagina standard da inserire.
5. Selezionare il file DWG interessato.
6. Nella finestra successiva, nella sezione **Tipo di percorso** a destra, selezionare **Percorso completo**.
7. Premere **OK**.
8. Posizionare il riferimento DWG nel foglio.

Questa procedura permette di mantenere il collegamento al DWG originale della pagina standard.

#### Legenda fogli

Per inserire la lista dei fogli del progetto:

1. Aprire il menu **Fogli**.
2. Cliccare **Legenda Fogli**.
3. Premere **Disegna**.
4. Selezionare un foglio vuoto.
5. Premere **OK** per confermare.

Per aggiornare la lista dei fogli, rigenerare la tabella e inserirla sempre nello stesso foglio.

---

## Procedure comuni di schema

Queste procedure valgono sia per lo schema unifilare sia per lo schema multifilare.

### Cross reference

Il cross reference dei rimandi e' una procedura comune sia allo schema unifilare sia allo schema multifilare.

Per creare il cross reference tra due fili o collegamenti, i fili devono avere lo stesso nome.

Il filo, l'alimentazione o il collegamento devono essere creati gia' predisposti con il rimando.

Procedura per creare il primo rimando:

1. Selezionare **Dynamic Coll** oppure **Dynamic Alim**.
2. Selezionare il numero di fili.
3. Tracciare il cavo.
4. Premere **Invio**.
5. Scegliere il tipo di rimando:

   - **Rimandi di arrivo**;
   - **Rimandi di partenza**;
   - **Rimandi di arrivo e partenza**.

6. Scegliere il numero o nome del filo.
7. Se necessario, scegliere il tipo di cavo.
8. Cliccare **Ok** per posizionare il filo.

Per ottenere il rimando a quel filo, o da quel filo, bisogna creare un secondo rimando con lo stesso nome.

La direzione del secondo rimando deve essere coerente con il primo:

- se il primo rimando e' di **partenza**, il secondo deve essere di **arrivo** oppure **arrivo e partenza**;
- se il primo rimando e' di **arrivo**, il secondo deve essere di **partenza** oppure **arrivo e partenza**.

Dopo aver creato i rimandi con lo stesso nome, aggiornare il cross reference.

Procedura:

1. Aprire il menu **UTIL**.
2. Selezionare **Cross Reference**.
3. Scegliere il tipo di elaborazione **Rimandi**.
4. Cliccare **Cross**.
5. Scegliere se visualizzare o meno l'output del cross reference, cioe' il file Excel generato.
6. Premere **Ok - Aggiorna**.

---

## Schema unifilare

Questa sezione descrive la realizzazione dello schema unifilare dopo le operazioni preliminari di creazione del progetto, inserimento fogli, inserimento fogli standard e rimozione del frame delle immagini.

### Preparazione

Prima di iniziare lo schema:

1. Assicurarsi di utilizzare la simbologia unifilare.
2. Nella barra superiore selezionare **UNIFILARE**.
3. Selezionare **Disegno Unifilare**.

### Impostazione snap e griglia

Per modificare le impostazioni del disegno, digitare nella riga comando:

```text
_DSETTINGS
```

Nel tab **Snap e griglia** si possono configurare gli intervalli di snap lungo gli assi X e Y.

Esempio:

```text
Intervallo snap X = 2,5
Intervallo snap Y = 2,5
```

Con questa impostazione il cursore si muove con passo di `2,5` in entrambe le direzioni. Se la griglia principale ha passo `10`, ogni quadrato della griglia viene suddiviso in 4 parti per lato, quindi in 16 quadratini.

### Disegno unifilare

Nella finestra **Disegno Unifilare** sono presenti diversi campi di configurazione.

Campi principali:

- **Scelta Circuiti memorizzati**: permette di selezionare circuiti gia' predisposti, per esempio ingresso linea, sottoquadro o blindo.
- **Tipo quadro**: permette di filtrare o selezionare il tipo di quadro, per esempio **Tutte**, **Blindo**, **Fotovoltaico**.
- **Monofase / Trifase**: definisce il tipo di alimentazione del circuito o del quadro.
- **Composizione/Tipologia**: definisce cosa deve contenere ogni livello, il tipo di cavo e il fine circuito.
- **Anteprima**: mostra come verra' disegnata automaticamente la linea configurata.
- **Scelta del quadro**: permette di associare la linea al quadro corretto.

A destra e' presente la tabella con i dati del componente da utilizzare per ogni livello.

Per associare il materiale:

1. Selezionare il livello interessato.
2. Selezionare il tipo di dispositivo.
3. Cliccare con il tasto destro sulla tabella dei materiali.
4. Selezionare **Avvio DbCenter**.
5. Scegliere il materiale da utilizzare.

### Ingresso linea e nuove linee

Per iniziare lo schema e' consigliato disegnare prima l'ingresso linea.

Procedura:

1. Selezionare la voce dedicata all'ingresso linea.
2. Compilare i livelli necessari.
3. Associare i materiali dei componenti.
4. Premere **Disegna**.

SPAC disegna automaticamente la linea nello schema e genera anche la tabella con le informazioni relative ai materiali utilizzati e al cavo della linea.

Ogni volta che viene disegnata una linea, la finestra resta in primo piano per permettere l'inserimento di una nuova linea.

Per disegnare una nuova linea singola:

1. Togliere la spunta da **Ingresso linea**.
2. Configurare la linea secondo necessita', come fatto per la linea di partenza.
3. Premere **Disegna**.
4. Scegliere nello schema la posizione della nuova linea.

### Numerazione fili non di alimentazione

Per numerare i fili:

1. Aprire il menu **SPAC**.
2. Selezionare **Numera Fili**.
3. Nella finestra che si apre, selezionare il tipo di cavo dalla lista.
4. Specificare la modalita' di numerazione.

A destra e' presente la sezione **Modalita' di Numerazione**.

Per configurarla:

1. Cliccare sull'immagine della modalita' di numerazione.
2. Nella finestra **Configurazione Numerazione Conduttori**, aprire il tab **Numerazione Conduttori**.
3. Selezionare la **Modalita' di Numerazione**.
4. Selezionando **Foglio Numero**, scegliere il separatore da utilizzare.

Con la modalita' **Foglio Numero**, l'output sara' del tipo:

```text
numeroPagina.numeroIncrementale
```

Dopo aver confermato:

1. Premere **OK** nella finestra **Configurazione Numerazione Conduttori**.
2. Premere **OK** nella finestra precedente.
3. Tornare allo schema.
4. Evidenziare il cavo da numerare tracciando una linea che interseca il cavo.

> Nota: si possono numerare solo i fili che non sono di alimentazione.

### Identificazione fili di alimentazione

I fili di alimentazione non vengono gestiti come semplici fili da numerare: devono avere un identificatore, in modo che SPAC sappia se si tratta di fasi, neutro o altri conduttori.

Con la procedura descritta per il disegno unifilare, la linea di partenza dovrebbe gia' avere l'identificatore perche' in **Composizione/Tipologia** e' stato definito come deve essere composta la linea.

Se il simbolo dell'identificatore non e' presente sulla linea:

1. Selezionare **Identificatore Linee** dalla barra dei menu.
2. Selezionare il tipo di linea.
3. Premere **OK**.
4. Evidenziare la linea interessata tracciando una linea che la interseca.

Una volta verificato che la linea ha il proprio identificatore, si puo' procedere con l'identificazione tramite numerazione.

Procedura:

1. Selezionare **Numerazione Fili**.
2. Nella finestra **Numerazione Fili Unifilare**, selezionare il tipo di fase/neutro da utilizzare, per esempio **L1 L2 L3 N**.
3. Nel campo accanto a **Numero**, indicare il numero di partenza, per esempio `1`.
4. Configurare l'uso del numero incrementale in base al risultato desiderato.

Se non si vuole usare un numero incrementale, disattivare l'uso del progressivo numerico. In questo caso sul filo verra' riportato solo l'identificatore, per esempio:

```text
L1
N
```

Nella sezione **Prefissi o Suffissi Locali**, selezionare **Abilita** se serve aggiungere un prefisso o un suffisso locale.

> Nota: prefissi e suffissi locali funzionano solo se viene utilizzato un numero incrementale. Se l'opzione **Non utilizzare numero incrementale** e' attiva, prefissi e suffissi locali non vengono applicati.

---

## Schema multifilare

Questa sezione raccoglie le procedure operative specifiche dello schema multifilare.

### Lista completa dei rimandi

Per visualizzare la lista completa dei rimandi usare il comando:

```text
Numerazione fili -> Lista numeri usati
```

Nella finestra **Lista numeri usati**:

1. Selezionare **Vedi solo i Rimandi**.
2. Selezionare i multifogli da analizzare, per esempio `SCHEMA`.
3. Premere **Scansiona i Multifogli**.

SPAC genera l'elenco dei numeri filo usati e, con il filtro sui rimandi attivo, mostra solo i numeri presenti sui simboli di rimando, cioe' quelli usati sulle frecce o sui rimandi di alimentazione.

Questa lista e' utile per verificare i rimandi presenti nello schema e individuare eventuali ripetizioni.

I numeri segnalati con asterisco sono numeri ripetuti.

### Eliminare numerazione fili

Per eliminare la numerazione dei fili usare il comando:

```text
SPAC -> Utility Fili -> Elimina numerazione
```

In alternativa, dalla riga comando si puo' usare:

```text
DEL_NUMF
```

Procedura:

1. Aprire il menu **SPAC**.
2. Selezionare **Utility Fili**.
3. Selezionare **Elimina numerazione**.
4. Selezionare la scelta.

Questa funzione elimina i numeri filo, ma non cancella i fili dallo schema.

### Inserimento e utilizzo di morsetti e morsettiere

Prima di inserire morsetti e morsettiere e' consigliato nominare tutti i fili presenti nella pagina, seguendo la procedura descritta in [Numerazione fili non di alimentazione](#numerazione-fili-non-di-alimentazione).

Per inserire i morsetti usare il comando:

```text
Inser Morsetti
```

In alternativa, dalla riga comando si puo' usare:

```text
SPINSMOR
```

> Nota: prima di usare il comando deve essere aperto un database dei materiali che contiene almeno una morsettiera. In caso contrario il comando restituisce un errore.

Gestione morsettiere:

1. Aprire **Inser Morsetti**.
2. Nel riquadro in alto a sinistra, dove compare **Elenco Quadri**, sono visibili le morsettiere gia' esistenti.
3. Per creare una nuova morsettiera, cliccare con il tasto destro su **Elenco Quadri**, sul nome del quadro oppure su una morsettiera gia' esistente.
4. Selezionare **Nuova morsettiera**.
5. Per modificare o eliminare una morsettiera esistente, selezionare la voce dedicata nel menu che si apre con il tasto destro.

Inserimento morsetto:

1. Selezionare la morsettiera da utilizzare.
2. Scegliere il tipo di morsetto.
3. Premere **Ok - Nuovo** in basso a destra.
4. Selezionare il filo che deve andare al morsetto appena creato.
5. Premere **Invio**.

Il punto in cui si clicca per selezionare il filo e' il punto in cui viene inserito il morsetto.

Per identificare un morsetto con `NumM` e il nome della morsettiera, selezionare il modello corretto nel riquadro **Anteprima** durante l'aggiunta del morsetto.

Significato delle sigle:

| Sigla | Significato |
|---|---|
| `NumI` | Numero filo di ingresso nel morsetto. |
| `NumO` | Numero filo di uscita dal morsetto. |
| `NumM` | Numero di morsetto. |

Per una lettura migliore dello schema si preferisce usare `NumM` insieme al nome della morsettiera.

### Associazione accessorio a dispositivo Madre

Questa regola vale per tutti gli accessori o elementi associati a un dispositivo principale.

Esempi:

- bobina associata a un interruttore magnetotermico;
- contatto ausiliario associato a un contattore, rele' o interruttore;
- sgancio, segnalazione, comando motorizzato o altro accessorio associato al dispositivo Madre.

Procedura generale:

1. Assicurarsi che nel progetto sia presente il componente Madre. Il componente Madre e' identificato da `PRES = M`.
2. L'accessorio deve essere Figlio della Madre, quindi deve avere `PRES = F`.
3. Inserire nel progetto entrambi i componenti.
4. Modificare gli attributi dell'accessorio con il comando:

   ```text
   EDITATT
   ```

5. Nell'attributo `PRES` dell'accessorio inserire `F`.
6. Assegnare all'accessorio lo stesso `NOME` del dispositivo Madre. Se SPAC avvisa che esiste gia' un dispositivo con lo stesso nome, confermare e proseguire.
7. Posizionare il componente Figlio vicino alla Madre, o nella posizione corretta dello schema. Non e' necessario collegare elettricamente l'accessorio alla Madre se il collegamento logico e' gia' definito tramite `PRES = F` e lo stesso `NOME`.

La bobina associata all'interruttore magnetotermico e' quindi solo un caso particolare di questa regola generale.

---

## Creazione e manutenzione simboli custom

Questa parte serve per creare, aggiornare e rendere coerenti i simboli della libreria custom.

### Creazione elemento grafico

Questa procedura serve per creare un simbolo grafico custom partendo da un DWG esterno o da un simbolo SPAC esistente.

#### Procedura

1. Aprire un foglio di lavoro di prova, non una commessa reale.
2. Selezionare ambiente **FUNZIONALE/UNIFILARE**.
3. La simbologia iniziale è indifferente perché verrà modificata durante la creazione.
4. Il cartiglio non è rilevante perché il file serve solo per creare il simbolo.
5. Il numero di fogli è ininfluente.
6. Inserire il disegno di partenza su un layer diverso da `0`.

#### Importazione da DWG esterno

1. Usare il comando:

   ```text
   _INSER
   ```

2. Nella finestra di inserimento scegliere il DWG dalla tab appropriata:
   - Disegno corrente;
   - Recenti;
   - Preferiti;
   - Librerie.

3. Usare la casella di ricerca o il pulsante di sfoglia per selezionare il file DWG.
4. Inserire il file nel disegno.
5. Se il DWG contiene attributi, SPAC/AutoCAD richiederà la compilazione tramite riga comando.

#### Importazione da simbolo SPAC esistente

1. Aprire la libreria dei simboli.
2. Inserire un simbolo esistente come base di partenza.

#### Pulizia e normalizzazione

1. Qualunque sia la sorgente, selezionare il disegno e digitare:

   ```text
   ESPLODI
   ```

2. Eliminare testo, linee o elementi non necessari.
3. Spostarsi sul layer `0`.
4. Normalizzare il disegno:
   - Colore: `DaBlocco`;
   - Tipo linea: `DaBlocco`;
   - Spessore linea: `DaBlocco`.

#### Creazione del blocco DWG

1. Selezionare il disegno.
2. Lanciare il comando:

   ```text
   MBLOCCO
   ```

3. In **Origine**, selezionare `Oggetti`.
4. Selezionare il punto base, cioè il punto di ancoraggio del simbolo.
   - Per un elemento puramente grafico, usare preferibilmente il centro grafico.
5. In **Destinazione → Nome e percorso del file**, selezionare la categoria corretta della libreria `_CUSTOM`.
6. Assegnare il nome del componente secondo la convenzione definita in questa guida.
7. In **Unità inser.**, lasciare `Senza unità`.

#### Creazione della slide SLD

1. Aprire direttamente il file DWG appena creato.
2. Centrare il disegno e regolare lo zoom.
3. Da riga comando usare:

   ```text
   _MSLIDE
   ```

4. Salvare la slide nella stessa cartella del DWG.
5. Il file `.sld` deve avere necessariamente lo stesso nome base del file `.dwg`.
6. Chiudere il DWG del simbolo.
7. Verificare nella libreria BLK che il simbolo e la relativa slide siano visibili.

Regola obbligatoria:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

### Differenza tra Simbolo Madre e Simbolo Figlio in SPAC

#### Sintesi rapida

| Aspetto | Simbolo Madre | Simbolo Figlio |
|---|---|---|
| Significato | È il componente principale. | È una parte/riferimento collegato alla Madre. |
| Ruolo | Identifica il dispositivo nello schema. | Rappresenta un contatto, ausiliario o elemento associato. |
| Attributo chiave | `PRES = M` | `PRES = F...` |
| Sigla `NOME` | È la sigla principale del componente. | Deve richiamare la sigla della Madre. |
| Materiale | Normalmente può avere materiale associato. | Di solito eredita o si collega alla Madre. |
| Distinta materiali | È il riferimento principale per la distinta. | Normalmente non genera un componente autonomo. |
| Cross reference | Può avere riferimenti ai Figli. | Viene registrato come elemento collegato alla Madre. |
| Esempi | `KM1`, `QF1`, `SA1`, `KA1`. | Contatto ausiliario di `KM1`, contatto NC di `KA1`, contatto di potenza di `KM1`. |

#### Simbolo Madre

Un **Simbolo Madre** è il simbolo principale di un componente.

Identifica il dispositivo vero e proprio nello schema elettrico.

Esempi:

- contattore;
- relè;
- interruttore;
- sezionatore;
- selettore;
- pulsante;
- termico;
- attuatore;
- dispositivo principale.

In SPAC un simbolo Madre viene riconosciuto tramite:

```text
PRES = M
```

#### Simbolo Figlio

Un **Simbolo Figlio** è un simbolo collegato alla Madre.

Non rappresenta un nuovo componente autonomo, ma una parte del componente associato alla Madre.

Esempi:

- contatto ausiliario aperto di un contattore;
- contatto ausiliario chiuso di un relè;
- contatto di potenza di un contattore;
- contatto temporizzato;
- riferimento associato a una Madre.

### Creazione elemento intelligente

Questa procedura serve per creare un simbolo SPAC intelligente con attributi.

#### Preparazione

1. Inserire un simbolo o un disegno di partenza.
2. Pulirlo da ciò che è superfluo.
3. Normalizzare il disegno:
   - layer `0`;
   - colore `DaBlocco`;
   - tipo linea `DaBlocco`;
   - spessore linea `DaBlocco`.

#### Attributo `NOME`

Usare il comando:

```text
ATTDEF
```

Configurazione consigliata:

| Campo | Valore |
|---|---|
| Etichetta | `NOME` |
| Messaggio | `Sigla componente` |
| Default | vuoto |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

L'attributo `NOME` deve essere posizionato dove si vuole visualizzare la sigla componente.

#### Attributo `PRES`

Configurazione consigliata:

| Campo | Valore |
|---|---|
| Etichetta | `PRES` |
| Default | `M` |
| Invisibile | Sì |
| Costante | Sì |
| Blocca posizione | Sì |

Il valore `M` indica che il simbolo è una Madre.

#### Attributi `PINA1` e `PINB1`

Configurazione consigliata per `PINA1`:

| Campo | Valore |
|---|---|
| Etichetta | `PINA1` |
| Default | `1` |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

Configurazione consigliata per `PINB1`:

| Campo | Valore |
|---|---|
| Etichetta | `PINB1` |
| Default | `2` |
| Invisibile | No |
| Costante | No |
| Blocca posizione | Sì |

Nota operativa:

- usare `PINA1` e `PINB1` quando il simbolo deve avere punti di connessione;
- nei DWG dei BLK custom, la grandezza testo standard dei pin e' `1.5`;
- per simboli puramente grafici senza collegamenti, i pin possono non essere necessari;
- se il simbolo rappresenta più contatti o più poli, usare progressivi coerenti: `PINA2`, `PINB2`, `PINA3`, `PINB3`, ecc.

#### Modifica stile attributi

Per modificare lo stile di un attributo:

1. Selezionare l'attributo.
2. Lanciare:

   ```text
   PROPRIETA
   ```

   oppure usare `CTRL+1`.

3. Modificare le proprietà dalla palette.

Per copiare lo stile da un attributo esistente:

1. Usare il comando:

   ```text
   CORRISPROP
   ```

2. Selezionare l'attributo sorgente.
3. Selezionare l'attributo destinazione.
4. Premere Invio.

#### Salvataggio simbolo intelligente

1. Verificare che siano presenti tutti gli attributi necessari.
2. Selezionare tutti gli oggetti.
3. Lanciare:

   ```text
   MBLOCCO
   ```

4. In **Origine**, selezionare `Oggetti`.
5. Selezionare il punto base.
6. Salvare il simbolo nella categoria corretta della libreria `_CUSTOM`.
7. Generare la slide `.sld` con `_MSLIDE`, usando lo stesso nome base del DWG.

### Associazione materiale al simbolo intelligente

1. Fare doppio click sul simbolo.
2. Nel riquadro **Materiali**, fare tasto destro.
3. Selezionare **Avvio Archivio Materiali (DbCenter)**.
4. Selezionare il materiale adatto.
5. Confermare l'associazione.

Nota operativa:

- un simbolo può rappresentare anche più materiali fisici;
- associare materiali solo quando il simbolo deve contribuire alla distinta;
- evitare di associare materiali a elementi puramente grafici se non devono comparire in distinta.

---

## Convenzioni e catalogo libreria

Questa parte raccoglie le regole di nomenclatura e i riferimenti usati per mantenere ordinata la libreria.

### Convenzione di nomenclatura simboli

#### Obiettivo

I nomi dei simboli devono essere:

- sintetici;
- leggibili;
- coerenti;
- compatibili con il limite massimo di **32 caratteri**;
- facilmente ricercabili nella libreria.

Il limite si applica al nome base del file, esclusa l'estensione.

Esempio:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

Il nome base è:

```text
NOME_SIMBOLO
```

#### Formato standard

Formato consigliato:

```text
<FAMIGLIA>_<TIPO>_<POLI>_<ESECUZIONE>_<AZIONAMENTO>_<ACCESSORI>
```

Non tutti i campi sono obbligatori.

La regola è: inserire solo i campi necessari a distinguere correttamente il simbolo.

#### Significato dei campi

| Campo | Significato | Esempi |
|---|---|---|
| `<FAMIGLIA>` | Classe principale del simbolo. | `INT`, `TOR`, `MULT`, `ATT`, `SPIA` |
| `<TIPO>` | Tipo funzionale principale. | `MT`, `MTD`, `SEZ`, `MAN`, `RELE`, `FUS` |
| `<POLI>` | Numero poli, solo se utile. | `1P`, `3P`, `4P` |
| `<ESECUZIONE>` | Caratteristica costruttiva/meccanica. | `ESTR`, `FUS` |
| `<AZIONAMENTO>` | Modalità di comando/azionamento. | `MOT`, `MAN` |
| `<ACCESSORI>` | Accessori o funzioni aggiuntive. | `SGL`, `AUS`, `SCB` |

#### Regole formali

- usare solo lettere maiuscole;
- non usare spazi;
- non usare accenti;
- non usare caratteri speciali;
- usare `_` come separatore;
- non superare 32 caratteri;
- evitare parole complete quando esiste un'abbreviazione standard;
- demandare la descrizione estesa alla tabella, non al nome file.

#### Regola di priorità

Il nome deve seguire questa priorità:

```text
FAMIGLIA → TIPO → POLI → ESECUZIONE → AZIONAMENTO → ACCESSORI
```

Esempi:

| Caso | Nome corretto |
|---|---|
| Interruttore magnetotermico estraibile con ausiliari | `INT_MT_ESTR_AUS` |
| Interruttore magnetotermico estraibile motorizzato con ausiliari | `INT_MT_ESTR_MOT_AUS` |
| Interruttore magnetotermico estraibile motorizzato con sgancio e ausiliari | `INT_MT_ESTR_MOT_SGL_AUS` |
| Interruttore magnetotermico differenziale con ausiliari | `INT_MTD_AUS` |
| Interruttore magnetotermico differenziale estraibile con ausiliari | `INT_MTD_ESTR_AUS` |
| Interruttore sezionatore manuale unipolare fusibilato | `INT_SEZ_MAN_1P_FUS` |
| Interruttore sezionatore manuale unipolare con contatto di scambio | `INT_SEZ_MAN_1P_SCB` |
| Interruttore manuale con contatto di scambio | `INT_MAN_SCB` |

### Dizionario abbreviazioni

| Abbreviazione | Significato |
|---|---|
| `ALIM` | Alimentatore / alimentazione |
| `ATT` | Attuatore |
| `AUS` | Contatti/accessori ausiliari generici |
| `CHIAVE` | Comando/selettore a chiave |
| `CONN` | Connettore |
| `DIFF` | Differenziale |
| `ESTR` | Estraibile |
| `EV` | Elettrovalvola |
| `FC` | Finecorsa |
| `FUS` | Fusibile / fusibilato |
| `GW` | Gateway |
| `INT` | Interruttore |
| `IO` | Ingressi/uscite |
| `INV` | Inverter |
| `LUM` | Luminosa |
| `MAGN` | Magnetico |
| `MAN` | Manuale / manovra manuale |
| `MOD` | Modulo |
| `MOR` | Morsetto |
| `MOT` | Motorizzato |
| `MT` | Magnetotermico |
| `MTD` | Magnetotermico differenziale |
| `MULT` | Multimetro |
| `PLC` | PLC / controllore logico programmabile |
| `RELE` | Relè |
| `SCB` | Contatto di scambio |
| `SENS` | Sensore |
| `SEZ` | Sezionatore |
| `SGL` | Sgancio a lancio di corrente |
| `SPIA` | Spia / lampada di segnalazione |
| `SPD` | Scaricatore di sovratensione |
| `SW` | Switch |
| `TERM` | Termico |
| `TOR` | Toroide |
| `TRF` | Trasformatore |
| `UPS` | Gruppo di continuità |

#### Note sulle abbreviazioni

- `MT` indica la funzione combinata magnetotermica.
- `MAGN` si usa solo quando il dispositivo ha funzione magnetica senza funzione termica.
- `TERM` si usa solo quando il dispositivo ha funzione termica senza funzione magnetica.
- `MTD` indica magnetotermico differenziale e sostituisce la forma estesa `MT_DIFF`.
- `SCB` è lo standard adottato per accorciare `SCAMBIO`.
- `AUS` resta valido solo quando l'accessorio è generico o non si vuole specificare il tipo di contatto.
- `FC` significa finecorsa: usarlo con attenzione perché può essere ambiguo in contesti PLC/software.

### Simboli realizzati

Come riferimento operativo è stato utilizzato il PDF:

```text
NHGG.ES.6104.CF00.IE.SH.XX.N.REV02-Schemi unifilari generali e tecnologici.pdf
```

A partire dagli schemi unifilari presenti nel documento sono stati realizzati simboli **grafici** e simboli **intelligenti SPAC**.

Per ogni simbolo sono riportati:

- categoria;
- nome del simbolo;
- file generati;
- lunghezza del nome simbolo;
- prima pagina del PDF in cui il simbolo compare;
- tipologia;
- descrizione funzionale.

> Nota: salvo diversa indicazione, il file `.dwg` e il relativo file `.sld` devono utilizzare lo stesso nome base.
