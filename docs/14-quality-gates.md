# Quality gates

I quality gates definiscono quando un contenuto può essere considerato pronto per la knowledge base.

## Definition of Done documentale

Una nuova procedura è pronta quando:

- ha un obiettivo chiaro;
- indica quando usarla;
- contiene passaggi verificabili;
- include una verifica finale;
- non contiene dati sensibili;
- rimanda a standard, decisioni o casi pratici collegati;
- è collocata nella sezione corretta.

## Quality gate per simboli custom

Un simbolo custom è documentabile come stabile quando:

- è stato inserito in un progetto prova;
- gli attributi sono verificati;
- la pinatura è testata, se presente;
- lo stato è indicato nell'inventario;
- eventuali limitazioni sono annotate.

## Quality gate per archivi materiali

Un archivio materiali è documentabile come stabile quando:

- esiste un backup dello stato precedente;
- i dati sono normalizzati;
- i duplicati sono stati controllati;
- l'import è stato testato in ambiente non critico;
- almeno un materiale è stato associato a un simbolo;
- distinta o report sono stati verificati;
- ogni record ha uno stato chiaro.

## Quality gate per Archivio Cavi DbCables

Un `DbCables.db` custom è rilasciabile solo quando:

- il database originale è stato salvato come backup;
- l'integrity check SQLite è OK;
- non sono presenti codici cavo duplicati indesiderati;
- ogni cavo ha conduttori coerenti nella tabella dedicata;
- i campi tecnici principali sono popolati;
- i cavi custom sono marcati con campi di tracciabilità;
- SPAC avvia il controllo versione;
- l'allineamento versione librerie è completato;
- SPAC viene riaperto dopo l'allineamento;
- Archivio Cavi è consultabile;
- almeno un cavo custom è selezionabile;
- il pannello dati tecnici è popolato;
- i conduttori sono visibili;
- il test posa cavo è stato eseguito;
- il rollback è verificabile.

## Quality gate per troubleshooting

Una nota di troubleshooting è pronta quando:

- descrive il sintomo;
- indica cause probabili;
- propone una diagnosi;
- include una soluzione;
- indica come prevenire il problema.

## Quality gate per decisioni

Una decisione è pronta quando:

- il contesto è chiaro;
- la scelta è esplicita;
- la motivazione è documentata;
- l'impatto è comprensibile;
- lo stato è assegnato.

## Regola finale

Se un contenuto non aiuta a decidere, risolvere, standardizzare o verificare, deve essere semplificato o rimosso.
