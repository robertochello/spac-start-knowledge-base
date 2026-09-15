# Playbook — Creare un simbolo custom

## Obiettivo

Creare un simbolo custom ordinato, riconoscibile e riutilizzabile in SPAC Start usando i comandi effettivi della procedura.

## Procedura operativa

### 1. Preparare o importare la geometria

Se devi inserire un DWG o un blocco di partenza, dalla riga comando usa:

```text
_INSER
```

Se devi modificare le singole entità della geometria importata, usa solo quando necessario:

```text
ESPLODI
```

Poi:

1. rimuovi entità inutili;
2. verifica scala e orientamento;
3. porta la geometria su **Layer 0**;
4. imposta colore, tipo linea e spessore su **DaBlocco**;
5. definisci il punto che dovrà diventare il punto base del simbolo.

### 2. Creare gli attributi

Per ogni attributo usa:

```text
ATTDEF
```

Per una Madre crea almeno:

- `NOME`;
- `PRES` con valore `M`.

Per un Figlio usa `PRES = F` e mantieni `NOME` coerente con la Madre.

Per i pin cablati usa:

```text
PINA1
PINA2
PINA3
...
```

Aggiungi `PINB<n>` solo quando il segnale deve essere riportato sul lato opposto.

Per i valori dettagliati dei campi ATTDEF usa [Attributi e pinatura](../04-attributes-and-pinning.md).

### 3. Creare il DWG del simbolo

1. Seleziona tutti gli oggetti che devono appartenere al simbolo.
2. Digita:

   ```text
   MBLOCCO
   ```

3. Nella finestra del comando, alla voce **Origine**, seleziona `Oggetti`.
4. Seleziona il **punto base**.
5. Salva il file nella categoria corretta della libreria:

   ```text
   C:\SPAC Start 26\Librerie\Blk\_CUSTOM\<CATEGORIA>
   ```

6. Usa il nome previsto dalla convenzione della libreria.

### 4. Creare l'anteprima SLD

1. Apri direttamente il `.dwg` appena creato.
2. Centra il simbolo e regola lo zoom.
3. Digita:

   ```text
   _MSLIDE
   ```

4. Salva il file `.sld` nella stessa cartella del `.dwg`.
5. Usa obbligatoriamente lo stesso nome base:

   ```text
   NOME_SIMBOLO.dwg
   NOME_SIMBOLO.sld
   ```

### 5. Testare gli attributi

Inserisci il simbolo in un progetto di prova.

Per modificare gli attributi dell'istanza usa:

```text
EDITATT
```

Per aprire le proprietà usa:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

Se devi copiare proprietà da un elemento già corretto usa:

```text
CORRISPROP
```

### 6. Testare la pinatura

1. Inserisci il simbolo in un foglio di prova.
2. Disegna un filo verso ogni `PINA<n>`.
3. Verifica che il filo agganci esattamente il punto del pin.
4. Se esiste `PINB<n>`, verifica anche la connessione corrispondente.
5. Se non aggancia, non spostare casualmente il filo: usa il playbook [Diagnosticare pin non agganciato](diagnose-pin-not-snapping.md).

### 7. Associare il materiale, se previsto

1. Fai **doppio click sul simbolo**.
2. Nel riquadro **Materiali**, fai **tasto destro**.
3. Procedi con l'associazione del materiale prevista dalla libreria.
4. Verifica poi distinta/report per evitare duplicazioni.

Per il flusso completo usa [Associare materiali](material-association.md).

### 8. Aggiornare l'inventario

Registra almeno:

- nome simbolo;
- categoria;
- Madre/Figlio;
- presenza di `PINA/PINB`;
- materiale associabile;
- stato del test;
- eventuali note.

## Verifica finale

Il simbolo è pronto solo se:

- `MBLOCCO` ha generato il DWG nella categoria corretta;
- `_MSLIDE` ha generato l'SLD con stesso nome base;
- `EDITATT` permette di modificare gli attributi previsti;
- i fili agganciano i pin previsti;
- il materiale, se presente, compare correttamente nei report;
- l'inventario è aggiornato.

## Comandi usati in questo playbook

| Operazione | Comando |
|---|---|
| Inserire DWG/blocco | `_INSER` |
| Esplodere geometria | `ESPLODI` |
| Creare attributo | `ATTDEF` |
| Salvare DWG simbolo | `MBLOCCO` |
| Creare anteprima SLD | `_MSLIDE` |
| Modificare attributi istanza | `EDITATT` |
| Aprire proprietà | `PROPRIETA` / `CTRL+1` |
| Copiare proprietà | `CORRISPROP` |

## Collegamenti

- [Comandi e percorsi esatti](../command-reference.md)
- [Simboli custom](../03-custom-symbols.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
- [Checklist validazione simbolo](../10-symbol-validation-checklist.md)
