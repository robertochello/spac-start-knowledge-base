# Playbook — Associare materiali

## Obiettivo

Associare un materiale a un simbolo SPAC usando il percorso effettivo dell'interfaccia e verificare che il risultato sia corretto in distinta/report.

## Percorso esatto sul simbolo

1. Nel disegno fai **doppio click sul simbolo** a cui vuoi associare il materiale.
2. Nella finestra/proprietà del simbolo individua il riquadro **Materiali**.
3. Nel riquadro **Materiali**, fai **tasto destro**.
4. Clicca:

   ```text
   Avvio Archivio Materiali (DbCenter)
   ```

5. In **DbCenter**, cerca e seleziona il materiale corretto.
6. Conferma l'associazione.
7. Torna al simbolo e verifica che il materiale risulti associato.
8. Genera o controlla la distinta/report prevista e verifica che il materiale compaia una sola volta nel punto corretto.

## Prima di associare

Controlla che:

- il simbolo sia un oggetto SPAC riconosciuto e non sola grafica CAD;
- il codice catalogo sia reale e verificato;
- costruttore e descrizione siano coerenti;
- sia chiaro se il materiale deve stare sulla Madre o su un Figlio/accessorio;
- l'archivio materiali corretto sia disponibile in DbCenter.

## Madre, Figlio e accessori

| Scenario | Punto di associazione consigliato |
|---|---|
| Componente principale con materiale unico | Simbolo Madre/principale |
| Accessorio compreso nel componente principale | Valutare associazione sulla Madre per evitare doppioni |
| Accessorio gestito separatamente in distinta | Simbolo/accessorio dedicato |
| Simbolo puramente grafico | Non usarlo come sorgente materiale stabile |

Se il simbolo è Madre/Figlio, verifica gli attributi con:

```text
EDITATT
```

Regole documentate:

```text
Madre  → PRES = M
Figlio → PRES = F
```

Quando il Figlio deve essere collegato logicamente alla Madre, `NOME` deve essere coerente.

## Verifica del record materiale

In DbCenter verifica almeno:

- codice catalogo;
- costruttore;
- descrizione;
- categoria;
- stato/validazione del record.

!!! warning "Dato non verificato"

    Se il codice catalogo o il record non è stato verificato sulla fonte corretta, non promuoverlo a standard. Marcalo `Da verificare`.

## Verifica finale in distinta/report

Dopo l'associazione controlla:

1. il materiale compare;
2. il codice è quello atteso;
3. la quantità è coerente;
4. non compare due volte per effetto di associazioni sia su Madre sia su Figlio;
5. non manca un accessorio che deve essere gestito separatamente.

## Se il materiale non compare

Controlla nell'ordine:

1. che il simbolo sia realmente intelligente SPAC;
2. doppio click sul simbolo → riquadro **Materiali**;
3. che l'associazione effettuata tramite **Avvio Archivio Materiali (DbCenter)** sia presente;
4. che il materiale sia stato associato al simbolo corretto;
5. che la distinta/report stia leggendo la stessa sorgente dati prevista.

## Se il materiale compare duplicato

1. Controlla la Madre.
2. Controlla eventuali Figli/accessori.
3. Apri ciascun simbolo con doppio click e verifica il riquadro **Materiali**.
4. Rimuovi l'associazione dal livello non corretto solo dopo aver identificato quale oggetto deve essere la sorgente reale della distinta.

## Riferimenti

- [Comandi e click esatti](../command-reference.md)
- [Archivi materiali custom](../21-material-archives.md)
- [Standard materiali](../standards/materials.md)
- [Back-check e controlli incrociati](../26-back-check-controls.md)
- [Multifilare](../09-multifilare.md)
- [Attributi e pinatura](../04-attributes-and-pinning.md)
