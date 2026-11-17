---
name: project-bootstrap
description: Initialize or reconcile portable AGENTS.md instructions; when a recurring, confirmed problem justifies a lasting rule, maintain a targeted .agents/rules/*.md file and index its loading condition in AGENTS.md. Preserve project conventions and avoid pre-creating rules.
---

# Project Bootstrap

This Skill provides a portable repository instruction entry point and **on-demand rule maintenance**. It is independent of the engineering governance Skill. The active agent is responsible for reading code, planning, specifications, TDD when useful, implementation, debugging, documentation, and ordinary verification.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule
```

If the active Harness does not recognize `$...` shorthand, request the installed Skill by name and say whether to bootstrap or add a rule.

## Common prerequisites

1. Discover the actual Git root when present; inspect `git status`, existing root or nested `AGENTS.md`, README, source/build/test conventions, current documentation and relevant existing rules.
2. Follow existing project instructions and established file locations. Preserve user edits, source code, configuration, Git remotes and branch state.
3. Treat code and running tests as evidence for **implemented behavior**, but preserve external standards, approved requirements, public contracts and hardware constraints as independent sources of requirements. Surface conflicts; do not fabricate facts.
4. Do not assume `.agents/rules/` is automatically discovered by any Harness. Only explicit instructions in `AGENTS.md` make the project's loading contract clear.

## Mode: bootstrap (default)

1. Create the root `AGENTS.md` only if missing; otherwise reconcile missing guidance without duplicating or overwriting existing instructions. Preserve relevant nested `AGENTS.md` files.
2. Include project orientation: where to find current source and build/test instructions, how to resolve conflicting guidance, and where applicable rule links are indexed.
3. For documents, **respect the existing structure first**. When no convention exists, use `docs/` as the default for project-wide documentation and the related module directory for module-specific documentation. The agent chooses document type, detail and amount based on task needs, existing conventions and durable project requirements. There is **no minimum-documentation policy or forced document quota**.
4. Do **not** create `.agents/rules/` or template rule files by default. If rules already exist, index only the relevant real files and state their loading conditions; prefer links to existing guidance over copying it.
5. Do not install companion Skills, create invented ADRs/Specs, configure issue trackers, initialize Git or alter production source as a side effect.

## Mode: add-rule

Use this when the user requests it or when the agent proposes a rule after **repeated, evidenced failures with a confirmed cause**. One failure or speculation is not sufficient grounds for a permanent rule.

1. Collect concrete examples of the repeated problem and identify its verified cause and where it applies. If the cause is unresolved, investigate first rather than writing a guessed rule.
2. Check whether existing source code, tests, project instructions, or a current rule already solve the problem. Prefer fixing the code/test or refining an existing rule to adding a duplicate.
3. Propose a **specific, actionable, testable, scoped** rule and explain what undesired behavior it prevents, when to read it and any possible over-constraint. Obtain the user's approval before persisting a new lasting rule, unless their current request already explicitly authorizes that exact rule.
4. Create or update `.agents/rules/<topic>.md` only for the approved rule. Use the optional `references/rules.template.md` as a format example, **not** a bundle of default generic rules.
5. Update root `AGENTS.md` to link to that **existing** file via its relative path, with a task-based condition. Do not use wildcard loading or claim that arbitrary Harnesses auto-load `.agents/rules/*.md`.
6. Avoid overlapping/conflicting instructions; narrow, revise or remove obsolete rules when approved. Do not use rules to lock the agent into an implementation or testing technique without a proven project need.
7. Review the actual diff, confirm referenced paths exist, and make the operation idempotent.

## Rule index example (only after a rule exists)

```markdown
## Task-specific rules
- When modifying STM32 DMA/cache handling, read
  [.agents/rules/stm32-dma.md](.agents/rules/stm32-dma.md).
```

Do not insert that line unless the indicated file exists.

## Verification and reporting

- Inspect changed files and, where available, `git diff` and `git status`.
- Confirm links resolve, instructions do not contradict existing guidance, no default rules were silently generated, and repeat invocations do not duplicate content.
- Report which documents/instructions changed, newly indexed rules and their triggers, conflicts, evidence and unperformed checks.
- Do not claim successful Harness discovery or tests without evidence.

## Boundaries

- The **active agent** owns routine design, specifications, implementation, tests and task-appropriate documentation.
- Grill / Wayfinder may assist with difficult undecided design or very large ambiguous projects **when chosen**, never as mandatory dependencies.
- `engineering-governance` is optional for significant change impact, integration verification and release, in either single- or multi-repository projects.
