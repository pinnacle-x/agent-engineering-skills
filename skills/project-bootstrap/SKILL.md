---
name: project-bootstrap
description: Initialize or reconcile a portable AGENTS.md with a stable .agents/rules/ directory convention. Maintain approved, evidence-based project rules within that directory without changing AGENTS.md for individual rule additions, updates, merges, or deletions.
---

# Project Bootstrap

This Skill maintains the repository's portable agent entry instructions and **on-demand project rules**. It is independent of engineering-governance. The active agent owns code exploration, planning, specs, TDD when useful, implementation, debugging, tests and task-appropriate documentation.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule
```

For modifying, merging or deleting existing rules, ask `project-bootstrap` to maintain the relevant project rules; the `add-rule` mode can reconcile existing rules rather than creating duplicates. If the Harness does not support command shorthand, request the Skill by name in natural language.

## Common prerequisites

1. Identify the actual project root (and Git root when present); inspect `git status`, current root/nested `AGENTS.md` files, README, source, tests, existing documents and `.agents/rules/` if it exists.
2. Preserve existing project conventions, source code, build configuration, Git metadata and user changes.
3. Code and executed tests are evidence for **implemented behavior**. Preserve external standards, approved requirements, interfaces and hardware constraints as sources for **intended behavior**; report conflicts.
4. Do not claim that any Harness automatically discovers `.agents/rules/`. The `AGENTS.md` directory instruction directs the active agent to inspect it when present.

## Mode: bootstrap (default)

1. Create the root `AGENTS.md` only if missing; otherwise reconcile it without duplicating or overwriting unrelated guidance. Preserve meaningful nested `AGENTS.md` files.
2. Include project orientation and a **stable directory-level rule policy**. The only rule location that `AGENTS.md` needs to name is `.agents/rules/`; **do not enumerate individual rule files or maintain a per-rule index in AGENTS.md**.
3. The rule policy must say: if `.agents/rules/` exists, inspect its current contents and read applicable rules for the task; if absent, there are no extra project rules. The directory is **not** assumed to be auto-loaded by the Harness.
4. **Do not create an empty `.agents/rules/` directory, `INDEX.md`, `.gitkeep` or individual rule files by default.** Existing project rules remain in place. If AGENTS.md contains legacy per-rule links, propose a one-time consolidation into the directory policy during bootstrap, respecting user-approved instructions.
5. For project documentation, follow the existing structure first. Without a convention, use `docs/` for project-wide documents and the relevant module for module-specific documents; the agent decides type, detail and amount based on task needs.
6. Do not install other Skills, invent ADRs/specifications, configure issue trackers, initialize Git, modify production code, or change Git remotes as a side effect.

## Mode: add-rule and rule maintenance

Use after user request or repeated, evidenced agent failures with a confirmed cause. Do not persist speculative rules for a single unexplained error.

1. Review the repeated problem, root-cause evidence and task scope. Prefer a code/test/configuration fix where appropriate.
2. Inspect existing `.agents/rules/` files and any local index. Avoid duplicates and conflicting instructions; propose a clear, narrow, testable rule with exceptions.
3. Seek user approval to persist, merge, revise or delete lasting rules unless the current request already authorizes the **specific** change.
4. Create `.agents/rules/` only when persisting the first approved rule. Store rules as `.agents/rules/<topic>.md` and include their applicability in the rule itself. For revisions or merges, update the relevant files; for deletion, remove obsolete files after verifying dependencies.
5. **Never update root `AGENTS.md` merely because a rule was added, revised, merged, renamed or deleted.** AGENTS.md permanently points only to `.agents/rules/`. If that directory policy is missing, recommend running the separate bootstrap mode to reconcile it; do not silently mutate AGENTS.md from this mode.
6. For larger rule sets where discovery needs help, optionally maintain `.agents/rules/INDEX.md` with file names, scopes and when-to-read conditions. The index is **inside `.agents/rules/`** and is maintained there after rule additions, updates, merges, renames or deletions. For a small rule set, reading files directly is sufficient; do not generate an index just to satisfy a template.
7. If the last rule is deleted, remove a now-useless index rather than leaving placeholders. Do not impose a fixed rule count or assume Git tracks empty directories.
8. Verify existing links/index references, check for overlap/conflicts and inspect the diff; running this mode twice must not duplicate entries or rule files.

## Stable AGENTS.md rule policy

The generated `AGENTS.md` should contain directory-level instructions like:

```markdown
## Project Rules
- Project-specific rules live in `.agents/rules/`; the directory is created only when needed.
- When it exists, inspect its contents and read rules applicable to the current task.
- If the directory does not exist, proceed without additional project-specific rules.
- Do not assume the agent runtime automatically loads this directory.
```

**No individual rule filenames, applicability mappings or internal index paths belong in AGENTS.md.** Those details can be stored and maintained in the rule files themselves or in an optional index under `.agents/rules/`.

## Verification and reporting

- Inspect changed files and `git diff` / `git status` where available.
- Confirm bootstrap creates no rules directory by default; validate the single directory-level policy.
- Confirm rule maintenance changes only the rules directory (unless the user separately requested unrelated edits), and internal index entries correspond to existing rule files.
- Report files added/modified/deleted, rationale, evidence, user approvals, conflicts and checks not performed. Do not claim automatic Harness discovery or unexecuted tests.

## Boundaries

- The active agent owns routine design, implementation, tests and documentation.
- Grill / Wayfinder are optional when difficult unresolved design or very large ambiguous projects benefit from them.
- `engineering-governance` is optional for change impact, integration verification and release across single-Git or multi-Git projects.
