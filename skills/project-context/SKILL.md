---
name: project-context
description: Bootstrap greenfield or existing-source projects, reuse Grill's native local-Markdown decisions and domain documents, maintain discoverable project entry instructions, and create or update current system architecture and high-level design from confirmed decisions and actual source evidence. Maintain approved project rules under .agents/rules/.
---

# Project Context

This Skill enters a new or existing engineering project and maintains **current, long-lived system architecture and high-level design documents**. It reuses upstream Grill/Wayfinder/local tracker storage rather than duplicating Map, decision tickets, or specs. The active agent executes engineering work directly.

## Invocation

```text
$project-context
$project-context update-design
$project-context add-rule
```

If shorthand is not supported, ask for the Skill and its intended mode in natural language. No other Skill is required for this Skill to be installed or to inspect an existing project.

## First: inspect existing project conventions

1. Find the actual project and Git root(s). Read relevant root/nested `AGENTS.md`, any `CLAUDE.md`, current source, build/test configuration, hardware/protocol files, README, prior design docs, current working state and available evidence.
2. Inspect whether the upstream `setup-matt-pocock-skills` has already configured `docs/agents/issue-tracker.md` and `docs/agents/domain.md`, or equivalent paths advertised by existing `AGENTS.md`/`CLAUDE.md`. **Respect actual existing paths.**
3. Check for `GLOSSARY.md` / `GLOSSARY-MAP.md`, applicable `docs/adr/` records, a configured local tracker (often `.scratch/`), existing architecture/overview documents and any pre-existing project document index. Do not treat an absent path as a failure or assume that Git ignores/retains `.scratch/`.
4. Preserve established project documentation, user changes, source, Git metadata and external authoritative requirements. Do not create a second spec, duplicate an existing approved design, or replace project conventions merely to fit an example.

## Mode: bootstrap (default)

**New project**

1. Start with confirmed goals, external constraints and user-accepted choices; do not invent an existing source baseline, configuration or approved architecture.
2. For consequential open decisions, the user may invoke `grill-with-docs` for focused discussions, or `wayfinder` for multi-session direction. Repeat at later design milestones as needed; they are **not** automatic prerequisites to every small change.
3. Reuse the upstream artifacts as their canonical records: glossary, ADRs, and local tracker Map/tickets/spec when configured. `to-spec` can consolidate multi-session confirmed work when requested. Never assume a Grill discussion saved every decision or that a Wayfinder Map is itself a complete implementation-ready scheme.
4. Where the confirmed solution already justifies it, establish the current system architecture and high-level design documents. Otherwise capture unresolved requirements/choices as pending and avoid empty or fictitious architecture files.
5. Reconcile root `AGENTS.md` as a **navigation entry**, using real project document paths (see the discovery section). Do not initialize production code, Git history, CI, dependencies or external tracker configuration as a bootstrap side effect.

**Existing-source project**

1. Treat actual code, build/project settings, relevant hardware files, interfaces and observed tests as evidence of the **currently implemented** system. Record file/revision evidence and identify unverified areas; never reconstruct old source from chat history.
2. From this baseline, create/update confirmed requirements and technical constraints (existing equivalents first, otherwise `docs/requirements.md` and `docs/technical-constraints.md`). Distinguish verified current engineering constraints from user-approved intended behavior; source alone does not prove customer intent.
3. Read the applicable approved ADRs, glossary, configured local tracker decisions/specs and existing design records. In case of conflict between code and accepted intent, flag the discrepancy and seek a decision; **do not silently rewrite approved requirements to match code**.
4. Create/reconcile **current system architecture** and **high-level design** when enough evidenced/confirmed material exists, reusing existing authoritative files; otherwise mark unresolved sections rather than guessing. These are living engineering views, not copies of every ADR or task spec.
5. Reconcile root `AGENTS.md` to expose those long-lived project documents and any established upstream tracker/domain configuration. Do not force a new `docs/README.md` index when upstream paths and a small stable set of architecture documents suffice.

## Native Grill / Wayfinder local-Markdown integration

- `to-spec` also expects the upstream tracker and triage-label vocabulary (including `ready-for-agent`). Depending on installed upstream Skills, setup may skip label setup; check that configuration before using `to-spec`, rather than assuming Local Markdown alone guarantees it works.
- The upstream `setup-matt-pocock-skills` configures an issue tracker. **For local-only projects, recommend choosing Local Markdown** and keep its settings in `docs/agents/issue-tracker.md` (or the existing documented path). The upstream setup selects `AGENTS.md` or `CLAUDE.md` according to its conventions; preserve that choice, and do not silently rerun/imitate the setup in bootstrap.
- The canonical upstream local tracker layout is `.scratch/<effort>/map.md` plus `.scratch/<effort>/issues/NN-<slug>.md` for Wayfinder and `.scratch/<feature>/spec.md` for `to-spec`. These are **workflow records**, not automatically the current architecture/overview. A different configured tracker/location overrides these example paths.
- Domain records remain canonical at configured `GLOSSARY.md` / `GLOSSARY-MAP.md` and `docs/adr/` or module-specific equivalents. Do not copy the same decision into multiple invented indices.
- To continue a task, discover the tracker using the configured pointer and find the **explicitly identified relevant Map/spec** from the user, task, branch, established project references or tracker lookup. **A configured tracker does not automatically identify which spec is active.** If several candidates conflict, ask for confirmation instead of guessing.
- After a consequential discussion, check what was actually persisted. If an important confirmed decision exists **only in a chat**, save the missing durable content in the existing appropriate project artifact; do not assume `grill-with-docs` wrote a complete project design automatically.
- Before relying on `.scratch/` across machines, inspect `.gitignore` and Git tracking. If ignored/untracked, warn that local files may be lost or unavailable after checkout. Do not modify ignore rules, add files to Git or move records without the user's direction. Durable architecture and overview documents should follow the project's normal version-control practice.

