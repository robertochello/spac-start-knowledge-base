# Libreria custom

Questa sezione raccoglie le regole operative per installare, organizzare e mantenere la libreria custom SPAC.

## Obiettivo

Mantenere la libreria ordinata, stabile e facilmente consultabile nel tempo.

## Struttura generale

La libreria custom deve essere organizzata in una cartella dedicata `_CUSTOM` all'interno della libreria BLK di SPAC Start.

La cartella deve contenere categorie funzionali stabili e una sezione documentale separata.

## Installazione operativa

Procedura consigliata:

1. Chiudere SPAC Start prima di intervenire sulla libreria.
2. Copiare la cartella `_CUSTOM` fornita.
3. Inserirla nella libreria BLK del software.
4. Verificare che siano presenti categorie e documentazione.
5. Riavviare SPAC Start.
6. Verificare la visibilità dei simboli nella libreria.

Se la cartella è già presente, verificare il contenuto prima di sovrascrivere file esistenti.

## Categorie libreria

| Categoria | Utilizzo |
|---|---|
| `00_SIMBOLI_GRAFICI` | Simboli grafici generici e rappresentazioni senza logica elettrica complessa |
| `01_ALIMENTATORI` | Alimentatori, trasformatori, UPS, sorgenti e dispositivi di alimentazione |
| `02_PROTEZIONI` | Protezioni non classificate come interruttori o sezionatori |
| `03_RELE_INTERFACCE` | Relè, interfacce, moduli di isolamento e dispositivi di appoggio ai comandi |
| `04_MODULI_IO_PLC` | PLC, moduli I/O, moduli remoti e dispositivi di automazione |
| `05_SENSORI` | Sensori, finecorsa, proximity, pressostati, termostati e dispositivi di rilevamento |
| `06_ATTUATORI_DRIVE` | Attuatori, motori, inverter, drive, elettrovalvole e dispositivi di movimento |
| `07_COMUNICAZIONE` | Switch, gateway, router, convertitori e dispositivi di comunicazione industriale |
| `08_MORSETTI_CONNETTORI` | Morsetti, connettori, spine, prese e punti di connessione |
| `09_STRUMENTAZIONE` | Multimetri, strumenti di misura, analizzatori e strumenti da pannello |
| `10_INTERRUTTORI` | Interruttori, magnetotermici, differenziali, sezionatori e dispositivi affini |
| `99_GENERICI` | Simboli provvisori o non ancora classificati |
| `Documentazione` | README, inventari e documenti di supporto alla libreria |

## Regole di classificazione

- I simboli che iniziano con `INT_` devono stare in `10_INTERRUTTORI`.
- La strumentazione deve stare in `09_STRUMENTAZIONE`.
- Le protezioni non riconducibili a interruttori o sezionatori possono stare in `02_PROTEZIONI`.
- `99_GENERICI` deve essere usata solo come area temporanea.

## Inventario

L'inventario completo dei simboli custom deve restare separato dal README e deve essere gestito con il template dedicato.

## Checklist manutenzione libreria

Prima di aggiungere un simbolo alla libreria:

- verificare categoria corretta;
- verificare nome secondo convenzione;
- verificare file DWG e anteprima;
- verificare attributi se simbolo intelligente;
- verificare eventuale pinatura;
- aggiornare inventario;
- aggiornare changelog se il simbolo diventa standard.
