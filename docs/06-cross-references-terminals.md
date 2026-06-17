# Rimandi, cross-reference e morsetti

Questa sezione raccoglie note operative su rimandi, alimentazioni, cross-reference e rappresentazione dei morsetti in SPAC Start.

## Cross-reference

Il cross-reference dei rimandi è una procedura comune sia allo schema unifilare sia allo schema multifilare.

Principio operativo:

- i collegamenti da mettere in relazione devono usare lo stesso nome;
- un rimando di partenza deve essere coerente con un rimando di arrivo;
- dopo la creazione dei rimandi è necessario aggiornare il cross-reference.

## Linea, alimentazione, oggetto e rimando

Prima di diagnosticare un rimando distinguere questi livelli.

| Livello | Significato operativo | Rischio tipico |
|---|---|---|
| Linea grafica | Entità CAD visibile nel foglio | La selezione non viene accettata come collegamento |
| Alimentazione SPAC | Collegamento creato e riconosciuto dalla logica SPAC | Rimando non applicabile se la linea è solo grafica |
| Oggetto intelligente | Elemento con dati, attributi o relazione interna | Cross-reference collegato a dati non più coerenti |
| Rimando | Simbolo o riferimento che collega logicamente punti dello schema | Riferimento duplicato, non aggiornato o diretto a posizione vecchia |

Regola: il rimando deve appoggiarsi a un collegamento o oggetto riconosciuto,
non alla sola geometria visibile.

## Direzione dei rimandi

Regole:

- se il primo rimando è di partenza, il secondo deve essere di arrivo oppure arrivo/partenza;
- se il primo rimando è di arrivo, il secondo deve essere di partenza oppure arrivo/partenza;
- la direzione deve essere coerente con il flusso logico dello schema.

## Aggiornamento cross-reference

Dopo aver creato o modificato rimandi:

1. aprire la funzione cross-reference;
2. selezionare l'elaborazione dedicata ai rimandi;
3. avviare l'aggiornamento;
4. verificare eventuale output generato;
5. controllare che i riferimenti puntino alle posizioni corrette.

## Rimandi per alimentazioni

I rimandi permettono di collegare graficamente e logicamente alimentazioni o segnali tra fogli diversi.

Prima di inserire un rimando:

- verificare che la linea sia riconosciuta come alimentazione o collegamento corretto;
- selezionare l'oggetto intelligente, non una semplice linea CAD;
- evitare entità grafiche duplicate o residue;
- rigenerare/verificare i riferimenti dopo modifiche importanti.

Se non è chiaro se la linea sia una alimentazione SPAC o solo grafica CAD,
marcare il caso come `Da verificare` e testare su un foglio pulito.

## Lista rimandi usati

Per controllare i rimandi presenti nello schema, usare la funzione che mostra la lista dei numeri usati e filtrare i soli rimandi.

Questa lista è utile per:

- individuare rimandi duplicati;
- verificare nomi usati;
- trovare ripetizioni;
- controllare riferimenti non più coerenti.

Nota: i numeri segnalati come ripetuti devono essere verificati prima di procedere con ulteriori modifiche.

## Quando la selezione risulta non valida

Se selezionando una linea il comando segnala selezione non valida, possibili cause:

- la linea è solo geometria CAD;
- l'alimentazione non è stata creata con il comando SPAC corretto;
- l'oggetto intelligente è stato esploso o alterato;
- esistono vecchi oggetti sovrapposti;
- la selezione avviene su un elemento grafico e non sul collegamento riconosciuto.

Diagnosi consigliata:

1. verificare se la linea è stata creata come collegamento o alimentazione SPAC;
2. controllare se esistono geometrie CAD sovrapposte;
3. selezionare il tratto o l'oggetto intelligente più vicino al punto logico;
4. riprodurre il caso su foglio pulito;
5. documentare come `Da verificare` se il comportamento non è ripetibile.

## Cross-reference non aggiornati

Se un cross-reference punta a una posizione dove prima esisteva un collegamento ma ora non più, controllare:

- vecchi oggetti intelligenti rimasti nel foglio;
- rimandi non più utilizzati;
- riferimenti non rigenerati;
- alimentazioni duplicate;
- oggetti cancellati graficamente ma non rimossi logicamente.

In questi casi il problema non va corretto spostando manualmente il testo del
riferimento. Prima verificare se il riferimento è ancora collegato a vecchie
celle, oggetti residui o rimandi non più utilizzati.

## Checklist rigenerazione rimandi

Prima di aggiornare o rigenerare i rimandi:

- salvare o lavorare su copia se il progetto contiene modifiche estese;
- verificare che le linee interessate siano oggetti SPAC riconosciuti;
- controllare nomi e direzione dei rimandi;
- cercare rimandi duplicati o non utilizzati;
- verificare oggetti residui nella zona interessata;
- annotare eventuali comportamenti `Da verificare`.

Dopo aggiornamento o rigenerazione:

- controllare che ogni rimando punti alla posizione attesa;
- verificare che non compaiano riferimenti a celle o posizioni vecchie;
- controllare la lista dei rimandi usati;
- testare almeno un caso su foglio pulito se il problema era ricorrente;
- aprire una known issue se il comportamento si ripete.

## Eliminare numerazione fili

La funzione di eliminazione numerazione fili rimuove i numeri filo, ma non cancella i fili dallo schema.

Usarla quando è necessario pulire una numerazione errata prima di rigenerarla.

## Morsetti

