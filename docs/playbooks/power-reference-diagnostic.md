# Playbook — Diagnosticare rimandi alimentazione

## Obiettivo

Capire perché un rimando o riferimento di alimentazione non viene accettato o punta a una posizione non coerente.

## Quando usarlo

Usare questo playbook quando:

- una linea non viene riconosciuta come selezione valida;
- il riferimento punta a una posizione non aggiornata;
- un rimando sembra collegato solo graficamente;
- dopo modifiche al foglio restano riferimenti non coerenti.

## Principio operativo

Un rimando deve appoggiarsi a un oggetto riconosciuto, non a una semplice geometria.

## Diagnosi

Verificare:

- se l'oggetto selezionato è intelligente;
- se esistono oggetti residui;
- se il riferimento è stato aggiornato;
- se ci sono duplicazioni;
- se il collegamento è stato cancellato solo graficamente.

## Procedura

### 1. Verificare l'oggetto selezionato

Assicurarsi che la selezione riguardi l'oggetto corretto e non una linea CAD sovrapposta.

### 2. Cercare residui

Controllare eventuali vecchi oggetti rimasti nella zona del foglio.

### 3. Rigenerare riferimenti

Aggiornare i riferimenti dopo modifiche strutturali.

### 4. Testare su foglio pulito

Riprodurre il rimando in un contesto semplice per distinguere problema locale e problema di procedura.

## Verifica finale

Il rimando è corretto quando:

- la selezione è valida;
- il riferimento punta al punto atteso;
- non esistono duplicazioni residue;
- il comportamento resta stabile dopo aggiornamento.

## Collegamenti

- [Multifilare](../09-multifilare.md)
- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Known Issue — Cross-reference obsoleto](../known-issues/obsolete-cross-reference.md)
