# Checklist validazione simbolo custom

Questa checklist serve per validare un simbolo custom prima di considerarlo riutilizzabile.

## 1. Identità del simbolo

- Nome simbolo chiaro.
- Categoria funzionale definita.
- Descrizione sintetica presente.
- Tipo simbolo identificato: Madre, Figlia, grafico, macro.
- Eventuale relazione Madre/Figlia documentata.

## 2. Attributi

Verificare la presenza e la coerenza degli attributi principali:

- NOME
- PRES
- DESCRIZIONE
- TIPO
- COSTRUTTORE
- QUADRO

Per simboli Madre, verificare:

```text
PRES = M
```

## 3. Pinatura

Per simboli cablati:

- pin allineati alla griglia;
- attributi PINA numerati in modo progressivo;
- eventuali PINB coerenti con i rispettivi PINA;
- nessun PINB inutile;
- test di aggancio filo eseguito.

## 4. Inserimento in progetto prova

Testare il simbolo in un progetto non critico.

Verificare:

- inserimento corretto;
- scala corretta;
- visibilità corretta;
- attributi modificabili;
- collegamenti agganciabili;
- nessuna entità grafica indesiderata.

## 5. Associazione materiale

Se il simbolo deve gestire materiale:

- verificare che il componente sia riconosciuto;
- verificare che l'associazione materiale sia possibile;
- controllare che il simbolo non sia solo grafica CAD;
- documentare eventuali limitazioni.

## 6. Macro e riuso

Se il simbolo fa parte di una macro:

- testare prima il simbolo singolo;
- testare poi la macro completa;
- verificare orientamento;
- verificare riferimenti;
- evitare duplicazioni di nomi o attributi.

## 7. Inventario

Aggiornare l'inventario simboli con:

- nome simbolo;
- categoria;
- descrizione;
- tipo simbolo;
- presenza pin;
- materiale associabile;
- stato test;
- note operative.

## Stato finale

Assegnare uno stato:

- Testato
- Da verificare
- In revisione
- Deprecato

Un simbolo può essere considerato stabile solo quando inserimento, attributi e pinatura sono stati verificati in un progetto prova.
