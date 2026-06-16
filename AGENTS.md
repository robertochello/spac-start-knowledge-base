# AGENTS.md

## Purpose

This file provides operating instructions for AI agents working on this repository.

The repository is a technical knowledge base for **SPAC Start Impianti**. Its purpose is to convert practical notes, tested procedures, standards, troubleshooting cases and recurring workflows into structured, reusable documentation.

This is not a replacement for the official SPAC Start documentation. Treat it as an operational, incremental and productivity-oriented knowledge base.

## Repository context

- Documentation is written in Italian.
- The site is built with **MkDocs Material**.
- The documentation source lives mainly under `docs/`.
- Navigation is controlled by `mkdocs.yml`.
- Templates live under `templates/`.
- Playbooks live under `docs/playbooks/`.
- Known issues live under `docs/known-issues/`.
- Standards live under `docs/standards/` and in general standard pages.
- The default Git branch is `master`.

## Primary goals

When modifying this repository, optimize for:

1. fast operational lookup during real SPAC work;
2. clear and reusable procedures;
3. reduced ambiguity;
4. consistent terminology;
5. traceable decisions;
6. maintainable MkDocs navigation;
7. safe public documentation without sensitive project data.

## Editorial language and tone

Use Italian unless the existing file is clearly in English.

Preferred style:

- technical;
- concise;
- operational;
- step-by-step when documenting a procedure;
- focused on what to do, when to do it and how to verify it.

Avoid:

- generic theory without operational value;
- verbose explanations that do not support a procedure, a decision or a checklist;
- duplicated content;
- unverified claims presented as stable standards.

## Content rules

Before adding new content, check whether the information already exists in:

- `docs/07-troubleshooting.md`;
- `docs/08-standards.md`;
- `docs/11-decision-log.md`;
- `docs/12-practical-cases.md`;
- `docs/13-maintenance-guidelines.md`;
- `docs/14-quality-gates.md`;
- related pages under `docs/playbooks/`, `docs/known-issues/` and `docs/standards/`.

Add or update content only when it is useful for future work and meets at least one of these criteria:

- the issue has occurred more than once;
- the procedure has been tested;
- the solution can be reused;
- the note reduces operational ambiguity;
- the content standardizes a recurring workflow.

Do not add content that:

- is specific to a single customer, site, machine or commessa;
- contains sensitive or non-public data;
- is a temporary note with no reusable value;
- duplicates an existing section;
- is not tied to a procedure, decision, standard, known issue or checklist.

## Recommended structure for procedures

When writing a procedure, use this order where applicable:

1. `Contesto`
2. `Obiettivo` or `Problema`
3. `Procedura`
4. `Verifica finale`
5. `Note operative`
6. `Collegamenti correlati`

Each procedure should be:

- brief;
- sequential;
- testable;
- unambiguous;
- linked to standards, decisions, playbooks or checklists when relevant.

## Status labels

Use these labels when content maturity must be explicit:

| Stato | Meaning |
|---|---|
| `Testato` | Procedure verified in practice |
| `Da verificare` | Plausible note, not yet consolidated |
| `In revisione` | Content still incomplete or being corrected |
| `Deprecato` | Superseded or no longer recommended procedure |

Never upgrade content to `Testato` unless the repository context or the user explicitly confirms the test.

## SPAC-specific standards

Respect the following consolidated standards unless the user explicitly updates them.

### CAD / DXF / DWG

For CAD/DXF/DWG content intended for SPAC:

```text
Layer 0
```

All generated CAD entities should be created on Layer 0 unless a documented exception is required.

### Custom symbols

For custom SPAC symbols:

- use clear and descriptive names;
- avoid undocumented abbreviations;
- document main attributes;
- use `PRES=M` for a Mother symbol when applicable;
- use pin attributes only when the symbol is wired;
- validate the symbol in a test project before considering it stable.

### Pinning convention

The adopted pinning convention is:

```text
PINA<n>
PINB<n>
```

Use `PINB<n>` only when the signal present on `PINA<n>` is carried through to an output pin.

