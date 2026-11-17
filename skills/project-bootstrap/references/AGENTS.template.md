# Project Agent Instructions

Adapt to the actual project. Do not insert unverified project facts.

## Project entry

- For an **existing project**, inspect current source and build/runtime state before deciding what is already true; consult the project's confirmed requirements and technical-constraints documents.
- For a **new project**, follow the user's confirmed goal and technology decisions; identify unresolved choices without inventing them.
- The agent directly handles project work once the goal and necessary decisions are clear.
- Respect existing project conventions and approved external standards.

## Documentation

- Prefer existing documentation locations. When none are defined, use `docs/` for project-wide documents and relevant module directories for module-specific documents.
- For an existing project, keep the confirmed requirements and technical constraints documented, with supporting source/evidence references. Do not promote inferred intentions to confirmed requirements without approval.
- Document the project to the level needed by actual goals and deliverables.

## Project Rules

- Project rules live in `.agents/rules/`; this directory is created only when needed.
- If it exists, inspect its contents and read the rules relevant to the task; if absent, proceed without additional rules.
- Do not assume the runtime automatically loads this directory.
- Rule additions, revisions, merges and deletions are managed inside that directory, not in this file.

## Completion

- Report actual checks, changed files, documentation updates, and any outstanding decisions.
