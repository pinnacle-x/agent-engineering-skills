# Agent-Led Engineering Workflow

## Start from what is known

- **Greenfield project:** begin from confirmed product goals and external constraints, not invented source.
- **Existing project:** inspect actual source/configuration/hardware artifacts/tests first. Document implemented facts with evidence, then establish confirmed requirements and technical constraints without assuming the code represents approved intent.

Use `$project-bootstrap` to establish accurate project entry instructions and current long-lived documents. Do not create another index unless an existing project already uses one or its real documentation complexity warrants it.

## Repeated decisions, directly executed

```text
Important unresolved question
       ↓
grill-with-docs (focused) / wayfinder (multi-session)
       ↓
User/project authority confirms proposal
       ↓
Use native persisted decisions (glossary/ADR/Map); to-spec if useful
       ↓
Agent finds applicable approved scheme and actual source
       ↓
Agent directly executes and checks the change
       ↓
Sync affected current architecture/high-level design
       ↓
New major decision? → repeat; otherwise continue
```

The user invokes Grill/Wayfinder/to-spec in a compatible Harness; do not assume the active Agent can implicitly invoke Skills marked user-only. Ordinary bug fixes and changes already covered by an approved scheme do not demand a new design interview.

## Local Markdown decisions and specs

Prefer upstream `/setup-matt-pocock-skills` with **Local Markdown**, which configures `docs/agents/issue-tracker.md` (or existing equivalent) and domain guidance. Wayfinder's Map/tickets and `to-spec`'s task specs stay under configured `.scratch/` locations. This is not GitHub Issues and is not a second project design system.

A Map is a **decision index**, not a complete product design. `to-spec` writes a **task-level snapshot**, not a living architecture document. To continue a task, identify its relevant spec/Map from the request, branch or real project references; configuration alone does not determine which spec is active. If the work can be executed from an approved ADR and existing design, a new spec may not be warranted.

Always check `.gitignore` and whether important `.scratch/` records will survive a new checkout.

## After code changes: keep long-lived documents aligned

The Agent checks whether the current system architecture or high-level design was affected. Update only relevant sections, backed by actual source and known approvals; do not overwrite accepted decisions to make documents agree with a buggy implementation.

For deliberate architecture/overview documentation work:

```text
$project-bootstrap update-design
```

Reuse existing architecture/overview paths, else use `docs/architecture.md` and `docs/design-overview.md` when enough evidence exists. If design and implementation diverge, describe **Current**, **Confirmed target** and **Pending resolution** separately.

## Optional integration and release

```text
$engineering-governance verify
$engineering-governance release
```

Governance reads the current code, approved requirements/architecture, applicable ADRs and selected task spec. Single-Git uses one immutable SHA; multi-Git pins the exact verified revision combination. Routine task checks remain with the Agent.
