# Linee guida immagini e screenshot

Questa sezione definisce come usare immagini, screenshot e diagrammi nella knowledge base.

## Obiettivo

Aggiungere supporto visuale alla guida senza introdurre confusione, dati sensibili o immagini non mantenibili.

## Tipi di immagini ammessi

| Tipo | Uso |
|---|---|
| Diagrammi Mermaid | Spiegare workflow, lifecycle e relazioni |
| Screenshot sanitizzati | Mostrare finestre, menu o configurazioni generiche |
| Immagini annotate | Evidenziare aree specifiche con frecce o box |
| Schemi generici | Usare Mermaid se rappresentano processi o relazioni |

## Regole di sanitizzazione

Prima di aggiungere uno screenshot:

- rimuovere nomi cliente;
- rimuovere codici commessa;
- rimuovere percorsi personali o aziendali non pubblicabili;
- rimuovere dati tecnici riservati;
- tagliare solo l'area utile;
- evitare schermate troppo grandi o non leggibili;
- verificare che l'immagine sia davvero necessaria.

## Struttura cartelle

Usare questa struttura:

```text
docs/assets/diagrams/
docs/assets/screenshots/
docs/assets/screenshots/symbols/
docs/assets/screenshots/materials/
docs/assets/screenshots/titleblocks/
docs/assets/screenshots/terminals/
docs/assets/screenshots/troubleshooting/
```

## Naming immagini

Usare nomi descrittivi, minuscoli e separati da trattini.

Esempi:

```text
custom-symbol-attributes-example.png
pin-not-snapping-diagnostic.png
material-import-validation.png
titleblock-logo-reference.png
terminal-num-m-representation.png
```

## Quando usare Mermaid

Usare Mermaid quando il contenuto spiega:

- un workflow;
- una relazione tra oggetti;
- un ciclo di validazione;
- un processo decisionale;
- una sequenza di controllo.

Regole:

- usare blocchi fenced `mermaid`;
- mantenere nodi brevi;
- usare colori solo per stato, rischio, dato o azione;
- non sostituire screenshot reali con Mermaid;
- non usare SVG statici per workflow o mappe concettuali.

## Quando usare uno screenshot

Usare uno screenshot quando serve mostrare:

- una finestra specifica;
- un campo da configurare;
- un errore ricorrente;
- un risultato atteso;
- una differenza tra rappresentazione corretta e non corretta.

## Regola editoriale

Ogni immagine deve avere una funzione. Se l'immagine non chiarisce una procedura, una decisione o un problema, non va inserita.

## Checklist prima del commit

- immagine sanitizzata;
- nome file coerente;
- cartella corretta;
- riferimento Markdown funzionante;
- testo alternativo presente;
- pagina aggiornata;
- nessun dato non pubblicabile.
