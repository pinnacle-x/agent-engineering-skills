# Project Bootstrap — Project Entry and Documentation Index

`$project-bootstrap` enters a new project or an existing source project and establishes an agent-readable document map. It is **not a one-time approval of all future design decisions**.

## New project

1. Establish confirmed goals and constraints; identify first important unknowns.
2. Use `grill-with-docs` for a focused consequential decision or `wayfinder` for broad multi-stage ambiguity when suitable.
3. Record the proposed outcome, obtain user/project confirmation, and ensure the **accepted design document** is available at an actual project path.
4. Establish root `AGENTS.md` and a document index (normally `docs/README.md`). Link only real documents, not imagined architecture or placeholder files.
5. Let the agent execute the confirmed scope directly. At later project phases or major design changes, repeat design confirmation and document/index maintenance.

## Existing project: code first, then continually refine the scheme

1. Inspect real source, build/project files, interface/hardware artifacts, tests and current working state.
2. Document present implementation facts with file references and relevant revision/test evidence. Do not replace current reality with older conversations.
3. From that baseline, **establish confirmed requirements and technical constraints**, preserving approved external standards and decisions. Use the established authoritative documents; absent a convention, `docs/requirements.md` and `docs/technical-constraints.md` are defaults.
4. Separate **current observed behavior** from **approved intended behavior**. Source-only assumptions about requirements belong under **Pending confirmation** until accepted.
5. Set up the document index to link those records and any confirmed architecture, protocol, design outputs and current source-evidence records.
6. New features, discovered conflicts and subsequent subsystem choices may invoke Grill/Wayfinder again. Each **confirmed** scheme is recorded and indexed before the agent executes that scope directly.

## Root AGENTS.md: stable paths

The root `AGENTS.md` points to:
- the actual **project document index** (normally `docs/README.md`), which links to effective project documents and their statuses;
- the `.agents/rules/` **directory**, which contains optional, approved, task-specific rules.

Do not add each document or rule file to `AGENTS.md`. The index and rules folder own their respective internal discovery details. If the project already uses a document map elsewhere, reuse it and reference its actual path.

Suggested wording lives in `skills/project-bootstrap/references/AGENTS.template.md`. A document index example is `skills/project-bootstrap/references/docs-index.template.md`. These are adaptable references, not required final filenames.

## Updating documents after future design rounds

A project is not frozen after bootstrap. Whenever a consequential design question is settled:

1. Update the authoritative design/requirements/constraints document or link to the confirmed Grill/Wayfinder output.
2. Update the document index with path, scope, confirmation status and supersession where relevant.
3. The agent reads the active scheme and current source and executes directly.
4. If later evidence or new requirements change the decision, repeat the loop; do not silently apply an obsolete scheme.

The agent can maintain the document index as part of ordinary project work; **there is no need to call bootstrap for every new confirmed decision**.

## Rules

No empty `.agents/rules/` directory is created during bootstrap. Use `$project-bootstrap add-rule` for specifically authorized or repeatedly evidenced rules. Maintain rule files and an optional `.agents/rules/INDEX.md` internally; no per-rule `AGENTS.md` edits.

See [Document Discovery](document-discovery.md) and [Sources of Truth](source-of-truth.md).
