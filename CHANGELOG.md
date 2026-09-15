# Changelog

Tutte le modifiche rilevanti alla knowledge base sono documentate in questo file.

## 0.8.0 - 2026-09-15 - Public downloads & visual refresh

### Privacy

- Rimossa dal contenuto corrente la vecchia dipendenza da riferimenti specifici a elaborati/commesse reali nel manuale monolitico.
- `guida-operativa-completa.md` sostituita con una guida consolidata e sanitizzata, costruita solo su esempi generici.
- Rimossi i metadati personali non necessari dal README/sito.
- Aggiunto `scripts/audit_public_content.py` per controllare prima del deploy file testuali e database SQLite pubblici.
- L'audit cerca pattern ad alta confidenza per email, IP, MAC, percorsi utente, UNC e assegnazioni di credenziali senza stampare il valore trovato.
- L'audit controlla anche nomi sospetti di tabelle/colonne SQLite e calcola SHA256 di tutti i file scaricabili.
- Il workflow `Deploy documentation` ora esegue l'audit prima di `mkdocs build --strict`.

### Download

- Pagina Download ridisegnata come area pubblica dedicata agli archivi.
- Materiali separati da cavi con card e stato di disponibilità.
- `ABB_Materials.db` esposto come archivio materiali disponibile.
- `archivio-materiali-custom-r01.db` esposto come archivio custom R01 disponibile.
- Area cavi mantenuta predisposta per un futuro `DbCables.db` sanitizzato/versionato.
- Aggiunte regole esplicite per privacy, SHA256, test SPAC e diritto di redistribuzione.
- Download promosso a voce principale della navigazione MkDocs.

### Visual refresh

- Home ridisegnata con hero principale e accessi rapidi a comandi, download e troubleshooting.
- Card operative ridisegnate con gerarchia visiva più chiara e stati hover più leggibili.
- Nuove card download e badge di stato.
- Larghezza contenuti e spaziatura riviste per desktop e mobile.
- Tabelle, admonition, pulsanti, immagini e blocchi codice uniformati.
- Migliorata la coerenza tra tema chiaro e scuro.
- Abilitati `navigation.instant`, progress indicator, `toc.follow` e tooltips di MkDocs Material.
- Disabilitato il footer generator predefinito.

## 0.7.0 - 2026-09-15 - Procedure fidelity pass

### Fixed

- Ripristinato il percorso cross-reference verificato: **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna**.
- Ripristinata la creazione rimandi tramite **Dynamic Coll / Dynamic Alim**.
- Completata la scansione rimandi: **Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli**.
- Completato l'inserimento morsetto: morsettiera → tipo → **Anteprima → Ok - Nuovo → clic filo → Invio**.
- Documentata la scelta `NumM`/`NumI`/`NumO` nel riquadro **Anteprima**.
- Completato `MBLOCCO` con destinazione, punto base e **Unità inser. → Senza unità**.
- Completati i campi `ATTDEF` di `NOME`, `PRES`, `PINA1`, `PINB1`.

### Quality rule

- Ogni procedura operativa deve preferire: **Dove cliccare → Cosa impostare → Esito atteso → Diagnosi se KO**.
- Una voce già verificata non deve essere degradata a descrizione generica o `Da verificare`.

## 0.6.0 - 2026-09-15 - Exact commands and click paths

### Changed

- `command-reference.md` trasformata nel riferimento centrale per comandi, menu, finestre, pulsanti e valori esatti.
- Home e guida pratica aggiornate con accesso diretto a **Comandi e click esatti**.
- `AGENTS.md` aggiornato con l'obbligo di usare nomi reali quando verificati.
- Pagine operative e playbook allineati ai comandi reali di SPAC Start 26.
- Workflow layer/oggetti residui documentato con `PURGE`, `QSELECT` e `BEDIT`.

### Explicitly unsupported

- `LAYISO` e `LAYWALK` non devono essere proposti come comandi disponibili nell'ambiente SPAC Start 26 verificato.

## 0.5.0 - 2026-09-15 - Navigation and onboarding refresh

- Home riscritta come selettore per attività reali.
- `00-how-to-use.md` trasformata in guida pratica.
- Navigazione MkDocs semplificata.
- Manuale completo declassato da punto di ingresso a riferimento.
- README orientato al sito pubblico.
- CSS iniziale delle card e delle tabelle migliorato.

## 0.4.0 - Site coherence pass

- Aggiunti back-check, Download e cartelle pubbliche per materiali/cavi.
- Aggiunti link per gli archivi materiali disponibili.
- Completata l'esposizione delle pagine principali nel sito.
- Risolti link rotti e incoerenze documentali.

## 0.3.0 - Documentation site foundation

- Configurazione MkDocs Material.
- Homepage documentale.
- Workflow GitHub Actions per build/deploy.
- Playbook operativi, glossario, Known Issues e quality gates.

## 0.2.0 - Knowledge base consolidation

- Checklist validazione simboli.
- Decision log.
- Casi pratici.
- Linee guida di manutenzione.
- Roadmap.

## 0.1.0 - Initial structure

- Struttura iniziale della knowledge base.
- Guide per interfaccia, CAD, simboli, attributi, cartigli, rimandi e troubleshooting.
- Standard operativi e template documentali.
