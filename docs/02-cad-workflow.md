# Workflow CAD 2D

Comandi CAD verificati e usati nel workflow SPAC Start 26.

## Standard grafico per simboli/blocchi

```text
Layer 0
Colore: DaBlocco
Tipo linea: DaBlocco
Spessore linea: DaBlocco
```

## Importare DWG o blocco

```text
_INSER
```

Nella finestra puoi usare:

- **Disegno corrente**;
- **Recenti**;
- **Preferiti**;
- **Librerie**;
- ricerca/sfoglia.

Dopo l'inserimento verifica scala e punto di inserimento.

## Esplodere

```text
ESPLODI
```

Usalo solo quando devi modificare le singole entità.

## Tratteggio pieno

1. **Disegna → Tratteggio**;
2. usa **I** per aprire le impostazioni;
3. finestra **Tratteggio e sfumatura**;
4. **Modello → SOLID**;
5. scegli colore;
6. seleziona area.

## Creare un DWG riutilizzabile

1. pulisci la geometria;
2. Layer `0`;
3. proprietà `DaBlocco`;
4. seleziona oggetti;
5. digita `MBLOCCO`;
6. **Origine → Oggetti**;
7. seleziona punto base;
8. **Destinazione → Nome e percorso del file**;
9. scegli il percorso;
10. **Unità inser. → Senza unità**;
11. salva.

Per la libreria custom usa:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM\<CATEGORIA>
```

## Creare anteprima SLD

1. apri il DWG;
2. centra e regola zoom;
3. `_MSLIDE`;
4. salva nella stessa cartella;
5. stesso nome base del DWG.

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

## Verificare proprietà

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

Sequenza: sorgente → destinazione → **Invio**.

## Disegno fuori scala

Procedura concettuale verificata:

1. misura una quota nota;
2. confrontala con il valore reale;
3. calcola il fattore;
4. scala l'insieme;
5. rimisura una seconda quota.

!!! warning "Comando scala: Da verificare"

    Il nome/comportamento esatto del comando di scala nell'ambiente SPAC Start 26 non è ancora consolidato nella knowledge base. Non viene inventato.

## Test finale

- `_INSER` riuscito;
- scala verificata;
- Layer 0;
- proprietà DaBlocco;
- `MBLOCCO` con **Origine: Oggetti**;
- **Unità inser.: Senza unità**;
- SLD coerente se previsto;
- nessuna entità residua/invisibile indesiderata.

## Riferimenti

- [Comandi e click esatti](command-reference.md)
- [Creare un simbolo custom](playbooks/create-custom-symbol.md)
