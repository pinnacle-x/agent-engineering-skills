---
name: project-bootstrap
description: Enter greenfield or existing-source projects; establish a source-evidenced current baseline, discoverable approved requirements/constraints/design documents, and portable AGENTS.md project instructions. Maintain approved rules under .agents/rules/ independently of AGENTS.md.
---

# Project Bootstrap

Use on project entry, either **from zero** or with an **existing codebase**. Establish a trustworthy entry point and a *discoverable map of effective project documents*. This Skill does not replace the agent's direct engineering work or run a separate execution process.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule
```

When shorthand is unavailable, request the Skill by name and state the task. Neither invocation requires engineering-governance to be installed.

## Inspect first

1. Identify the actual project root and Git root(s), if present. Inspect current root/nested `AGENTS.md`, source, build/runtime configuration, tests, interfaces, project documents, external constraints and current `.agents/rules/` content. Note the working tree and relevant revision.
2. Preserve existing code, user edits, technical decisions, document ownership, external specifications, repository layout and relevant nested instructions. Do not reconstruct a superseded version from memory.
3. Detect any existing project document index (for example `docs/README.md`, `docs/index.md` or an established equivalent). If a suitable one exists, **reuse** it instead of creating a competing index or moving source documents.
4. Classify the initial context: **greenfield without an established implementation** or **existing engineering project**, including firmware, hardware and other design source files.

## Path A: project from zero

1. Begin with the user's stated goals, accepted constraints, and already confirmed decisions. Do not invent an existing source baseline or declare undecided architecture to be approved.
2. Identify the next **important design decision** needed to make progress. For a focused high-impact unresolved question, use or recommend `grill-with-docs`; for an unusually broad, ambiguous, multi-stage problem, use or recommend `wayfinder`. These may be used **repeatedly at later milestones**, not merely once at project start.
3. Ensure the outcome of each meaningful design round is captured in an **actual project document** (existing project document, Grill/Wayfinder output, or a suitable new record). Only mark a proposal confirmed after user acceptance or another explicit project-approved authority. Keep unresolved decisions distinct.
4. Create or reconcile root `AGENTS.md` and the project document index; link only real, relevant documents. If no project index convention exists, use `docs/README.md` for the index and prefer `docs/` for project-wide records, with module documents beside their modules.
5. Once the current task's necessary design has been confirmed, the **active agent executes directly** using the confirmed documents. When implementation or user feedback reveals another consequential design question, repeat the design → confirmation → document/index update → direct execution loop.

## Path B: existing project with source

**Actual source, build configuration, hardware/project artifacts and observed state are the factual baseline for what is implemented now.** They do not automatically establish what the project is *supposed* to do.

1. Inspect relevant current code, build/dependency configuration, protocol files, hardware constraints, test results and available runtime evidence. Reference actual files and, when useful, Git revision or workspace state. Do not claim a test ran if it did not.
2. Establish what the project currently does and how major modules/interface boundaries behave. Preserve previously confirmed standards and requirements even when they disagree with source; surface discrepancies explicitly.
3. **Using that factual baseline**, create or update **confirmed requirements** and **confirmed technical constraints** documents (or existing authoritative equivalents). Confirmed requirements need user acceptance, an approved contract, a standard or other authoritative confirmation; code-only inferred intent belongs under **Pending confirmation**. For technical constraints distinguish the verified current system from accepted future design limits.
4. Maintain a project-document index linking those authoritative documents and any existing architecture, protocol and effective design documents. Use the project's established index and paths; absent a convention, use `docs/README.md` as index and `docs/requirements.md` / `docs/technical-constraints.md` as defaults. Do not create duplicate sources of truth.
5. For subsequent features, defects revealing design ambiguity, changing requirements, architecture revisions and major interface choices, conduct **new design rounds** with `grill-with-docs` or `wayfinder` when appropriate. They are available throughout the project's life; do not assume the initial source analysis or first design round permanently settles all future decisions.
6. After each important confirmed decision, update the appropriate authoritative design/requirement/constraint record and the **document index**, then let the agent directly implement from the active documents and current source. Keep unresolved or superseded alternatives visibly out of the effective set.
7. Report the evidence inspected, confirmed baseline, created/updated project documents, index location, accepted decisions and what remains uncertain.

## Project-document discovery contract

The goal is for an agent entering any session to find **the current effective scheme** without searching through stale conversations or contradictory document copies.

1. Root `AGENTS.md` must name **one stable entry path to the project's document index** (normally `docs/README.md`; use the actual established path when different). It should also instruct the agent to read applicable **confirmed/active** documents from that index before implementing a task.
2. Maintain the **specific document paths, applicability and lifecycle status inside the document index**, not as a continuously growing list in root `AGENTS.md`. Project-local module documents and Grill/Wayfinder outputs may live anywhere under the established project convention; link their actual locations from the index.
3. A useful index identifies: **current implementation baseline**, **confirmed requirements**, **technical constraints**, **current approved design/architecture**, **open decisions**, and **superseded or historical designs**. Include each actual path, a concise applicability note and a status. A section may be omitted if it has no document.
4. The index is a **directory/map, not a parallel specification**. Do not paste entire design documents into it. Every link must resolve; remove or correct stale links and distinguish an active source from history.
5. After a consequential Grill/Wayfinder round, an accepted design revision, or a change invalidating an existing document, the **agent itself** maintains the affected project document and index. No recurring bootstrap invocation is required, and `AGENTS.md` should not need editing for each document addition or replacement.
6. An output from Grill/Wayfinder is **not automatically approved**. Record who/what confirmed a decision and the scope when material. Mark working proposals `Pending` and replaced schemes `Superseded`; implementation must use the accepted active revision.
7. For existing projects, link source paths and relevant revision/test evidence to current-state assertions. **Do not automatically update confirmed requirements to match code** when code diverges; resolve the discrepancy with the user/owner or controlling standard.
8. A new project may start with only confirmed goals or open decisions. Do not generate misleading approved designs or empty placeholder files; create the index when there are actual documents to discover. Root `AGENTS.md` can name the intended `docs/README.md` entry *conditionally* until it exists.

Use `references/AGENTS.template.md` and `references/docs-index.template.md` as adaptable examples, not rigid directory trees. Project documentation quantity/detail follows project needs, not a fixed document quota.

## Stable project rules directory

Root `AGENTS.md` separately mentions **only the directory** `.agents/rules/` for project-specific rules. Rules are not assumed to be auto-loaded by any Harness.

```markdown
## Project Rules
- Project rules live in `.agents/rules/`; create this directory only when needed.
- If present, inspect its contents and read relevant rules; otherwise continue normally.
- Do not assume automatic rule discovery by the runtime.
```

Do not create an empty `.agents/rules/`, placeholder rules, `INDEX.md` or `.gitkeep` during normal bootstrap. Individual rule paths, applicability and optional `.agents/rules/INDEX.md` stay **inside** the rules directory. Do not mirror them into `AGENTS.md`.

## Mode: add-rule and rule maintenance

1. Use for a specifically requested rule or repeated, evidenced agent failures with a confirmed cause. Prefer fixing code/tests/configuration where that addresses the underlying failure.
2. Inspect existing rules and any internal index. Propose a scoped, actionable, testable rule with exceptions; obtain user approval for the specific persistent change unless already explicitly authorized.
3. Create `.agents/rules/` only for the first approved rule, and maintain relevant rule files and optional internal index. Handle revision, merge, rename and deletion there.
4. Never update root `AGENTS.md` solely because an individual rule changed. If the directory-level rule policy is missing, suggest a separate bootstrap reconciliation.
5. Verify references, conflicts, duplicates and actual diff; do not assert unrun checks or automatic Harness loading.

## Boundaries and checks

- Bootstrap sets up project context and discovery; it does not silently modify production code, hardware, dependencies, CI, Git remotes or branch state.
- Major new design choices may recur throughout a project. Distinguish meaningful unresolved decisions from routine code questions; **do not force Grill/Wayfinder for every small implementation change**.
- Existing source establishes current reality; accepted design documents express intended behavior. When in conflict, present the divergence, do not silently elevate either to authority for the other.
- Verify the `AGENTS.md` index path and the documentation index links; check applicable active documents, status, current revisions, unconfirmed decisions and `git diff` / `git status` where available.
- Report document and rule changes, evidence, decisions, blockers and unperformed checks. The agent itself carries out implementation once the scheme for that task is confirmed.
