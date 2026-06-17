# AGENTS.md

## Project scope

This repository is a technical knowledge base for SPAC Start 26.

The repository is published as a static documentation website with MkDocs
Material and GitHub Pages.

The main goal is to maintain a clear, operational and reusable knowledge base
for:

- SPAC Start 26 workflows;
- custom symbols;
- attributes and pinning;
- project templates;
- title blocks and images;
- unifilare and multifilare documentation;
- cross-references, terminals and wire numbering;
- material archives;
- cable archives;
- troubleshooting;
- operational standards and quality gates.

## Language and tone

Write documentation in Italian.

Use a technical, concise and operational style.

Prefer:

- procedures;
- checklists;
- tables;
- decision records;
- troubleshooting flows;
- practical examples.

Avoid:

- long theoretical explanations;
- generic filler text;
- client-specific information;
- project-specific confidential data;
- unverified claims presented as facts.

## Repository structure

Use the current MkDocs structure as the source of truth.

Main areas:

- `docs/` contains the published documentation.
- `docs/playbooks/` contains guided operational procedures.
- `docs/known-issues/` contains recurring problems and diagnostics.
- `docs/standards/` contains stable operational standards.
- `docs/assets/downloads/` contains public downloadable files.
- `mkdocs.yml` defines the published navigation.
- `requirements.txt` defines the documentation build dependencies.

Do not manually edit generated files in the `gh-pages` branch.

Make source changes on the main documentation branch and let GitHub Actions
publish the site.

## Editorial rules

Every new documentation page should have:

- a clear purpose;
- when to use the procedure;
- operational steps;
- final verification;
- links to related standards, playbooks, known issues or quality gates when
  relevant.

Every troubleshooting page should include:

- symptom;
- probable causes;
- diagnostic checks;
- solution;
- prevention.

Every operational standard should include:

- context;
- adopted rule;
- rationale;
- impact;
- verification method.

## SPAC-specific rules

Do not invent SPAC commands, menu paths or behaviors.

If a command, menu path or behavior is not verified in SPAC Start 26, mark it
clearly as `Da verificare`.

When documenting SPAC workflows:

- distinguish between SPAC Start 26 and SPAC Automazione if relevant;
- distinguish between unifilare and multifilare;
- distinguish between graphical CAD objects and SPAC intelligent objects;
- state whether the procedure has been tested;
- prefer practical validation steps.

## Custom symbol rules

For custom symbols, keep the documentation aligned with these rules:

- the full inventory of custom symbols is not stored in the README;
- the inventory is maintained in the Excel file named
  `SPAC_Custom_Simboli_Convenzione`;
- pin attributes use `PINA` followed by an incremental number;
- `PINB` followed by the same number means that the signal on `PINA<n>` is
  carried to `PINB<n>`;
- use `SCAMBIO`, not `SCB`;
- future CAD, DXF and DWG assets intended for SPAC should use Layer 0 unless
  explicitly stated otherwise.

## Download and archive governance

Files published under `docs/assets/downloads/` must be generic, reusable and
free from sensitive data.

Before adding or replacing downloadable files:

- verify that no client, project or order data is present;
- verify that the file opens correctly;
- verify that the file name is clear and versioned;
- verify that the related documentation page is updated;
- verify that the download link works after the MkDocs build;
- update the changelog or decision log if the file becomes a stable reference.

For `.db`, `.zip`, material archives and cable archives, do not replace
existing files without making the change explicit in the documentation.

## MkDocs rules

When adding a new documentation page:

- place it in the correct `docs/` subfolder;
- add it to `mkdocs.yml` only if it should appear in the published navigation;
- keep navigation labels short and operational;
- avoid duplicate navigation entries;
- keep related pages cross-linked.

## Validation commands

Before completing a change, run:

```bash
pip install -r requirements.txt
mkdocs build --strict
```

If the change affects links or downloads, also perform a link-oriented review
of the affected pages.

If a validation command fails:

- explain the failure;
- fix it when possible;
- rerun the validation;
- report any remaining limitation clearly.

## GitHub Actions and GitHub Pages

The documentation is deployed to GitHub Pages through GitHub Actions.

Keep the deployment model simple and stable.

Preferred workflow:

```text
push to documentation branch -> MkDocs build -> deploy to gh-pages
```

Do not manually modify generated GitHub Pages output.

Do not change the deployment branch, repository visibility or publishing
strategy without explicit confirmation.

## Safe change policy

For this repository, low-risk changes must be completed autonomously.

When the task scope is clear and the change is low risk, do not stop for an
approval step. Apply the change, run the required validation commands, create a
focused commit and push it to the repository.

Low-risk changes:

- fixing typos;
- improving headings;
- improving tables;
- adding cross-links;
- adding checklist items;
- clarifying procedures;
- updating MkDocs navigation consistently;
- adding new documentation pages;
- improving CI validation for documentation.

Ask for confirmation before:

- deleting files;
- deleting documentation sections;
- replacing downloadable .db, .zip, .xlsx, .dwg, .dxf or archive
  files;
- changing repository visibility;
- changing branch strategy;
- force-pushing;
- modifying secrets or credentials;
- publishing releases;
- changing GitHub Pages deployment strategy;
- introducing external dependencies not needed for documentation validation.

## Commit and pull request rules

Use focused commits.

Use clear commit messages.

Recommended commit prefixes:

- `docs:`
- `ci:`
- `chore:`
- `fix:`
- `refactor:`

For pull requests, include:

- summary of changes;
- validation performed;
- files or sections affected;
- any item marked as `Da verificare`.

## Quality bar

A change is complete only when:

- the documentation remains coherent;
- the navigation builds correctly;
- no sensitive information is introduced;
- the build passes or the failure is clearly explained;
- the affected pages remain practical and operational;
- new content is connected to standards, playbooks, known issues or quality
  gates where appropriate.
