---
name: praxflow
description: Portable repository instruction bootstrap and lightweight cross-repository governance. Use for AGENTS.md/rule discovery setup, shared-contract owner/consumer coordination, exact-revision integrated verification, or reproducible release manifests; delegate design interviews, ADRs, implementation and routine testing to the active agent and companion Skills.
---

# PraxFlow

PraxFlow is deliberately narrow and **one Agent Skill**. It supplies missing project governance capabilities without duplicating normal agent work, `grill-with-docs`, or `setup-matt-pocock-skills`. The active agent handles document/code reading, specification, implementation, repository-local tests, and code review. Grill owns unresolved design decisions and ADRs; PraxFlow does **not** conduct design interviews or redefine interface semantics.

Use PraxFlow for these non-overlapping responsibilities:

1. **bootstrap** — create/reconcile the portable root `AGENTS.md` and explicitly indexed `.agents/rules/` for a repository; do not duplicate issue-tracker/domain-doc setup from `setup-matt-pocock-skills`;
2. **interface-change** — coordinate an **already designed** public contract across independent repositories: identify owner/consumers, compatibility consequences, owner-first rollout, migration and test obligations; no design interviews or ADR drafting;
3. **system-verify** — bind integrated verification evidence to exact repository revisions;
4. **manifest-release** — pin the exact verified multi-repository composition.

## Invocation

```text
$praxflow bootstrap
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

If `$praxflow` is invoked without a mode, infer a mode only when the task clearly matches one of the four modes. Otherwise use the agent's native capability or an appropriate companion Skill. If the harness lacks the `$praxflow` invocation syntax, ask it in natural language to use the installed `praxflow` Skill in the named mode.

## What PraxFlow does not do

Do not use PraxFlow for:

- PDF reading, OCR, extraction, or document interpretation;
- Git repository initialization, Git remotes, issue-tracker configuration and domain-doc setup (delegate those to the active agent or `setup-matt-pocock-skills` as appropriate);
- codebase/repository discovery;
- domain modeling, design interviews and ADR writing (use `grill-with-docs` for unresolved important design decisions);
- specification drafting or materialization;
- generic specification validation;
- creating or deciding protocol/API semantics, protocol analysis or protocol validation;
- implementation, TDD, debugging, or code review;
- routine single-repository work.

Use the active agent for routine engineering, and `grill-with-docs` for unresolved important design choices. For `interface-change`, read the approved owner contract/ADR rather than independently deciding interface design. Do not automatically invoke another Skill from bootstrap.

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

# Mode: `bootstrap`

Use once for a new/imported repository or to reconcile existing `AGENTS.md` instructions. The scope is **portable instructions and explicit rule discovery only**; it does not replicate issue tracker configuration, triage labels, glossary/ADR layout, or the full engineering life cycle already handled by companion engineering Skills.

## Inspect before writing

1. Identify the real repository root. Inspect `git status` if Git exists; do not run `git init`, alter remotes or create branches automatically.
2. Read existing `AGENTS.md`, `README.md`, `.agents/`, relevant `docs/`, engineering configuration and source/build layout. Preserve any established patterns.
3. Check actual rules and their references. Do not assume `.agents/rules/` will be auto-discovered by every harness.
4. If existing instructions conflict, preserve them and surface the conflict; do not silently impose a new hierarchy.

## Write minimal, non-destructive bootstrap

1. Create root `AGENTS.md` if missing; otherwise reconcile the existing entry point **in place** without replacing unrelated content. Keep it concise.
2. Create `.agents/rules/general.md` only when a reusable rule set is warranted and the repository does not already have an adequate equivalent. Add task-specific rules (`development.md`, `testing.md`, `documentation.md`) **only if meaningful**.
3. Add an explicit index to `AGENTS.md` that lists only actual rule files, with a condition for loading each one. Never claim automatic discovery for arbitrary rule folders.
4. Use `references/AGENTS.template.md` and `references/rules.template.md` as **editable examples**, not universal policies. Remove inapplicable lines and do not invent technical facts.
5. Preserve existing docs and source; prefer links to established instructions over duplicating them. Do not generate placeholder requirements, ADRs, project status, versions or empty docs.
6. Do not modify production code, hardware designs, build settings, CI, secrets, dependencies or git metadata. Do not copy global Skills into a project-local skills directory.
7. Do not run Grill, PraxFlow's other modes or issue tracker setup as an automatic side effect.

## Verify and report

- Check that every referenced required path actually exists and that the rule index distinguishes always-on from conditional instructions.
- Check for conflicts, duplication, circular references and hardcoded vendor-specific assumptions.
- Inspect `git diff` / `git status` when available and verify unrelated code/configuration was not modified.
- Re-running bootstrap should not append duplicate sections or overwrite existing rules.
- Report created/edited/preserved files, rule-loading map, unresolved conflicts and any separate harness-specific discovery adapter needed.
- Installed skill files alone do not guarantee harness discovery. Never claim tests passed unless actually executed.

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

Do not require PraxFlow-specific spec files. Use whatever source of truth the repositories already define.

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
