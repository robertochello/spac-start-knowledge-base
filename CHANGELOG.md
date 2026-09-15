# Changelog

Tutte le modifiche rilevanti alla knowledge base saranno documentate in questo file.

## 0.7.0 - 2026-09-15 - Procedure fidelity pass

### Fixed

- Ripristinato il percorso cross-reference già verificato: **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna**; rimosso il falso `Da verificare` dalle pagine operative.
- Ripristinata la creazione rimandi tramite **Dynamic Coll / Dynamic Alim** con tipi arrivo/partenza e regole di direzione.
- Completata la scansione rimandi: **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli**.
- Completato l'inserimento morsetto: morsettiera → tipo → **Anteprima → Ok - Nuovo → clic filo → Invio**.
- Documentata la scelta `NumM`/`NumI`/`NumO` direttamente nel riquadro **Anteprima**.
- Completato il salvataggio simboli `MBLOCCO` con **Destinazione → Nome e percorso del file** e **Unità inser. → Senza unità**.
- Completati i campi `ATTDEF` di `NOME`, `PRES`, `PINA1`, `PINB1` inclusi Invisibile, Costante e Blocca posizione.

### Added

- Apertura ambiente unifilare: **UNIFILARE → Disegno Unifilare**.
- Associazione materiale nei livelli unifilari tramite tasto destro tabella → **Avvio DbCenter**.
- Conferme esplicite **OK → OK** nella configurazione di numerazione conduttori.
- Regola **Prefissi o Suffissi Locali → Abilita** e dipendenza dal numero incrementale.
- Dettagli `_INSER` sulle aree **Disegno corrente**, **Recenti**, **Preferiti**, **Librerie**.
- Home trasformata in cheat sheet operativo con i percorsi più usati direttamente visibili.

### Quality rule

- Ogni procedura operativa deve preferire la struttura: **Dove cliccare → Cosa impostare → Esito atteso → Diagnosi se KO**.
- Una voce già verificata nel manuale completo non deve essere degradata a descrizione generica o `Da verificare` nelle pagine operative.

## 0.6.0 - 2026-09-15 - Exact commands and click paths

### Changed

- `command-reference.md` trasformata in riferimento centrale per **comandi, menu, finestre, pulsanti e valori esatti** già verificati in SPAC Start 26.
- Home e guida pratica aggiornate con accesso diretto a **Comandi e click esatti**.
- Navigazione MkDocs aggiornata per mostrare **Comandi e click esatti** nella sezione Guida pratica.
- `AGENTS.md` aggiornato: una procedura non è completa se usa descrizioni generiche al posto di comandi/percorsi già noti.
- Pagine operative aggiornate con i comandi reali per libreria, interfaccia, CAD, simboli, attributi, immagini, unifilare, multifilare, fili, morsetti e materiali.
- Playbook aggiornati con passaggi esatti per creazione/validazione simboli, pinatura, Madre/Figlio, materiali, morsetti, immagini e diagnostica rimandi.
- Workflow layer/oggetti residui documentato con `PURGE`, **Trova elementi non eliminabili**, `QSELECT` e `BEDIT`.

### Added

- Percorsi verificati come **SPAC → Numera Fili**, **SPAC → Utility Fili → Elimina numerazione**, **Numerazione fili → Lista numeri usati**, **Modifica/Inserisci → Gestioni immagini**, **Inser Morsetti → Elenco Quadri → Nuova morsettiera**.
- Nomi esatti delle finestre **Configurazione Numerazione Conduttori**, **Numerazione Fili Unifilare**, **Personalizza interfaccia utente**, **Inser Morsetti**.
- Associazione materiali documentata come **doppio click simbolo → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)**.
- Comandi consolidati: `SP_XML_MENU`, `CUI`, `_CUI`, `_DSETTINGS`, `IMMAGINI`, `IMAGEFRAME`, `_INSER`, `ESPLODI`, `MBLOCCO`, `_MSLIDE`, `ATTDEF`, `PROPRIETA`, `CORRISPROP`, `EDITATT`, `DEL_NUMF`, `SPINSMOR`, `PURGE`, `QSELECT`, `BEDIT`.

### Explicitly unsupported / not to document as SPAC commands

