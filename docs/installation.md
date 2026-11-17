# Installing Agent Engineering Skills

The repository provides **two independent Skills**, both using the portable Agent Skills directory convention where supported.

- `project-bootstrap` — portable `AGENTS.md` and `.agents/rules/` setup.
- `cross-repo-governance` — shared-contract coordination, integrated verification and release composition.

## Install both

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Expected:

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
│       ├── AGENTS.template.md
│       └── rules.template.md
└── cross-repo-governance/
    └── SKILL.md
```

## Install independently

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill cross-repo-governance
```

For a project-scoped install:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-bootstrap
```

These commands use the repository's actual installer and do not depend on any other Skill. An installation in `.agents/skills/` is **not** the same as project rules in `.agents/rules/`.

## Invocation

```text
$project-bootstrap
$cross-repo-governance interface-change
$cross-repo-governance system-verify
$cross-repo-governance manifest-release
```

If `$...` commands are unsupported by the active Harness, request the Skill by name in natural language and confirm discovery.

## Updating

For copy installations after updating the local source checkout:

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

`--force` replaces the installed Skill directory or directories. Preserve any local modifications before using it. The installer does not alter a target project's generated rules or delete old renamed Skills automatically. When migrating from an older Skill name, inspect the old installed folder for custom edits before removing it.

For symlink installs, a source checkout update is sufficient. Windows symlinks can require Developer Mode or elevated permissions.

## Scope separation

Bootstrap only reconciles `AGENTS.md` and explicit rules. `setup-matt-pocock-skills` separately manages issue-tracker and domain-doc conventions. `grill-with-docs` handles major unresolved design decisions and ADRs. Cross-repo Governance coordinates approved designs across independent repositories, verifies exact revisions and creates release manifests. Normal coding and local checks remain the responsibility of the active agent.
