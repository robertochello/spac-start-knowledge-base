# Attributi e pinatura

Questa pagina documenta i campi `ATTDEF` verificati per i simboli custom SPAC Start 26.

## Comando da usare

```text
ATTDEF
```

## Attributo NOME

1. Digita `ATTDEF`.
2. Imposta:

| Campo | Valore |
|---|---|
| **Etichetta** | `NOME` |
| **Messaggio** | `Sigla componente` |
| **Default** | vuoto |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

3. Conferma.
4. Posiziona l'attributo nel punto in cui deve essere visualizzata la sigla.

## Attributo PRES per una Madre

1. Digita `ATTDEF`.
2. Imposta:

| Campo | Valore |
|---|---|
| **Etichetta** | `PRES` |
| **Default** | `M` |
| **Invisibile** | Sì |
| **Costante** | Sì |
| **Blocca posizione** | Sì |

`PRES = M` identifica il simbolo Madre.

Per un Figlio usa `PRES = F` e lo stesso `NOME` della Madre quando deve essere associato logicamente.

## Attributo PINA1

1. Digita `ATTDEF`.
2. Imposta:

| Campo | Valore |
|---|---|
| **Etichetta** | `PINA1` |
| **Default** | `1` |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

3. Posiziona l'attributo esattamente sul punto di connessione.

Per altri pin usa `PINA2`, `PINA3`, ecc.

## Attributo PINB1

Usa `PINB1` quando il segnale di `PINA1` deve essere riportato sul lato opposto.

1. Digita `ATTDEF`.
2. Imposta:

| Campo | Valore |
|---|---|
| **Etichetta** | `PINB1` |
| **Default** | `2` |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

3. Posiziona `PINB1` sul punto di uscita previsto.

Per le coppie successive usa `PINA2`/`PINB2`, `PINA3`/`PINB3`, ecc.

## Dimensione testo pin

Nei DWG dei BLK custom la grandezza testo standard dei pin è:

```text
1.5
```

## Modificare proprietà

Seleziona l'attributo e usa:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

Modifica le proprietà nella palette.

## Copiare proprietà da un attributo corretto

1. Digita:

   ```text
   CORRISPROP
   ```

2. seleziona l'attributo sorgente;
3. seleziona l'attributo destinazione;
4. premi **Invio**.

## Modificare attributi di un simbolo già inserito

Usa:

```text
EDITATT
```

Per un accessorio Figlio verifica:

```text
PRES = F
NOME = stesso NOME della Madre
```

Se SPAC avvisa che esiste già un dispositivo con lo stesso `NOME`, conferma quando la duplicazione è intenzionale per creare la relazione Madre/Figlio.

## Regola PINA/PINB

- solo `PINA<n>`: punto di connessione singolo;
- `PINA<n>` + `PINB<n>`: collegamento attraversa il simbolo;
- non aggiungere `PINB` se non serve realmente.

## Test pinatura

1. Configura la griglia con `_DSETTINGS → Snap e griglia`.
2. Inserisci il simbolo in un progetto prova.
3. Usa `EDITATT` per verificare gli attributi.
4. Collega un filo a ogni `PINA<n>`.
5. Se esiste `PINB<n>`, verifica anche il lato opposto.
6. Salva, chiudi e riapri.

Il test è superato solo se il collegamento aggancia realmente il pin e resta corretto dopo la riapertura.

## Tabella rapida

| Attributo | Default | Invisibile | Costante | Blocca posizione |
|---|---:|---|---|---|
| `NOME` | vuoto | No | No | Sì |
| `PRES` Madre | `M` | Sì | Sì | Sì |
| `PINA1` | `1` | No | No | Sì |
| `PINB1` | `2` | No | No | Sì |

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Creare un simbolo custom](playbooks/create-custom-symbol.md)
- [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md)
- [Gestire accessori e bobine](playbooks/manage-accessories-and-coils.md)
