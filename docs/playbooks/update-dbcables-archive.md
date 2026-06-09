# Playbook — Aggiornare Archivio Cavi DbCables

## Obiettivo

Aggiornare l'archivio cavi avanzato di SPAC tramite sostituzione controllata del file `DbCables.db`.

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

## Verifica funzionale

La procedura è valida quando:

- SPAC si apre senza blocchi;
- Archivio Cavi è consultabile;
- produttori e cavi custom sono visibili;
- il pannello dati tecnici è popolato;
- la tabella conduttori è coerente;
- la posa cavo accetta il cavo selezionato.

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

## Collegamenti

- [Archivio Cavi DbCables](../25-cable-archive-dbcables.md)
- [Known Issue — DbCables versione non congruente](../known-issues/dbcables-version-mismatch.md)
- [Quality gates](../14-quality-gates.md)
