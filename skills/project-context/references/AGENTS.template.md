# Project Agent Instructions

Adapt to the actual project, existing `AGENTS.md`/`CLAUDE.md` guidance and real file paths. Do not fabricate documents or approval.

## Project entry

- Existing project: use source/build/hardware files and observed results to establish **current behavior**; read approved requirements to establish **intended behavior**.
- New project: begin with confirmed goals and constraints, and clarify consequential unresolved decisions with Grill/Wayfinder as needed throughout the work.
- The agent directly executes tasks with a confirmed plan. If evidence and approved design disagree, flag the conflict rather than rewriting the approved design.

## Engineering documentation

- **System architecture:** `docs/architecture.md` (when present; replace with the project's real authoritative path).
- **High-level design:** `docs/design-overview.md` (when present; replace with the project's real authoritative path).
- **Confirmed requirements / technical constraints:** `docs/requirements.md` and `docs/technical-constraints.md` when present, or the project's equivalents.
- **Grill domain guidance:** `docs/agents/domain.md` when configured; consult applicable Glossary and ADRs through it.
- **Local Markdown tracker:** `docs/agents/issue-tracker.md` when configured; use it to locate the relevant Wayfinder Map or spec. The relevant Map/spec must be selected by task context or explicit reference, not guessed by folder name.
- A project may have an existing document index; consult it if present. Do **not** create another index by default.
- After meaningful code or design changes, reconcile **affected current architecture and high-level design sections** with source and accepted decisions. Mark target-but-unimplemented or disputed behaviors clearly; do not silently update approved requirements to match code.
- Read only applicable documents. Existing established paths take precedence over example paths above.

## Project Rules

- Project rules live in `.agents/rules/`. Create the directory only when a real approved rule is needed.
- When it exists, inspect its contents and read relevant rules; otherwise continue without extra project-specific rules.
- Do not assume runtime automatic loading; manage individual rules and any internal index inside the directory.

## Completion

- Report actual checks, affected document synchronization, pending design decisions and unverified items.