## Document discovery without a mandatory second index

1. Root `AGENTS.md` should direct the agent to read project domain/tracker configuration **at their actual paths** (commonly `docs/agents/domain.md` and `docs/agents/issue-tracker.md` when they exist).
2. Root `AGENTS.md` should also name the **stable current architecture and overview documents** (existing project equivalents first; typical defaults `docs/architecture.md` and `docs/design-overview.md`), plus relevant requirement/constraint entry paths. Name only files that exist, or clearly mark optional expected paths as conditional.
3. Domain docs describe how to consume glossary and ADRs; tracker config describes where to locate Map and spec. Prefer those existing upstream pointers over listing every `.scratch/` issue or creating competing `docs/README.md` records.
4. **If the project already has a useful document index, retain and maintain it.** For many distributed design documents with no reliable navigation, an index may be warranted, but it is **optional**, never an automatic additional source of truth. No duplicate substantive descriptions in an index.
5. When a stable document path changes, update the corresponding `AGENTS.md` pointer; do not churn it after ordinary content updates or new Map/spec tickets. Do not claim the Harness auto-loads all linked documents: the active agent must actually read the relevant files.

## Mode: update-design

Use when the user requests architecture/overview generation or synchronization, **after a meaningful code change**, after accepting a consequential design choice, or when existing long-lived docs are stale. It updates documentation; it does not perform the product-code change itself.

1. Identify affected scope and actual changes (diff, Git revision or user-specified modules). Read **real current source/configuration**, authoritative requirements/constraints, applicable approved ADRs and the relevant confirmed tracker spec/Map where discoverable. Do not pretend an unapproved proposal is a current requirement.
2. Locate the project's **existing** system architecture and high-level design files. If absent and needed, prefer `docs/architecture.md` and `docs/design-overview.md`, or the established project equivalents. Do not create placeholders for unrelated modules.
3. **System architecture**: reconcile system/subsystem boundaries, responsibilities, deployment/hardware topology, external interfaces, major data/control flows, cross-component dependencies, key design choices and constraints. Capture **current as-built facts** with source evidence; clearly label a confirmed design not yet implemented as **target**.
4. **High-level design**: reconcile modules, component responsibilities, interface/protocol contracts, data models, state/control flows, startup/shutdown/error behavior and important resource/timing assumptions **only where actually relevant and evidenced**. Link to existing detailed technical specs/protocol definitions instead of reproducing them.
5. Compare **accepted intended design** with **observed implementation** and actual verification results. If code and approved design conflict, report the difference as `Pending resolution`; do not silently change an ADR/requirement or declare unimplemented behavior completed. If changing direction is warranted, use a new user-confirmed Grill/Wayfinder decision before elevating it to Active.
6. Update only the affected sections; preserve good existing explanations and history. Add source paths, links to applicable ADRs and relevant Map/spec references where useful; avoid restating their complete content. Distinguish `Current / Implemented`, `Confirmed target / Not yet implemented`, and `Pending` where needed.
7. Check `AGENTS.md` discovery pointers and any existing index **only if the relevant document paths changed or require correction**. Keep the configured tracker/domain pointers untouched and do not migrate or duplicate `.scratch/` content.
8. Review the diff for substantive accuracy, unresolved contradictions and broken links; report updated documents, inspected evidence, outstanding questions and validation not performed.

**After ordinary Agent code work:** the agent should examine whether system architecture or high-level design was affected and update the relevant long-lived document in the same change when appropriate; it need **not** call this mode every time. `$project-context update-design` is the dedicated entry for requested reviews, catch-up synchronization or larger documentation changes. A local bug fix with no architectural/design effect should not create gratuitous edits.

Use `references/architecture.template.md` and `references/design-overview.template.md` as **examples**, never as rigid mandatory content.

## Stable project rules directory

`AGENTS.md` points only to `.agents/rules/` for project-specific rules. If it exists, inspect and read applicable files; otherwise continue without additional rules. Do not assume Harness auto-discovery. Bootstrap does **not** create an empty `.agents/rules/` directory, placeholder files or `INDEX.md`.

## Mode: add-rule and rule maintenance

1. Use for explicitly requested rules or repeated evidenced failures with a confirmed cause. Prefer correcting actual source/tests/configuration when appropriate.
2. Inspect current rules, avoid duplicates/conflicts, propose a focused actionable and testable rule with limits, and obtain approval for the specific persistent edit unless already authorized.
3. Create `.agents/rules/` only for the first approved rule; manage additions, revisions, merges, renames, deletions and optional `.agents/rules/INDEX.md` **inside** that directory.
4. Never update root `AGENTS.md` solely for a rule file edit. If its rules-directory policy is missing, reconcile only through the separate bootstrap mode.
5. Validate links and diffs; report what actually changed.

## Boundaries

- The Agent owns direct engineering execution. Grill/Wayfinder design sessions may recur at meaningful unresolved decisions, but do not require a new session for every code change.
- `project-context` maintains current project context, source-evidenced documents and approved design navigation, **not** a second tracker or duplicate specification system.
- `engineering-governance` remains optional for integrated verification and reproducible release of single- or multi-Git products.
