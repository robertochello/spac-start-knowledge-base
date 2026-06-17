# Known Issue — Cross-reference obsoleto

## Sintomo

Un rimando o cross-reference punta a una posizione dove il collegamento non è più presente.

Il caso tipico è un riferimento che sembra puntare a una vecchia cella, a un
oggetto cancellato graficamente o a un rimando non più utilizzato.

## Cause probabili

- Vecchi oggetti intelligenti rimasti nel foglio.
- Riferimenti non rigenerati.
- Oggetti cancellati solo graficamente.
- Rimandi duplicati o non più utilizzati.

## Diagnosi

1. Distinguere linea grafica, alimentazione SPAC, oggetto intelligente e rimando.
2. Verificare oggetti residui.
3. Controllare rimandi non utilizzati.
4. Controllare nomi e direzione dei rimandi.
5. Rigenerare o aggiornare i riferimenti.
6. Verificare che il cross-reference non punti a celle o oggetti vecchi.
7. Testare su un foglio pulito.

## Soluzione

Consultare:

- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Diagnosticare rimandi alimentazione](../playbooks/power-reference-diagnostic.md)
- [Pulire oggetti residui](../playbooks/clean-residual-objects.md)
- [Troubleshooting](../07-troubleshooting.md)

## Prevenzione

- Evitare correzioni solo grafiche.
- Verificare sempre oggetti intelligenti e dati sorgente.
- Rigenerare i riferimenti dopo modifiche strutturali.
