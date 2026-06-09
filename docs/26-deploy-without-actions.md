# Deploy manuale senza GitHub Actions

Questa pagina descrive come pubblicare il sito documentale MkDocs quando GitHub Actions è disattivato.

## Contesto

La documentazione viene sviluppata sul branch principale della repository, ma il sito pubblico viene servito dal branch `gh-pages`.

Se GitHub Actions è disattivato, i commit su `master` non aggiornano automaticamente il sito pubblicato.

## Conseguenza

La repo può essere aggiornata e coerente, ma il sito pubblico può restare indietro.

Esempio:

- pagina presente in `docs/` su `master`;
- pagina non ancora presente su `gh-pages`;
- pagina non raggiungibile da `robertochello.github.io/spac-start-knowledge-base`.

## Metodo consigliato

Usare il deploy manuale da PC locale.

## Prerequisiti

- Git installato.
- Python installato.
- Repository clonata localmente.
- Permessi di push sulla repository.
- Branch `gh-pages` usato come sorgente GitHub Pages.

## Procedura

Aprire un terminale nella cartella della repository ed eseguire:

```bash
pip install -r requirements.txt
mkdocs build
mkdocs gh-deploy --force --no-history
```

## Verifica

Dopo il deploy:

1. aprire il sito pubblico;
2. verificare la Home;
3. verificare il menu di navigazione;
4. aprire una pagina appena aggiunta;
5. controllare il sitemap generato;
6. verificare immagini e diagrammi.

## Pagine da controllare dopo il deploy DbCables

Dopo l'ultimo aggiornamento, verificare almeno:

```text
/spac-start-knowledge-base/25-cable-archive-dbcables/
/spac-start-knowledge-base/playbooks/update-dbcables-archive/
/spac-start-knowledge-base/known-issues/dbcables-version-mismatch/
```

## Quando usare GitHub Actions

GitHub Actions resta il metodo più comodo se si vuole aggiornare il sito automaticamente a ogni push.

Se Actions rimane disattivato, il deploy manuale diventa il metodo ufficiale.

## Regola operativa

Ogni volta che si aggiungono o modificano pagine nella documentazione, eseguire un deploy manuale per aggiornare il branch `gh-pages`.
