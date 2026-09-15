# Simboli custom

Questa pagina raccoglie il workflow operativo per creare e gestire simboli custom in SPAC Start 26. I comandi consolidati sono riportati con il loro nome reale.

## Workflow rapido

1. Importa o prepara la geometria.
2. Pulisci Layer, colore e linee.
3. Crea gli attributi con `ATTDEF`.
4. Crea il DWG con `MBLOCCO`.
5. Crea l'anteprima con `_MSLIDE`.
6. Inserisci il simbolo in un progetto di prova.
7. Modifica gli attributi con `EDITATT`.
8. Verifica pin e materiali.
9. Aggiorna l'inventario.

## Importare una geometria

Per inserire un DWG/blocco di partenza:

```text
_INSER
```

Se devi modificare le singole entità:

```text
ESPLODI
```

Usa `ESPLODI` solo quando serve realmente.

## Pulizia grafica

Per i simboli custom usa:

```text
Layer 0
```

Impostazioni grafiche adottate:

- **Colore**: `DaBlocco`;
- **Tipo linea**: `DaBlocco`;
- **Spessore linea**: `DaBlocco`.

## Creare gli attributi

Comando:

```text
ATTDEF
```

Attributi principali:

- `NOME`;
- `PRES`;
- `PINA1`, `PINA2`, ...;
- `PINB1`, `PINB2`, ... solo quando necessario.

Per i campi esatti da compilare vedi [Attributi e pinatura](04-attributes-and-pinning.md).

## Madre e Figlio

Regole documentate:

```text
Madre  → PRES = M
Figlio → PRES = F
```

Quando il Figlio deve essere associato alla Madre, `NOME` deve essere coerente con la Madre.

## Creare il DWG del simbolo

1. Seleziona tutti gli oggetti.
2. Digita:

   ```text
   MBLOCCO
   ```

3. In **Origine** seleziona:

   ```text
   Oggetti
   ```

4. Seleziona il **punto base**.
5. Salva nella categoria corretta della libreria:

   ```text
   C:\SPAC Start 26\Librerie\Blk\_CUSTOM\<CATEGORIA>
   ```

## Creare l'anteprima SLD

1. Apri direttamente il DWG appena creato.
2. Centra il simbolo.
3. Regola lo zoom.
4. Digita:

   ```text
   _MSLIDE
   ```

5. Salva il `.sld` nella stessa cartella del `.dwg`.
6. Usa lo stesso nome base:

   ```text
   NOME_SIMBOLO.dwg
   NOME_SIMBOLO.sld
   ```

## Modificare e verificare gli attributi

Per modificare gli attributi del simbolo già inserito:

```text
EDITATT
```

Per aprire le proprietà:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

Per copiare proprietà:

```text
CORRISPROP
```

## Associare un materiale

1. Fai **doppio click sul simbolo**.
2. Nel riquadro **Materiali**, fai **tasto destro**.
3. Clicca:

   ```text
   Avvio Archivio Materiali (DbCenter)
   ```

4. Seleziona il materiale corretto.
5. Verifica distinta/report.

Approfondimento: [Associare materiali](playbooks/material-association.md).

## Test pinatura

1. Inserisci il simbolo in un progetto prova.
2. Usa `EDITATT` per verificare gli attributi.
3. Collega un filo a ogni `PINA<n>` previsto.
4. Se esiste `PINB<n>`, verifica anche il lato di uscita.
5. Se il filo non aggancia, usa [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md).

## Checklist finale

Un simbolo è riutilizzabile solo se:

- geometria pulita;
- Layer 0;
- attributi creati con `ATTDEF`;
- DWG creato con `MBLOCCO`;
- SLD creato con `_MSLIDE`;
- `.dwg` e `.sld` con stesso nome base;
- `EDITATT` funziona;
- pin testati;
- materiale testato se previsto;
- inventario aggiornato.

## Collegamenti

- [Creare un simbolo custom passo-passo](playbooks/create-custom-symbol.md)
- [Attributi e pinatura](04-attributes-and-pinning.md)
- [Comandi e click esatti](command-reference.md)
- [Checklist validazione simbolo](10-symbol-validation-checklist.md)
