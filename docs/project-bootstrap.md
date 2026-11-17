# Project Bootstrap and Rule Maintenance

`project-bootstrap` maintains the portable project entry point and project-specific rules. It does not take over ordinary design, implementation, TDD, testing or documentation from the active agent.

## Bootstrap

```text
$project-bootstrap
```

Read the project structure, README, source, build settings and existing instructions. Create or reconcile root `AGENTS.md` while preserving existing conventions.

### Documentation locations

Follow project conventions first. Without one, use `docs/` for project-wide material and module directories for module-specific material. Agent documentation is based on the user and project's needs, without a fixed count or detail restriction.

### Rule directory policy in AGENTS.md

**`AGENTS.md` names only the directory `.agents/rules/`, not any individual rule files.** It tells the agent to inspect that directory when it exists and read relevant rules; when absent, proceed without additional project rules. An agent Harness is not assumed to load this path automatically.

The default bootstrap **does not create `.agents/rules/`, `INDEX.md`, generic rule files or placeholders**.

An appropriate `AGENTS.md` section is:

```markdown
## Project Rules
- Project-specific rules live in `.agents/rules/`; this directory is created only when needed.
- If the directory exists, inspect its files and read applicable rules for this task.
- If it does not exist, there are no additional project rules.
- The runtime is not assumed to auto-load this directory.
```

No per-rule file links or applicability lists should be added to `AGENTS.md`.

## Add, edit, merge and delete rules

```text
$project-bootstrap add-rule
```

Use for repeated, evidenced agent problems with confirmed root causes. A single speculative failure does not justify a permanent rule. An explicit user request can authorize a specified rule.

1. Examine existing code/tests, the repeated failure, and any existing project rules.
2. Propose targeted behavior and scope; obtain user approval unless the exact change was already requested.
3. On first addition, create `.agents/rules/` and the approved `<topic>.md` file. Each rule describes its own applicability, evidence and exceptions.
4. For revision, merge, rename or removal, edit the affected rules. Keep any optional `.agents/rules/INDEX.md` internally consistent, if used.
5. **Do not modify `AGENTS.md` for rule maintenance.** It remains a stable directory-level pointer. If a legacy project has no directory-level policy, use the separate bootstrap operation to add it once.
6. Verify referenced files exist, no rule was duplicated and the diff is limited to intended rule directory changes.

For many rules, an optional `INDEX.md` *inside `.agents/rules/`* can summarize names and applicability. For a few easily inspected rules, it is unnecessary. Avoid creating index or placeholder files at bootstrap.

When a rule becomes obsolete, merge/revise/delete it with authorization. After the last rule is deleted, remove any empty index; Git does not track empty directories.

See the format example at `skills/project-bootstrap/references/rules.template.md`.

## Sources of truth

Code and verified tests describe current implemented behavior. Standards, approved requirements, interfaces and hardware constraints describe intended behavior. Conflicts must be raised rather than silently resolved. Grill and Wayfinder are optional helpers.
