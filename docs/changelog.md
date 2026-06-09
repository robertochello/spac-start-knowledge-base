# Changelog

## 0.8.1 - Restore automatic deploy path

### Changed

- Rimossa la documentazione di deploy manuale dopo la riattivazione di GitHub Actions.
- Rimossi gli script locali di deploy manuale.
- Navigazione MkDocs ripulita dalla voce di deploy manuale.
- Homepage documentale ripulita dai riferimenti al deploy senza Actions.

## 0.8.0 - DbCables archive sprint

### Added

- Diagramma workflow sostituzione controllata `DbCables.db`.
- Guida `Archivio Cavi DbCables`.
- Playbook `Aggiornare Archivio Cavi DbCables`.
- Known issue `DbCables versione non congruente`.
- Quality gate specifico per rilascio `DbCables.db` custom.
- Decisione D008 per sostituzione controllata e allineamento librerie.

### Changed

- Homepage documentale aggiornata con accesso rapido all'Archivio Cavi.
- Indice playbook aggiornato con procedura DbCables.
- Indice known issues aggiornato con avviso versione non congruente.

## 0.7.0 - Operational examples sprint

### Added

- Esempio visuale simbolo Madre.
- Esempio visuale simbolo cablato con pin.
- Esempio visuale rappresentazione morsetto.
- Esempio visuale record materiale.
- Pagina `Esempi operativi` con riferimenti e verifiche minime.

### Changed

- Homepage documentale aggiornata con accesso rapido agli esempi operativi.

## 0.6.0 - Professional polish and materials workflow

### Added

- Diagramma visuale della knowledge base.
- Diagramma lifecycle simbolo custom.
- Diagramma workflow archivi materiali custom.
- Guida archivi materiali custom.
- Standard materiali.
- Template record materiale.
- Quality gate specifico per archivi materiali.
- Decisioni operative per import materiali e stati record.

### Changed

- Homepage documentale resa più visuale e orientata all'accesso rapido.
- Guida simboli custom riorganizzata con diagramma lifecycle e tabella fasi/output.
- Indice playbook aggiornato con tutti i playbook operativi disponibili.
- Indice standard aggiornato con standard materiali.

## 0.5.1 - Workflow hardening

### Changed

- Dipendenze documentazione rese esplicite in `requirements.txt`.
- Workflow GitHub Actions reso più robusto per il deploy MkDocs.
- Build deploy non più eseguita in modalità strict, per evitare failure su warning non bloccanti.
- Configurazione Git author aggiunta prima del deploy.
- Deploy configurato con `--no-history`.

## 0.5.0 - README integration sprint

### Added

- Sezione libreria custom con installazione, categorie e checklist manutenzione.
- Sezione template progetto con pagine standard e riferimento DWG.
- Sezione schema unifilare.
- Sezione numerazione e identificazione fili.
- Sezione nomenclatura simboli.
- Dizionario abbreviazioni.

### Changed

- Guida simboli custom ampliata con workflow DWG, SLD, normalizzazione, Madre/Figlio e materiali.
- Guida attributi e pinatura ampliata con relazione Madre/Figlio e dettagli configurazione pin.
- Guida pagine, cartigli e immagini ampliata con gestione riferimenti e cartella risorse.
- Guida rimandi, cross-reference e morsetti ampliata con direzioni rimandi, lista rimandi, morsettiere e rappresentazioni NumI/NumO/NumM.
- Navigazione MkDocs aggiornata con le sezioni importate dal README operativo.

## 0.4.0 - Operational playbooks sprint

### Added

- Sezione multifilare ampliata con workflow, materiali, morsetti, rimandi e checklist.
- Playbook gestione accessori e bobine.
- Playbook verifica rappresentazione morsetti.
- Playbook diagnosi rimandi alimentazione.
- Playbook associazione materiali.
- Playbook pulizia oggetti residui.

### Changed

- Navigazione MkDocs aggiornata con i nuovi playbook operativi.
- Knowledge base collegata al portfolio personale come progetto dedicato.

## 0.3.0 - Documentation site foundation

### Added

- Configurazione MkDocs Material.
- Homepage documentale.
- Playbook operativi.
- Glossario.
- Known Issues.
- Workflow GitHub Actions per build e deploy documentazione.

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
