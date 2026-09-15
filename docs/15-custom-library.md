# Libreria custom

Questa sezione raccoglie le regole operative per installare, aprire, organizzare e mantenere la libreria custom SPAC.

## Installazione della libreria `_CUSTOM`

Path di installazione:

```text
C:\SPAC Start 26\Librerie\Blk\_CUSTOM
```

Procedura:

1. Chiudi **SPAC Start 26**.
2. Apri Esplora file.
3. Vai in:

   ```text
   C:\SPAC Start 26\Librerie\Blk
   ```

4. Copia qui la cartella `_CUSTOM` completa.
5. Verifica che il risultato sia:

   ```text
   C:\SPAC Start 26\Librerie\Blk\_CUSTOM
   ```

6. Verifica che dentro `_CUSTOM` siano presenti le categorie della libreria e la cartella `Documentazione`.
7. Riavvia **SPAC Start 26**.

Se `_CUSTOM` è già presente, non sovrascriverla alla cieca: confronta prima il contenuto.

## Aprire la libreria simboli

Il comando verificato da riga comando è:

```text
SP_XML_MENU
```

Risultato atteso: apertura della libreria simboli SPAC.

## Creare una scorciatoia per aprire la libreria

1. Nella riga comando digita:

   ```text
   CUI
   ```

   oppure:

   ```text
   _CUI
   ```

2. Nella finestra **Personalizza interfaccia utente**, individua **Elenco comandi**.
3. Tasto destro in **Elenco comandi** → **Nuovo comando**.
4. Assegna il nome `Libreria simboli`.
5. Nel campo **Macro** inserisci:

   ```text
   ^C^CSP_XML_MENU;
   ```

6. Nell'albero di personalizzazione apri:

   ```text
   Tasti di scelta rapida → Tasti di scelta rapida
   ```

7. Trascina il nuovo comando dentro **Tasti di scelta rapida**.
8. Seleziona il comando.
9. Nel campo **Accesso-Tasto/i** imposta la combinazione desiderata, ad esempio:

   ```text
   CTRL+SHIFT+L
   ```

10. Clicca **Applica** → **OK**.

## Categorie libreria

| Categoria | Utilizzo |
|---|---|
| `00_SIMBOLI_GRAFICI` | Simboli grafici generici e rappresentazioni senza logica elettrica complessa |
| `01_ALIMENTATORI` | Alimentatori, trasformatori, UPS, sorgenti e dispositivi di alimentazione |
| `02_PROTEZIONI` | Protezioni non classificate come interruttori o sezionatori |
| `03_RELE_INTERFACCE` | Relè, interfacce, moduli di isolamento e dispositivi di appoggio ai comandi |
| `04_MODULI_IO_PLC` | PLC, moduli I/O, moduli remoti e dispositivi di automazione |
| `05_SENSORI` | Sensori, finecorsa, proximity, pressostati, termostati e dispositivi di rilevamento |
| `06_ATTUATORI_DRIVE` | Attuatori, motori, inverter, drive, elettrovalvole e dispositivi di movimento |
| `07_COMUNICAZIONE` | Switch, gateway, router, convertitori e dispositivi di comunicazione industriale |
| `08_MORSETTI_CONNETTORI` | Morsetti, connettori, spine, prese e punti di connessione |
| `09_STRUMENTAZIONE` | Multimetri, strumenti di misura, analizzatori e strumenti da pannello |
| `10_INTERRUTTORI` | Interruttori, magnetotermici, differenziali, sezionatori e dispositivi affini |
| `99_GENERICI` | Simboli provvisori o non ancora classificati |
| `Documentazione` | README, inventari e documenti di supporto alla libreria |

## Regole di classificazione

- simboli `INT_*` → `10_INTERRUTTORI`;
- strumentazione → `09_STRUMENTAZIONE`;
- protezioni non riconducibili a interruttori/sezionatori → `02_PROTEZIONI`;
- `99_GENERICI` solo temporanea.

## Verifica dopo l'installazione

1. Avvia SPAC Start 26.
2. Digita `SP_XML_MENU`.
3. Verifica che `_CUSTOM` sia raggiungibile nella libreria simboli.
4. Apri almeno una categoria.
5. Inserisci un simbolo in un progetto di prova.
6. Se il simbolo non compare, verifica prima il path fisico della cartella e poi la configurazione della libreria.

## Prima di aggiungere un simbolo

- verifica categoria;
- verifica nome secondo convenzione;
- verifica `.dwg`;
- verifica `.sld` con stesso nome base;
- verifica attributi con `EDITATT` se il simbolo è intelligente;
- verifica pinatura se presente;
- aggiorna inventario.

## Collegamenti

- [Comandi e percorsi esatti](command-reference.md)
- [Simboli custom](03-custom-symbols.md)
- [Attributi e pinatura](04-attributes-and-pinning.md)
- [Nomenclatura simboli](19-symbol-naming.md)
- [Checklist validazione simbolo](10-symbol-validation-checklist.md)
