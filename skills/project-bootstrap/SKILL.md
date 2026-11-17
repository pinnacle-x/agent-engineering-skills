---
name: project-bootstrap
description: Start a new project or understand an existing codebase before establishing its AGENTS.md, evidenced requirements, and technical constraints. Maintain approved project rules under .agents/rules/ without per-rule changes to AGENTS.md.
---

# Project Bootstrap

Use this Skill when entering a **new project without source code** or adopting an **existing project with source code**. It establishes project context and a portable agent entry point. The active agent performs engineering work directly after the goal and relevant decisions are clear; do not invoke an extra execution workflow or substitute this Skill for the agent's judgment.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule
```

When shorthand is unsupported, request the Skill by name. Neither mode requires the governance Skill.

## Identify the starting point

1. Discover the actual project directory and Git root when present. Inspect current `AGENTS.md` (including relevant nested files), README, source, build and runtime configuration, tests, documents, rules, and Git status.
2. Decide between **new project** (no established codebase) and **existing project** (source/build or deployed engineering artifacts already present). A new directory with a few exploratory files may require treating those files as unconfirmed evidence; do not overwrite them.
3. Preserve existing project structure, user changes, source, Git metadata, build settings, and external design artifacts. If goals or major architectural decisions are unresolved, the agent can clarify them; Grill or Wayfinder may be used when beneficial, not by default.

## Path A: new project from zero

1. Establish the user's stated goal, intended behavior, confirmed requirements, technology choices, and known constraints. Do not invent architecture, dependencies, board configuration, or confirmed decisions.
2. Create or reconcile a useful root `AGENTS.md` with project entry instructions and the directory-level rule policy below. Do not create Git history, production code, external tooling configuration, or placeholder rule directories as a bootstrap side effect.
3. Follow existing document conventions. Where none exist, prefer `docs/` for project-wide documents and module directories for module-specific documents. Create requirements or technical-constraints documents when their content and project needs warrant them; record unknown decisions explicitly rather than filling them with guesses.
4. Once the necessary scheme is settled, **the active agent directly executes the project task**; this Skill does not route that execution through another workflow.

## Path B: existing project with source

**The current source code and actual engineering state are the factual baseline for understanding the existing project.** Do not reconstruct an older version from memory or treat an outdated README as proof of current behavior.

1. Inspect enough relevant code, hardware/project files, dependency and build configurations, interfaces, test results, and available runtime evidence to form an accurate current-state map. When practical, run existing safe inspection/build/test commands, distinguishing observed results from unexecuted checks.
2. Record what the repository **currently does**, key module boundaries, build entry points, implemented interfaces, hardware assumptions and existing configuration. Link each substantive assertion to its source path, configuration or actual verification evidence. Avoid reinterpreting the present code as a different intended architecture.
3. **From that evidence, establish and maintain two project documents** (or update their existing equivalents):
   - **Confirmed requirements**: user-accepted or otherwise explicitly approved behavior, external standards, and contracts. Existing code can provide supporting evidence and candidate requirements, but **code alone does not prove intended requirements**.
   - **Confirmed technical constraints**: verified platform and resource limits, hardware/firmware interfaces, dependencies, compatibility rules, build/deployment constraints and accepted architectural decisions. Identify which facts come from inspected source/configuration versus external confirmed constraints.
4. If the project has no established document locations, use `docs/requirements.md` and `docs/technical-constraints.md`. Existing equivalent documents and project conventions take precedence; do not create duplicate competing sources of truth.
5. Put ambiguous inferred intent, missing source evidence, outdated-document conflicts and unapproved design assumptions in a clearly labeled **Pending confirmation** section, or the project's existing issue/decision mechanism. Never label guesses as confirmed. Ask for clarification where a consequential requirement cannot be established; progress on the confirmed portions without pretending the rest is decided.
6. Reconcile root `AGENTS.md` with current project entry points and the stable rules directory. Avoid copying detailed requirements/constraints into `AGENTS.md`; refer to the project's existing authoritative documents where useful.
7. Report which evidence was inspected, confirmed statements established, documents created or updated, and what remains unverified or requires user confirmation.

## Stable AGENTS.md rules directory

`AGENTS.md` must mention only the **directory** `.agents/rules/` for project-specific rule discovery, not individual rule paths or their loading conditions.

```markdown
## Project Rules
- Project rules live in `.agents/rules/`; this directory is created only when needed.
- If the directory exists, inspect its contents and read rules relevant to this task.
- If it does not exist, proceed without additional project rules.
- Do not assume the runtime automatically loads that directory.
```

**Do not create an empty `.agents/rules/` directory, `INDEX.md`, rule files or `.gitkeep` during default bootstrap.** When rules exist, an optional index and each rule's applicability stay inside the rules directory; individual rule additions, edits, merges and deletions do not change `AGENTS.md`.

## Mode: add-rule and rule maintenance

1. Use this mode when the user requests a rule or when repeated, evidenced failures have a verified root cause. Prefer correcting source, tests or configuration when that is the actual problem.
2. Inspect existing `.agents/rules/` content; propose the smallest actionable, scoped and testable rule with exceptions. Do not create permanent restrictions for speculative one-off failures.
3. Obtain user approval for the specific persistent addition, revision, merge or deletion, unless explicitly authorized already.
4. Create `.agents/rules/` only for the first approved rule. Add/modify/merge/remove its files and maintain `.agents/rules/INDEX.md` **only if an index is useful and already present or justified**.
5. Do **not** update root `AGENTS.md` due to individual rule changes. If its directory-level policy is missing, propose reconciling it under the separate bootstrap mode, not as a side effect of rule maintenance.
6. Verify internal index references, duplicates, conflicting rules and diff. Record actual checks; never claim runtime discovery or tests not performed.

## General boundaries

- Documentation reflects project needs and existing standards; no fixed number or maximum detail is imposed.
- Do not silently modify production code, hardware files, dependencies, CI, Git remotes or branches as a side effect of bootstrap.
- The agent decides whether a clear task can proceed directly. Major unresolved design choices may use Grill; exceptionally broad, ambiguous programs may use Wayfinder. After decisions are established, the **agent executes directly**.
- `engineering-governance`, when available, is optional for system-level verification and reproducible releases across one or multiple Git repositories.
