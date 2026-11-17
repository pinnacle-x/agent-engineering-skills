# Project Bootstrap

`project-bootstrap` is an **independent Agent Skill**, not a mode of Cross-Repo Governance.

## Use

After installing the Skill and opening the target repository:

```text
$project-bootstrap
```

Or ask any capable supported Harness to use the installed `project-bootstrap` Skill to reconcile the current repository's `AGENTS.md` and explicit `.agents/rules/` without overwriting existing files.

## Responsibilities

1. Inspect current `AGENTS.md`, README, source tree, Git state, docs and instructions before changes.
2. Create the root `AGENTS.md` only if missing; preserve/merge existing instructions.
3. Add `.agents/rules/` files only when genuine rules are needed.
4. Explicitly index each existing rule in `AGENTS.md` with its loading condition. Never imply that every Harness auto-discovers this directory.
5. Use `skills/project-bootstrap/references/AGENTS.template.md` and `skills/project-bootstrap/references/rules.template.md` only as adaptable examples.
6. Inspect `git diff`; report files changed, preserved conventions and unresolved conflicts. Do not fabricate tests or source-of-truth documents.

Example, **not** a required fixed directory tree:

```text
project/
├── AGENTS.md
├── .agents/
│   └── rules/
│       ├── general.md
│       ├── development.md     # optional
│       ├── testing.md         # optional
│       └── documentation.md   # optional
└── ... existing source and docs
```

Do not initialize Git, change remotes, modify production code, invent requirements/status docs, or configure engineering issue trackers as a side effect.

## Boundaries

- `project-bootstrap`: portable entry and rule discovery.
- `setup-matt-pocock-skills`: issue tracker, triage and domain docs as needed.
- `grill-with-docs`: major unresolved design choices and ADRs.
- `cross-repo-governance`: owner/consumer coordination of approved shared contracts, exact-revision verification and release manifests.

The two repository-provided Skills can be installed, invoked, updated and tested independently.
