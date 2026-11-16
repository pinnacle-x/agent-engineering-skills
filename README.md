# PraxFlow

This repository contains **two independent, portable Agent Skills**:

- **`project-bootstrap`** — initialize or reconcile a project's root `AGENTS.md`, explicit `.agents/rules/` and minimum documentation without overwriting existing source or configuration.
- **`praxflow`** — lightweight governance for public interface changes, exact-revision multi-repository verification and reproducible release manifests.

They can be installed and used separately. `project-bootstrap` does not invoke PraxFlow; PraxFlow does not create `AGENTS.md`.

## Install

The installer discovers Skills under `skills/`. By default it installs both to the user-level `~/.agents/skills/` path:

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Install only the new Skill if desired:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
```

After installation, verify the active harness discovers the Skills. If it does not support `$skill-name` shorthand, invoke the Skill by name using a natural-language request.

## Bootstrap a project

From the target project root, invoke:

```text
$project-bootstrap
```

Or: "Use the project-bootstrap Skill to initialize or reconcile this repository's AGENTS.md, explicitly indexed .agents/rules, and minimal docs, preserving existing files."

The bootstrap workflow is non-destructive and idempotent in intent: it inspects first, only adds needed rules, links to existing conventions, and does not touch production code. See [bootstrap guide](docs/project-bootstrap.md).

## PraxFlow governance modes

Use PraxFlow only for the three cross-repository concerns it owns:

```text
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

- `interface-change` records contract owner/consumers, compatibility, owner-first update order, migration and verification requirements.
- `system-verify` binds integration evidence to the exact commit SHA of every included repository.
- `manifest-release` pins precisely that verified revision combination.

Use the active agent for reading, implementing and repository-local tests. Use `grill-with-docs` separately when important **design choices** require interactive review and ADRs; Grill is not an automatic substitute for owner/consumer governance.

## Source layout

```text
PraxFlow/
├── skills/
│   ├── project-bootstrap/
│   │   ├── SKILL.md
│   │   └── references/
│   └── praxflow/
│       └── SKILL.md
├── docs/
├── examples/
├── templates/
└── scripts/
```

See [installation](docs/installation.md), [workflow](docs/workflow.md) and [cross-repository interface guide](docs/cross-repo-workflow.md).
