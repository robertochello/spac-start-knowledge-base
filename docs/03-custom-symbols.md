# Simboli custom

Questa pagina è la panoramica operativa. Per il passo-passo completo usa [Creare un simbolo custom](playbooks/create-custom-symbol.md).

## Workflow

```text
_INSER / SP_XML_MENU
        ↓
     ESPLODI
        ↓
Layer 0 + DaBlocco
        ↓
      ATTDEF
        ↓
     MBLOCCO
        ↓
     _MSLIDE
        ↓
      EDITATT
        ↓
Test pin/materiali
```

## Preparare la geometria

DWG esterno:

```text
_INSER
```

Simbolo SPAC esistente:

```text
SP_XML_MENU
```

Per modificare le singole entità:

```text
ESPLODI
```

Normalizzazione:

```text
Layer 0
Colore: DaBlocco
Tipo linea: DaBlocco
Spessore: DaBlocco
```

## Attributi

```text
ATTDEF
```

Regole principali:

```text
Madre  → PRES = M
Figlio → PRES = F
Figlio → NOME uguale alla Madre
```

Pin:

```text
PINA1, PINA2, ...
PINB1, PINB2, ... solo quando serve riportare il segnale
```

I valori esatti dei campi sono in [Attributi e pinatura](04-attributes-and-pinning.md).

## Salvare il simbolo DWG

1. seleziona gli oggetti;
2. `MBLOCCO`;
3. **Origine → Oggetti**;
4. seleziona punto base;
5. **Destinazione → Nome e percorso del file**;
6. scegli `C:\SPAC Start 26\Librerie\Blk\_CUSTOM\<CATEGORIA>`;
7. **Unità inser. → Senza unità**;
8. salva.

## Creare anteprima

1. apri il DWG;
2. centra/zoom;
3. `_MSLIDE`;
4. stessa cartella;
5. stesso nome base.

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

Verifica poi che simbolo e slide siano visibili nella libreria BLK.

## Modificare un'istanza

Attributi:

```text
EDITATT
```

Proprietà:

```text
PROPRIETA
CTRL+1
```

Copia proprietà:

```text
CORRISPROP
```

## Materiale

```text
doppio click simbolo
→ Materiali
→ tasto destro
→ Avvio Archivio Materiali (DbCenter)
```

Poi seleziona il materiale e verifica distinta/report.

## Test pin

1. `_DSETTINGS → Snap e griglia`;
2. inserisci simbolo in progetto prova;
3. collega filo a `PINA<n>`;
4. verifica `PINB<n>` se presente;
5. salva/riapri.

## Definition of Done simbolo

- geometria pulita;
- Layer 0 + DaBlocco;
- attributi corretti;
- `MBLOCCO` con **Unità inser.: Senza unità**;
- DWG/SLD stesso nome base;
- simbolo visibile in libreria;
- `EDITATT` funzionante;
- pin testati;
- materiale testato se previsto;
- inventario aggiornato.

## Collegamenti

- [Creare un simbolo custom](playbooks/create-custom-symbol.md)
- [Attributi e pinatura](04-attributes-and-pinning.md)
- [Comandi e click esatti](command-reference.md)
- [Validare un simbolo](playbooks/validate-custom-symbol.md)
