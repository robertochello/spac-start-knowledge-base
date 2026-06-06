# Archivi materiali custom

Questa sezione definisce un workflow controllato per preparare, importare e validare archivi materiali personalizzati.

![Workflow archivi materiali](assets/diagrams/material-archive-workflow.svg)

## Obiettivo

Gestire materiali custom in modo ordinato, evitando duplicazioni, import non controllati e dati non coerenti.

La guida non sostituisce la procedura ufficiale del software: definisce un metodo operativo sicuro da seguire prima di importare o consolidare archivi materiali.

## Principio operativo

Un archivio materiali non deve essere importato direttamente in ambiente operativo senza:

- backup;
- normalizzazione dati;
- controllo duplicati;
- import in ambiente di prova;
- validazione su progetto non critico;
- documentazione della provenienza.

## Workflow consigliato

1. **Raccolta dati**  
   Raccogliere codici, descrizioni, costruttori e categorie.

2. **Normalizzazione**  
   Uniformare nomi, descrizioni, categorie e campi obbligatori.

3. **Staging**  
   Preparare un archivio di prova separato da quello operativo.

4. **Backup**  
   Salvare lo stato precedente dell'archivio materiali.

5. **Import controllato**  
   Importare in ambiente di test o progetto non critico.

6. **Validazione**  
   Verificare ricerca, associazione ai simboli, distinta e report.

7. **Promozione**  
   Solo dopo validazione, rendere l'archivio disponibile come standard.

## Campi consigliati

Per ogni materiale, mantenere almeno queste informazioni:

| Campo | Scopo |
|---|---|
| Codice | Codice articolo o identificativo materiale |
| Descrizione | Descrizione tecnica sintetica |
| Costruttore | Marca o produttore |
| Categoria | Famiglia funzionale |
| Tipo | Tipologia tecnica |
| Note | Informazioni operative o limitazioni |
| Stato | Bozza, Da verificare, Validato, Deprecato |

## Stati materiali

| Stato | Significato |
|---|---|
| Bozza | Materiale inserito ma non verificato |
| Da verificare | Materiale plausibile ma non ancora validato in progetto prova |
| Validato | Materiale testato e pronto per il riuso |
| Deprecato | Materiale da non usare per nuovi progetti |

## Controllo duplicati

Prima dell'import controllare duplicati su:

- codice articolo;
- costruttore;
- descrizione simile;
- categoria;
- variante tecnica.

Quando due record sembrano simili, non unificarli automaticamente: verificare se rappresentano davvero lo stesso materiale.

## Import in ambiente di prova

La prima importazione deve avvenire in ambiente controllato.

Checklist:

- archivio originale salvato;
- file da importare verificato;
- categorie coerenti;
- campi obbligatori compilati;
- duplicati controllati;
- progetto prova disponibile;
- report materiali verificabile.

## Validazione su simboli

Dopo l'import:

1. selezionare un simbolo coerente;
2. associare il materiale importato;
3. verificare che il materiale sia ricercabile;
4. generare report o distinta;
5. controllare descrizione e costruttore;
6. verificare che non compaiano duplicazioni.

## Regole di governance

- Non importare materiali non verificati in un archivio stabile.
- Non cancellare record storici senza decisione documentata.
- Non usare descrizioni troppo generiche.
- Non mischiare materiali validati e bozze senza stato.
- Aggiornare il changelog quando un archivio diventa standard.

## Checklist finale

Un archivio materiali è pronto quando:

- i dati sono normalizzati;
- i duplicati sono controllati;
- l'import è stato testato;
- almeno un materiale è stato associato a un simbolo;
- distinta o report sono stati verificati;
- lo stato dei record è documentato.

## Collegamenti

- [Associare materiali](playbooks/material-association.md)
- [Simboli custom](03-custom-symbols.md)
- [Quality gates](14-quality-gates.md)
- [Decision log](11-decision-log.md)
