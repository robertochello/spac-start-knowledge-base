# Creare un simbolo custom

Segui questi passaggi nell'ordine.

## 1. Inserisci il disegno

Se parti da un DWG:

```text
_INSER
```

Se parti da un simbolo SPAC già esistente:

```text
SP_XML_MENU
```

## 2. Pulisci il disegno

Se devi modificare le singole entità:

```text
ESPLODI
```

Poi controlla:

- Layer = `0`;
- Colore = `DaBlocco`;
- Tipo linea = `DaBlocco`;
- Spessore = `DaBlocco`.

Elimina testi o linee che non servono.

## 3. Crea gli attributi

Digita:

```text
ATTDEF
```

Per un simbolo Madre:

```text
NOME
PRES = M
```

Per un simbolo Figlio:

```text
PRES = F
NOME = stesso NOME della Madre
```

Per i pin usa:

```text
PINA1
PINB1
```

Per i valori esatti dei campi apri [Attributi e pin](../04-attributes-and-pinning.md).

## 4. Salva il simbolo

1. Seleziona tutti gli oggetti.
2. Digita `MBLOCCO`.
3. In **Origine** scegli **Oggetti**.
4. Scegli il **punto base**.
5. In **Destinazione → Nome e percorso del file** scegli la cartella `_CUSTOM` corretta.
6. Inserisci il nome del simbolo.
7. In **Unità inser.** scegli **Senza unità**.
8. Salva.

## 5. Crea l'anteprima

1. Apri il DWG appena salvato.
2. Centra bene il simbolo.
3. Digita:

   ```text
   _MSLIDE
   ```

4. Salva nella stessa cartella del DWG.
5. Usa lo stesso nome base.

Esempio:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

## 6. Prova il simbolo

Inseriscilo in un progetto di prova.

Per controllare gli attributi usa:

```text
EDITATT
```

Per le proprietà usa:

```text
PROPRIETA
```

oppure `CTRL+1`.

## 7. Prova i pin

1. Inserisci il simbolo.
2. Collega un filo a ogni `PINA`.
3. Se hai `PINB`, controlla che il collegamento continui correttamente.
4. Salva e riapri il progetto.

Se il filo non si aggancia, apri [Pin non agganciato](diagnose-pin-not-snapping.md).

## 8. Associa il materiale

1. Doppio click sul simbolo.
2. Apri **Materiali**.
3. Tasto destro.
4. Clicca **Avvio Archivio Materiali (DbCenter)**.
5. Scegli il materiale.
6. Conferma.
7. Controlla la distinta.

## Controllo finale

Il simbolo è pronto se:

- il DWG è nella cartella giusta;
- **Unità inser. = Senza unità**;
- esiste anche il file `.sld`;
- gli attributi funzionano;
- i pin agganciano;
- il materiale compare correttamente.
