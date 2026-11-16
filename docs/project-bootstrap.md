# Project Bootstrap Guide

`project-bootstrap` is a standalone, prompt-driven Agent Skill. It creates or reconciles a project's **portable instruction entry point**, not its product requirements, source tree, Git configuration or engineering implementation.

## Install

From a checkout of this repository:

```bash
python scripts/install.py --agent generic --scope user --skill project-bootstrap
```

The installed Skill should be discoverable at `~/.agents/skills/project-bootstrap/SKILL.md` when the active harness supports this shared location.

## Use in a new project

Open the project root in a supported agent and request:

```text
$project-bootstrap
```

Or, independent of invocation shorthand:

> Use the project-bootstrap Skill to set up an AGENTS.md entry point and explicitly indexed .agents/rules for this repository. Create only the rules and docs that are actually needed. Do not invent requirements or modify source files.

For a new software repository, one possible result is:

```text
project/
├── AGENTS.md
├── .agents/
│   └── rules/
│       ├── general.md
│       ├── development.md
│       ├── testing.md
│       └── documentation.md
└── ...existing project files
```

This is **not** a mandatory fixed tree. A small/new or documentation-only project might need only `AGENTS.md` and `general.md`. Formal documentation folders are created only when they have a real use.

## Use in an existing project

```text
Use project-bootstrap to audit and reconcile the existing AGENTS.md
and rule files. Preserve current instructions, source layout, and
working configuration; show the actual diff.
```

The Skill should inspect first, avoid duplicate sections, preserve existing documentation conventions, and report conflicts rather than overwrite them. Running it twice should not generate duplicate rule entries.

## AGENTS.md and rules

A root `AGENTS.md` is the single portable entry. The rules directory is an **explicit project convention**, not a universal auto-discovery feature:

- Always read `.agents/rules/general.md` (if created).
- Read `.agents/rules/development.md` for implementation changes.
- Read `.agents/rules/testing.md` for verification tasks.
- Read `.agents/rules/documentation.md` for documentation changes and behavior changes that affect documentation.

Only refer to files that exist. The Skill bundles examples under `references/` but must adapt them rather than blindly copy.

## Relationship with other Skills

- `project-bootstrap`: repository instructions and rule discovery; suitable before any project-specific engineering work.
- `setup-matt-pocock-skills`: optional, separate issue-tracker and domain-doc configuration. It may add an `Agent skills` section to `AGENTS.md` after bootstrap.
- `grill-with-docs`: clarify major unresolved design choices and create ADRs; do not use it just to initialize a repository.
- `praxflow interface-change`: plan and document the public contract owner/consumer rollout when independently versioned repositories share an interface.
- `praxflow system-verify` and `praxflow manifest-release`: verify the exact combined revisions and pin them for release.

A typical sequence is:

```text
project-bootstrap → read AGENTS.md/rules → normal engineering / Grill as needed
               → interface-change if shared contracts change
               → implementation and local tests
               → system-verify → manifest-release if applicable
```

## Manual acceptance checks

After invocation:

1. `AGENTS.md` exists and each required rule path referenced in it exists.
2. Rule-index entries identify when they must be read; they do not promise automatic scanning by all harnesses.
3. Existing content was preserved, and `git diff` contains no unrelated source/build/CI modifications.
4. Re-running bootstrap would not duplicate sections or destroy previous rules.
5. No unverified project facts, test outcomes or release versions were created.
6. The active harness has discovered the Skill; installed files alone are not proof of activation.

## Cross-harness caveat

Agent Skills and `AGENTS.md` support vary by harness and version. A separate, minimal adapter may be needed to enable discovery or recognition. Keep the canonical files under `AGENTS.md` and `.agents/` without vendor-specific syntax.
