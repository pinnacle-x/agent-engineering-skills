# PraxFlow Bootstrap Mode

Repository instruction bootstrap is now **part of the single `praxflow` Skill**, not a separately installed or separately invoked `project-bootstrap` Skill.

## Use

Install PraxFlow once, then open the target repository in the agent and request:

```text
$praxflow bootstrap
```

Or use cross-harness natural language:

> Use the praxflow Skill in bootstrap mode to create or reconcile this repository's AGENTS.md and explicitly indexed .agents/rules. Preserve existing source, documents, configuration and Git state.

## Scope

This mode **only** supplies portable project instructions and rule discovery:

1. Inspect root `AGENTS.md`, README, source layout, Git status, docs and any existing instruction conventions.
2. Create or reconcile `AGENTS.md` in place, preserving existing content.
3. Organize rules under `.agents/rules/` only when appropriate and refer to each real file explicitly in `AGENTS.md`.
4. Explain always-on versus task-conditional rules; do not assume any harness auto-loads `.agents/rules`.
5. Use `skills/praxflow/references/AGENTS.template.md` and `skills/praxflow/references/rules.template.md` as optional examples.
6. Inspect diff/status, avoid duplicate sections, and report actual changes and conflicts.

This mode does **not** initialize Git, change remotes, create source code, alter build/CI configuration, generate invented specs or ADRs, configure the issue tracker, or replicate the domain-doc setup from `setup-matt-pocock-skills`.

## Possible project layout (not mandatory)

```text
project/
├── AGENTS.md
├── .agents/
│   └── rules/
│       ├── general.md
│       ├── development.md       # only if useful
│       ├── testing.md           # only if useful
│       └── documentation.md     # only if useful
└── ... existing source and docs
```

Other valid projects may already have adequate rules in different locations. Link to existing rules where possible instead of duplicating their content. Only create `docs/` or other files when they serve real project needs.

## Acceptance

- All required rule links in `AGENTS.md` refer to existing files.
- Only appropriate files were created or edited; source/config remains intact.
- Rules do not contradict one another or make false auto-discovery promises.
- A second run would not duplicate entries.
- Actual build/test outcomes are not invented.
- If the current harness cannot discover the Skill, state that limitation and propose the smallest adapter.

## Division of responsibilities

- `praxflow bootstrap`: portable AGENTS.md and rules.
- `setup-matt-pocock-skills`: issue tracker, triage and domain docs when desired.
- `grill-with-docs`: decisions, tradeoffs, and ADRs.
- `praxflow interface-change`: approved shared-contract owner/consumer governance.
- `praxflow system-verify` / `manifest-release`: exact-revision validation and release composition.
