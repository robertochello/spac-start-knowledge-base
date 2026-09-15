# Download

<div class="kb-hero kb-hero--compact" markdown>

<span class="kb-eyebrow">ARCHIVI PUBBLICI</span>

Scarica gli archivi destinati a **SPAC Start 26**. Materiali e cavi sono separati, versionati e sottoposti a controllo prima del deploy.

<div class="hero-actions" markdown>

[Archivi materiali](#archivi-materiali){ .md-button .md-button--primary }
[Archivi cavi](#archivi-cavi){ .md-button }

</div>

</div>

!!! warning "Pubblicazione controllata"

    Un file presente in questa pagina è pubblico. Prima del deploy il workflow esegue `scripts/audit_public_content.py`, che controlla i file testuali e i database SQLite alla ricerca di pattern sensibili e calcola il relativo SHA256.

    L'audit automatico **non sostituisce** il controllo umano di nomi cliente, codici commessa, proprietà intellettuale e diritti di redistribuzione.

## Archivi materiali

<div class="download-grid" markdown>

<div class="download-card" markdown>

<span class="download-kind">MATERIALI · ABB</span>

### ABB Materials

<span class="status-pill status-pill--available">Disponibile</span>

Archivio materiali ABB destinato alla consultazione/importazione nel workflow SPAC.

**File:** `ABB_Materials.db`  
**Dimensione:** circa 3,43 MB  
**Formato:** SQLite / archivio materiali  
**Stato privacy:** controllo automatico richiesto al deploy

[Scarica ABB_Materials.db](assets/downloads/materiali/ABB_Materials.db){ .md-button .md-button--primary }

</div>

<div class="download-card" markdown>

<span class="download-kind">MATERIALI · CUSTOM</span>

### Archivio materiali custom R01

<span class="status-pill status-pill--available">Disponibile</span>

Archivio materiali custom riutilizzabile, separato dagli archivi sorgente di commessa.

**File:** `archivio-materiali-custom-r01.db`  
**Versione:** R01  
**Dimensione:** circa 856 KB  
**Formato:** SQLite / archivio materiali  
**Stato privacy:** controllo automatico richiesto al deploy

[Scarica archivio R01](assets/downloads/materiali/archivio-materiali-custom-r01.db){ .md-button .md-button--primary }

</div>

</div>

## Archivi cavi

<div class="download-grid" markdown>

<div class="download-card download-card--pending" markdown>

<span class="download-kind">CAVI · DBCABLES</span>

### Archivio Cavi SPAC

<span class="status-pill status-pill--pending">In preparazione</span>

La cartella pubblica è già predisposta, ma al momento non contiene ancora un archivio cavi scaricabile.

**Cartella repository:**

```text
docs/assets/downloads/cavi/
```

Quando sarà disponibile, il file dovrà essere una copia **sanitizzata e verificata** di `DbCables.db`, preferibilmente versionata, ad esempio:

```text
dbcables-r01.db
```

oppure:

```text
archivio-cavi-dbcables-r01.zip
```

[Procedura DbCables](playbooks/update-dbcables-archive.md){ .md-button }

</div>

</div>

## Cosa deve essere controllato prima di pubblicare

| Controllo | Materiali | Cavi |
|---|---:|---:|
| file apribile | obbligatorio | obbligatorio |
| dati cliente/commessa assenti | obbligatorio | obbligatorio |
| email, IP, MAC, percorsi utente assenti | obbligatorio | obbligatorio |
| codici catalogo reali | obbligatorio | obbligatorio |
| duplicati controllati | obbligatorio | obbligatorio |
| test in SPAC | obbligatorio | obbligatorio |
| SHA256 calcolato | automatico al deploy | automatico al deploy |
| licenza/redistribuzione verificata | obbligatorio | obbligatorio |

## Regole per i file pubblici

I file scaricabili devono vivere esclusivamente nelle cartelle:

```text
docs/assets/downloads/materiali/
docs/assets/downloads/cavi/
```

Non pubblicare:

- file provenienti direttamente da commesse cliente;
- backup con nomi cliente o codici ordine;
- database contenenti note operative private;
- percorsi locali `C:\Users\...`;
- email, credenziali, IP/MAC reali;
- file vendor la cui licenza non consente la redistribuzione.

## Convenzione nomi

Preferire nomi brevi, senza spazi e con release quando applicabile:

```text
abb-materials-r01.db
archivio-materiali-custom-r01.db
dbcables-r01.db
archivio-cavi-dbcables-r01.zip
```

Per ogni nuova release aggiornare questa pagina e il changelog.

## Verifica tecnica

Il controllo automatico viene eseguito con:

```bash
python scripts/audit_public_content.py
```

Il controllo:

- scansiona i file testuali pubblici;
- apre i `.db` SQLite in sola lettura;
- analizza nomi di tabelle/colonne e valori testuali;
- non stampa nei log il valore sensibile trovato;
- calcola SHA256 dei file scaricabili;
- blocca il deploy in presenza di pattern ad alta confidenza.

## Collegamenti

- [Archivi materiali custom](21-material-archives.md)
- [Archivio Cavi DbCables](25-cable-archive-dbcables.md)
- [Back-check e controlli incrociati](26-back-check-controls.md)
- [Quality gates](14-quality-gates.md)
