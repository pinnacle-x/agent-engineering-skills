# Project Bootstrap — New and Existing Projects

Use `$project-bootstrap` to enter either a greenfield project or one that already contains engineering source files.

## New project: no established codebase

1. Identify the actual project goal and confirmed needs and technology choices.
2. Record important unresolved design questions without inventing an architecture.
3. Create/reconcile root `AGENTS.md` and existing documentation where appropriate. Do not initialize Git, generate production code or make design decisions as a bootstrap side effect.
4. Once the necessary decisions are settled, the **agent executes the requested project work directly**.

## Existing project: source-first adoption

**Use current source, build configurations and observed engineering state as the starting factual standard**, not older chat history or an outdated README.

1. Read the actual modules, interfaces, toolchain/project configuration, relevant hardware or protocol source files, tests, README and existing architecture/requirements records. Run safe existing checks when possible and record what was actually verified.
2. Extract a current-state baseline with file/path and test evidence. Separate what the project **currently does** from what someone has confirmed it **must do**.
3. Use that baseline to **create or update confirmed project requirements and technical-constraints documents**. Keep previously approved customer requirements, standards and contract obligations; do not quietly rewrite them to match a possibly incorrect implementation.
4. If source-only evidence suggests a requirement but does not prove user or standards approval, record it as **pending confirmation**. Do not mislabel an inferred intention as confirmed.
5. Preserve existing authoritative documentation and locations. When absent, use `docs/requirements.md` and `docs/technical-constraints.md`. Reuse existing equivalents rather than creating duplicates.

Optional reference formats: `skills/project-bootstrap/references/requirements.template.md` and `technical-constraints.template.md`. They are **templates**, not source facts.

## AGENTS.md and rule directory

Create root `AGENTS.md` only when absent; otherwise reconcile existing instructions without overwriting user content. The rule policy mentions just the directory:

```markdown
## Project Rules
- Project rules are stored in `.agents/rules/`, created only when needed.
- If the directory exists, inspect the files and read rules relevant to the task.
- If absent, proceed without additional project rules.
- Do not assume the runtime automatically loads the directory.
```

Do not add per-rule filenames, indices or rule applicability descriptions to `AGENTS.md`. Do not create the empty `.agents/rules/` directory or placeholder files during bootstrap.

## Rule maintenance

```text
$project-bootstrap add-rule
```

Use only for repeated, confirmed agent problems or an explicitly authorized specific rule. Check the actual cause, current code/tests and existing rules before writing a scoped rule. Seek approval before persisting unless the request already authorizes the exact action.

Create/modify/merge/rename/delete rules **inside `.agents/rules/`**; optionally maintain `.agents/rules/INDEX.md` there when useful. Never change `AGENTS.md` just because a rule file changed.

The bootstrap and governance Skills remain independent.
