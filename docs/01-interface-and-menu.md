# Interfaccia, menu e comandi

Questa sezione raccoglie note operative sulla gestione dell'interfaccia SPAC Start e dei comandi utili per ripristinare o velocizzare l'ambiente di lavoro.

## Ripristino menu

Se i menu non sono visibili o l'ambiente risulta alterato, usare il comando CAD di gestione menu:

```text
_MENU
```

Questo comando permette di ricaricare o ripristinare i menu dell'ambiente CAD/SPAC.

## Libreria simboli SPAC

Per aprire la libreria simboli/menu XML SPAC usare:

```text
SP_XML_MENU
```

Questo comando apre la libreria simboli generica.

## Shortcut da tastiera per libreria simboli

Per creare una scorciatoia da tastiera:

1. aprire la personalizzazione interfaccia con:

   ```text
   _CUI
   ```

2. creare un nuovo comando nella Command List;
3. associare al comando l'apertura della libreria simboli SPAC;
4. trascinare il comando in Keyboard Shortcuts / Shortcut Keys;
5. assegnare una combinazione, ad esempio CTRL + SHIFT + L;
6. confermare con Apply/OK.

## Macro contestuali

Per richiamare sezioni specifiche della libreria simboli, usare macro contestuali basate sul menu desiderato.

La logica generale è:

```text
richiamo menu contestuale + apertura libreria simboli
```

Annotare sempre l'identificativo del menu richiamato e testare la macro su un progetto non critico prima di usarla in modo stabile.

## Note operative

- Mantenere gli shortcut solo per comandi realmente ricorrenti.
- Evitare macro troppo specifiche se non sono documentate.
- Annotare sempre il comando reale usato, non solo il nome descrittivo.
- Quando un comando viene testato, riportarlo nella knowledge base con eventuali limitazioni.
