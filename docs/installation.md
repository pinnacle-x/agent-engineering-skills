# Installing PraxFlow

PraxFlow is **one Agent Skill** with four modes: `bootstrap`, `interface-change`, `system-verify` and `manifest-release`.

It can use the shared Agent Skills locations on harnesses that support them:

- user/global: `~/.agents/skills/praxflow/`
- project-local: `.agents/skills/praxflow/`

These paths are not universal guarantees of harness discovery; check the active runtime.

## Install

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
python scripts/validate_portability.py
```

Verify the expected files:

```text
~/.agents/skills/
└── praxflow/
    ├── SKILL.md
    └── references/
        ├── AGENTS.template.md
        └── rules.template.md
```

To install only in a particular project:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project
```

The installed `.agents/skills/praxflow` directory is a Skill; the generated `.agents/rules` directory holds project rules. Do not confuse them.

## Invocation

```text
$praxflow bootstrap
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

If the runtime lacks this command syntax, ask it to **use the praxflow Skill in bootstrap mode** (or the relevant mode). Ensure the Skill is discoverable before relying on this instruction.

## Updating

From a local checkout, copy-mode updates can use:

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

`--force` overwrites the installed `praxflow` Skill directory; do not store project-specific edits there. It does not overwrite any target project's generated `AGENTS.md` or rules.

Link-mode updates require only `git pull`. On Windows, links may require Developer Mode or elevated privileges.

## If an older standalone bootstrap Skill was installed

The current design has only `praxflow`. If `~/.agents/skills/project-bootstrap/` exists from an earlier, separate installation, inspect it for local edits and uninstall that duplicate Skill separately. The PraxFlow installer intentionally does not delete other Skill directories automatically.

## Boundaries

- PraxFlow `bootstrap` handles only portable instruction entry and explicit rule index.
- `setup-matt-pocock-skills`, when installed, configures engineering-Skill issue tracking and domain-doc layout; PraxFlow does **not** duplicate those tasks.
- `grill-with-docs` owns open design decisions and ADRs.
- PraxFlow `interface-change` only tracks shared-contract ownership/consumer coordination after design is agreed.
- The active agent handles normal implementation, tests and review.
