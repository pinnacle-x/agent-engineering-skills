# Agent-Led Engineering Workflow

The active agent is the **direct executor** of project work. Skills are used only when they provide additional, relevant capabilities.

## 1. Enter the project

```text
$project-bootstrap
```

- **From zero:** establish the confirmed goal, technology decisions and relevant constraints; set up the project entry instructions without inventing unapproved details.
- **Existing source:** inspect current code, build configuration, module boundaries, related hardware/interface artifacts and available verification evidence. Treat the actual engineering state as the factual baseline, then establish/update confirmed requirements and technical-constraints documents. Do not present guesses about intended behavior as confirmed requirements.
- For existing docs, preserve their established locations. Without an established convention, use `docs/requirements.md` and `docs/technical-constraints.md`.

`AGENTS.md` states only the `.agents/rules/` directory policy; rule files and an optional index live inside that directory. No empty rules directory is created. Repeated confirmed agent failures can be addressed via `$project-bootstrap add-rule` with approval; individual rule maintenance does not edit `AGENTS.md`.

## 2. Determine whether major design is unresolved

- **Clear goal and necessary decisions:** the agent executes directly, even when the engineering task is technically difficult.
- **Important unresolved design choice:** optional `grill-with-docs` to settle the decision, followed by direct agent execution.
- **Very large, ambiguous project needing extended exploration:** optional `wayfinder` to establish direction and boundaries, followed by direct agent execution.

Task difficulty or the number of changed files is **not** itself a trigger to call a design Skill. Project safety, external standards and accepted contracts remain governing constraints.

## 3. Verification and delivery, when required

The agent analyzes downstream effects on dependent modules as part of its own work; there is **no dedicated impact-analysis Skill mode**.

```text
$engineering-governance verify
$engineering-governance release
```

Invoke governance when system integration evidence or reproducible delivery warrants it. A single Git repository can contain many components and still require just one commit SHA; multi-Git products require a verified SHA for every relevant repository. Routine task checks remain with the active agent.

See [engineering governance](engineering-governance.md).
