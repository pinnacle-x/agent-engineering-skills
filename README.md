# Agent Engineering Skills

This repository provides **two independent, portable Agent Skills**. They establish project context and coordinate verification/release when needed; the active agent executes engineering work directly.

- **`project-bootstrap`** — enter either a project **from zero** or an **existing codebase**; establish `AGENTS.md` and, for existing projects, evidence-based confirmed requirements and technical constraints. Maintain approved rules within `.agents/rules/` via `add-rule`.
- **`engineering-governance`** — optional integrated `verify` and reproducible `release` workflows for single-Git and multi-Git products.

## Workflow principles

- **Source first for existing projects:** The current codebase, actual build configuration and observed engineering state are the factual baseline. Use these facts to establish documents covering confirmed requirements and technical constraints. Distinguish observed behavior from approved intent; keep unresolved assumptions explicitly pending.
- **New projects:** Begin from the user's goals, confirmed needs and technical decisions; do not assume an existing codebase or invent requirements.
- **Direct agent execution:** When goals and necessary design decisions are clear, the agent executes the task. When substantial design is unresolved, use `grill-with-docs` if helpful; for very large ambiguous initiatives, `wayfinder` may help. Neither is mandatory or an execution intermediary.
- **Project documents:** Respect existing structure. Without a convention, use `docs/` for project-wide documents and module directories for module-specific ones. Use the amount and detail warranted by project requirements.
- **Rules on demand:** `AGENTS.md` mentions only `.agents/rules/`; bootstrap does not create an empty directory. Approved rules and any optional index are maintained **inside** that directory without updating `AGENTS.md` per change.
- **Governance on demand:** The agent checks affected code, modules and interfaces as part of direct work. The governance Skill is for integrated evidence and releases when needed; it does not introduce a separate impact-analysis step.

## Install

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Install one Skill independently:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

The installed shared directory is typically `~/.agents/skills/` on supported Harnesses; verify discovery in the active runtime.

## Invoke

```text
$project-bootstrap
$project-bootstrap add-rule

$engineering-governance verify
$engineering-governance release
```

If the runtime does not recognize the shorthand, request the installed Skill by name in ordinary language.

## Layout

```text
skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── engineering-governance/
    └── SKILL.md
```

See [project bootstrap](docs/project-bootstrap.md), [agent-led workflow](docs/workflow.md), [engineering governance](docs/engineering-governance.md), [installation](docs/installation.md) and [sources of truth](docs/source-of-truth.md).
