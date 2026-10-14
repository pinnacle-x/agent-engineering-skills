# PraxFlow

PraxFlow is a **small cross-repository governance Skill** for product engineering. It intentionally does not duplicate capabilities that modern agents already provide.

DeepSeek, Codex, and other capable agents can already read PDFs and code, inspect repositories, analyze protocols, draft specifications, run tests, and review implementation. Use those native capabilities directly. Use `grill-with-docs` for important unresolved design choices.

PraxFlow is only for three product-level concerns that must remain consistent across independent repositories and sessions:

1. public interface changes;
2. integrated verification tied to exact repository revisions;
3. reproducible release manifests.

## Skill

PraxFlow installs as one Agent Skill:

```text
skills/praxflow/SKILL.md
```

Supported modes:

```text
$praxflow interface-change
$praxflow system-verify
$praxflow manifest-release
```

Everything else should use the active agent or companion engineering Skills.

## Recommended stack

```text
Agent (DeepSeek / Codex)
  ├─ read PDF / code / docs
  ├─ analyze / plan / implement / test / review
  │
  ├─ grill-with-docs          # only when major design choices need human review
  │
  └─ praxflow                # only when cross-repo governance is required
       ├─ interface-change
       ├─ system-verify
       └─ manifest-release
```

## Repository model

```text
PraxFlow/
├── skills/
│   └── praxflow/
│       └── SKILL.md
├── docs/
├── examples/
├── templates/
└── scripts/
```

See `docs/installation.md` and `docs/workflow.md`.
