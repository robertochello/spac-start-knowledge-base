# Playbook — Validare un simbolo custom

## Obiettivo

Verificare con passaggi ripetibili che un simbolo custom sia pronto per essere riutilizzato.

## 1. Verificare i file della libreria

Nella categoria `_CUSTOM` devono essere presenti:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

Il nome base deve essere identico.

Se devi rigenerare l'anteprima:

1. apri il DWG;
2. centra il simbolo;
3. digita `_MSLIDE`;
4. salva l'SLD nella stessa cartella con lo stesso nome base.

## 2. Verificare Layer e proprietà grafiche

Il simbolo custom deve rispettare lo standard:

```text
Layer 0
```

e, dove previsto:

- Colore `DaBlocco`;
- Tipo linea `DaBlocco`;
- Spessore linea `DaBlocco`.

Per controllare le proprietà usa:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

## 3. Inserire il simbolo in un progetto prova

Apri la libreria simboli con:

```text
SP_XML_MENU
```

Inserisci il simbolo custom in un foglio/progetto di prova.

Verifica:

- scala;
- orientamento;
- punto base;
- visibilità;
- assenza di geometrie residue.

## 4. Verificare gli attributi

Sul simbolo inserito usa:

```text
EDITATT
```

Controlla almeno:

- `NOME`;
- `PRES`;
- eventuali `PINA<n>`;
- eventuali `PINB<n>`.

Regole:

```text
Madre  → PRES = M
Figlio → PRES = F
```

Se un attributo manca e deve essere aggiunto nel DWG sorgente, usa:

```text
ATTDEF
```

## 5. Verificare la pinatura

1. Configura snap/griglia con:

   ```text
   _DSETTINGS
   ```

2. Apri il tab **Snap e griglia**.
3. Inserisci il simbolo.
4. Collega un filo a ogni `PINA<n>`.
5. Se esiste `PINB<n>`, verifica la connessione corrispondente.
6. Salva, chiudi e riapri il progetto.

Il test è superato solo se il filo aggancia realmente il pin e non si limita a passare graficamente vicino al simbolo.

## 6. Verificare il materiale, se previsto

1. Fai doppio click sul simbolo.
2. Riquadro **Materiali** → tasto destro.
3. **Avvio Archivio Materiali (DbCenter)**.
4. Verifica/seleziona il materiale.
5. Controlla distinta/report.

## 7. Verificare il DWG sorgente se qualcosa non torna

Se devi correggere il blocco:

- `ATTDEF` per attributi;
- `PROPRIETA` / `CTRL+1` per proprietà;
- `CORRISPROP` per copiare proprietà;
- `MBLOCCO` per rigenerare il DWG;
- `_MSLIDE` per rigenerare l'anteprima.

## Esito

Assegna uno stato nell'inventario:

- **Testato**;
- **Da verificare**;
- **In revisione**;
- **Deprecato**.

Un simbolo può essere **Testato** solo se:

- DWG/SLD coerenti;
- proprietà grafiche corrette;
- inserimento riuscito;
- `EDITATT` mostra/modifica gli attributi previsti;
- pinatura verificata;
- materiale verificato se previsto;
- comportamento stabile dopo salvataggio/riapertura.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Creare un simbolo custom](create-custom-symbol.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
- [Diagnosticare pin non agganciato](diagnose-pin-not-snapping.md)
- [Checklist validazione simbolo](../10-symbol-validation-checklist.md)
