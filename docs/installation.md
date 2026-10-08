# Installing PraxFlow

PraxFlow is **Agent Skills first**. The canonical workflow now lives in one skill:

```text
skills/praxflow/SKILL.md
```

PraxFlow currently targets **Codex** and **DeepSeek Harness**. Both use the shared Agent Skills location:

- user/global: `~/.agents/skills/`
- project-local: `.agents/skills/`

Claude is not a supported PraxFlow target for this project.

## Recommended installation model

Clone PraxFlow once, then install or link the single `praxflow` directory into `~/.agents/skills/`.

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent deepseek --scope user
```

The Codex target installs to the same location:

```bash
python scripts/install.py --agent codex --scope user
```

Because both targets resolve to `~/.agents/skills/`, only one physical installation is required. Installing once is enough for both Codex and DeepSeek Harness, as long as each agent discovers the shared Agent Skills path.

After installation:

```text
~/.agents/skills/
└── praxflow/
    ├── SKILL.md
    └── scripts/
        └── extract_pdf.py
```

## Invocation model

PraxFlow is a single Skill with workflow modes:

```text
$praxflow repo-bootstrap
$praxflow pdf-ingest input/<file>.pdf
$praxflow system-discovery
$praxflow spec-materialize
$praxflow spec-validate
$praxflow protocol-validate
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

Use project scope when the Skill should travel with one repository:

```bash
python scripts/install.py --agent deepseek --scope project --project /path/to/project
```

Use `--mode link` while developing PraxFlow so edits are visible without reinstalling:

```bash
python scripts/install.py --agent deepseek --scope user --mode link
```

On Windows, creating symbolic links may require Developer Mode or elevated privileges. Use the default `copy` mode if linking is unavailable.

## Supported targets

| Target | User scope | Project scope | Notes |
|---|---|---|---|
| `generic` | `~/.agents/skills` | `.agents/skills` | Shared Agent Skills location. |
| `codex` | `~/.agents/skills` | `.agents/skills` | Supported. |
| `deepseek` | `~/.agents/skills` | `.agents/skills` | Supported for DeepSeek Harness. |

## Grill skills used with PraxFlow

The Grill skills are maintained upstream in `mattpocock/skills`; they are not duplicated inside PraxFlow.

For the Grill workflow used by this project, install all four into the same `~/.agents/skills/` directory:

- `grill-with-docs`
- `grill-me`
- `grilling`
- `domain-modeling`

`grill-with-docs` delegates to `grilling` and `domain-modeling`, while `grill-me` delegates to `grilling`.

A typical shared directory is therefore:

```text
~/.agents/skills/
├── praxflow/
├── grill-with-docs/
├── grill-me/
├── grilling/
└── domain-modeling/
```

## Updating

For copy-mode installs:

```bash
git pull
python scripts/install.py --agent deepseek --scope user --force
```

For link-mode installs, `git pull` is sufficient because the installed path points back to the checkout.

## DeepSeek Harness discovery

DeepSeek Harness must load its Skill registry and filesystem Skill provider. With default roots enabled, the filesystem provider scans `<agentsHome>/skills`, where `agentsHome` defaults to `~/.agents` unless `DSH_AGENTS_HOME` overrides it.

If `~/.agents/skills/praxflow/SKILL.md` exists but DeepSeek does not list it, check:

1. the Skill registry/filesystem provider is enabled;
2. `includeDefaultRoots` has not been disabled;
3. `DSH_AGENTS_HOME` is not pointing somewhere other than `~/.agents`;
4. `praxflow/SKILL.md` has valid frontmatter.

## Portability policy

The canonical PraxFlow workflow remains agent-neutral. Codex- or DeepSeek-specific integration belongs in the adapter/configuration layer; workflow semantics belong in `skills/praxflow/SKILL.md`.
