# Decision log

Questo file raccoglie le decisioni operative consolidate nella knowledge base.

Lo scopo è evitare che le stesse scelte vengano ridiscusse o applicate in modo incoerente.

## Formato decisione

Ogni decisione dovrebbe indicare:

- contesto;
- decisione;
- motivazione;
- stato;
- eventuali note.

## Decisioni attive

### D001 — Entità CAD su Layer 0

**Contesto**  
File CAD, DXF o DWG destinati a SPAC devono essere semplici da importare e gestire.

**Decisione**  
Creare le entità CAD sul Layer 0.

**Motivazione**  
Riduce problemi di visibilità, importazione e gestione grafica.

**Stato**  
Attiva.

---

### D002 — Inventario simboli separato dal README

**Contesto**  
Il README deve restare leggibile e non diventare un archivio operativo troppo lungo.

**Decisione**  
L'inventario completo dei simboli custom deve stare in un file separato.

**Motivazione**  
Migliora manutenzione, filtro, ordinamento e consultazione.

**Stato**  
Attiva.

---

### D003 — Pinatura custom con PINA e PINB

**Contesto**  
I simboli custom cablati devono avere una pinatura coerente e riutilizzabile.

**Decisione**  
Usare PINA seguito da numero progressivo. Usare PINB con lo stesso numero solo quando il segnale deve essere riportato in uscita.

**Motivazione**  
Rende chiara la relazione ingresso/uscita e limita attributi inutili.

**Stato**  
Attiva.

---

### D004 — Usare SCAMBIO, non abbreviazioni non documentate

**Contesto**  
Le abbreviazioni possono generare ambiguità nei nomi dei simboli o nelle descrizioni.

**Decisione**  
Per contatti di scambio usare la parola SCAMBIO.

**Motivazione**  
Maggiore chiarezza e minore ambiguità.

**Stato**  
Attiva.

---

### D005 — Preferire approccio raster controllato per loghi ricorrenti

**Contesto**  
I loghi nei cartigli possono essere gestiti come immagini collegate o come geometria vettoriale.

**Decisione**  
Usare preferibilmente immagini raster con riferimenti controllati quando il workflow deve restare semplice.

**Motivazione**  
È più pratico e più rapido, purché i riferimenti siano mantenuti in modo stabile.

**Stato**  
Attiva.

---

### D006 — Import materiali sempre tramite staging

**Contesto**  
Gli archivi materiali possono impattare distinta, report e associazioni ai simboli.

**Decisione**  
Ogni archivio materiali custom deve passare da backup, staging, controllo duplicati e validazione su progetto non critico prima di diventare standard.

**Motivazione**  
Riduce il rischio di duplicazioni, dati incoerenti e import non reversibili.

**Stato**  
Attiva.

---

### D007 — Ogni materiale deve avere uno stato

**Contesto**  
Un archivio materiali può contenere record in fasi diverse di maturità.

**Decisione**  
Ogni record materiale deve avere uno stato tra Bozza, Da verificare, Validato e Deprecato.

**Motivazione**  
Permette di distinguere materiali pronti all'uso da materiali ancora da validare.

**Stato**  
Attiva.
