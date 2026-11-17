# Installing Agent Engineering Skills

The repository offers two independent portable Skills:

- `project-bootstrap` — enter a **new or existing project**, establish `AGENTS.md`, derive evidence-backed confirmed requirements and technical constraints for existing codebases, and optionally maintain approved project rules.
- `engineering-governance` — integrated verification and reproducible release coordination for single-Git and multi-Git products.

## Install both

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Expected on runtimes supporting the shared path:

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
│       ├── AGENTS.template.md
│       ├── rules.template.md
│       ├── requirements.template.md
│       └── technical-constraints.template.md
└── engineering-governance/
    └── SKILL.md
```

## Install independently

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

For a project-scoped Skill install:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-bootstrap
```

`.agents/skills/` stores installed Skills. The target project's `.agents/rules/` is **not** created by the installer or by default bootstrap. Root `AGENTS.md` only names the rules directory; optional rule files and internal indexes are maintained there. Runtime discovery depends on the active Harness.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule
$engineering-governance verify
$engineering-governance release
```

If `$...` shorthand is unsupported, request the Skill by name and describe the goal.

## Upgrade

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

`--force` replaces installed Skill directories; preserve any local modifications. The installer does not remove old renamed Skill folders automatically. Inspect and uninstall an obsolete `cross-repo-governance` folder before using `engineering-governance` to avoid duplicate capabilities. Link-mode installs track the source checkout; on Windows, creating links may require Developer Mode or elevated permissions.
