---
name: project-bootstrap
description: Initialize or reconcile a repository's portable AGENTS.md entry point and explicitly indexed .agents/rules while preserving existing project files and conventions. Independent of cross-repository governance and design Skills.
---

# Project Bootstrap

Create a minimal portable project instruction entry point. This Skill is **independent** of cross-repository governance and Grill; it does not need either of them to run. Use it for new repositories and for existing projects whose rules need reconciliation.

## Invocation

```text
$project-bootstrap
```

When the harness does not support shorthand, ask it to "Use the project-bootstrap Skill to initialize or reconcile this repository's AGENTS.md and explicit .agents/rules."

## Inspect before writing

1. Identify the actual project/repository root. Inspect `git status` when Git is present. Do not initialize Git, change remotes or create branches without explicit instruction.
2. Read existing `AGENTS.md`, `README.md`, `.agents/`, project-specific instruction files, relevant docs, and source/build layout.
3. Identify existing rules, conventions and sources of truth, including existing external tool configuration. **Preserve** existing instructions and comments.
4. Examine Skill availability when discoverable; do not assume an installed Skill exists or copy user/global Skills into the project.
5. If existing rules conflict or ownership is uncertain, surface the discrepancy rather than choosing an arbitrary precedence.

## Write the minimum useful instructions

1. Add a root `AGENTS.md` only when missing; otherwise reconcile or append a small missing section in place without overwriting current content.
2. When useful, organize stable reusable rules under `.agents/rules/`; create `general.md` only when the project needs a new general rule, and `development.md`, `testing.md` or `documentation.md` only when actual project-specific guidance exists.
3. Index **only existing files** from `AGENTS.md`, distinguishing always-on rules from rules to read for implementation, verification, and docs. Do not imply that every Harness automatically scans `.agents/rules/`.
4. Prefer references to established instructions over duplicate rule files. Existing project directory layout takes precedence over example trees.
5. Use `references/AGENTS.template.md` and `references/rules.template.md` only as adaptable starting examples; delete unused lines and never invent technical facts.
6. Create docs, ADR or status directories **only when necessary** for real work. Never generate blank formal requirements or fabricated project status.
7. Do not touch production source code, hardware designs, dependencies, CI/build configuration, secrets or Git metadata.
8. Do not automatically run design review, issue tracker setup or cross-repository governance. Their Skills can be used independently later if appropriate.

## Verify and report

- Check that every required path referenced from `AGENTS.md` exists, and rules have explicit conditions for reading.
- Inspect for duplicate sections, conflicting guidance, circular references, absolute machine paths and vendor-specific assumptions.
- Review `git diff` and `git status` when available; ensure only the intended instructions/docs changed.
- Running the Skill a second time must not duplicate entries or replace previously adopted rules.
- Report actual added/modified/preserved files, rule-loading map, conflicts and any minimal harness adapter needed.
- Do not claim successful tests or Skill discovery without actual evidence.

## Separation from other Skills

- `project-bootstrap` owns portable repository entry instructions and explicit rule discovery.
- `setup-matt-pocock-skills` may separately configure an engineering-Skill issue tracker, triage labels and domain-doc layout. Do not recreate these in bootstrap.
- `grill-with-docs` handles important unresolved design decisions and ADRs.
- `cross-repo-governance` handles approved cross-repository contract rollout, integrated verification and reproducible releases.
