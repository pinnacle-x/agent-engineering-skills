# Project Agent Instructions

Adapt this example to the actual project. Preserve established conventions and do not claim unverified project facts.

## Project entry

- For an existing project, inspect current source, build/runtime state and relevant hardware/configuration files to establish the implemented baseline.
- For a new project, begin from confirmed goals and technical decisions; do not fabricate current code or approved designs.
- When a new important design choice is unresolved, use the appropriate Grill/Wayfinder design discussion, obtain confirmation and capture the accepted outcome. Such decisions can recur throughout the project.
- For a task with an effective confirmed design, the agent executes the work directly; do not route engineering execution through a separate workflow.
- If code and an approved design disagree, report the discrepancy rather than silently changing the approved requirements.

## Project documentation

- Document entry: [Project document index](docs/README.md) **when it exists**. Replace this path with the actual project index if the project already uses another one.
- Before work, read the index and then only the relevant **Active / Confirmed** documents for the task; consider open decisions but do not treat them as approved designs.
- When a design is accepted, replaced or invalidated, update the authoritative document and the document index, **not** a growing list in this AGENTS.md.
- Follow the project's existing documentation locations. Without a convention, use `docs/` for project-wide documents and module folders for module-specific documents.

## Project Rules

- Project rules live in `.agents/rules/`; create this directory only when needed.
- When the directory exists, inspect its contents and read applicable rules; otherwise proceed without additional rules.
- Do not assume the runtime automatically loads the directory.
- Manage individual rules and any optional rule index inside that directory, without per-rule updates to this AGENTS.md.

## Completion

- Report actual checks, changed files, confirmed design/document updates and unresolved decisions.
