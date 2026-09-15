# Playbook — Diagnosticare pin non agganciato

## Obiettivo

Capire perché un filo non si aggancia al pin di un simbolo custom usando controlli e comandi ripetibili.

## 1. Verificare gli attributi del simbolo inserito

Sul simbolo inserito usa:

```text
EDITATT
```

Controlla che siano presenti gli attributi previsti:

```text
PINA1
PINA2
PINA3
...
```

Se il segnale deve attraversare il simbolo, verifica anche la coppia:

```text
PINB1
PINB2
PINB3
...
```

La numerazione `PINA<n>` / `PINB<n>` deve essere coerente.

## 2. Verificare snap e griglia

Digita:

```text
_DSETTINGS
```

Apri il tab **Snap e griglia**.

Controlla che il punto del pin sia allineato alla stessa griglia usata per il collegamento.

## 3. Verificare il DWG sorgente

Se il pin manca o è posizionato male, apri il DWG sorgente del simbolo.

Per creare/correggere un attributo usa:

```text
ATTDEF
```

Per controllare le proprietà dell'attributo usa:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

Per copiare proprietà corrette da un pin già funzionante usa:

```text
CORRISPROP
```

## 4. Verificare che il filo sia un collegamento SPAC

Non basta che una linea CAD tocchi graficamente il punto del pin.

Controlla che il filo sia creato come collegamento riconosciuto da SPAC e non come semplice geometria CAD.

## 5. Testare su progetto pulito

1. Apri un foglio/progetto di prova.
2. Apri la libreria simboli con:

   ```text
   SP_XML_MENU
   ```

3. Inserisci il simbolo.
4. Disegna un nuovo collegamento verso `PINA1`.
5. Ripeti sugli altri pin.
6. Salva, chiudi e riapri.

## 6. Se correggi il DWG, rigenerare anche l'anteprima

Dopo una correzione strutturale del simbolo:

1. rigenera il DWG con:

   ```text
   MBLOCCO
   ```

2. in **Origine** scegli `Oggetti`;
3. seleziona il punto base corretto;
4. apri il DWG;
5. rigenera l'anteprima con:

   ```text
   _MSLIDE
   ```

6. mantieni stesso nome base per DWG e SLD.

## Diagnostica rapida

| Sintomo | Comando / controllo |
|---|---|
| `PINA` non presente | `EDITATT`; se manca nel sorgente → `ATTDEF` |
| pin fuori griglia | `_DSETTINGS` → **Snap e griglia** |
| proprietà pin incoerenti | `PROPRIETA` / `CTRL+1` |
| devo copiare impostazioni da un pin corretto | `CORRISPROP` |
| linea tocca ma non si collega | verifica collegamento SPAC vs linea CAD |
| correzione sorgente non compare | rigenera `MBLOCCO` e `_MSLIDE`, poi reinserisci/testa |

## Verifica finale

Il problema è risolto quando:

- il pin è presente in `EDITATT` quando previsto;
- il punto del pin è allineato alla griglia;
- il filo aggancia realmente il pin;
- eventuale `PINB<n>` funziona sul lato opposto;
- il comportamento resta stabile dopo salvataggio e riapertura.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
- [Creare un simbolo custom](create-custom-symbol.md)
- [Validare un simbolo](validate-custom-symbol.md)
