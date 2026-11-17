---
name: engineering-governance
description: Optional integrated verification and reproducible releases for single-Git or multi-Git products, using source evidence, current architecture and high-level design, and approved decisions/specs discoverable through project and upstream tracker guidance.
---

# Engineering Governance

Use when system-level integration evidence or reproducible release coordination is needed. The active Agent handles normal code changes, affected-module checks and architecture/overview synchronization directly.

## Invocation

```text
$engineering-governance
$engineering-governance verify
$engineering-governance release
```

Without a mode, infer verify or release from the user request, or state that normal Agent work suffices. Skills are independently installable.

## Determine scope and applicable authority

1. Inspect the actual Git root(s), current source/build/test/hardware configuration, affected modules and dirty/uncommitted state. Folder count does not determine repository count.
2. Read root `AGENTS.md` and its real references to current system architecture/high-level design, confirmed requirements and technical constraints. Prefer existing project paths.
3. If upstream Grill is configured, read its domain/tracker guidance (often `docs/agents/domain.md` and `docs/agents/issue-tracker.md`). Use relevant applicable ADRs and identify the **actual task's** Wayfinder Map or spec when referenced/locatable. Do not pick an arbitrary `.scratch/` spec merely because it exists.
4. The actual source and observed checks show **what is implemented**; confirmed project decisions/requirements show **what was intended**. Flag conflicts and unapproved proposals instead of rewriting requirements. If important acceptance conditions remain undecided, ask for confirmation.
5. `.scratch/` records can be ignored or untracked. If required evidence depends on them, check they exist and are accessible; otherwise report the missing source instead of claiming it was reviewed.
6. Do not impose a separate change-impact process, new index, mandatory manifest or fixed number of documentation records.

## Mode: verify

1. Determine relevant system, interface, deployment and hardware acceptance checks from actual project code and current approved design.
2. **Single Git:** identify one exact commit SHA and affected modules plus any dirty state, then run/review appropriate integrated checks for the revision.
3. **Multi Git:** pin the exact SHA of each included repository and verify cross-component compatibility for that tested combination.
4. Record actual commands, artifact/revision identities, observed evidence and result per required check: `PASS`, `FAIL`, `BLOCKED`, `MANUAL_PENDING` or `NOT_APPLICABLE`.
5. Use existing report conventions; `templates/SYSTEM_VERIFICATION.md` is optional. Do not claim hardware/manual or unrun tests passed.
6. Overall verification succeeds only when every required check passes or genuinely does not apply. Highlight implementation/design discrepancies and documentation that still needs synchronization.

## Mode: release

1. Confirm requested version, scope, verified revision(s) and applicable acceptance conditions.
2. Only release revisions matching required successful verification. Dirty/unrecorded content that prevents reproduction is a blocker.
3. **Single Git:** use one verified SHA and project tag/release conventions, without a multi-repository manifest by default.
4. **Multi Git:** pin every included, actually verified SHA in the project's existing/preferred composition format; introduce a manifest only when reproducibility demands it.
5. Preserve previously published releases, do not substitute a moving branch for immutable identity, and report any required checks not performed.
6. Ensure long-lived architecture/overview documents accurately identify the current implementation and known pending approved target changes before presenting a release as fully documented.

## Separation

`project-bootstrap` establishes a project entry and can synchronize current system architecture/high-level design via `update-design`. This governance Skill consumes those documents and the native upstream decision records; it does not duplicate them or control ordinary Agent execution.
