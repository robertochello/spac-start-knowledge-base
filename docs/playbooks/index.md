# Playbook

I playbook sono procedure operative guidate. Servono per passare da un problema
o obiettivo a un risultato verificabile.

Usarli quando il caso è abbastanza concreto da richiedere una sequenza di
controlli. Per concetti generali usare prima le pagine operative.

## Quando usare quale playbook

| Necessità operativa | Playbook | Prima pagina di contesto |
|---|---|---|
| creare un simbolo custom riutilizzabile | [Creare un simbolo custom](create-custom-symbol.md) | [Simboli custom](../03-custom-symbols.md) |
| validare un simbolo prima del riuso | [Validare un simbolo custom](validate-custom-symbol.md) | [Checklist validazione simbolo](../10-symbol-validation-checklist.md) |
| diagnosticare pin che non aggancia | [Diagnosticare pin non agganciato](diagnose-pin-not-snapping.md) | [Attributi e pinatura](../04-attributes-and-pinning.md) |
| pulire entità residue o comportamenti anomali | [Pulire oggetti residui](clean-residual-objects.md) | [Troubleshooting](../07-troubleshooting.md) |
| gestire accessori, contatti o bobine | [Gestire accessori e bobine](manage-accessories-and-coils.md) | [Multifilare](../09-multifilare.md) |
| verificare il dato mostrato da un morsetto | [Verificare rappresentazione morsetti](terminal-representation.md) | [Rimandi e morsetti](../06-cross-references-terminals.md) |
| diagnosticare rimandi di alimentazione | [Diagnosticare rimandi alimentazione](power-reference-diagnostic.md) | [Rimandi e morsetti](../06-cross-references-terminals.md) |
| associare materiali e controllare la distinta | [Associare materiali](material-association.md) | [Archivi materiali custom](../21-material-archives.md) |
| aggiornare `DbCables.db` in modo reversibile | [Aggiornare Archivio Cavi DbCables](update-dbcables-archive.md) | [Archivio Cavi DbCables](../25-cable-archive-dbcables.md) |

## Playbook disponibili

| Playbook | Obiettivo |
|---|---|
| [Creare un simbolo custom](create-custom-symbol.md) | Creare un simbolo riutilizzabile e riconoscibile da SPAC |
| [Validare un simbolo custom](validate-custom-symbol.md) | Verificare attributi, pinatura, inserimento e riuso |
| [Diagnosticare pin non agganciato](diagnose-pin-not-snapping.md) | Capire perché un filo non si collega al pin del simbolo |
| [Gestire cartiglio e logo](titleblock-logo-workflow.md) | Ridurre problemi con immagini e riferimenti nei cartigli |
| [Gestire accessori e bobine](manage-accessories-and-coils.md) | Governare elementi associati a un componente principale |
| [Verificare rappresentazione morsetti](terminal-representation.md) | Capire quale dato viene mostrato dal simbolo morsetto |
| [Diagnosticare rimandi alimentazione](power-reference-diagnostic.md) | Analizzare selezioni non valide e riferimenti non coerenti |
| [Associare materiali](material-association.md) | Associare materiali evitando duplicazioni e ambiguità |
| [Aggiornare Archivio Cavi DbCables](update-dbcables-archive.md) | Sostituire controllatamente il database cavi e validare l'allineamento |
| [Pulire oggetti residui](clean-residual-objects.md) | Gestire residui grafici o intelligenti che alterano i riferimenti |

## Regola playbook

Ogni playbook deve terminare con una verifica finale. Una procedura senza verifica non è ancora una procedura stabile.
