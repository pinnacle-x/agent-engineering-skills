# Sources of Truth

## Current implementation versus approved intent

- **As built:** actual source, build configuration, hardware artifacts and observed results are facts of the **current implementation**. Record file paths and relevant revisions/check evidence.
- **As designed:** approved requirements, accepted technical choices, applicable ADRs, accepted interface contracts and the task's confirmed spec/decision record govern **intended behavior**.
- **Pending or replaced:** drafts, unapproved discussions and superseded decisions are not instructions to silently implement.

A defect or design discrepancy is a discrepancy to resolve, not permission to silently rewrite approved requirements or ADRs.

## Upstream decision artifacts

Grill's glossary and qualifying ADRs, and Wayfinder's configured Map/decision tickets, remain the canonical decision sources. `to-spec` produces a task-oriented snapshot in the configured tracker, typically `.scratch/<feature>/spec.md` for Local Markdown. Do not copy a complete spec or decision Map into another mandatory docs index.

When an important approved decision exists only in conversation, preserve the missing durable content in the project's appropriate authoritative record. Do not pretend every Grill outcome is saved as an ADR.

## Living engineering design

System architecture and high-level design describe the **current** system, plus clearly separated approved future targets where appropriate. They should be reviewed when code or design choices materially affect them, using the actual source and approved decisions. Their purpose is not to replay every decision or ticket.

Existing project filenames and hierarchy take priority; when absent and justified, use `docs/architecture.md` and `docs/design-overview.md`. The Agent maintains these in ordinary work or through `$project-bootstrap update-design`.

## Finding documents across sessions

`AGENTS.md` provides real stable pointers to current long-lived docs and upstream tracker/domain configuration. No new mandatory `docs/README.md` index is required. Because `.scratch/` may be ignored or local-only, portability of task specs must be checked explicitly. The correct active spec must be determined by task/branch/project reference, not guessed simply because a file exists.

## Shared contracts

Keep one authoritative owner of a shared protocol/interface. The Agent checks affected consumers while doing engineering work; `engineering-governance verify` can gather system-level evidence for the verified revision combination.
