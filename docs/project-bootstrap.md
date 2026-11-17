# Project Bootstrap and Rule Maintenance

`project-bootstrap` is independent of the governance Skill. It manages how an agent reads project instructions, **not** how it performs ordinary development.

## Bootstrap

```text
$project-bootstrap
```

Inspect the current repository, its root and nested `AGENTS.md` files, README, source layout and conventions. Reconcile root instructions without overwriting existing content.

### Documentation location

Follow existing conventions first. Without a convention, use `docs/` for project-wide documents and place module-specific docs near their module. The active agent decides what documents and detail the project needs, consistent with user requests, standards, design and product delivery. Do not enforce a fixed document count or format.

### Default rule behavior

**Do not create `.agents/rules/`, `general.md`, `testing.md` or other rule files as a side effect of bootstrap.** If approved rules already exist, add exact conditional links to real paths in `AGENTS.md`. Other Harnesses are not guaranteed to scan that directory.

## Add or revise a proven rule

```text
$project-bootstrap add-rule
```

Use after repeated failures with a verified cause and a demonstrated need for a lasting rule, or when the user requests an explicitly specified rule. The agent should:

1. Review examples, root cause and scope; a single unexplained failure is not enough.
2. Check existing rules, tests, source and project documentation to avoid duplicating instructions.
3. Propose a targeted, testable rule and note situations where it should **not** apply.
4. Get the user's approval to persist it unless the current request already authorizes that exact rule.
5. Create or update `.agents/rules/<topic>.md`.
6. Update `AGENTS.md` with a working relative path and **when-to-read** condition.
7. Verify no contradictory rules or duplicate index entries; inspect the diff and report changes.

Example `AGENTS.md` entry, only if the file exists:

```markdown
## Task-specific rules
- When changing STM32 DMA/cache code, read
  [.agents/rules/stm32-dma.md](.agents/rules/stm32-dma.md).
```

Periodically revise or delete obsolete rules with approval; do not accumulate rules for hypothetical problems.

## Source-of-truth boundaries

Use source and verified tests to understand current implementation. Preserve standards, customer requirements and approved interfaces as intended behavior. Design/implementation/tests/documentation remain tasks for the active agent; Grill/Wayfinder are optional.

See `skills/project-bootstrap/references/AGENTS.template.md` and `rules.template.md` for *examples*, not files to copy into every new project.
