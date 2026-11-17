# Installing Agent Engineering Skills

The repository contains two **independent** portable Agent Skills:

- `project-bootstrap` — root `AGENTS.md` management and optional, evidence-based `add-rule` for `.agents/rules/*.md`.
- `engineering-governance` — optional change impact, integrated verification and release for single-Git and multi-Git products.

## Install both

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Expected (on Harnesses that support the shared directory):

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
│       ├── AGENTS.template.md
│       └── rules.template.md
└── engineering-governance/
    └── SKILL.md
```

## Install just one

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

For a project-scoped installation:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-bootstrap
```

`.agents/skills/` stores installed Skills; `.agents/rules/` stores approved project-specific instructions and is **not created by the installer or bootstrap**. The project's `AGENTS.md` mentions only the `.agents/rules/` directory and directs the agent to inspect it when present. File-level scope and any index belong inside the rules directory; changing individual rules does not change `AGENTS.md`. Harness discovery of either location is not universal.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule

$engineering-governance
$engineering-governance change-impact
$engineering-governance verify
$engineering-governance release
```

If a runtime does not support the command shorthand, ask it to use the installed Skill by name and describe the mode.

## Update

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

`--force` overwrites installed Skill directories; inspect local edits before replacing them. The installer never deletes installed folders from **old Skill names** automatically. When moving from `cross-repo-governance` to `engineering-governance`, inspect then uninstall the former yourself; do not let two similarly purposed Skills coexist by mistake.

Link-mode installs update when their source checkout is updated; on Windows symbolic links may require Developer Mode or elevated privileges.
