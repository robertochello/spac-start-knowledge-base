# Workflow CAD 2D

SPAC Start può essere usato anche per disegno CAD 2D quando il contenuto non è direttamente elettrico. Questa pagina riporta i comandi già verificati per le operazioni ricorrenti.

## Layer standard

Per file CAD/DXF/DWG destinati a SPAC, usa:

```text
Layer 0
```

Per geometria destinata a diventare blocco/simbolo usa inoltre:

- **Colore**: `DaBlocco`;
- **Tipo linea**: `DaBlocco`;
- **Spessore linea**: `DaBlocco`.

## Importare un DWG o un blocco

Nella riga comando digita:

```text
_INSER
```

Poi seleziona il file/blocco da inserire e verifica scala e punto di inserimento.

## Esplodere una geometria importata

Se devi modificare le singole entità usa:

```text
ESPLODI
```

Non esplodere automaticamente ogni oggetto: fallo solo quando serve per pulire o modificare la geometria.

## Riempire una forma con colore pieno

Percorso verificato:

1. apri il menu **Disegna**;
2. clicca **Tratteggio**;
3. nella barra dei comandi clicca/digita **I** per aprire le impostazioni;
4. nella finestra **Tratteggio e sfumatura**, alla voce **Modello**, seleziona:

   ```text
   SOLID
   ```

5. scegli il colore;
6. conferma;
7. seleziona l'area o la forma da riempire.

## Creare un blocco DWG riutilizzabile

1. Pulisci la geometria.
2. Porta tutto su **Layer 0**.
3. Imposta **DaBlocco** per colore/tipo linea/spessore quando previsto.
4. Seleziona tutti gli oggetti del futuro blocco.
5. Digita:

   ```text
   MBLOCCO
   ```

6. In **Origine**, seleziona:

   ```text
   Oggetti
   ```

7. Seleziona il punto base.
8. Salva il DWG nel percorso previsto.

Se il blocco è un simbolo della libreria custom, usa una categoria sotto:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM
```

## Creare l'anteprima del blocco/simbolo

Per un simbolo della libreria:

1. apri direttamente il DWG;
2. centra il disegno;
3. regola lo zoom;
4. digita:

   ```text
   _MSLIDE
   ```

5. salva la slide nella stessa cartella del DWG;
6. usa lo stesso nome base per `.dwg` e `.sld`.

## Disegni fuori scala

Quando un disegno copiato/importato risulta fuori scala:

1. identifica una quota reale nota;
2. misura la quota attuale;
3. calcola il fattore di scala;
4. applica la scalatura all'insieme selezionato;
5. misura di nuovo la quota nota.

!!! warning "Comando di scala"

    In questa knowledge base non è ancora consolidato il nome/comportamento esatto del comando di scala usato nell'ambiente SPAC Start 26. Finché non viene verificato direttamente, non viene indicato un comando ipotetico.

## Test prima del riuso

- apri/inserisci il file con `_INSER`;
- verifica scala;
- verifica Layer 0;
- verifica eventuali riferimenti esterni;
- controlla che non ci siano entità invisibili o inutili;
- se è un simbolo, verifica DWG + SLD.

## Riferimenti

- [Comandi e click esatti](command-reference.md)
- [Simboli custom](03-custom-symbols.md)
- [Creare un simbolo custom](playbooks/create-custom-symbol.md)
