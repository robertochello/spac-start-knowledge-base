# Attributi e pinatura

Questa sezione raccoglie le convenzioni operative sugli attributi principali dei simboli custom SPAC e sulla gestione della pinatura.

## Procedura pratica: creare gli attributi

Per creare gli attributi non usare indicazioni generiche: il comando verificato è:

```text
ATTDEF
```

### Creare `NOME`

1. Digitare `ATTDEF` nella riga comando.
2. Nella finestra di definizione attributo impostare:

| Campo | Valore |
|---|---|
| **Etichetta** | `NOME` |
| **Messaggio** | `Sigla componente` |

3. Confermare.
4. Posizionare l'attributo nel punto in cui deve comparire la sigla componente.

### Creare `PRES` per una Madre

1. Digitare `ATTDEF`.
2. Impostare:

| Campo | Valore |
|---|---|
| **Etichetta** | `PRES` |
| **Default** | `M` |

3. Confermare e posizionare l'attributo.

`PRES = M` identifica il simbolo Madre.

Per un simbolo Figlio usare `PRES = F` e mantenere `NOME` coerente con la Madre a cui deve essere associato.

### Creare `PINA1`

1. Digitare `ATTDEF`.
2. Impostare:

| Campo | Valore |
|---|---|
| **Etichetta** | `PINA1` |
| **Default** | `1` |
| **Invisibile** | No |
| **Costante** | No |
| **Blocca posizione** | Sì |

3. Posizionare l'attributo esattamente sul punto di connessione previsto.
4. Per i pin successivi usare `PINA2`, `PINA3`, ecc.

### Creare `PINB1`

Usare `PINB1` solo se il segnale presente su `PINA1` deve essere riportato sul lato opposto del simbolo.

1. Digitare `ATTDEF`.
2. Impostare l'etichetta `PINB1`.
3. Mantenere la stessa numerazione della relativa `PINA1`.
4. Posizionare il pin sul punto di uscita previsto.

Per le coppie successive usare `PINA2`/`PINB2`, `PINA3`/`PINB3`, ecc.

## Modificare attributi e proprietà

Per modificare le proprietà dell'oggetto selezionato usare:

```text
PROPRIETA
```

oppure:

```text
CTRL+1
```

Per copiare proprietà da un oggetto già configurato a un altro usare:

```text
CORRISPROP
```

Per modificare gli attributi di un'istanza già inserita usare:

```text
EDITATT
```

## In questa pagina impari

- quali attributi controllare nei simboli custom;
- come distinguere Madre, Figlio e relazione logica;
- quando usare solo `PINA<n>` e quando aggiungere `PINB<n>`;
- quali comandi digitare per creare e modificare gli attributi;
- quali test fare prima di validare il simbolo.

## Attributi principali

| Attributo | Uso operativo |
|---|---|
| `NOME` | Identificativo del componente |
| `PRES` | Ruolo del simbolo, ad esempio Madre o Figlio |
| `DESCRIZIONE` | Descrizione funzionale |
| `TIPO` | Tipo componente |
| `COSTRUTTORE` | Costruttore o marca |
| `QUADRO` | Quadro o area di appartenenza |

## Simbolo Madre

```text
PRES = M
```

La Madre identifica il componente principale nello schema.

## Simbolo Figlio

Regola operativa:

- `PRES = F`;
- stesso `NOME` della Madre quando deve essere associato logicamente;
- la relazione non deve dipendere dalla sola vicinanza grafica.

Esempi: contatti ausiliari, bobine, accessori ed elementi funzionali associati.

## Pinatura standard

Lo standard adottato è:

```text
PINA1
PINA2
PINA3
...
```

La presenza di `PINB<n>` con lo stesso numero indica che il segnale su `PINA<n>` viene riportato su `PINB<n>`.

| Ingresso | Uscita collegata | Significato |
|---|---|---|
| `PINA1` | `PINB1` | Segnale riportato dalla coppia 1 |
| `PINA2` | `PINB2` | Segnale riportato dalla coppia 2 |

## Quando usare solo PINA

Usare solo `PINA<n>` quando il simbolo rappresenta un singolo punto di connessione o non deve riportare il segnale in uscita.

## Quando usare PINA e PINB

Usare `PINA<n>` + `PINB<n>` quando il simbolo è attraversato da un collegamento o quando il segnale deve essere rappresentato in ingresso e uscita.

## Configurazione grafica dei pin

- testo pin standard nei BLK custom: `1.5`;
- posizione coerente con la griglia;
- attributi bloccati in posizione quando necessario;
- orientamento coerente con il significato elettrico.

## Test dopo il salvataggio

1. Inserire il simbolo in un progetto di prova.
2. Selezionarlo e usare `EDITATT` per verificare la modifica degli attributi.
3. Collegare un filo a ogni `PINA<n>` previsto.
4. Verificare l'aggancio reale al pin.
5. Se presente `PINB<n>`, verificare anche il lato di uscita corrispondente.
6. Controllare eventuali report o associazioni materiali.
7. Aggiornare l'inventario simboli custom.

!!! warning "Errore da evitare"

    Non aggiungere pin per tentativi. Se il filo non aggancia, verificare prima
    posizione del pin, etichetta `PINA/PINB`, griglia e struttura del simbolo.

## Riferimenti

- [Comandi e percorsi esatti](command-reference.md)
- [Simboli custom](03-custom-symbols.md)
- [Creare un simbolo custom](playbooks/create-custom-symbol.md)
- [Diagnosticare pin non agganciato](playbooks/diagnose-pin-not-snapping.md)
