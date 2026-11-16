# PraxFlow

PraxFlow is **one portable Agent Skill** that adds a small set of project-governance capabilities not covered by ordinary agents or the companion Grill engineering Skills. It is not a second general-purpose development workflow.

## Modes

```text
$praxflow bootstrap
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

- **bootstrap**: initialize or reconcile root `AGENTS.md` and explicitly indexed `.agents/rules/`; do not recreate issue-tracker, domain documentation or source files.
- **interface-change**: coordinate the owner, consumers, compatibility and rollout for an **approved** shared contract across independent repositories. Design interviews, competing designs and ADR decisions belong to `grill-with-docs`.
- **system-verify**: link integration evidence and manual/hardware results to exact commit SHAs across repositories.
- **manifest-release**: pin a release to the exact verified repository revision set.

Run ordinary discovery, PDF/code analysis, specifications, implementation, local tests and review with the active agent and general engineering Skills. Use `grill-with-docs` for important unresolved design decisions. PraxFlow does not duplicate those capabilities.

## Install

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Expected installation:

```text
~/.agents/skills/
└── praxflow/
    ├── SKILL.md
    └── references/
```

If a harness does not support the `$praxflow` shorthand, invoke the installed Skill in natural language and name the mode.

## Project startup

From the target project:

```text
$praxflow bootstrap
```

Bootstrap writes the smallest useful portable entry and rule index. It does not guarantee that every harness discovers arbitrary files at `.agents/rules/`; `AGENTS.md` must reference actual rule paths and loading conditions.

## Workflow

```text
PraxFlow bootstrap (once)
    → active agent + Grill for design when needed
    → PraxFlow interface-change only for shared-contract governance
    → implementation and local tests
    → PraxFlow system-verify
    → PraxFlow manifest-release after verification PASS
```

## Repository structure

```text
PraxFlow/
├── skills/
│   └── praxflow/
│       ├── SKILL.md
│       └── references/
├── docs/
├── examples/
├── templates/
└── scripts/
```

See [bootstrap](docs/project-bootstrap.md), [installation](docs/installation.md), [workflow](docs/workflow.md) and [shared-contract coordination](docs/cross-repo-workflow.md).
