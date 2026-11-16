# PraxFlow Workflow

PraxFlow fills gaps in the regular agent + Grill engineering workflow; it does not replace it.

## 1. Repository bootstrap (once per repository)

```text
$praxflow bootstrap
```

Reconcile the root `AGENTS.md`, add only needed `.agents/rules/` and include explicit rule-loading conditions. Preserve existing engineering files and issue-tracker/domain-doc conventions. See [bootstrap](project-bootstrap.md).

## 2. Normal engineering and Grill

Use the active agent and companion engineering Skills for reading, specifications, planning, implementation, repository-local tests and code review.

When major design choices are unresolved, use `grill-with-docs` to interview, compare alternatives and create durable decisions/ADRs. This includes **what a protocol or public interface should mean**. Do not do a duplicate design interview in PraxFlow.

## 3. Cross-repository public contract coordination (only if applicable)

After the design is agreed and **before** consumer semantic changes:

```text
$praxflow interface-change
```

Record the owner and consumers, approved contract reference, compatibility, owner-first rollout, migration and required verification. Output: `docs/changes/IC-XXXX-<slug>.md` in the designated system/product owner repository. This is a governance record, not a second design specification. See [cross-repo-workflow](cross-repo-workflow.md).

A repository-local refactor needs neither this mode nor an extra change record.

## 4. Integrated verification

After affected repositories are implemented and locally tested:

```text
$praxflow system-verify
```

Record each repository's exact commit SHA and actual automated/integration/hardware evidence in `docs/verification/VER-<id>.md`. Unperformed manual/hardware checks remain `MANUAL_PENDING`.

## 5. Reproducible release

Only after integrated verification is `PASS`:

```text
$praxflow manifest-release
```

Pin exactly the verified repository revisions in immutable release artifacts.

## One workflow, no duplicate responsibilities

```text
PraxFlow bootstrap → AGENTS.md + rule index
         ↓
Active agent: read requirements/code/docs
         ↓
Design open? → grill-with-docs → approved ADR/contract
         ↓
Cross-repo public interface? → PraxFlow interface-change
         ↓
Owner implementation → consumer implementation → local checks
         ↓
PraxFlow system-verify → PASS → manifest-release
```

Rules: one semantic owner for each public contract; don't independently redesign it in consumers; don't claim tests that weren't run; and never release unverified revisions.
