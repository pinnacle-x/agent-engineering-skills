# Installing PraxFlow

PraxFlow is one lightweight Agent Skill:

```text
skills/praxflow/SKILL.md
```

It currently targets Codex and DeepSeek Harness through the shared Agent Skills location:

- user/global: `~/.agents/skills/`
- project-local: `.agents/skills/`

## Install

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent deepseek --scope user
```

Codex uses the same destination:

```bash
python scripts/install.py --agent codex --scope user
```

After installation:

```text
~/.agents/skills/
└── praxflow/
    └── SKILL.md
```

Only one physical PraxFlow installation is required when both agents discover `~/.agents/skills`.

## Modes

```text
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

Do not use PraxFlow for PDF ingestion, repository bootstrap, system discovery, specification generation/validation, protocol analysis, implementation, or code review. Use the active agent and companion engineering Skills instead.

For major unresolved design choices, install and use `grill-with-docs` separately from its upstream skill repository.

## Project-local installation

```bash
python scripts/install.py --agent deepseek --scope project --project /path/to/project
```

## Link mode for PraxFlow development

```bash
python scripts/install.py --agent deepseek --scope user --mode link
```

On Windows, symbolic links may require Developer Mode or elevated privileges. Use the default copy mode if linking is unavailable.

## Updating

Copy mode:

```bash
git pull
python scripts/install.py --agent deepseek --scope user --force
```

Link mode:

```bash
git pull
```

## DeepSeek discovery

If `~/.agents/skills/praxflow/SKILL.md` exists but DeepSeek does not list it, verify that its filesystem Skill provider includes the default `~/.agents` root and that `DSH_AGENTS_HOME` has not redirected the agent home.