Per i morsetti, distinguere sempre tra:

- nome morsettiera;
- numero morsetto;
- numero filo;
- riferimento funzionale;
- rappresentazione grafica selezionata.

Prima di inserire morsetti è consigliato nominare i fili presenti nella pagina.

## Oggetto, dati e rappresentazione

Un morsetto deve essere verificato su tre livelli distinti.

| Livello | Cosa controllare | Errore tipico |
|---|---|---|
| Oggetto intelligente | Il morsetto esiste come oggetto SPAC collegato al filo corretto | Testo corretto ma oggetto non coerente |
| Dati morsetto | Morsettiera, numero morsetto, numero filo e riferimento funzionale | Numero morsetto e numero filo confusi |
| Rappresentazione grafica | Campo mostrato dal simbolo o dalla grafica selezionata | La grafica mostra `NumI` o `NumO` invece di `NumM` |

Il testo visibile è un risultato della rappresentazione. Non deve essere usato
come unica fonte di verità.

## Morsettiere

Durante la gestione morsettiere, verificare:

- quadro di appartenenza;
- morsettiera selezionata;
- tipo morsetto;
- progressione dei morsetti;
- rappresentazione scelta.

Per creare una nuova morsettiera, usare il menu contestuale della gestione morsettiere e assegnare un nome coerente.

## Inserimento morsetto

Workflow generale:

1. selezionare la morsettiera;
2. scegliere il tipo morsetto;
3. creare un nuovo morsetto;
4. selezionare il filo interessato;
5. verificare il punto di inserimento;
6. controllare rappresentazione e dati.

Il punto in cui viene selezionato il filo determina il punto di inserimento del morsetto.

## Rappresentazione morsetti

Sigle operative:

| Sigla | Significato |
|---|---|
| `NumI` | Numero filo di ingresso nel morsetto |
| `NumO` | Numero filo di uscita dal morsetto |
| `NumM` | Numero di morsetto |

Per una lettura più chiara dello schema, preferire rappresentazioni che mostrino `NumM` insieme al nome della morsettiera.

Se sul morsetto compare il numero filo invece del numero morsetto, il problema è probabilmente nella configurazione della rappresentazione grafica o nei dati visualizzati dal simbolo morsetto.

## Diagnostica visualizzazione morsetti

| Sintomo | Verifiche minime | Azione documentale |
|---|---|---|
| Compare il numero filo invece del numero morsetto | Controllare se la rappresentazione mostra `NumI` o `NumO` invece di `NumM` | Annotare la rappresentazione usata |
| Compare una morsettiera inattesa | Controllare dati morsettiera e appartenenza del morsetto | Verificare su morsetto nuovo |
| Il numero morsetto è corretto ma la grafica non lo mostra | Controllare campi visualizzati dal simbolo morsetto | Non correggere solo il testo |
| Il morsetto non mantiene il comportamento dopo aggiornamenti | Controllare oggetto intelligente, dati sorgente e riferimenti | Aprire caso pratico o known issue se ricorrente |
| Il riferimento punta a una posizione non più valida | Controllare oggetti residui e cross-reference non aggiornati | Usare [Known Issue - Cross-reference obsoleto](known-issues/obsolete-cross-reference.md) |

## Checklist morsetti

Quando la rappresentazione del morsetto non è corretta:

1. distinguere oggetto morsetto, dati sorgente e testo visibile;
2. verificare proprietà del morsetto;
3. controllare dati morsettiera;
4. verificare numero morsetto, numero filo e riferimento funzionale;
5. verificare campi visualizzati dal simbolo;
6. controllare impostazioni grafiche della rappresentazione;
7. aggiornare o rigenerare i riferimenti quando necessario;
8. testare su un morsetto nuovo in progetto prova.

## Checklist diagnostica rapida

- `NumM` atteso ma non visibile: controllare rappresentazione grafica.
- `NumI` o `NumO` visibile al posto di `NumM`: controllare campo mostrato.
- Morsettiera errata: controllare appartenenza e dati del morsetto.
- Numero filo errato: controllare numerazione fili prima del morsetto.
- Comportamento non ripetibile: testare su morsetto nuovo e documentare esito.

## Regola pratica

Non correggere solo il testo visibile se l'oggetto è intelligente. Verificare sempre il dato sorgente e la configurazione grafica che lo mostra.

## Collegamenti

- [Multifilare](09-multifilare.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Verificare rappresentazione morsetti](playbooks/terminal-representation.md)
- [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md)
- [Known Issue - Cross-reference obsoleto](known-issues/obsolete-cross-reference.md)
- [Known Issues](known-issues/index.md)

## Baseline sezione

La sezione rimandi e morsetti è completa come riferimento operativo quando copre:

- principio del cross-reference tra rimandi;
- direzione coerente arrivo/partenza;
- aggiornamento dei riferimenti;
- controllo lista rimandi usati;
- diagnosi di selezioni non valide;
- distinzione tra linea grafica, alimentazione SPAC, oggetto intelligente e rimando;
- checklist prima/dopo rigenerazione rimandi;
- pulizia numerazione fili;
- gestione morsettiere e inserimento morsetti;
- distinzione tra oggetto morsetto, dati sorgente e rappresentazione grafica;
- differenza tra `NumI`, `NumO` e `NumM`;
- diagnostica della visualizzazione morsetti;
- verifica finale della rappresentazione morsetti.

Nuove anomalie ricorrenti vanno documentate come known issue o playbook dedicato.
