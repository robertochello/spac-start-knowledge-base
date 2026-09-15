# Playbook — Pulire oggetti residui e layer non eliminabili

## Obiettivo

Individuare il motivo per cui un layer apparentemente vuoto non può essere eliminato oppure perché un oggetto cancellato continua a influenzare rimandi e cross-reference.

## Comandi da usare in SPAC Start 26

Comandi verificati:

```text
PURGE
QSELECT
BEDIT
```

!!! danger "Comandi da non usare in questa guida"

    In **SPAC Start 26** sono stati verificati come non disponibili:

    ```text
    LAYISO
    LAYWALK
    ```

    Non inserirli come soluzione SPAC.

## Caso 1 — Layer apparentemente vuoto ma non eliminabile

### Passo 1: aprire PURGE

Nella riga comando digita:

```text
PURGE
```

Nella finestra verifica:

```text
Elementi eliminabili → Layer
```

Se il layer compare tra gli elementi eliminabili, eliminalo da qui.

### Passo 2: se il layer NON è eliminabile

Sempre nella finestra `PURGE`, usa:

```text
Trova elementi non eliminabili
```

Seleziona il layer interessato e leggi cosa lo sta referenziando.

Questa è la verifica fondamentale: un layer che sembra vuoto può essere ancora usato da:

- un oggetto diretto nel disegno;
- un blocco;
- un oggetto annidato dentro un blocco;
- un blocco non più usato ma ancora presente nella definizione del DWG.

## Caso 2 — PURGE indica un oggetto diretto sul layer

Usa:

```text
QSELECT
```

Nella finestra **Selezione rapida**:

1. imposta il filtro/proprietà sul **Layer**;
2. seleziona il nome del layer problematico;
3. conferma la selezione;
4. individua gli oggetti selezionati;
5. eliminali oppure spostali sul layer corretto;
6. esegui nuovamente `PURGE`.

Esempio già usato: filtro Layer=`Q.E.`.

## Caso 3 — Il layer è referenziato dentro un blocco

Se `PURGE` / **Trova elementi non eliminabili** indica che il layer è usato dentro un blocco:

1. annota il nome del blocco indicato;
2. digita:

   ```text
   BEDIT
   ```

3. nella finestra di modifica blocco seleziona il blocco corretto;
4. dentro il Block Editor individua le geometrie rimaste sul layer problematico;
5. elimina le geometrie inutili oppure spostale su un layer corretto;
6. salva e chiudi il blocco;
7. esegui di nuovo:

   ```text
   PURGE
   ```

8. verifica se ora il layer compare in **Elementi eliminabili → Layer**.

## Caso 4 — BEDIT mostra ancora residui non eliminabili

Se dentro il blocco vedi elementi ma non riesci a eliminarli:

1. verifica che il layer non sia **bloccato**;
2. sblocca il layer se necessario;
3. verifica se l'elemento visibile appartiene in realtà a un **blocco annidato**;
4. se è annidato, individua il blocco interno;
5. apri anche quello con `BEDIT`;
6. elimina/sposta la geometria nel blocco effettivamente proprietario dell'oggetto;
7. salva le modifiche;
8. torna al disegno e riesegui `PURGE`.

## Caso 5 — Blocchi inutilizzati che mantengono il layer

Un blocco non inserito nel disegno può comunque mantenere una definizione che usa il layer.

Procedura:

1. `PURGE`;
2. elimina prima i **blocchi inutilizzati** quando sono effettivamente eliminabili;
3. richiama `PURGE`;
4. torna a **Elementi eliminabili → Layer**;
5. verifica se il layer è diventato eliminabile.

## Sequenza consigliata completa

```text
PURGE
  ↓
Layer eliminabile?
  ├─ Sì → elimina layer
  └─ No → Trova elementi non eliminabili
              ↓
        Oggetto diretto?
          ├─ Sì → QSELECT → filtro Layer → elimina/sposta → PURGE
          └─ No → Blocco?
                    ├─ Sì → BEDIT → elimina/sposta residuo → salva → PURGE
                    └─ Blocco annidato → BEDIT sul blocco interno → PURGE
```

## Verifica finale

La pulizia è completa quando:

- `PURGE` non segnala più riferimenti al layer indesiderato;
- il layer può essere eliminato;
- non sono stati rimossi oggetti SPAC utili;
- rimandi/cross-reference non puntano più a oggetti residui;
- salvataggio e riapertura del DWG non fanno ricomparire il problema.

## Regola di sicurezza

Prima di eliminare un residuo dentro `BEDIT`, verifica sempre **che cosa rappresenta realmente l'oggetto**. Non eliminare geometrie di un simbolo/blocco solo per liberare un layer senza aver verificato che siano effettivamente inutili.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Rimandi e cross-reference](../06-cross-references-terminals.md)
- [Cross-reference obsoleto](../known-issues/obsolete-cross-reference.md)
- [Troubleshooting](../07-troubleshooting.md)
