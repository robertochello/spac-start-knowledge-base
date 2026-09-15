# Multifilare

Questa pagina raccoglie le operazioni multifilari già verificate in SPAC Start 26. Dove il comando o la voce di menu è nota viene riportata con il **nome esatto**.

## Lista completa dei numeri usati

Per visualizzare la lista dei numeri già presenti nello schema usa il percorso:

```text
Numerazione fili → Lista numeri usati
```

Controllo:

- verifica i numeri presenti;
- i numeri segnalati con **asterisco** indicano numerazioni ripetute.

## Eliminare la numerazione dei fili

Percorso da menu:

```text
SPAC → Utility Fili → Elimina numerazione
```

Comando equivalente da riga comando:

```text
DEL_NUMF
```

Usa questa funzione quando devi rimuovere la numerazione esistente prima di rigenerarla.

## Inserire morsetti

Il comando verificato è:

```text
SPINSMOR
```

### Prerequisito

Prima di eseguire `SPINSMOR` deve essere aperto un **database materiali che contenga almeno una morsettiera**. Se il database non contiene una morsettiera, il comando può restituire errore.

### Creare una nuova morsettiera

Dopo l'apertura della finestra **Inser Morsetti**:

1. guarda il riquadro in alto a sinistra **Elenco Quadri**;
2. fai **tasto destro** su una delle seguenti voci:
   - **Elenco Quadri**;
   - nome del quadro;
   - una morsettiera già esistente;
3. clicca **Nuova morsettiera**;
4. completa i dati della nuova morsettiera;
5. verifica che la morsettiera compaia sotto il quadro corretto.

## Verificare un morsetto che mostra il dato sbagliato

Non modificare subito il testo grafico. Prima distingui:

- morsettiera;
- numero morsetto;
- numero filo;
- rappresentazione grafica;
- dato sorgente visualizzato.

Procedura dedicata: [Verificare rappresentazione morsetti](playbooks/terminal-representation.md).

## Rimandi e cross-reference

Un rimando deve essere collegato a un oggetto SPAC coerente e non a una semplice linea CAD.

Quando un rimando non funziona:

1. verifica se l'elemento selezionato è un oggetto SPAC o sola grafica CAD;
2. verifica residui o oggetti sovrapposti;
3. aggiorna i riferimenti previsti dalla procedura specifica;
4. esegui un test su un foglio pulito se il comportamento resta ambiguo.

Il nome esatto del comando di rigenerazione cross-reference resta **Da verificare** finché non viene confermato direttamente in SPAC Start 26.

Per la diagnosi usa:

- [Rimandi, cross-reference e morsetti](06-cross-references-terminals.md);
- [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md);
- [Cross-reference obsoleto](known-issues/obsolete-cross-reference.md).

## Componenti Madre, Figli e accessori

La relazione non deve dipendere dalla vicinanza grafica.

Regola documentata:

- Madre: `PRES = M`;
- Figlio: `PRES = F`;
- Figlio associato: `NOME` uguale/coerente con la Madre.

Per creare gli attributi nel DWG sorgente usa:

```text
ATTDEF
```

Per modificare gli attributi di un simbolo già inserito usa:

```text
EDITATT
```

Per la procedura completa: [Gestire accessori e bobine](playbooks/manage-accessories-and-coils.md).

## Associare un materiale a un simbolo

Percorso verificato:

1. fai **doppio click sul simbolo**;
2. nel riquadro **Materiali**, fai **tasto destro**;
3. clicca **Avvio Archivio Materiali (DbCenter)**;
4. in DbCenter seleziona il materiale corretto;
5. conferma l'associazione;
6. controlla distinta/report per verificare che il materiale compaia una sola volta dove previsto.

Approfondimento: [Associare materiali](playbooks/material-association.md).

## Sequenza consigliata di verifica multifilare

1. Identifica il componente principale.
2. Controlla `NOME` e `PRES` con `EDITATT` se necessario.
3. Verifica gli elementi Figlio/accessori associati.
4. Controlla fili e numerazioni.
5. Per la lista numeri usa **Numerazione fili → Lista numeri usati**.
6. Se devi azzerare la numerazione usa **SPAC → Utility Fili → Elimina numerazione** oppure `DEL_NUMF`.
7. Per i morsetti usa `SPINSMOR` e lavora nella finestra **Inser Morsetti**.
8. Verifica rimandi e cross-reference.
9. Per i materiali usa **doppio click → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)**.
10. Verifica distinta/report.

## Diagnostica rapida

| Sintomo | Prima azione concreta |
|---|---|
| Numero filo duplicato | **Numerazione fili → Lista numeri usati**; cerca asterischi |
| Devo eliminare i numeri esistenti | **SPAC → Utility Fili → Elimina numerazione** oppure `DEL_NUMF` |
| Devo inserire/gestire morsetti | `SPINSMOR` |
| Devo creare una morsettiera | **Inser Morsetti → tasto destro su Elenco Quadri → Nuova morsettiera** |
| Accessorio non collegato alla Madre | `EDITATT` e verifica `NOME` / `PRES` |
| Materiale manca o è duplicato | **doppio click → Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)** |
| Rimando non accetta la selezione | verifica prima se stai selezionando un oggetto SPAC o una linea CAD |

## Da verificare

Se per una funzione non è ancora noto il nome esatto della voce di menu o del comando in SPAC Start 26, la guida deve riportare **Da verificare**. Non usare descrizioni inventate come se fossero comandi reali.

## Collegamenti

- [Comandi e percorsi esatti](command-reference.md)
- [Rimandi e morsetti](06-cross-references-terminals.md)
- [Numerazione e identificazione fili](18-wire-numbering.md)
- [Attributi e pinatura](04-attributes-and-pinning.md)
- [Troubleshooting](07-troubleshooting.md)
