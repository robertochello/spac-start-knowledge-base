# Known Issue — DbCables versione non congruente

## Sintomo

Dopo la sostituzione diretta del file `DbCables.db`, SPAC può mostrare un avviso di versione non congruente del database.

Messaggio tipico:

```text
Il file DbCables.db non ha una versione congruente con il programma.
È necessario l'adeguamento strutturale.
```

## Ambienti verificati

La stessa gestione è stata verificata sia su SPAC Automazione sia su SPAC Start.

## Causa probabile

Il file `DbCables.db` è strutturalmente valido, ma non è allineato alla versione attesa dall'installazione SPAC corrente.

Questo può accadere quando il database è stato modificato manualmente o generato a partire da una base diversa.

## Correzione

Usare la funzione di allineamento versione librerie proposta da SPAC.

Procedura sintetica:

1. Confermare l'avviso.
2. Aprire la finestra di ripristino/allineamento.
3. Usare:

   ```text
   Allinea la versione delle librerie
   ```

4. Attendere il completamento.
5. Chiudere la finestra.
6. Se SPAC si chiude, riaprirlo.
7. Verificare Archivio Cavi.

## Comportamento atteso

Dopo l'allineamento e il riavvio, il database sostituito può risultare utilizzabile.

## Quando fare rollback

Eseguire rollback se:

- SPAC non si riapre correttamente;
- Archivio Cavi non è consultabile;
- i cavi custom non sono visibili;
- i conduttori risultano incoerenti;
- la posa cavo non accetta i cavi selezionati.

## Prevenzione

- Usare sempre backup.
- Testare su ambiente non critico.
- Eseguire integrity check prima del rilascio.
- Marcare i cavi custom con campi dedicati.
- Verificare i dati tecnici su datasheet prima dell'uso reale.
- Applicare i back-check quando il database è destinato a più ambienti.

## Collegamenti

- [Archivio Cavi DbCables](../25-cable-archive-dbcables.md)
- [Aggiornare Archivio Cavi DbCables](../playbooks/update-dbcables-archive.md)
- [Back-check e controlli incrociati](../26-back-check-controls.md)
