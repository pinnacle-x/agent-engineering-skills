# Project Context — Local Markdown and Living Design Documents

`project-context` supports new and existing engineering projects, and provides dedicated **system architecture** and **high-level design** synchronization. It neither replaces the upstream local tracker nor routes engineering execution through an additional Skill.

## Bootstrap a new project

1. Establish confirmed goals, accepted constraints and still-open high-impact choices.
2. When useful, the user invokes `grill-with-docs` for focused decisions or `wayfinder` for long multi-session exploration. Repeat as later major design questions arise.
3. Use existing accepted glossary, ADRs, Wayfinder decisions and `to-spec` output **where actually persisted**. If confirmed content remains only in conversation, save the missing durable information in an appropriate existing project record.
4. Create/reconcile root `AGENTS.md` as navigation to the project's real domain/tracker configuration and long-lived documents. Do **not** require a new `docs/README.md` index.
5. Add current system architecture/high-level design documents only when meaningful content is confirmed or evidenced; otherwise avoid speculative templates/placeholder files.

## Bootstrap an existing project

1. Inspect actual source, hardware, build configuration, interfaces, tests, working tree and relevant files to establish **what exists now**.
2. Keep approved external standards and requirements distinct from observed code behavior. Populate existing requirements/constraints documents, or defaults `docs/requirements.md` and `docs/technical-constraints.md` if required.
3. Reconcile current architecture and high-level design with actual code and user-approved intent, documenting discrepancies rather than pretending they agree.
4. Reuse upstream domain guidance, local tracker configuration and any existing project document map. Root `AGENTS.md` names their real stable entry paths, rather than an extra mandatory index.

## Local-only Grill workflow

Use upstream `/setup-matt-pocock-skills` once in the target project and choose **Local Markdown** if GitHub/GitLab Issues are not part of development. That upstream setup configures `docs/agents/issue-tracker.md` and `docs/agents/domain.md` (or established alternatives). It may update `AGENTS.md` or `CLAUDE.md` according to its own selection logic; preserve existing project instructions and avoid duplicate blocks.

For local-mode Map/spec layout and hazards, see [Document Discovery](document-discovery.md).

## Update architecture and high-level design

```text
$project-context update-design
```

This is an **on-demand project-document synchronization mode**. It is also a responsibility the Agent should perform in ordinary work whenever changes materially affect the long-lived design, without needing to invoke the Skill after every small code edit.

- **System architecture:** subsystem/system boundaries, module responsibilities, deployment/hardware topology, external interfaces, major data/control flows and design constraints. Common default `docs/architecture.md`.
- **High-level design:** important module-level responsibilities, dependencies, major protocols, data models, significant state/interaction flows, fault handling and relevant resource/timing behavior. Common default `docs/design-overview.md`.
- **Evidence and lifecycle:** cite actual source/config paths, differentiate current implementation from confirmed not-yet-implemented targets, link relevant approved ADRs/task specs rather than copying them, and identify outstanding verification.
- **Update policy:** prefer existing project documents. Edit relevant sections, do not generate dummy details, and do not rewrite approved requirements or ADR history solely to match code. If the discrepancy requires a new decision, return to Grill/Wayfinder.
- **Pointers:** change `AGENTS.md` or an existing index only if the authoritative document path actually changed or a pointer is stale; ordinary design content updates should not churn navigation.

Optional examples are in `skills/project-context/references/architecture.template.md` and `design-overview.template.md`.

## Rules remain separate

`AGENTS.md` points to `.agents/rules/` by directory only. No empty directory is created by bootstrap. `$project-context add-rule` manages approved evidence-based rules and any optional index **inside** that directory; no per-rule edits to `AGENTS.md`.

The active Agent implements the project directly. `engineering-governance` remains optional for system verification and release.
