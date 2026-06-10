# Playbook — Aggiornare Archivio Cavi DbCables

## Obiettivo

Aggiornare l'archivio cavi avanzato di SPAC tramite sostituzione controllata del file `DbCables.db`.

## Ambito verificato

La procedura è stata testata sia su:

- SPAC Automazione;
- SPAC Start.

Il workflow operativo è lo stesso in entrambi gli ambienti.

## Quando usarlo

Usare questa procedura quando si devono aggiungere cavi custom all'Archivio Cavi avanzato di SPAC.

Non usare il metodo Import/Export se SPAC restituisce:

```text
Il DB scelto non è un DB di SPAC valido
```

## Prerequisiti

- SPAC chiuso.
- Backup del `DbCables.db` originale.
- `DbCables.db` modificato già validato.
- Accesso alla cartella Librerie/Archivi.
- Test previsto su progetto non critico.
- Elenco dei cavi custom da verificare.
- Ambiente di test identificato: SPAC Automazione, SPAC Start o entrambi.

## Procedura

1. Chiudere SPAC.
2. Aprire la cartella archivi delle librerie SPAC.
3. Salvare il file originale con nome di backup.
4. Copiare il database modificato nella stessa cartella.
5. Rinominare il database modificato in:

```text
DbCables.db
```

6. Avviare SPAC.
7. Se compare l'avviso di versione non congruente, proseguire.
8. Nella finestra di ripristino usare:

```text
Allinea la versione delle librerie
```

9. Attendere il completamento.
10. Chiudere la finestra di allineamento.
11. Se SPAC si chiude o si comporta in modo anomalo, riaprirlo.
12. Aprire Archivio Cavi e verificare i nuovi cavi.

## Back-check prima dell'avvio SPAC

Prima di aprire SPAC, verificare:

| Controllo | Esito atteso |
|---|---|
| File originale salvato | Backup presente |
| File modificato presente | Nome corretto |
| Integrità database | Nessun errore |
| Cavi custom marcati | Release o stato riconoscibile |
| Conduttori collegati | Nessun cavo senza dettaglio conduttori |

## Verifica funzionale

La procedura è valida quando:

- SPAC si apre senza blocchi;
- Archivio Cavi è consultabile;
- produttori e cavi custom sono visibili;
- il pannello dati tecnici è popolato;
- la tabella conduttori è coerente;
- la posa cavo accetta il cavo selezionato.

## Verifica incrociata SPAC Automazione / SPAC Start

Quando il database deve essere considerato riutilizzabile in entrambi gli ambienti, eseguire la stessa verifica su entrambi.

| Check | SPAC Automazione | SPAC Start |
|---|---|---|
| Avvio software | OK / KO | OK / KO |
| Allineamento librerie | OK / KO | OK / KO |
| Archivio Cavi consultabile | OK / KO | OK / KO |
| Cavo custom ricercabile | OK / KO | OK / KO |
| Dati tecnici visibili | OK / KO | OK / KO |
| Conduttori coerenti | OK / KO | OK / KO |
| Posa cavo testata | OK / KO | OK / KO |
| Rollback verificato | OK / KO | OK / KO |

## Rollback

Se qualcosa non funziona:

1. Chiudere SPAC.
2. Rimuovere il `DbCables.db` modificato.
3. Ripristinare il backup originale.
4. Rinominare il backup in:

```text
DbCables.db
```

5. Riaprire SPAC.
6. Verificare Archivio Cavi.

## Avvertenze

- Non sostituire il database mentre SPAC è aperto.
- Non lavorare mai senza backup.
- Non usare direttamente su commessa reale prima del test.
- Non considerare i dati dei cavi custom certificati senza verifica datasheet.
- Documentare sempre release e marcatura dei cavi custom.
- Se il database è destinato a più ambienti, validarlo sia su SPAC Automazione sia su SPAC Start.

## Collegamenti

- [Archivio Cavi DbCables](../25-cable-archive-dbcables.md)
- [Back-check e controlli incrociati](../26-back-check-controls.md)
- [Known Issue — DbCables versione non congruente](../known-issues/dbcables-version-mismatch.md)
- [Quality gates](../14-quality-gates.md)
