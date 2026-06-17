# Casi pratici

Questa sezione raccoglie casi pratici risolti o da consolidare.

Ogni caso deve essere generico e privo di dati sensibili.

## Formato consigliato

Ogni caso dovrebbe contenere:

- contesto;
- problema;
- causa probabile;
- procedura applicata;
- verifica finale;
- collegamento a standard o troubleshooting.

## Caso 001 — Simbolo non riconosciuto come componente

**Contesto**  
Un simbolo custom viene inserito correttamente dal punto di vista grafico, ma non si comporta come componente SPAC.

### Possibili cause

- attributi mancanti;
- simbolo creato come semplice blocco CAD;
- valore PRES assente o non coerente;
- simbolo non testato in progetto prova.

### Procedura consigliata

1. Verificare attributi principali.
2. Controllare se il simbolo deve essere Madre.
3. Verificare eventuale PRES.
4. Testare associazione materiale, se richiesta.
5. Aggiornare inventario simboli.

### Riferimenti

- `docs/03-custom-symbols.md`
- `docs/04-attributes-and-pinning.md`
- `docs/10-symbol-validation-checklist.md`

---

## Caso 002 — Pin che non si aggancia al filo

**Contesto**  
Il simbolo è visibile, ma il collegamento non si aggancia correttamente al pin.

### Possibili cause

- pin non allineato alla griglia;
- attributo pin errato;
- filo non intelligente;
- simbolo modificato graficamente senza aggiornare attributi.

### Procedura consigliata

1. Verificare posizione del pin.
2. Allineare il punto alla griglia.
3. Controllare nomenclatura PINA/PINB.
4. Inserire un filo nuovo in progetto prova.
5. Validare il simbolo con checklist.

### Riferimenti

- `docs/04-attributes-and-pinning.md`
- `docs/10-symbol-validation-checklist.md`

---

## Caso 003 — Cross-reference verso posizione non più valida

**Contesto**  
Un riferimento punta a un punto del foglio dove il collegamento non è più presente.

### Possibili cause

- vecchi oggetti intelligenti rimasti nel progetto;
- rimandi non aggiornati;
- oggetti cancellati solo graficamente;
- rigenerazione riferimenti non eseguita.

### Procedura consigliata

1. Verificare presenza di oggetti residui.
2. Controllare rimandi non utilizzati.
3. Rigenerare riferimenti.
4. Testare il collegamento su un foglio pulito.

### Riferimenti

- `docs/06-cross-references-terminals.md`
- `docs/07-troubleshooting.md`
