# Linee guida di manutenzione

Questa pagina definisce come evitare che la knowledge base torni a essere generica o ambigua.

## Regola principale

La documentazione deve essere utile **mentre si sta lavorando in SPAC**.

Una frase come:

> apri la gestione morsetti e crea un nuovo morsetto

non è sufficiente se i nomi esatti sono già noti.

La forma corretta è:

```text
SPINSMOR
→ seleziona morsettiera
→ scegli tipo morsetto
→ Anteprima
→ Ok - Nuovo
→ clic sul filo
→ Invio
```

## Struttura obbligatoria di una procedura operativa

Quando applicabile, ogni procedura deve contenere:

1. **Dove cliccare / cosa digitare**;
2. **nome esatto della finestra**;
3. **campo o pulsante da usare**;
4. **valore da impostare**;
5. **esito atteso**;
6. **cosa controllare se l'esito è KO**;
7. **prerequisiti o errori noti**.

## Fonte di verità

Ordine di priorità:

1. comportamento verificato direttamente in SPAC Start 26;
2. `docs/command-reference.md`;
3. pagina operativa/playbook specifico;
4. `docs/guida-operativa-completa.md` come riferimento storico consolidato;
5. ipotesi non verificate, che devono restare marcate **Da verificare**.

Se il manuale completo contiene già un percorso verificato, una pagina nuova **non deve degradarlo** a frase generica o `Da verificare`.

## Uso di Da verificare

Usare **Da verificare** solo sul dettaglio realmente mancante.

Corretto:

> Creazione progetto: il flusso è noto, ma il nome esatto del pulsante iniziale è **Da verificare**.

Non corretto:

> Aprire la funzione corretta e proseguire.

Non inventare mai un nome plausibile di menu o pulsante.

## Aggiornare una procedura dopo una verifica reale

Quando durante il lavoro viene verificato un nuovo click/comando:

1. aggiorna la pagina specialistica;
2. aggiorna `command-reference.md` se è un comando riutilizzabile;
3. aggiorna eventuale playbook/troubleshooting collegato;
4. rimuovi il relativo **Da verificare**;
5. aggiungi esito atteso e comportamento KO;
6. aggiorna il changelog se la modifica è rilevante.

## Evitare duplicazioni incoerenti

Se la stessa operazione appare in più pagine, i nomi devono essere identici.

Esempio canonico:

```text
UTIL → Cross Reference → Rimandi → Cross → Ok - Aggiorna
```

Non usare in altre pagine varianti generiche come “aggiorna i cross-reference”.

## Revisione periodica

Controllare almeno:

- `Da verificare` ancora necessari;
- procedure con verbi generici (`apri`, `vai`, `crea`, `aggiorna`) senza nome UI;
- comandi presenti nel manuale completo ma assenti nelle pagine operative;
- nomi diversi per la stessa finestra/pulsante;
- link interni;
- duplicazioni;
- changelog;
- build MkDocs.

## Quando aggiungere contenuto

Aggiungere una nuova nota/procedura quando:

- è stata verificata o è marcata chiaramente come non verificata;
- è riutilizzabile;
- non contiene dati cliente/commessa;
- riduce una reale ambiguità operativa.

Non aggiungere appunti generici che non permettono di eseguire o diagnosticare un'operazione.

## Definition of Done documentale

Una procedura SPAC è pronta quando un tecnico che non l'ha scritta può seguirla senza dover indovinare:

- quale comando digitare;
- quale voce cliccare;
- quale valore scegliere;
- quale risultato aspettarsi;
- dove iniziare la diagnosi se non funziona.

## Collegamenti

- [Comandi e click esatti](command-reference.md)
- [Quality gate](14-quality-gates.md)
- [Guida pratica](00-how-to-use.md)
