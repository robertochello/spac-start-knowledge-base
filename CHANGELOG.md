# Changelog

Tutte le modifiche rilevanti alla knowledge base saranno documentate in questo file.

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
- Standard nomenclatura allineato a `SCB` per contatto di scambio.
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
