# Playbook — Creare un simbolo custom

## Obiettivo

Creare un simbolo custom riutilizzabile in SPAC Start 26 con comandi e campi verificati.

## 1. Importare la geometria

Per un DWG esterno:

```text
_INSER
```

Nella finestra di inserimento puoi usare:

- **Disegno corrente**;
- **Recenti**;
- **Preferiti**;
- **Librerie**;
- ricerca/sfoglia.

Se il DWG contiene attributi, SPAC/AutoCAD può richiederne la compilazione dalla riga comando.

Per partire da un simbolo SPAC esistente, apri la libreria con:

```text
SP_XML_MENU
```

## 2. Pulire e normalizzare

Se devi modificare le singole entità:

```text
ESPLODI
```

Poi:

- elimina geometrie/testi inutili;
- Layer `0`;
- Colore `DaBlocco`;
- Tipo linea `DaBlocco`;
- Spessore `DaBlocco`.

## 3. Creare gli attributi

Usa:

```text
ATTDEF
```

Per Madre:

```text
NOME
PRES = M
```

Per Figlio:

```text
PRES = F
NOME = stesso NOME della Madre
```

Per pin:

```text
PINA1
PINB1
```

Per i campi esatti usa [Attributi e pinatura](../04-attributes-and-pinning.md).

## 4. Salvare il DWG del simbolo

1. seleziona tutti gli oggetti;
2. digita:

   ```text
   MBLOCCO
   ```

3. in **Origine** seleziona `Oggetti`;
4. seleziona il **punto base**;
5. in **Destinazione → Nome e percorso del file** scegli la categoria `_CUSTOM` corretta;
6. assegna il nome secondo la convenzione;
7. in **Unità inser.** lascia:

   ```text
   Senza unità
   ```

8. salva il DWG.

Per un simbolo puramente grafico il punto base può essere il centro grafico; per un simbolo cablato sceglilo in modo coerente con l'inserimento/pinatura.

## 5. Creare l'anteprima SLD

1. apri direttamente il DWG appena creato;
2. centra il disegno e regola lo zoom;
3. digita:

   ```text
   _MSLIDE
   ```

4. salva nella stessa cartella del DWG;
5. usa lo stesso nome base;
6. chiudi il DWG;
7. verifica nella libreria BLK che simbolo e slide siano visibili.

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

## 6. Testare attributi

Inserisci il simbolo in un progetto prova.

Usa:

```text
EDITATT
```

per verificare gli attributi dell'istanza.

Per proprietà:

```text
PROPRIETA
```

oppure `CTRL+1`.

Per copiare proprietà:

```text
CORRISPROP
```

Sequenza: attributo sorgente → attributo destinazione → **Invio**.

## 7. Testare pinatura

1. `_DSETTINGS → Snap e griglia`;
2. inserisci il simbolo;
3. collega un filo a ogni `PINA<n>`;
4. verifica eventuale `PINB<n>`;
5. salva, chiudi e riapri.

Se il filo non aggancia, usa [Diagnosticare pin non agganciato](diagnose-pin-not-snapping.md).

## 8. Associare materiale

1. doppio click sul simbolo;
2. riquadro **Materiali**;
3. tasto destro;
4. **Avvio Archivio Materiali (DbCenter)**;
5. scegli il materiale;
6. conferma;
7. verifica distinta/report.

## Verifica finale

Il simbolo è pronto solo se:

- DWG salvato con `MBLOCCO` nella categoria corretta;
- **Unità inser. = Senza unità**;
- SLD creato con `_MSLIDE` e stesso nome base;
- libreria BLK mostra correttamente il simbolo;
- `EDITATT` modifica gli attributi previsti;
- pin agganciano;
- materiale/report coerenti;
- inventario aggiornato.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
- [Validare un simbolo](validate-custom-symbol.md)
