<div class="kb-hero" markdown>

<span class="kb-eyebrow">SPAC START 26 · KNOWLEDGE BASE</span>

# Lavora in SPAC senza cercare a caso

Procedure operative con **comandi reali, nomi esatti delle finestre e percorsi da cliccare**. Parti dall'attività che devi svolgere oppure dal problema che hai davanti.

<div class="hero-actions" markdown>

[Comandi e click esatti](command-reference.md){ .md-button .md-button--primary }
[Scarica archivi](downloads.md){ .md-button }
[Diagnosi rapida](07-troubleshooting.md){ .md-button }

</div>

</div>

<div class="home-grid" markdown>

[**Comandi e click esatti**<br>Cheat sheet da tenere aperto mentre lavori: menu, comandi, pulsanti e valori.](command-reference.md){ .home-card }

[**Prepara un progetto**<br>Template, pagine standard, cartiglio, riferimenti DWG e libreria custom.](16-project-template.md){ .home-card }

[**Schema unifilare**<br>Disegno Unifilare, ingresso linea, materiali, identificatori e numerazione.](17-unifilare.md){ .home-card }

[**Schema multifilare**<br>Rimandi, cross-reference, morsetti, accessori e fili.](09-multifilare.md){ .home-card }

[**Crea o correggi un simbolo**<br>DWG, attributi, pinatura, punto base, SLD, materiale e validazione.](playbooks/create-custom-symbol.md){ .home-card }

[**Scarica archivi**<br>Archivio materiali ABB, archivio custom e futura area DbCables.](downloads.md){ .home-card }

[**Risolvi un problema**<br>Parti dal sintomo: pin, rimandi, morsetti, layer, immagini, materiali o cavi.](07-troubleshooting.md){ .home-card }

[**Non sai dove andare?**<br>Apri l'indice per attività e scegli il caso più vicino a quello che devi fare.](00-how-to-use.md){ .home-card }

</div>

!!! important "Come è scritta questa guida"

    Quando un nome è stato verificato in SPAC Start 26 viene riportato **esattamente come compare nell'interfaccia**. Se non è stato verificato, il punto è marcato **Da verificare**: non vengono inventati comandi o pulsanti.

## Operazioni frequenti

| Voglio... | Fai esattamente... |
|---|---|
| aprire la libreria simboli | `SP_XML_MENU` |
| aprire Disegno Unifilare | **UNIFILARE → Disegno Unifilare** |
| inserire una pagina standard | **Modifica/Inserisci → Riferimento DWG → Tipo di percorso: Percorso completo → OK** |
| creare la legenda fogli | **Fogli → Legenda Fogli → Disegna → foglio vuoto → OK** |
| numerare fili | **SPAC → Numera Fili** |
| vedere solo i rimandi | **Numerazione fili → Lista numeri usati → Vedi solo i Rimandi → Scansiona i Multifogli** |
| aggiornare cross-reference | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** |
| inserire un morsetto | `SPINSMOR` → morsettiera → tipo → **Anteprima → Ok - Nuovo → clic filo → Invio** |
| creare un attributo | `ATTDEF` |
| salvare un simbolo | `MBLOCCO` → **Origine: Oggetti** → punto base → **Destinazione** → **Unità inser.: Senza unità** |
| creare anteprima simbolo | `_MSLIDE` |
| associare materiale | doppio click → **Materiali → tasto destro → Avvio Archivio Materiali (DbCenter)** |
| capire perché un layer non si elimina | `PURGE → Trova elementi non eliminabili` |
| ripristinare un'immagine | **Modifica/Inserisci → Gestioni immagini → Sfoglia → Salva percorso** |

Per l'elenco completo usa **[Comandi e click esatti](command-reference.md)**.

## Se hai già il sintomo davanti

| Sintomo | Prima azione | Procedura |
|---|---|---|
| pin non aggancia | `EDITATT`, poi `_DSETTINGS` | [Pin non agganciato](playbooks/diagnose-pin-not-snapping.md) |
| cross-reference vecchio | **UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna** | [Rimandi](playbooks/power-reference-diagnostic.md) |
| morsetto mostra numero filo | `SPINSMOR` → **Anteprima** → modello `NumM` | [Morsetti](playbooks/terminal-representation.md) |
| accessorio non associato | `EDITATT` → `PRES = F`, stesso `NOME` della Madre | [Accessori](playbooks/manage-accessories-and-coils.md) |
| materiale manca/duplica | **Materiali → Avvio Archivio Materiali (DbCenter)** | [Materiali](playbooks/material-association.md) |
| layer non eliminabile | `PURGE → Trova elementi non eliminabili` | [Oggetti residui](playbooks/clean-residual-objects.md) |
| immagine mancante | **Gestioni immagini → Sfoglia → Salva percorso** | [Immagini](05-pages-titleblocks-images.md) |
| archivio cavi non allineato | verifica `DbCables.db` e versione librerie | [DbCables](known-issues/dbcables-version-mismatch.md) |

## Flusso di lavoro consigliato

1. **Setup** — `_CUSTOM`, progetto, cartiglio e pagine standard.
2. **Schema** — unifilare o multifilare usando oggetti SPAC coerenti.
3. **Dati** — attributi, fili, rimandi, morsetti, materiali e cavi.
4. **Verifica** — distinta, report, cross-reference e checklist.
5. **Condivisione** — pubblica solo archivi sanitizzati nella sezione [Download](downloads.md).

!!! note "Manuale consolidato"

    La [Guida operativa consolidata](guida-operativa-completa.md) è una vista unica e sanitizzata. Per il lavoro quotidiano usa le pagine specialistiche: sono quelle mantenute con il massimo dettaglio operativo.
