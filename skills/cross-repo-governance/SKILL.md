---
name: cross-repo-governance
description: Coordinate approved public contract changes across independent repositories, bind integrated verification to exact revisions, and create reproducible multi-repository release manifests. Do not duplicate Grill's design or ordinary agent implementation.
---

# Cross-Repo Governance

This Skill is only for **multi-repository governance**. It does not initialize repositories, create AGENTS.md, conduct design interviews, create ADRs, implement code, or replace repository-local tests.

The active agent and general engineering Skills handle repository inspection, protocol/code analysis, implementation, local tests and reviews. Use `grill-with-docs` **when substantial interface design decisions are unresolved**, then reference the approved ADR/contract in the governance record.

## Invocation

```text
$cross-repo-governance interface-change
$cross-repo-governance system-verify
$cross-repo-governance manifest-release
```

If the harness does not recognize this invocation shorthand, request the `cross-repo-governance` Skill by name and specify its mode. If the request does not require multi-repository governance, do not invoke this Skill.

## Scope and exclusions

- **interface-change:** public contract ownership, consumers, approved compatibility/migration plan and owner-first rollout across separate repositories. Do **not** independently decide contract semantics or duplicate an ADR.
- **system-verify:** integration evidence tied to exact commit SHA of every included repository; manual and hardware tests need explicit evidence.
- **manifest-release:** immutable product composition manifest based on an overall `PASS` verification record.
- **Excluded:** project initialization, writing AGENTS.md/rules, PDF extraction, ordinary source exploration, specification authoring, routine code review, unit tests or local refactors.

## Global governance rules

1. Every public contract has one semantic owner repository. Consumers reference the owner contract.
2. Unknown/conflicting interface facts must be resolved by the contract owner or design review, never silently invented.
3. Update and approve the owner contract **before** consumer semantic changes.
4. Integrated verification records the exact revision of each participating repository.
5. Hardware/manual steps remain `MANUAL_PENDING` until evidence supports completion.
6. Release only a revision set that passed all required verification; do not silently alter released manifests.

---

# Mode: `interface-change`

Use before implementing a change that modifies a contract consumed by more than one independent repository, such as a protocol command, register, public API, data schema, shared state, or hardware/software boundary. **This mode governs an agreed design; it does not replace Grill.** If important semantics or tradeoffs remain undecided, use `grill-with-docs` first and continue only with the approved contract/ADR.

Do not use this mode for a change contained entirely inside one repository.

## Read first

Use the agent's normal repository-reading capability. When available, inspect:

1. the system/product repository rules and relevant cross-repository documentation;
2. the owner repository contract/specification;
3. affected consumer repository rules and relevant contract references;
4. the development manifest when one exists.

Do not require Cross-Repo Governance-specific spec files. Use whatever source of truth the repositories already define.

## Actions

1. Identify the public contract being changed.
2. Identify its owner repository.
3. Identify every known consumer and affected repository.
4. Based on the already approved design, classify the change as `compatible`, `conditionally-compatible`, or `breaking` and flag uncertainty for human resolution.
5. Reference the owner-controlled current and approved proposed contract; do not write a rival semantic contract or decide missing interface behavior.
6. Define the owner-first update order.
7. Define migration/versioning requirements when needed.
8. Define automated, integration, and hardware/manual verification needed.
9. When design questions remain unresolved, stop before consumer implementation and request `grill-with-docs`; use its ADR rather than duplicating a design-review interview here.

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
- approved proposed contract reference (and brief change summary);
- compatibility classification;
- required owner changes;
- required consumer changes;
- implementation order;
- migration/versioning notes;
- required tests;
- manual/hardware checkpoints;
- unresolved decisions delegated to Grill or the contract owner;
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
3. Read each repository's existing build/test instructions rather than inventing Cross-Repo Governance-specific commands.
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
