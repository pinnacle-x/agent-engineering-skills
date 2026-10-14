---
name: praxflow
description: Lightweight cross-repository governance for product engineering. Use only for public interface changes, integrated system verification, and reproducible multi-repository releases. Let the agent and companion skills handle PDF reading, repository discovery, design, specification, protocol analysis, implementation, testing, and code review.
---

# PraxFlow

PraxFlow is deliberately narrow. Modern agents can already read PDFs and code, inspect repositories, analyze protocols, draft specifications, run tests, and review implementation. PraxFlow must not duplicate those capabilities.

Use PraxFlow only where a multi-repository product needs durable governance that is easy to lose across independent agent sessions or repositories:

1. owner-first public interface changes;
2. integrated verification tied to exact repository revisions;
3. reproducible releases that pin the verified repository combination.

## Invocation

```text
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

If `$praxflow` is invoked without a mode, infer the mode only when the request clearly matches one of the three modes. Otherwise explain that PraxFlow is not needed and use the agent's native capability or an appropriate companion skill.

## What PraxFlow does not do

Do not use PraxFlow for:

- PDF reading, OCR, extraction, or document interpretation;
- repository bootstrap or creation of `AGENTS.md`;
- codebase/repository discovery;
- domain modeling or design interviews;
- specification drafting or materialization;
- generic specification validation;
- protocol analysis or protocol validation;
- implementation, TDD, debugging, or code review;
- routine single-repository work.

Use the active agent's native capabilities for those tasks. For important unresolved design choices, use a dedicated design-review skill such as `grill-with-docs` when installed.

## Global governance rules

These rules apply to all PraxFlow modes:

- A public fact or interface has one owner repository.
- Consumers reference the owner contract instead of maintaining divergent definitions.
- Public contract changes are owner-first.
- Unknown or conflicting facts are never guessed into a cross-repository contract.
- Exact repository revisions must be recorded for integrated verification and release.
- Manual or hardware checks are never marked `PASS` without explicit evidence.
- A release must correspond to a successfully verified repository combination.
- Existing released manifests are immutable unless the user explicitly authorizes a correction and the correction policy is documented.

---

# Mode: `interface-change`

Use before implementing a change that modifies a contract consumed by more than one independent repository, such as a protocol command, register, public API, data schema, shared state, or hardware/software boundary.

Do not use this mode for a change contained entirely inside one repository.

## Read first

Use the agent's normal repository-reading capability. When available, inspect:

1. the system/product repository rules and relevant cross-repository documentation;
2. the owner repository contract/specification;
3. affected consumer repository rules and relevant contract references;
4. the development manifest when one exists.

Do not require PraxFlow-specific spec files. Use whatever source of truth the repositories already define.

## Actions

1. Identify the public contract being changed.
2. Identify its owner repository.
3. Identify every known consumer and affected repository.
4. Classify the change as `compatible`, `conditionally-compatible`, or `breaking`.
5. Record the current contract and proposed contract.
6. Define the owner-first update order.
7. Define migration/versioning requirements when needed.
8. Define automated, integration, and hardware/manual verification needed.
9. Surface unresolved high-impact design choices instead of resolving them silently. Recommend `grill-with-docs` or another human-in-the-loop design review when appropriate.

## Output

Create the change record in the product/system owner repository:

```text
docs/changes/IC-XXXX-<slug>.md
```

Choose the next available stable numeric ID without rewriting existing IDs.

The record must contain:

- goal;
- owner repository;
- affected repositories;
- current contract;
- proposed contract;
- compatibility classification;
- required owner changes;
- required consumer changes;
- implementation order;
- migration/versioning notes;
- required tests;
- manual/hardware checkpoints;
- unresolved decisions;
- approval status.

## Gate

Do not implement consumer-side semantic changes before the owner contract has been updated and approved according to the project's normal process.

Stop after producing the cross-repository change plan unless the user explicitly asks to continue with implementation using the agent's normal tools.

---

# Mode: `system-verify`

Use after all repositories affected by a product-level change are implemented and ready for integration verification.

This mode does not replace repository-local tests. It binds their results and integration evidence to one exact multi-repository revision set.

## Inputs

Accept one of:

- an interface-change ID such as `IC-0001`;
- a release-candidate identifier;
- an explicit product verification goal.

## Actions

1. Identify all repositories required by the verification scope.
2. Record the exact branch/tag and commit SHA for every included repository.
3. Read each repository's existing build/test instructions rather than inventing PraxFlow-specific commands.
4. Run available automated repository-local tests when permitted.
5. Run or coordinate available integration tests.
6. Confirm that public contract versions/revisions match across owner and consumers.
7. Record hardware/manual checks separately.
8. Never convert an unperformed manual/hardware check into `PASS`.

## Status values

For each required check use one of:

- `PASS`
- `FAIL`
- `BLOCKED`
- `MANUAL_PENDING`
- `NOT_APPLICABLE`

Overall verification is `PASS` only when every required check is `PASS` or `NOT_APPLICABLE`.

## Output

Create in the system/product repository:

```text
docs/verification/VER-<id>.md
```

Include:

- verification goal/change ID;
- exact repository revisions;
- public contract/interface revision references;
- commands actually executed;
- automated test results;
- integration results;
- hardware/manual results;
- failures/blockers;
- overall result;
- evidence references.

## Gate

If the result is not `PASS`, do not proceed to `manifest-release`.

---

# Mode: `manifest-release`

Use only after `system-verify` has produced an overall `PASS` for the exact repository combination being released.

The purpose of this mode is reproducibility, not release-note writing alone.

## Preconditions

Require:

- a requested product version;
- a successful system verification artifact;
- exact immutable repository revisions from that verification;
- a manifest repository or another explicitly designated product-composition owner.

Stop if any required verification is `FAIL`, `BLOCKED`, or `MANUAL_PENDING`.

## Actions

1. Confirm every release revision exactly matches the successful verification record.
2. Reject dirty or unrecorded workspace state when it prevents reproducibility.
3. Pin every included repository to an immutable revision, normally a commit SHA or approved immutable tag.
4. Preserve the development manifest separately from the immutable release manifest unless the user explicitly requests a baseline update.
5. Create a human-readable release record tied to the verification artifact.

## Outputs

Create:

```text
releases/v<version>.xml
releases/v<version>.md
```

If the project uses a non-XML manifest format, preserve the same semantic rule: the release record must pin the exact verified revisions.

The release record must include:

- product version;
- source verification artifact;
- repository names/paths and pinned revisions;
- relevant public interface/protocol versions when applicable;
- known limitations;
- release date when available;
- reproducibility instructions.

## Rules

- Do not release moving branch names such as `main` or `develop` as the authoritative revision when an immutable commit is available.
- Do not release unverified revisions.
- Do not silently rewrite an existing released version.

Stop after creating the release artifacts and reporting the exact pinned revisions.
