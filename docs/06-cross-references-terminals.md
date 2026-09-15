# Rimandi, cross-reference e morsetti

Questa pagina raccoglie le procedure operative per rimandi, cross-reference, morsetti e morsettiere in SPAC Start 26. I nomi esatti vengono riportati quando già verificati; ciò che non è ancora consolidato resta marcato `Da verificare`.

## Prima distinzione: CAD o oggetto SPAC

Prima di correggere un rimando o un morsetto verifica sempre se stai lavorando su:

- semplice linea CAD;
- collegamento/alimentazione SPAC;
- simbolo intelligente;
- rimando;
- morsetto;
- testo generato da una rappresentazione.

Non correggere manualmente il testo se il dato sorgente è sbagliato.

## Lista numeri/rimandi usati

Percorso verificato:

```text
Numerazione fili → Lista numeri usati
```

Usa questa lista per:

- individuare numeri ripetuti;
- verificare rimandi duplicati;
- controllare numerazioni/riferimenti ancora presenti.

I numeri segnalati con **asterisco** sono ripetuti.

## Eliminare numerazione fili

Percorso:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente:

```text
DEL_NUMF
```

Questa funzione elimina la numerazione, non i fili.

## Inserire morsetti

Prima di inserire morsetti è consigliato numerare/nominare i fili interessati.

Nome funzione:

```text
Inser Morsetti
```

Comando equivalente da riga comando:

```text
SPINSMOR
```

!!! warning "Prerequisito"

    Deve essere aperto un database materiali contenente almeno una morsettiera. In caso contrario `SPINSMOR` può restituire errore.

## Creare una nuova morsettiera

Nella finestra **Inser Morsetti**:

1. individua il riquadro in alto a sinistra **Elenco Quadri**;
2. fai **tasto destro** su:
   - **Elenco Quadri**;
   - il nome del quadro;
   - oppure una morsettiera già esistente;
3. clicca **Nuova morsettiera**;
4. completa i dati richiesti;
5. verifica che la morsettiera sia sotto il quadro corretto.

## Inserire un morsetto sul filo

Dopo aver aperto **Inser Morsetti**:

1. seleziona la morsettiera corretta;
2. scegli il tipo di morsetto previsto;
3. crea/seleziona il nuovo morsetto;
4. seleziona il filo interessato nel disegno;
5. verifica il punto di inserimento;
6. controlla i dati del morsetto e la rappresentazione grafica.

Il punto in cui viene selezionato il filo determina il punto di inserimento del morsetto.

!!! warning "Pulsante di creazione morsetto"

    Il nome esatto di ogni pulsante interno usato per creare/selezionare il singolo morsetto non è ancora consolidato nella knowledge base. Non va inventato: verificare nell'installazione SPAC Start 26 e poi aggiornare questa pagina.

## Numero filo vs numero morsetto

Sigle operative documentate:

| Sigla | Significato |
|---|---|
| `NumI` | numero filo in ingresso al morsetto |
| `NumO` | numero filo in uscita dal morsetto |
| `NumM` | numero morsetto |

Se compare il numero filo invece del numero morsetto:

1. verifica quale campo sta mostrando la rappresentazione;
2. controlla se è `NumI`/`NumO` invece di `NumM`;
3. non correggere il testo a mano;
4. verifica i dati sorgente del morsetto;
5. prova la rappresentazione corretta su un morsetto nuovo.

## Rimandi: regole logiche

- rimando di **partenza** ↔ rimando di **arrivo** o arrivo/partenza;
- rimando di **arrivo** ↔ rimando di **partenza** o arrivo/partenza;
- i due punti che devono riferirsi allo stesso collegamento devono usare un nome coerente.

## Cross-reference: aggiornamento

Sequenza consolidata a livello logico:

1. verifica che i collegamenti siano oggetti SPAC riconosciuti;
2. verifica nome e direzione dei rimandi;
3. apri la funzione di cross-reference;
4. seleziona l'elaborazione dedicata ai rimandi;
5. avvia l'aggiornamento;
6. verifica i riferimenti generati sul foglio;
7. controlla **Numerazione fili → Lista numeri usati** per eventuali duplicati/residui.

!!! warning "Comando cross-reference da verificare"

    Il nome esatto del comando/percorso menu che avvia l'elaborazione cross-reference non è ancora consolidato per l'installazione SPAC Start 26 documentata. Finché non viene verificato direttamente, la guida non deve assegnargli un nome ipotetico.

## Quando un rimando dice selezione non valida

Controlla nell'ordine:

1. la linea è semplice geometria CAD o un collegamento SPAC?
2. l'oggetto intelligente è stato esploso/alterato?
3. esistono linee od oggetti sovrapposti?
4. stai selezionando il collegamento reale o solo una geometria vicina?
5. il comportamento si ripete su un foglio pulito?

Non disegnare una nuova linea CAD sopra quella esistente per “far funzionare” il rimando.

## Cross-reference che punta a una vecchia posizione

Verifica:

- oggetti intelligenti residui;
- rimandi non più usati;
- riferimenti non rigenerati;
- alimentazioni duplicate;
- oggetti cancellati graficamente ma ancora presenti logicamente.

Poi rigenera i riferimenti con la funzione cross-reference verificata nell'ambiente.

## Diagnostica rapida

| Sintomo | Azione concreta |
|---|---|
| Numero/rimando duplicato | **Numerazione fili → Lista numeri usati**; controlla asterischi |
| Devo rimuovere numeri filo | **SPAC → Utility Fili → Elimina numerazione** / `DEL_NUMF` |
| Devo aprire gestione morsetti | **Inser Morsetti** / `SPINSMOR` |
| Devo creare una morsettiera | **Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera** |
| Morsetto mostra numero filo | verifica `NumI`/`NumO` vs `NumM` |
| Rimando non accetta linea | verifica oggetto SPAC vs geometria CAD |
| Cross-reference vecchio | cerca residui e rigenera con funzione cross-reference; nome comando `Da verificare` |

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Schema multifilare](09-multifilare.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Verificare rappresentazione morsetti](playbooks/terminal-representation.md)
- [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md)
- [Cross-reference obsoleto](known-issues/obsolete-cross-reference.md)
