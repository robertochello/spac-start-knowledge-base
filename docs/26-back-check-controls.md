# Back-check e controlli incrociati

Questa sezione definisce un metodo generale per verificare le procedure documentate nella knowledge base.

## Obiettivo

Evitare che una procedura venga considerata valida solo perché ha funzionato una volta.

Ogni procedura importante deve avere:

- controllo prima dell'azione;
- controllo durante l'azione;
- controllo dopo l'azione;
- verifica incrociata;
- rollback o piano di recupero.

## Metodo in 5 fasi

| Fase | Domanda | Esempio |
|---|---|---|
| Pre-check | Sono nelle condizioni corrette? | Backup presente, software chiuso, file corretto |
| Action check | Sto applicando la procedura giusta? | Passi eseguiti in ordine |
| Post-check | Il risultato è visibile? | Archivio consultabile, simbolo inseribile |
| Cross-check | Lo stesso risultato è confermato altrove? | Test su SPAC Automazione e SPAC Start |
| Rollback-check | Posso tornare indietro? | Backup ripristinabile |

## Regola back-check

Una procedura è stabile solo se supera almeno tre livelli:

1. **verifica tecnica**;
2. **verifica funzionale**;
3. **verifica operativa**.

## Verifica tecnica

Controlla che il dato o file sia formalmente valido.

Esempi:

- database integro;
- file presente;
- formato corretto;
- nessun errore evidente;
- nomi e percorsi coerenti.

## Verifica funzionale

Controlla che il software legga e usi correttamente il dato.

Esempi:

- archivio aperto;
- elemento ricercabile;
- simbolo inseribile;
- attributi modificabili;
- report generabile.

## Verifica operativa

Controlla che la procedura sia utile in un caso realistico.

Esempi:

- cavo selezionabile in posa;
- materiale riportato in distinta;
- morsetto rappresentato con il dato corretto;
- rimando coerente dopo modifica schema.

## Matrice esito

| Esito | Significato | Azione |
|---|---|---|
| OK | Verifica superata | Procedere |
| KO | Verifica fallita | Fermarsi e diagnosticare |
| N/A | Non applicabile | Motivare perché non serve |
| Da ripetere | Esito non stabile | Ripetere in ambiente pulito |

## Controllo incrociato tra ambienti

Quando una procedura può essere usata su più ambienti, registrare l'esito separatamente.

| Procedura | SPAC Automazione | SPAC Start | Esito finale |
|---|---|---|---|
| Archivio Cavi DbCables | OK / KO | OK / KO | Validato / Da verificare |
| Simbolo custom | OK / KO | OK / KO | Validato / Da verificare |
| Associazione materiali | OK / KO | OK / KO | Validato / Da verificare |

## Regola di pubblicazione

Una procedura può diventare standard solo quando:

- è stata testata;
- è stato documentato l'ambiente di test;
- sono noti i limiti;
- esiste un rollback o una procedura di ripristino;
- è collegata a un quality gate.

## Collegamenti

- [Quality gates](14-quality-gates.md)
- [Decision log](11-decision-log.md)
- [Archivio Cavi DbCables](25-cable-archive-dbcables.md)
- [Aggiornare Archivio Cavi DbCables](playbooks/update-dbcables-archive.md)
