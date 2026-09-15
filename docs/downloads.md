# Download

Scarica da qui gli archivi da usare con SPAC.

## Materiali

<div class="download-grid" markdown>

<div class="download-card" markdown>

### ABB Materials

<span class="status-pill status-pill--available">Disponibile</span>

**File:** `ABB_Materials.db`  
**Dimensione:** circa 3,43 MB

[Scarica ABB_Materials.db](assets/downloads/materiali/ABB_Materials.db){ .md-button .md-button--primary }

</div>

<div class="download-card" markdown>

### Materiali custom R01

<span class="status-pill status-pill--available">Disponibile</span>

**File:** `archivio-materiali-custom-r01.db`  
**Versione:** R01  
**Dimensione:** circa 856 KB

[Scarica archivio R01](assets/downloads/materiali/archivio-materiali-custom-r01.db){ .md-button .md-button--primary }

</div>

</div>

## Cavi

<div class="download-grid" markdown>

<div class="download-card download-card--pending" markdown>

### Archivio Cavi SPAC

<span class="status-pill status-pill--pending">Non ancora disponibile</span>

Qui verrà pubblicato l'archivio `DbCables.db` quando sarà pronto e verificato.

[Come si aggiorna DbCables](playbooks/update-dbcables-archive.md){ .md-button }

</div>

</div>

## Prima di usare un archivio

1. Fai una copia del database che stai usando adesso.
2. Scarica il nuovo archivio.
3. Segui la procedura relativa a materiali o cavi.
4. Provalo prima su un progetto non critico.

!!! warning

    I file di questa pagina sono pubblici. Non devono contenere dati cliente, commessa, email, IP, password o altri dati privati.

??? info "Controlli tecnici della pubblicazione"

    Prima del deploy viene eseguito automaticamente:

    ```text
    python scripts/audit_public_content.py
    ```

    Il controllo cerca pattern sensibili nei file testuali e nei database SQLite e calcola lo SHA256 dei file scaricabili.

## Guide collegate

- [Archivi materiali](21-material-archives.md)
- [Archivio cavi DbCables](25-cable-archive-dbcables.md)
- [Associare un materiale](playbooks/material-association.md)
- [Aggiornare DbCables](playbooks/update-dbcables-archive.md)
