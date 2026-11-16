# Installing the portable Agent Skills

This repository provides two independent Skills:

- `skills/project-bootstrap/SKILL.md` — repository instruction and rule initialization.
- `skills/praxflow/SKILL.md` — cross-repository governance.

Both can use the shared Agent Skills locations when supported by the active harness:

- user/global: `~/.agents/skills/`
- project-local: `.agents/skills/`

The installer supports `generic` and `codex` targets (and retains other legacy target aliases). All currently map to these shared paths.

## Install both Skills

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

The installer discovers all `skills/*/SKILL.md` entries by default. Expected paths:

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── praxflow/
    └── SKILL.md
```

## Install separately

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill praxflow
```

## Install in a particular project

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-bootstrap
```

The installed Skill location is `/path/to/project/.agents/skills/project-bootstrap/`. Do not confuse that with the **generated rules** at `/path/to/project/.agents/rules/`.

## Invoke

```text
$project-bootstrap
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

`$...` is a syntax example for harnesses that support it. Otherwise request the Skill by name, e.g. "Use project-bootstrap to initialize this repository." The harness must actually discover the installed Skill; path presence alone does not guarantee activation.

## Updating safely

For a copy-mode installation, first update the source checkout:

```bash
git pull
python scripts/install.py --agent generic --scope user --skill project-bootstrap --force
```

`--force` **replaces the installed Skill directory**. Do not store project-specific edits there. It does not change an existing target project's `AGENTS.md` or rules. If you use link mode for developing the Skill, only `git pull` is required.

On Windows, directory links may need Developer Mode or elevated permissions; copy mode avoids that issue.

## Scope boundaries

`project-bootstrap` is a standalone initialization Skill. It does not install engineering Skills, configure issue trackers, initialize Git or invoke PraxFlow automatically.

`praxflow` does not bootstrap repositories, read PDFs for its own sake, generate specifications, implement features or review routine code. Use the active agent and appropriate engineering Skills for those tasks. For major open design decisions, invoke `grill-with-docs` separately.