- `LAYISO` e `LAYWALK` risultano non disponibili in SPAC Start 26 e non devono essere proposti nella procedura di pulizia layer.

### Rule

- Dove il nome esatto di un comando/percorso non è ancora verificato, la documentazione deve indicare **Da verificare** nel punto preciso invece di inventare un nome plausibile.

## 0.5.0 - 2026-09-15 - Navigation and onboarding refresh

### Changed

- Home del sito riscritta come selettore per attività reali: setup, schemi, simboli, archivi e diagnosi.
- Pagina `00-how-to-use.md` trasformata in guida pratica con percorsi diretti per obiettivo e sintomo.
- Navigazione MkDocs semplificata e rinominata in aree più immediate: Home, Guida pratica, Lavoro in SPAC, Procedure, Problemi e diagnosi, Riferimenti.
- Guida operativa completa marcata in navigazione come documento di riferimento, non come punto di ingresso principale.
- README orientato al sito pubblico e ai collegamenti principali.
- CSS delle card e delle tabelle migliorato per rendere più leggibile la Home anche su mobile.
- Aggiunti breadcrumb e tab sticky tramite funzionalità native di MkDocs Material.

### Goal

- Ridurre il tempo necessario per capire dove cercare una procedura.
- Rendere la documentazione utilizzabile partendo dall'attività o dal problema concreto.
- Evitare che il manuale monolitico nasconda i playbook e le pagine operative più mirate.

## 0.4.0 - Site coherence pass

### Added

- Pagina `26-back-check-controls.md` per back-check e controlli incrociati.
- Pagina `downloads.md` e cartelle pubbliche per archivi materiali e archivi cavi.
- Link download per gli archivi materiali `ABB_Materials.db` e `archivio-materiali-custom-r01.db`.
- CSS minimale per migliorare leggibilità del sito MkDocs su GitHub Pages.
- Collegamento alla guida operativa completa in navigazione e Home.

### Changed

- README principale reso più sintetico e orientato al sito documentale.
- Navigazione MkDocs completata con pagine non ancora esposte.
- Navigazione MkDocs riorganizzata per percorsi operativi e sottogruppi.
- Navigazione pubblica semplificata in cinque aree principali: Start, Operativo, Playbook, Diagnosi e Governance.
- Home resa più leggibile con percorsi principali e dettagli secondari richiudibili.
- Stato Home aggiornato: le aree principali sono dichiarate come baseline completata o verificata.
- Standard nomenclatura allineato alla convenzione adottata nella knowledge base.
- Stato multifilare aggiornato da placeholder a base operativa presente.
- Command Reference estesa con i comandi citati nella guida operativa.

### Fixed

- Link rotti verso la pagina di back-check.
- Riga isolata non documentale nella guida operativa completa.

## 0.3.0 - Documentation site foundation

### Added

- Configurazione MkDocs Material.
- Dipendenze MkDocs in `requirements.txt`.
- Homepage documentale in `docs/index.md`.
- Workflow GitHub Actions per build e deploy documentazione.
- Playbook operativi:
  - creazione simbolo custom;
  - validazione simbolo custom;
  - diagnosi pin non agganciato;
  - gestione cartiglio e logo.
- Glossario operativo.
- Sezione Known Issues.
- Quality gates documentali.
- Changelog interno per sito documentale.

### Changed

- README aggiornato per riflettere il nuovo sito documentale.
- Navigazione documentale organizzata per aree operative.

## 0.2.0 - Knowledge base consolidation

### Added

- Checklist validazione simbolo custom.
- Decision log per tracciare scelte operative.
- Sezione casi pratici.
- Linee guida di manutenzione della knowledge base.
- Roadmap aggiornata con fasi di consolidamento.

### Changed

- README riorganizzato con stato progetto, mappa rapida, workflow consigliato e principi editoriali.

## 0.1.0 - Initial structure

### Added

- README principale.
- Struttura `docs/`.
- Overview della knowledge base.
- Guida interfaccia e menu.
- Workflow CAD 2D.
- Guida simboli custom.
- Guida attributi e pinatura.
- Guida pagine standard, cartigli e immagini.
- Guida rimandi, cross-reference e morsetti.
- Troubleshooting iniziale.
- Standard operativi.
- Roadmap.
- Placeholder multifilare.
- Template inventario simboli.
- Template troubleshooting.
