# Playbook — Verificare rappresentazione morsetti

## Obiettivo

Capire perché un morsetto mostra un'informazione diversa da quella attesa e riportare la rappresentazione a una logica coerente.

## Quando usarlo

Usare questo playbook quando sul morsetto viene visualizzato un dato non desiderato, ad esempio un riferimento diverso dal numero morsetto.

## Principio operativo

Un morsetto è un oggetto dati, non solo testo visibile. Prima di modificare graficamente la scritta, verificare il dato sorgente e la configurazione della rappresentazione.

## Diagnosi

Controllare separatamente:

- morsettiera;
- numero morsetto;
- numero filo;
- riferimento funzionale;
- campi mostrati dal simbolo;
- impostazioni grafiche.

## Procedura

### 1. Verificare proprietà del morsetto

Controllare che il morsetto appartenga alla morsettiera corretta e abbia numero coerente.

### 2. Verificare dato visualizzato

Capire se il testo mostrato proviene dal numero morsetto, dal filo o da altro riferimento.

### 3. Controllare rappresentazione

Verificare quale campo viene richiamato dalla rappresentazione grafica del morsetto.

### 4. Testare su morsetto nuovo

Creare un morsetto di prova per capire se il problema è locale o di configurazione generale.

## Verifica finale

La configurazione è corretta quando:

- il morsetto mostra il dato previsto;
- la morsettiera è coerente;
- il numero morsetto non viene confuso con altri riferimenti;
- il comportamento è stabile su un nuovo morsetto di prova.

## Collegamenti

- [Rimandi, cross-reference e morsetti](../06-cross-references-terminals.md)
- [Troubleshooting](../07-troubleshooting.md)
