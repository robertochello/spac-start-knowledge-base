# Numerazione e identificazione fili

Questa sezione raccoglie le regole operative per numerare e identificare fili e alimentazioni.

## Obiettivo

Separare correttamente:

- fili non di alimentazione;
- conduttori di alimentazione;
- identificatori di fase/neutro;
- numerazione progressiva;
- rimandi.

## Fili non di alimentazione

Per i fili non di alimentazione è possibile usare una numerazione progressiva.

Configurazioni tipiche:

- numerazione progressiva semplice;
- numerazione legata al foglio;
- separatore tra foglio e numero progressivo.

Esempio logico:

```text
pagina.numero
```

## Fili di alimentazione

I fili di alimentazione non devono essere trattati come semplici fili da numerare.

Devono avere un identificatore coerente, ad esempio:

- L1;
- L2;
- L3;
- N;
- PE.

## Identificatore linea

Se la linea non mostra il simbolo identificatore, applicare la funzione di identificazione linee e verificare il tipo di conduttore selezionato.

## Progressivo numerico

Quando non serve il progressivo, usare solo l'identificatore della linea.

Quando serve aggiungere prefisso o suffisso locale, verificare che la modalità di numerazione supporti il progressivo.

## Rimandi

I rimandi devono essere gestiti con lo stesso nome quando devono riferirsi allo stesso collegamento.

Regola direzionale:

- un rimando di partenza deve avere un corrispondente rimando di arrivo;
- un rimando di arrivo deve avere un corrispondente rimando di partenza;
- un rimando arrivo/partenza può essere usato quando la logica lo richiede.

## Checklist

Prima di validare la numerazione:

- fili non di alimentazione numerati;
- alimentazioni identificate;
- fasi e neutro coerenti;
- rimandi con nomi coerenti;
- cross-reference aggiornato;
- duplicazioni verificate.

## Collegamenti

- [Schema unifilare](17-unifilare.md)
- [Rimandi, cross-reference e morsetti](06-cross-references-terminals.md)
- [Diagnosticare rimandi alimentazione](playbooks/power-reference-diagnostic.md)
