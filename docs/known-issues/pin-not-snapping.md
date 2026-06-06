# Known Issue — Pin non agganciato

## Sintomo

Il filo non si aggancia correttamente al pin del simbolo custom.

## Cause probabili

- Pin non allineato alla griglia.
- Attributo pin assente o scritto in modo non coerente.
- Simbolo non riconosciuto come oggetto intelligente.
- Collegamento creato come semplice linea CAD.

## Diagnosi

1. Verificare attributi PINA/PINB.
2. Controllare posizione grafica del pin.
3. Verificare aggancio su progetto prova.
4. Controllare che il collegamento sia un filo riconosciuto.

## Soluzione

Applicare il playbook dedicato:

[Diagnosticare pin non agganciato](../playbooks/diagnose-pin-not-snapping.md)

## Prevenzione

- Allineare sempre i pin alla griglia.
- Validare ogni simbolo prima del riuso.
- Aggiornare inventario e stato test.
