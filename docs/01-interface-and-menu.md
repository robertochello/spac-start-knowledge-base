# Interfaccia, menu e comandi

Questa sezione raccoglie i comandi effettivi già consolidati per gestire l'interfaccia SPAC Start.

## Ripristinare o ricaricare i menu

Nella riga comando digita:

```text
_MENU
```

Usa questo comando quando i menu CAD/SPAC non sono visibili o l'ambiente risulta alterato.

!!! warning "Scelta del file/menu"

    Il file/menu specifico da caricare dipende dalla configurazione installata. Se non è già noto nell'ambiente in uso, non indicare un nome file ipotetico nella documentazione.

## Aprire la libreria simboli

Nella riga comando digita:

```text
SP_XML_MENU
```

Risultato atteso: apertura della libreria simboli SPAC.

## Creare una shortcut per la libreria simboli

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
4. Imposta un nome, ad esempio `Libreria simboli`.
5. Nel campo **Macro** inserisci:

   ```text
   ^C^CSP_XML_MENU;
   ```

6. Nell'albero vai in:

   ```text
   Tasti di scelta rapida → Tasti di scelta rapida
   ```

7. Trascina il nuovo comando in **Tasti di scelta rapida**.
8. Seleziona il comando.
9. Nel campo **Accesso-Tasto/i** imposta, ad esempio:

   ```text
   CTRL+SHIFT+L
   ```

10. Clicca **Applica** → **OK**.

## Verifica della shortcut

1. Chiudi la finestra **Personalizza interfaccia utente**.
2. Premi la combinazione assegnata.
3. Verifica che si apra la stessa libreria ottenuta digitando `SP_XML_MENU`.

## Regola sulle macro contestuali

Le macro che richiamano sezioni specifiche della libreria vanno documentate solo dopo verifica reale.

Per ogni macro consolidata devono essere riportati:

- testo completo della macro;
- nome del comando creato;
- percorso dentro **Personalizza interfaccia utente**;
- shortcut assegnata;
- risultato atteso.

Se manca uno di questi dati, segnare il passaggio `Da verificare`.

## Riferimenti

- [Comandi e click esatti](command-reference.md)
- [Libreria custom](15-custom-library.md)
