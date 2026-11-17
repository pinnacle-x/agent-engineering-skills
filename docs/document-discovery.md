# Discovering Grill Decisions and Current Engineering Design

**The project does not need a second scheme index by default.** Prefer the upstream Grill domain guidance and local-Markdown tracker, combined with a small set of durable, directly referenced current design documents.

## Configure the upstream Local Markdown tracker

Run upstream `/setup-matt-pocock-skills` in the target project and choose **Local Markdown**. It configures how the upstream Skills access local files and writes the appropriate agent entry block.

Typical paths, subject to actual project configuration:

```text
project/
├── AGENTS.md                      # project instructions, navigation
├── docs/
│   ├── agents/
│   │   ├── issue-tracker.md        # upstream local tracker settings
│   │   └── domain.md               # upstream glossary/ADR consumer guidance
│   ├── architecture.md             # living system architecture, when needed
│   ├── design-overview.md          # living high-level design, when needed
│   └── adr/                        # qualifying permanent architectural decisions
├── GLOSSARY.md                     # if the project has resolved domain terminology
└── .scratch/
    ├── <effort>/
    │   ├── map.md                  # wayfinder's decision Map
    │   └── issues/
    │       └── NN-<slug>.md        # decision ticket and resolved answer
    └── <feature>/
        └── spec.md                 # to-spec's task snapshot
```

This tree is illustrative, **not** a bootstrap-created scaffold. Upstream setup may choose `CLAUDE.md` instead of `AGENTS.md`; do not overwrite or duplicate existing guidance.

## What the upstream Skills actually save

| Upstream workflow | Durable artifact | Important limitation |
| --- | --- | --- |
| `grill-with-docs` | `GLOSSARY.md` and an ADR when one qualifies | Many other settled details may remain only in the conversation |
| `wayfinder` | Map and resolved decision tickets in configured tracker | Map is an index to decisions, not a complete build specification |
| `to-spec` | `.scratch/<feature>/spec.md` in Local Markdown mode | Task snapshot, not a current architecture document; upstream setup is prerequisite |
| `setup-matt-pocock-skills` | Tracker/domain configuration and AGENTS/CLAUDE pointers | Does not select a particular active spec for every future task |

`to-spec` expects the upstream tracker **and triage-label vocabulary**. If setup skipped label configuration because its associated upstream Skill was absent, finish the supported upstream configuration before expecting local Spec publication to work.

The active Agent must resolve **which** spec/Map applies to the current task. A folder of historical specs is not self-selecting. Use the user-provided task path, established branch/issue association or explicit project references; ask when it remains ambiguous.

## The minimum stable pointers

Use root `AGENTS.md` to direct the Agent to real paths for:

1. Upstream domain guidance (`docs/agents/domain.md` when configured), so applicable ADRs and glossary are read.
2. Upstream issue tracker guidance (`docs/agents/issue-tracker.md` when configured), so relevant local Maps and task specs can be located.
3. The project's current architecture and high-level design (existing paths, or `docs/architecture.md` and `docs/design-overview.md` when present), and important requirement/constraint sources.

**Do not enumerate every Map, ticket or task spec in AGENTS.md.** A pre-existing project docs index may be retained; use one only if justified by actual document complexity, not as a mandatory duplicate of upstream tracker navigation.

## Persistence and tracking warning

`.scratch/` is a *path*, not a guarantee of Git tracking. Inspect `.gitignore` and `git ls-files` / `git status`. If the spec/decision Map is ignored or untracked, it may disappear or be inaccessible on another machine. Report the risk and let the project owner choose whether to track, export or archive it. Never auto-add, force-track, rewrite `.gitignore` or move files solely due to bootstrap.

For durable system engineering, keep current architecture/overview docs in the project's normal version-controlled documentation location when warranted. These docs **summarize the current system**, not the entire history of local tracker decisions.

## After engineering work

Whenever a change alters architecture/high-level design, the Agent should update the affected long-lived documentation using actual source evidence and approved decisions. `$project-context update-design` can perform this as a requested dedicated task. Use `Current / Implemented`, `Confirmed target` and `Pending resolution` where needed. If a fresh decision invalidates an ADR or approved scheme, clarify it with Grill/Wayfinder rather than rewriting history as if it never existed.

## Avoid unnecessary duplication

Use existing project paths and upstream artifacts. No compulsory `docs/README.md` project index, duplicate spec exports or empty architecture templates. An existing index remains welcome when useful. Keep any replacement pointers valid when an actual authoritative path is moved.
