# Agent Engineering Skills

This repository maintains **two independent Agent Skills** with different responsibilities and no mandatory dependency between them:

- **`project-bootstrap`** — initialize or reconcile a repository's portable root `AGENTS.md` and explicit `.agents/rules/` index without overwriting existing project conventions.
- **`cross-repo-governance`** — govern an **approved** public contract across independent repositories, record integrated verification tied to exact commit revisions, and create reproducible release manifests.

They complement—not replace—the active agent and engineering Skills. Use `grill-with-docs` for major design decisions and ADRs; neither Skill duplicates those interviews.

## Install

The existing installer discovers Skills from `skills/*/SKILL.md`:

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

To install only one:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill cross-repo-governance
```

Expected paths when both are installed:

```text
~/.agents/skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── cross-repo-governance/
    └── SKILL.md
```

Some harnesses require a small configuration adapter to discover this path. File presence is not evidence of runtime activation.

## Invocation

```text
$project-bootstrap

$cross-repo-governance interface-change
$cross-repo-governance system-verify
$cross-repo-governance manifest-release
```

For harnesses that do not support `$...` shorthand, request the installed Skill by name in natural language.

## Responsibilities and boundaries

| Task | Owner |
| --- | --- |
| Portable AGENTS.md and rule index | project-bootstrap |
| Issue tracker/domain-doc engineering setup | setup-matt-pocock-skills (optional) |
| Important design decisions, API/protocol semantics, ADRs | grill-with-docs (when needed) |
| Implementation, repository-local tests and review | active agent and engineering Skills |
| Approved multi-repository contract rollout | cross-repo-governance interface-change |
| Exact multi-repository revision verification | cross-repo-governance system-verify |
| Immutable release composition | cross-repo-governance manifest-release |

## Repository layout

```text
skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── cross-repo-governance/
    └── SKILL.md
```

See [installation](docs/installation.md), [bootstrap](docs/project-bootstrap.md), [workflow](docs/workflow.md) and [cross-repository coordination](docs/cross-repo-workflow.md).

The GitHub repository URL retains its existing spelling until a separate repository rename is performed. The **Skill names and invocation commands** above are the canonical new names.
