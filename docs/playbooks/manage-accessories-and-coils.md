# Playbook — Gestire accessori e bobine

## Obiettivo

Associare logicamente un accessorio, contatto o bobina a un dispositivo Madre in ambiente multifilare SPAC Start 26.

## Regola Madre/Figlio

Il componente principale deve avere:

```text
PRES = M
```

L'accessorio deve avere:

```text
PRES = F
```

Quando l'accessorio deve essere associato alla Madre, deve usare lo **stesso `NOME`** della Madre.

## Procedura esatta

1. Inserisci nel progetto il componente Madre.
2. Inserisci anche il simbolo dell'accessorio/contatto/bobina.
3. Seleziona l'accessorio.
4. Digita:

   ```text
   EDITATT
   ```

5. Nell'attributo `PRES` dell'accessorio imposta:

   ```text
   F
   ```

6. Nell'attributo `NOME` inserisci **lo stesso valore usato dalla Madre**.
7. Se SPAC avvisa che esiste già un dispositivo con lo stesso nome, **conferma e prosegui**: in questo caso l'uguaglianza del nome è voluta per creare la relazione logica.
8. Posiziona il Figlio nella posizione corretta dello schema.

Non è necessario creare un collegamento elettrico fittizio tra Figlio e Madre se la relazione è già definita tramite:

```text
PRES = F
NOME = stesso NOME della Madre
```

## Verificare la Madre

Se hai dubbi sul componente principale:

1. seleziona la Madre;
2. usa `EDITATT`;
3. verifica:

   ```text
   PRES = M
   ```

4. annota il valore di `NOME`;
5. usa esattamente quel valore nel Figlio.

## Esempi

Questa regola vale per:

- bobina associata a interruttore magnetotermico;
- contatto ausiliario associato a contattore, relè o interruttore;
- sgancio;
- segnalazione;
- comando motorizzato;
- altri accessori associati a un dispositivo principale.

## Materiale dell'accessorio

Se il materiale deve essere gestito separatamente:

1. doppio click sul simbolo accessorio;
2. riquadro **Materiali** → tasto destro;
3. **Avvio Archivio Materiali (DbCenter)**;
4. seleziona il materiale corretto;
5. verifica distinta/report.

Se invece l'accessorio è già compreso nel materiale della Madre, evita una seconda associazione che genererebbe un doppione.

## Diagnostica

| Sintomo | Verifica |
|---|---|
| accessorio non risulta associato | `EDITATT` → verifica `PRES = F` |
| accessorio punta al componente sbagliato | confronta `NOME` Figlio con `NOME` Madre |
| SPAC avvisa nome duplicato | se l'associazione è intenzionale, conferma e prosegui |
| distinta duplica il materiale | verifica associazione materiale su Madre e Figlio |
| relazione funziona solo graficamente | verifica `PRES` e `NOME`, non la sola vicinanza |

## Verifica finale

La relazione è corretta quando:

- Madre: `PRES = M`;
- Figlio: `PRES = F`;
- `NOME` Figlio = `NOME` Madre;
- il Figlio è riconosciuto come elemento associato;
- non sono stati creati collegamenti elettrici fittizi solo per simulare la relazione;
- distinta/materiali non generano doppioni.

## Collegamenti

- [Comandi e click esatti](../command-reference.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
- [Multifilare](../09-multifilare.md)
- [Associare materiali](material-association.md)