### Changeover contacts

Use:

```text
SCAMBIO
```

Do not use the abbreviation `SCB`.

### Symbol inventory

Do not store the complete custom-symbol inventory in the README.

The inventory should remain in the dedicated Excel file:

```text
SPAC_Custom_Simboli_Convenzione.xlsx
```

### Materials and cable archives

For material archives and `DbCables.db` work:

- never invent catalogue codes;
- never create placeholder catalogue codes based on the user's initials or internal guesses;
- prefer official manufacturer data when available;
- mark uncertain records as `Da verificare`;
- preserve or document backup/rollback logic;
- check duplicates before considering an archive stable;
- for `DbCables.db`, verify that cable records and conductor records remain coherent.

## MkDocs rules

When adding a new documentation page:

1. place it in the most appropriate existing directory;
2. avoid creating new directories unless there is clear long-term value;
3. update `mkdocs.yml` navigation if the page should appear in the site;
4. use relative internal links;
5. keep titles consistent with nearby pages;
6. run or recommend `mkdocs build --strict` after navigation or link changes.

Use Markdown features already enabled in `mkdocs.yml`, including tables, admonitions, details blocks, task lists and code highlighting.

## Local commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Preview locally:

```bash
mkdocs serve
```

Build strictly:

```bash
mkdocs build --strict
```

When changing documentation structure, navigation or links, the preferred validation command is:

```bash
mkdocs build --strict
```

## Quality gates

A documentation change is ready when:

- the objective is clear;
- the placement is coherent with the repository structure;
- the content is operational and reusable;
- sensitive data is absent;
- the procedure includes verification where applicable;
- related standards, known issues, playbooks or decisions are linked when useful;
- `mkdocs.yml` is updated if navigation changes;
- `mkdocs build --strict` passes or any failure is explicitly reported.

For troubleshooting notes, include:

- symptom;
- likely causes;
- diagnostic steps;
- solution;
- prevention or future mitigation.

For decisions, include:

- context;
- decision;
- rationale;
- impact;
- status.

For material/cable archive content, include:

- source of information;
- validation status;
- import/test notes;
- rollback or backup notes when relevant.

## Git and change-management workflow

Before editing:

1. inspect the relevant existing files;
2. identify the correct section or page;
3. prefer updating existing content over creating new parallel content;
4. keep the diff minimal and scoped.

During editing:

- do not reformat unrelated files;
- do not rename files unless required;
- do not move sections without a clear reason;
- do not delete historical decisions; mark them as `Deprecato` or superseded instead;
- do not modify secrets, credentials or private environment files.

After editing:

- summarize changed files;
- explain why the change was made;
- report validation performed;
- report any unresolved uncertainty.

Commit/push guidance:

- If the user explicitly assigns a repository task, implementation changes may be committed and pushed when they are low risk and scoped.
- Ask before high-risk operations such as force-push, deleting files, changing protected branches, modifying credentials/secrets or publishing releases.
- Prefer clear commit messages such as `Update DbCables troubleshooting notes` or `Add SPAC terminal representation playbook`.

## High-value update patterns

Prefer these update patterns:

- new recurring issue -> add or update `docs/known-issues/` and link from troubleshooting;
- new tested procedure -> add or update a playbook;
- new consolidated rule -> update standards and decision log;
- new symbol convention -> update symbol standards and checklist;
- new cable/material archive workflow -> update archive page, related playbook and quality gates if needed;
- new command discovered in SPAC -> update command reference and related procedure.

## Repository-specific priorities

Current high-value areas are:

- completing multifilare documentation;
- improving rimandi, morsetti and cross-reference workflows;
- consolidating custom symbol standards;
- improving material and cable archive procedures;
- keeping known issues actionable;
- linking practical cases to decisions and standards;
- maintaining a clean MkDocs navigation.

## Final operating principle

Keep the knowledge base useful during real SPAC work.

If a change does not help decide, solve, standardize, verify or reuse something, simplify it or do not add it.