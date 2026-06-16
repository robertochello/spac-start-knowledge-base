# Download

Questa pagina raccoglie i file scaricabili collegati alla knowledge base.

## Regola generale

Pubblicare solo file generici, riutilizzabili e privi di dati sensibili.

Prima di aggiungere un file:

- verificare che non contenga dati cliente o commessa;
- verificare che il contenuto sia coerente con gli standard della guida;
- indicare versione, data e stato;
- aggiornare questa pagina;
- aggiornare il changelog se il file diventa riferimento stabile.

## Cartelle pubbliche

I file devono essere inseriti nelle cartelle:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

MkDocs pubblica queste cartelle nel sito statico. I link vanno quindi scritti con percorso relativo da questa pagina.

## File disponibili

| Area | File | Stato | Note |
|---|---|---|---|
| Materiali | [ABB_Materials.db](assets/downloads/materiali/ABB_Materials.db) | Pubblicato | Archivio materiali ABB |
| Materiali | [archivio-materiali-custom-r01.db](assets/downloads/materiali/archivio-materiali-custom-r01.db) | Pubblicato | Archivio materiali custom |
| Cavi | Da caricare in `assets/downloads/cavi/` | Non pubblicato | Archivio cavi o `DbCables.db` sanitizzato/verificato |

## Template riga download

Quando il file è disponibile, sostituire la riga corrispondente con un link diretto.

Esempio:

```text
Area: Materiali
File: archivio-materiali-custom-r01.zip
Percorso: assets/downloads/materiali/archivio-materiali-custom-r01.zip
Stato: Pubblicato
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
- eventuale archivio compresso testato;
- versione indicata nel nome o nelle note;
- link provato dopo build del sito.

## Collegamenti

- [Archivi materiali custom](21-material-archives.md)
- [Archivio Cavi DbCables](25-cable-archive-dbcables.md)
- [Back-check e controlli incrociati](26-back-check-controls.md)
- [Quality gates](14-quality-gates.md)
