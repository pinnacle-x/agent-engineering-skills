# PraxFlow Portability Contract

PraxFlow is an **agent-neutral Agent Skill**. The canonical implementation is:

```text
skills/praxflow/SKILL.md
```

Vendor-specific plugin formats exist only to make that Skill easier to install or discover.

## Canonical skill rules

The `skills/praxflow/` package must:

1. Contain the canonical `SKILL.md` entry point.
2. Keep frontmatter `name: praxflow` aligned with the directory name.
3. Provide a clear description that explains the complete workflow and when it is relevant.
4. Use only portable frontmatter unless a field is known to be harmless across supported agents.
5. Reference bundled resources using paths relative to the `praxflow` Skill directory.
6. Prefer portable Python for executable helpers when practical; scripts must fail with actionable messages when a dependency is missing.
7. Keep product facts, architecture decisions, and repository-specific configuration out of the Skill package.
8. Represent workflow stages as modes inside the one Skill rather than separate PraxFlow Skill packages.

## Do not hard-code an agent runtime

The canonical Skill must not require:

- Codex-specific tool names
- Claude-only shell interpolation or environment variables
- Cursor-only commands
- Gemini-only activation APIs
- Copilot-only tool grants
- OpenCode-only metadata
- a particular model vendor

The Skill may describe optional companion capabilities semantically. Example:

> If a high-impact unresolved decision remains, recommend an interactive deep-design review. If the environment provides a `grill-with-docs` skill, it is one compatible implementation.

Do not make PraxFlow depend on slash-command syntax that another agent may not implement.

## Adapter boundary

Agent-specific integration belongs outside the canonical workflow logic.

Current adapters include:

- `.codex-plugin/plugin.json` — Codex packaging metadata
- `scripts/install.py` — filesystem installer for supported agents

Additional adapters may exist, but they must package the same `skills/praxflow/` implementation rather than fork workflow semantics.

## Shared paths first

When an agent supports `.agents/skills`, prefer that path because it lets one PraxFlow installation work across several agents. Use an agent-specific directory only when necessary or when the user explicitly wants agent-specific precedence.

## Human gates are semantic

PraxFlow uses human gates for high-impact decisions, specification approval, safety-sensitive validation, and product release. These gates must be expressed in the Skill instructions as required behaviors, not as assumptions about one agent's approval UI.

For example:

- good: "Stop and request explicit human approval before resolving a CRITICAL open decision."
- avoid: "Call Codex approval tool X."

## Compatibility testing

A PraxFlow release should eventually validate at least:

- YAML frontmatter and `name: praxflow`
- mode names and routing rules
- relative resource links
- script portability on Windows and Linux
- discovery in the shared Agent Skills path
- explicit invocation and automatic discovery behavior where supported

Agent-specific enhancements may be added later, but they must not fork the workflow semantics of the canonical Skill.
