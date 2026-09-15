# Guida operativa consolidata — SPAC Start 26

Questa pagina è un riferimento unico e **sanitizzato** della knowledge base.
Non contiene nomi cliente, codici commessa, nomi di elaborati reali, percorsi utente o altri riferimenti specifici a progetti.

Per il lavoro quotidiano sono preferibili le pagine operative dedicate, perché vengono mantenute con i click e i nomi esatti dell'interfaccia.

## Accessi principali

| Devo fare | Pagina |
|---|---|
| sapere esattamente cosa cliccare | [Comandi e click esatti](command-reference.md) |
| preparare un progetto | [Template progetto](16-project-template.md) |
| lavorare in unifilare | [Schema unifilare](17-unifilare.md) |
| lavorare in multifilare | [Schema multifilare](09-multifilare.md) |
| gestire rimandi e morsetti | [Rimandi, cross-reference e morsetti](06-cross-references-terminals.md) |
| creare un simbolo custom | [Creare un simbolo custom](playbooks/create-custom-symbol.md) |
| gestire materiali | [Archivi materiali](21-material-archives.md) |
| gestire cavi | [Archivio Cavi DbCables](25-cable-archive-dbcables.md) |
| scaricare archivi | [Download](downloads.md) |
| risolvere un problema | [Troubleshooting](07-troubleshooting.md) |

## Setup base

Percorso libreria custom standard:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM
```

Per aprire la libreria simboli:

```text
SP_XML_MENU
```

Per creare una scorciatoia:

```text
CUI
```

oppure:

```text
_CUI
```

Nella finestra **Personalizza interfaccia utente**:

```text
Elenco comandi → Nuovo comando
```

Macro esempio:

```text
^C^CSP_XML_MENU;
```

Poi:

```text
Tasti di scelta rapida → Tasti di scelta rapida
```

## Pagine standard e cartigli

Per inserire una pagina standard mantenendo il collegamento al DWG sorgente:

```text
Modifica/Inserisci → Riferimento DWG
→ Tipo di percorso: Percorso completo
→ OK
```

Per la legenda:

```text
Fogli → Legenda Fogli → Disegna → foglio vuoto → OK
```

Per immagini:

```text
IMMAGINI
```

Ripristino path:

```text
Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso
```

Bordo immagini:

```text
IMAGEFRAME
0
```

## Schema unifilare

Aprire:

```text
UNIFILARE → Disegno Unifilare
```

Campi principali:

- **Scelta Circuiti memorizzati**;
- **Tipo quadro**;
- **Monofase / Trifase**;
- **Composizione/Tipologia**;
- **Anteprima**;
- **Scelta del quadro**.

Per associare un materiale a un livello:

```text
tasto destro tabella materiali → Avvio DbCenter
```

Per snap e griglia:

```text
_DSETTINGS → Snap e griglia
```

Per numerare fili normali:

```text
SPAC → Numera Fili
```

Per l'identificazione alimentazioni:

```text
Identificatore Linee → tipo linea → OK
```

Per fasi e neutro:

```text
Numerazione Fili → Numerazione Fili Unifilare
```

## Rimandi e cross-reference

Creazione rimando:

```text
Dynamic Coll / Dynamic Alim
→ numero fili
→ traccia collegamento
→ Invio
→ Rimandi di arrivo / partenza / arrivo e partenza
→ nome filo
→ Ok
```

Lista rimandi:

```text
Numerazione fili → Lista numeri usati
→ Vedi solo i Rimandi
→ Scansiona i Multifogli
```

Aggiornamento cross-reference:

```text
UTIL → Cross Reference
→ Rimandi
→ Cross
→ Ok - Aggiorna
```

## Multifilare e morsetti

Aprire gestione morsetti:

```text
SPINSMOR
```

oppure **Inser Morsetti**.

Nuova morsettiera:

```text
Inser Morsetti
→ tasto destro su Elenco Quadri
→ Nuova morsettiera
```

Nuovo morsetto:

```text
morsettiera
→ tipo morsetto
→ Anteprima
→ Ok - Nuovo
→ clic filo
→ Invio
```

Campi rappresentazione:

| Campo | Significato |
|---|---|
| `NumI` | numero filo ingresso |
| `NumO` | numero filo uscita |
| `NumM` | numero morsetto |

Per eliminare numerazioni:

```text
SPAC → Utility Fili → Elimina numerazione
```

oppure:

```text
DEL_NUMF
```

## Simboli custom

Importazione DWG:

```text
_INSER
```

Pulizia geometria:

```text
ESPLODI
```

Standard grafico:

- Layer `0`;
- Colore `DaBlocco`;
- Tipo linea `DaBlocco`;
- Spessore `DaBlocco`.

Creazione attributi:

```text
ATTDEF
```

Attributi principali:

```text
NOME
PRES
PINA1, PINA2, ...
PINB1, PINB2, ...
```

Madre:

```text
PRES = M
```

Figlio:

```text
PRES = F
```

Quando il Figlio è associato alla Madre deve usare lo stesso `NOME` previsto dalla relazione.

Salvataggio DWG:

```text
MBLOCCO
→ Origine: Oggetti
→ punto base
→ Destinazione: Nome e percorso del file
→ Unità inser.: Senza unità
```

Anteprima:

```text
_MSLIDE
```

Regola:

```text
NOME_SIMBOLO.dwg
NOME_SIMBOLO.sld
```

## Materiali

Sul simbolo intelligente:

```text
doppio click
→ Materiali
→ tasto destro
→ Avvio Archivio Materiali (DbCenter)
→ seleziona materiale
→ conferma
```

Dopo l'associazione verificare distinta/report.

## Archivio Cavi

Il database avanzato è:

```text
DbCables.db
```

La procedura di aggiornamento deve sempre prevedere:

1. backup;
2. sostituzione controllata;
3. avvio SPAC;
4. **Allinea la versione delle librerie** se richiesto;
5. riapertura;
6. test su cavo reale;
7. rollback disponibile.

Procedura completa: [Aggiornare Archivio Cavi DbCables](playbooks/update-dbcables-archive.md).

## Layer e residui

Layer apparentemente vuoto:

```text
PURGE → Trova elementi non eliminabili
```

Oggetti diretti:

```text
QSELECT → filtro Layer
```

Residui dentro blocco:

```text
BEDIT → modifica blocco → salva → PURGE
```

Non proporre `LAYISO` o `LAYWALK` come soluzione nell'ambiente SPAC Start 26 verificato.

## Download pubblici

Gli archivi pubblici devono stare solo in:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

Ogni file destinato al download deve essere:

- generico e riutilizzabile;
- privo di dati cliente/commessa;
- controllato prima del deploy;
- documentato nella pagina [Download](downloads.md);
- pubblicabile anche dal punto di vista delle licenze e dei diritti di redistribuzione.

Il workflow di pubblicazione esegue l'audit automatico `scripts/audit_public_content.py` prima della build MkDocs.

## Regola privacy

Non inserire nella documentazione pubblica:

- nomi cliente;
- codici commessa o ordine;
- nomi di elaborati reali;
- indirizzi IP/MAC di impianti reali;
- email o credenziali;
- percorsi `C:\Users\...` o home directory personali;
- screenshot con dati identificativi;
- file di progetto cliente;
- database non sanitizzati.

Gli esempi devono essere generici.

## Regola editoriale

Ogni procedura deve preferire questa struttura:

```text
Dove cliccare / cosa digitare
→ cosa impostare
→ risultato atteso
→ diagnosi se KO
```

Se un nome non è stato verificato, indicare **Da verificare** nel punto preciso.
