# Installing Agent Engineering Skills

The repository contains two independent Skills:

- `project-bootstrap` — enter a new or existing source project, establish `AGENTS.md` and a **discoverable index** for authoritative requirements, constraints and confirmed designs, plus optional approved rules.
- `engineering-governance` — optional integration verification and reproducible release for single-Git and multi-Git projects.

## Install both

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Expected on supported runtimes:

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
│       ├── AGENTS.template.md
│       ├── docs-index.template.md
│       ├── requirements.template.md
│       ├── technical-constraints.template.md
│       └── rules.template.md
└── engineering-governance/
    └── SKILL.md
```

## Install independently

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

Project-local Skills can be installed with:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-bootstrap
```

These commands install the Skills, not an initialized target project. Open the project and run `$project-bootstrap` to establish the project entry and document index.

## Discovery contract for the target project

`AGENTS.md` should reference the **actual project document index** (default `docs/README.md`, or an existing equivalent). That index links to active/confirmed scheme documents, accepted requirements/constraints and pending/superseded designs. During future Grill/Wayfinder rounds, update the source document and index, not a growing `AGENTS.md` list.

Separately, `AGENTS.md` mentions the `.agents/rules/` directory. It is not created by installer or default bootstrap; approved rules and any internal index live there. The two directories serve different purposes.

## Invocation

```text
$project-bootstrap
$project-bootstrap add-rule

$engineering-governance verify
$engineering-governance release
```

Grill and Wayfinder are optional recurring design-clarification steps, not required dependencies for installing these Skills. The agent directly executes confirmed schemes. If shorthand is unavailable, ask for the Skill by name.

## Updating

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

`--force` replaces installed Skill directories; preserve local modifications. The installer cannot automatically remove previously renamed folders. Remove an obsolete `cross-repo-governance` installation manually after checking any local edits, to avoid two governance entry points. On Windows, directory symlinks can require Developer Mode or elevated permissions.
