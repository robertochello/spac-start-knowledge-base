# SPAC Start Knowledge Base

Guida operativa per **SPAC Start 26 / SPAC Start Impianti**. Parti da quello che devi fare: non è necessario leggere il manuale in ordine.

<div class="home-grid" markdown>

[**Voglio sapere cosa cliccare**<br>Comandi reali, finestre, pulsanti e percorsi menu.](command-reference.md){ .home-card }

[**Sto iniziando un progetto**<br>Template, pagine standard, cartiglio e libreria.](16-project-template.md){ .home-card }

[**Sto lavorando in unifilare**<br>Disegno Unifilare, materiali, linee e numerazione.](17-unifilare.md){ .home-card }

[**Sto lavorando in multifilare**<br>Rimandi, cross-reference, morsetti e accessori.](09-multifilare.md){ .home-card }

[**Sto creando un simbolo**<br>DWG, attributi, pinatura, SLD e test.](playbooks/create-custom-symbol.md){ .home-card }

[**Ho un problema**<br>Parti dal sintomo e dal primo comando da provare.](07-troubleshooting.md){ .home-card }

</div>

!!! important "Regola della guida"

    Se un nome è stato verificato in SPAC Start 26, viene scritto **esattamente come compare nell'interfaccia**. Se non è verificato, il punto è marcato **Da verificare** invece di inventare un comando plausibile.

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

Per tutti i dettagli: **[Comandi e click esatti](command-reference.md)**.

## Se non sai quale pagina aprire

| Caso | Vai a |
|---|---|
| libreria `_CUSTOM`, setup iniziale | [Libreria custom](15-custom-library.md) |
| struttura nuovo progetto | [Template progetto](16-project-template.md) |
| schema unifilare | [Schema unifilare](17-unifilare.md) |
| schema multifilare | [Multifilare](09-multifilare.md) |
| rimandi, cross-reference, morsetti | [Rimandi e morsetti](06-cross-references-terminals.md) |
| simboli custom | [Creare un simbolo custom](playbooks/create-custom-symbol.md) |
| `PRES`, `PINA`, `PINB` | [Attributi e pinatura](04-attributes-and-pinning.md) |
| materiali | [Associare materiali](playbooks/material-association.md) |
| archivio cavi | [Archivio Cavi DbCables](25-cable-archive-dbcables.md) |
| problema non chiaro | [Troubleshooting](07-troubleshooting.md) |
| indice per attività | [Guida pratica](00-how-to-use.md) |

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

## Percorso consigliato per una commessa

1. **Setup** — `_CUSTOM`, progetto, cartiglio, pagine standard.
2. **Schema** — unifilare/multifilare con oggetti SPAC corretti.
3. **Dati** — attributi, fili, rimandi, morsetti, materiali e cavi.
4. **Verifica** — report, distinta, cross-reference, checklist.

!!! note "Manuale completo"

    La [Guida operativa completa](guida-operativa-completa.md) resta utile per ricerca testuale e storico consolidato. Nel lavoro quotidiano usa le pagine operative sopra: sono quelle che vengono mantenute con i click esatti.
