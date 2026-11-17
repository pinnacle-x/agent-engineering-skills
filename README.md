# Agent Engineering Skills

Two **independent, portable Agent Skills** to support—rather than replace—the engineering judgment and capabilities of the active agent.

- **`project-bootstrap`** — create or reconcile `AGENTS.md` and, **only when a recurring, confirmed problem warrants one**, maintain a scoped rule in `.agents/rules/*.md` via `add-rule`.
- **`engineering-governance`** — optional, risk-based change impact, integrated verification and release management for **single-Git and multi-Git** projects.

## Engineering principles

- **Agent-first:** The agent owns code exploration, planning, specifications, TDD when useful, implementation, debugging, review and project documentation.
- **Evidence and sources:** Source code and actual tests establish current implemented behavior; external standards, approved product requirements and shared contracts remain authoritative for intended behavior.
- **Documentation by purpose:** Preserve existing organization. Without a convention, use `docs/` for project-level docs and a module folder for module-specific docs. Let the agent create and maintain the documentation actually warranted by the project or task; do not enforce a fixed document count, format or level of detail.
- **Rules only when justified:** No `.agents/rules/` directory is created by default. Add lasting rules in response to repeated problems with verified root causes and user approval; link each rule and its loading condition from `AGENTS.md`.
- **Proportionate governance:** Routine single-module changes do not need governance ceremonies. Significant interface, integration and release risks may merit governance regardless of the number of Git repositories.
- **Optional companions:** Grill and Wayfinder can help with difficult undecided design or large ambiguous projects, but are not mandatory steps or dependencies.

## Install

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

To install only one Skill:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

When supported, these install into `~/.agents/skills/`. Not every Harness discovers this directory automatically; verify runtime support.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule

$engineering-governance
$engineering-governance change-impact
$engineering-governance verify
$engineering-governance release
```

If the Harness lacks these shortcuts, request the installed Skill by name in normal language.

## Source layout

```text
skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── engineering-governance/
    └── SKILL.md
```

See [installation](docs/installation.md), [bootstrap and adding rules](docs/project-bootstrap.md), [agent-led workflow](docs/workflow.md) and [single-/multi-Git governance](docs/engineering-governance.md).
