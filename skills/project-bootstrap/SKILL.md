---
name: project-bootstrap
description: Initialize or reconcile a repository's portable AGENTS.md entry point, explicit .agents/rules, and minimal project documentation. Use for new or imported projects; preserve existing files and never overwrite source code.
---

# Project Bootstrap

Create the smallest useful, harness-neutral project instruction layer. This Skill is independent of PraxFlow, Grill, and any particular agent runtime. It is prompt-driven and uses the active agent's normal repository/file tools; it does not require a special bootstrap executable.

## When to use

- A new repository needs an `AGENTS.md` entry point and explicit rule discovery.
- An existing repository needs its agent rules organized without losing current conventions.
- A project is moving between agent harnesses and needs portable project instructions.

Do not invoke for ordinary feature work, code review, protocol changes, releases, or when the user only wants to read an existing repository.

## Non-destructive constraints

1. Locate the actual project/repository root. Inspect `git status` when Git exists. Do not initialize Git or change remotes without explicit instruction.
2. Read existing `AGENTS.md`, `README.md`, `.agents/`, `docs/`, source/build layout, and any existing agent or engineering configuration before writing.
3. Existing project rules, decisions, source files and documentation are inputs to reconcile, not objects to replace. Preserve unrelated content and comments. Never overwrite an existing file with a generic template.
4. Do not modify production source, hardware design, build settings, dependencies, secrets, CI or Git configuration as a side effect.
5. Do not create made-up technical requirements, project status, architecture records, release versions or placeholder documents.
6. If existing instructions conflict or ownership cannot be determined, surface the conflict and preserve both files until a decision is made. Do not silently assign precedence that contradicts the host harness or repository instructions.

## Workflow

### 1. Discover

- Identify project type (new/empty, existing single repository, or multi-repository product) and actual file layout.
- Inspect whether a root `AGENTS.md` already exists and what rule files it references.
- Inspect `.agents/rules/` and `.agents/skills/` if present. List user/global Skills only when the active harness exposes them.
- Note `docs/agents/` or other existing conventions; do not move or duplicate them just to conform to an example.
- Prefer the repository's existing working test, documentation, and Git workflow.

### 2. Plan the minimum changes

- Root `AGENTS.md` is the single portable entry point for this repository. Add it only when missing, or merge a small missing section when it exists.
- Organize stable, reusable instructions under `.agents/rules/`. At minimum create `general.md` if this convention is adopted; add `development.md`, `testing.md` and `documentation.md` only when the project has actual rules for them.
- Include an explicit rule index in `AGENTS.md` listing **only files that exist** and the conditions for loading each. Do not claim that every harness auto-loads `.agents/rules/`.
- Keep `AGENTS.md` brief. Detailed rules live in the referenced files; source code and project docs are read only as relevant to the task.
- `docs/`, `docs/adr/`, `docs/agents/`, task files and project status files are optional. Create or reuse them only when needed; never add empty formal documents.
- Do not copy global Skills into `.agents/skills/`. Project-local Skills belong there only if actually required.
- Do not introduce harness-specific configuration into the canonical `AGENTS.md` or `.agents/rules/`. Report any runtime-specific adapter needed as a separate recommendation.

Use `references/AGENTS.template.md` and `references/rules.template.md` as editable starting examples for missing files, not as universal policy. Remove unused sections and replace examples with verified project facts.

### 3. Write with reconciliation

- On a new repository, write the minimal root entry and applicable rule files.
- On an existing repository, edit the current entry point in place; preserve headings, section content and links where possible.
- Prefer linking to existing rules/documents over duplicating their content in new files.
- An existing repository may already have specialized instructions. Do not create contradictory `.agents/rules` copies merely to satisfy a directory layout.
- Do not add references to Skills that are not installed and discoverable. If mentioned as optional workflows, clearly mark them as conditional.
- Never invoke `grill-with-docs` or `praxflow` automatically as a bootstrap side effect. Their use is a later, task-specific decision.

### 4. Verify

- Confirm every path referenced from `AGENTS.md` exists and points inside the intended repository, or label it as an optional convention rather than an instruction to read a missing file.
- Confirm the rule index explains always-on and task-specific loading.
- Check for duplicate or conflicting instructions, circular references, hardcoded machine paths, and harness-specific assumptions.
- Review `git diff` and `git status` if available; verify source code and production configuration were not changed.
- Re-running bootstrap should not duplicate sections or recreate already-adopted files.

### 5. Report

Summarize (a) created files, (b) edited files, (c) preserved existing conventions, (d) rule-loading map, (e) unresolved conflicts, and (f) any optional harness adapter needed. Do not claim tests passed unless run.

## Boundaries with other Skills

- `grill-with-docs`: for major unresolved design decisions and durable ADRs, **after** initial repository entry points exist.
- `setup-matt-pocock-skills`: optional configuration of issue tracker/domain docs; may augment existing `AGENTS.md` without replacing the bootstrap entry.
- `praxflow`: a separate Skill for cross-repository contract governance, integrated verification and reproducible manifests, **not** project initialization.

If the active harness does not recognize the `$project-bootstrap` shorthand, tell the user to invoke the Skill by name in natural language.
