# Download

Questa pagina raccoglie i file scaricabili collegati alla knowledge base.

## Regola generale

Pubblicare solo file generici, riutilizzabili e privi di dati sensibili.

Prima di aggiungere un file:

- verificare che non contenga dati cliente o commessa;
- verificare che il contenuto sia coerente con gli standard della guida;
- indicare versione, data e stato;
- registrare provenienza o criterio di generazione del file;
- registrare un hash SHA256 per i file binari pubblicati;
- aggiornare questa pagina;
- aggiornare il changelog se il file diventa riferimento stabile.

## Cartelle pubbliche

I file devono essere inseriti nelle cartelle:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

MkDocs pubblica queste cartelle nel sito statico. I link vanno quindi scritti con percorso relativo da questa pagina.

## Metadati minimi

Ogni download pubblicato deve essere tracciabile con:

- nome file;
- area di appartenenza;
- versione o release;
- data di pubblicazione o aggiornamento;
- stato;
- hash SHA256, se il file è binario;
- nota di sanitizzazione;
- pagina o procedura collegata.

## File disponibili

| Area | File | Versione/release | Stato | Note |
|---|---|---|---|---|
| Materiali | [ABB_Materials.db](assets/downloads/materiali/ABB_Materials.db) | Da documentare | Pubblicato | Archivio materiali ABB; completare metadati di tracciabilità |
| Materiali | [archivio-materiali-custom-r01.db](assets/downloads/materiali/archivio-materiali-custom-r01.db) | R01 | Pubblicato | Archivio materiali custom; completare metadati di tracciabilità |
| Cavi | Da caricare in `assets/downloads/cavi/` | Non applicabile | Non pubblicato | Archivio cavi o `DbCables.db` sanitizzato/verificato |

## Template riga download

Quando il file è disponibile, sostituire la riga corrispondente con un link diretto.

Esempio:

```text
Area: Materiali
File: archivio-materiali-custom-r01.zip
Percorso: assets/downloads/materiali/archivio-materiali-custom-r01.zip
Versione/release: R01
Data: AAAA-MM-GG
Stato: Pubblicato
SHA256: <hash>
Note: Release verificata
```

## Convenzione nomi file

Usare nomi minuscoli, senza spazi e con versione.

Esempi:

```text
archivio-materiali-custom-r01.zip
archivio-cavi-dbcables-r01.zip
dbcables-r01.zip
```

## Verifica prima della pubblicazione

- file apribile;
- nome coerente;
- contenuto sanitizzato;
- hash SHA256 registrato per file binari;
- origine o criterio di generazione documentato;
- per archivi materiali, codici catalogo reali e senza iniziali personali;
- per archivi materiali, almeno un record testato in associazione e report;
- eventuale archivio compresso testato;
- versione indicata nel nome o nelle note;
- link provato dopo build del sito.

## Collegamenti

- [Archivi materiali custom](21-material-archives.md)
- [Archivio Cavi DbCables](25-cable-archive-dbcables.md)
- [Back-check e controlli incrociati](26-back-check-controls.md)
- [Quality gates](14-quality-gates.md)
