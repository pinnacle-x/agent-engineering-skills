# Installing PraxFlow

PraxFlow is **Agent Skills first**. The canonical skills live in `skills/` and use the `SKILL.md` Agent Skills format.

PraxFlow currently targets **Codex** and **DeepSeek Harness**. Both use the shared Agent Skills location:

- user/global: `~/.agents/skills/`
- project-local: `.agents/skills/`

Claude is no longer a supported target for this project.

## Recommended installation model

Clone PraxFlow once, then install or link the canonical `skills/` directories into `~/.agents/skills/`.

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent deepseek --scope user
```

The Codex target installs to the same location:

```bash
python scripts/install.py --agent codex --scope user
```

Because both targets resolve to `~/.agents/skills/`, only one physical installation is required. Installing once is enough for both Codex and DeepSeek Harness, as long as each agent is configured to discover the shared Agent Skills path.

Use project scope when the skills should travel with one repository:

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

## Installing only selected PraxFlow skills

Repeat `--skill` to select a subset:

```bash
python scripts/install.py --agent deepseek --scope user \
  --skill praxflow-pdf-ingest \
  --skill praxflow-system-discovery
```

## Grill skills used with PraxFlow

The Grill skills are maintained upstream in `mattpocock/skills`; they are not duplicated inside the PraxFlow repository.

For the Grill workflow used by this project, install all four of these into the same `~/.agents/skills/` directory:

- `grill-with-docs`
- `grill-me`
- `grilling`
- `domain-modeling`

`grill-with-docs` delegates to `grilling` and `domain-modeling`, while `grill-me` delegates to `grilling`. Installing only the two user-facing Grill skills leaves their dependencies missing.

After installation, a typical shared directory contains:

```text
~/.agents/skills/
├── grill-with-docs/
├── grill-me/
├── grilling/
├── domain-modeling/
├── praxflow-interface-change/
├── praxflow-manifest-release/
├── praxflow-pdf-ingest/
├── praxflow-protocol-validate/
├── praxflow-repo-bootstrap/
├── praxflow-spec-materialize/
├── praxflow-spec-validate/
├── praxflow-system-discovery/
└── praxflow-system-verify/
```

## Updating

For copy-mode PraxFlow installs:

```bash
git pull
python scripts/install.py --agent deepseek --scope user --force
```

For link-mode installs, `git pull` is sufficient because the installed paths point back to the checkout.

## DeepSeek Harness discovery

DeepSeek Harness must load its Skill registry and filesystem Skill provider. With default roots enabled, the filesystem provider scans `<agentsHome>/skills`, where `agentsHome` defaults to `~/.agents` unless `DSH_AGENTS_HOME` overrides it.

If Skills exist under `~/.agents/skills/` but DeepSeek still does not list them, check:

1. the Skill registry/filesystem provider is enabled;
2. `includeDefaultRoots` has not been disabled;
3. `DSH_AGENTS_HOME` is not pointing somewhere other than `~/.agents`;
4. every Skill directory contains a valid `SKILL.md` with valid frontmatter.

## Portability policy

The canonical PraxFlow workflow remains agent-neutral. Codex- or DeepSeek-specific integration belongs in the adapter/configuration layer; workflow semantics belong in `skills/`.
