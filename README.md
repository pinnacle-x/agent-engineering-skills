# Agent Engineering Skills

Two **independent Agent Skills** help an active agent enter a project, discover authoritative design documents, and coordinate integration or release when needed.

- **`project-bootstrap`** — greenfield or existing-source project entry; evidence-based current-state baseline; confirmed requirements/constraints; a stable project-document index linked from `AGENTS.md`; on-demand project rules under `.agents/rules/`.
- **`engineering-governance`** — optional `verify` and `release` for single-Git and multi-Git projects.

## The engineering loop

```text
New project / existing source baseline
                ↓
Identify next important unresolved design question
                ↓
Grill or Wayfinder as appropriate → user/project confirms decision
                ↓
Update the authoritative scheme document and document index
                ↓
Agent reads current active scheme + actual source → executes directly
                ↓
Actual checks and feedback → next decision or continuation
```

**This loop repeats throughout the project**, rather than treating Grill/Wayfinder as an initialization-only step. A well-scoped change already covered by accepted design can be implemented directly; every minor coding question does not require another design session.

For **existing projects**, current source/build/runtime evidence establishes **present implementation facts**. From that baseline, maintain confirmed requirements, technical constraints and design records. Source behavior alone does not establish an approved future requirement. Uncertain intent stays pending.

For **new projects**, start from accepted goals and constraints, iteratively clarify architectural and subsystem choices, then carry out each confirmed scope directly.

## Document discoverability

- Root `AGENTS.md` points to **one stable project document index** (normally `docs/README.md`, or the existing project index) and to the `.agents/rules/` directory.
- The **document index** lists the actual current baseline, accepted requirements/constraints, active design documents and open/superseded decisions, with real paths and applicability. It is a map, not a competing source of requirements.
- After each meaningful confirmed design round, the **agent updates the source document and index**. No repeated bootstrap invocation or growth of `AGENTS.md` is needed.
- Use the project's existing documentation structure; without one, project-wide documents belong under `docs/` and module docs alongside their modules. Maintain the detail required by the project rather than a fixed document count.
- The `.agents/rules/` directory is **not** created until an approved rule is necessary. Individual rules and any internal index are maintained there without changing `AGENTS.md`.

## Install

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Install independently:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

Typical supported shared installation path: `~/.agents/skills/`. Confirm the active Harness actually discovers installed Skills.

## Invoke

```text
$project-bootstrap
$project-bootstrap add-rule

$engineering-governance verify
$engineering-governance release
```

The agent calls Grill or Wayfinder as needed for **new important design questions**, and then **executes the confirmed solution itself**. There is no separate execution or change-impact Skill.

## Layout

```text
skills/
├── project-bootstrap/
│   ├── SKILL.md
│   └── references/
└── engineering-governance/
    └── SKILL.md
```

See [bootstrap](docs/project-bootstrap.md), [workflow](docs/workflow.md), [document discovery](docs/document-discovery.md), [sources of truth](docs/source-of-truth.md), [governance](docs/engineering-governance.md), and [installation](docs/installation.md).
