# Agent Engineering Skills

Two independent portable Agent Skills supporting **direct Agent engineering work**, with upstream Grill/Wayfinder for consequential decisions and **no mandatory parallel specification index**.

- **`project-context`** — enter greenfield or existing-source projects; establish evidence-backed requirements/constraints and project entry pointers; **create or update current system architecture and high-level design** through `update-design`; maintain approved rules on demand.
- **`engineering-governance`** — optional `verify` and `release` for single-Git or multi-Git products.

## Preferred project flow

```text
New project goals / existing project actual source
                 ↓
Grill (focused) or Wayfinder (multi-session), when decisions are unresolved
                 ↓
Use upstream glossary / ADRs / decision Map / to-spec as appropriate
                 ↓
Confirm what is approved and find its real saved location
                 ↓
Agent reads code + confirmed scheme and executes directly
                 ↓
Verify changed behavior and sync affected architecture/overview docs
                 ↺  Repeat when important new decisions emerge
```

**Grill/Wayfinder do not guarantee every confirmed detail is stored in a durable project file.** `grill-with-docs` stores terms and qualifying ADRs; `wayfinder` stores a Map and decision tickets. `to-spec` can consolidate longer decision work into a task specification. Check the saved artifacts and persist any important missing confirmed decisions in the existing appropriate project record. A proposal is not approved merely because a Skill generated it.

## Prefer upstream Local Markdown; no GitHub Issues requirement

Use upstream `/setup-matt-pocock-skills` once per target project and choose **Local Markdown** as the issue tracker when GitHub/GitLab Issues are not desired. The upstream configuration normally records:

- `docs/agents/issue-tracker.md` — where the local Map/spec live.
- `docs/agents/domain.md` — how to read glossary and ADRs.
- `.scratch/<effort>/map.md` and `.scratch/<effort>/issues/NN-<slug>.md` — Wayfinder's native decision artifacts.
- `.scratch/<feature>/spec.md` — `to-spec`'s native task specification.

These are **upstream-owned locations**, not additional templates we require. The project may use other established paths. `.scratch/` may be ignored by Git: inspect `.gitignore` and decide whether those decisions need preservation across checkouts.

## Long-lived engineering documents

Keep **current system architecture** and **high-level design** under project version control when appropriate. Existing project paths win; common defaults are `docs/architecture.md` and `docs/design-overview.md`. These describe the current engineering system and confirmed future changes, not duplicated Wayfinder tickets or a second Spec.

- The Agent checks whether a code change affects these documents and syncs relevant sections as part of ordinary work.
- For explicit review, creation or catch-up synchronization, use `$project-context update-design`.
- Existing source and observed results describe **what is actually implemented**; approved requirements, ADRs and selected task spec describe **intended behavior**. If they disagree, flag the discrepancy instead of silently rewriting a requirement.

Root `AGENTS.md` points to the actual stable architecture/overview paths and the upstream domain/tracker configuration when present. A project with a useful index may keep it, but **`docs/README.md` is not a mandatory second index**. Project rules still use only the directory pointer `.agents/rules/`; do not create that folder until an approved rule is needed.

## Installation

```bash
git clone https://github.com/pinnacle-x/agent-engineering-skills.git
cd agent-engineering-skills
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

To install one Skill:

```bash
python scripts/install.py --agent generic --scope user --skill project-context
python scripts/install.py --agent generic --scope user --skill engineering-governance
```

## Invocation

```text
$project-context
$project-context update-design
$project-context add-rule

$engineering-governance verify
$engineering-governance release
```

If shorthand is not available, request a Skill by name in natural language. Grill/Wayfinder and upstream tracker setup are **separate installs**, not dependencies shipped in this repository.

See [project bootstrap](docs/project-context.md), [local Markdown and document discovery](docs/document-discovery.md), [engineering workflow](docs/workflow.md), [sources of truth](docs/source-of-truth.md), [governance](docs/engineering-governance.md), and [installation](docs/installation.md).

## Renamed Skill (v0.10.0)

The former `project-bootstrap` is now **`project-context`**. Previous installations are not removed automatically; after checking for local edits, remove only the old installed Skill directory to avoid duplicate names. [Migration details](docs/installation.md#rename-migration-project-bootstrap--project-context).
