# Installing Agent Engineering Skills

Two independent Skills are provided:

- `project-context` — new/existing project entry; current source-based requirements/constraints; direct pointers to upstream Grill local tracker/domain documents; **system architecture/high-level design synchronization** with `update-design`; approved rules.
- `engineering-governance` — optional integrated system verification and reproducible release.

## Install both

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

On runtimes supporting the shared Skill location:

```text
~/.agents/skills/
├── project-context/
│   ├── SKILL.md
│   └── references/
│       ├── AGENTS.template.md
│       ├── architecture.template.md
│       ├── design-overview.template.md
│       ├── docs-index.template.md
│       ├── requirements.template.md
│       ├── technical-constraints.template.md
│       └── rules.template.md
└── engineering-governance/
    └── SKILL.md
```

Install individually:

```bash
python scripts/install.py --agent generic --scope user --skill project-context
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

Or project-scoped:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project --skill project-context
```

The installer installs **Skills**, not target-project documentation, upstream Grill/Wayfinder or a tracker configuration.

## Set up Grill's Local Markdown tracker separately

In the target repository, after installing compatible upstream Skills, use `/setup-matt-pocock-skills` and choose **Local Markdown**. This sets up local tracker guidance and domain-doc consumers in the project's existing `AGENTS.md` or `CLAUDE.md` as appropriate.

Typical upstream local locations:

- `docs/agents/issue-tracker.md` and `docs/agents/domain.md` for navigation rules.
- `.scratch/<effort>/map.md` and decision issue files from Wayfinder.
- `.scratch/<feature>/spec.md` from `to-spec`.
- `GLOSSARY.md` and `docs/adr/` for domain terms and qualifying architecture decisions.

Upstream `to-spec` also expects the configured triage-label vocabulary; if upstream setup skipped it, complete that configuration before invoking `to-spec`. The `ready-for-agent` label describes readiness, not automatic authorization to start coding.

**Check `.gitignore`** for `.scratch/`: local Markdown files are not necessarily tracked or available after a fresh checkout. Configure retention with the project owner; this Skill does not auto-edit Git ignore rules or migrate the files.

## Invoke our Skills

```text
$project-context
$project-context update-design
$project-context add-rule

$engineering-governance verify
$engineering-governance release
```

If shorthand is unsupported, request by Skill name. Grill/Wayfinder/to-spec are external user-invoked design workflows. The Agent itself executes engineering tasks and checks whether current architecture and high-level design require synchronization.

## Project navigation

`AGENTS.md` should link actual relevant project architecture/overview and approved requirements/constraints documents, plus the configured upstream tracker/domain guidance. A project may retain its existing docs index, but **no extra `docs/README.md` index is mandatory**. Rules stay directory-scoped at `.agents/rules/` and are created only when approved.

## Upgrade

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

## Rename migration: project-bootstrap → project-context

This release renames the Skill directory and invocation to `project-context` without changing the `update-design` or `add-rule` modes. The installer discovers the new directory automatically but **does not remove** a previously installed `project-bootstrap`. Even with `--force`, both could remain, causing duplicated Skill choices.

After reinstalling, inspect any locally modified files under the **old** user or project Skill path (`~/.agents/skills/project-bootstrap/` or `<project>/.agents/skills/project-bootstrap/`), then remove **only that old installed Skill directory** when safe. Keep your actual target project's engineering documents, `.agents/rules/` and `.scratch/` untouched. The installer prints a warning when it sees the old directory alongside the new one.

`--force` replaces only selected installed Skill directories. Inspect any historical `cross-repo-governance` installation separately before cleanup. Windows link-mode installation can require Developer Mode or elevated permissions.
