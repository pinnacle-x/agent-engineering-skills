# Sources of Truth

## Existing projects: source-first facts, separately confirmed intent

The **current codebase and actual engineering state** are the factual standard for what the project presently contains and does. Inspect current source, project/build configuration, interface definitions, relevant hardware artifacts and observed test/runtime evidence. Cite concrete file paths and observations in project records.

Two kinds of statements must remain distinct:

- **Current implementation facts:** directly supported by inspected source/configuration or actual verification; an old README alone cannot override current source.
- **Confirmed requirements and technical constraints:** behavior, standards, interfaces, resource limits and architectural decisions supported by accepted requirements, authoritative standards, explicit user confirmation or reliable engineering evidence. Distinguish currently verified technical platform constraints from future design decisions.

Build or maintain `docs/requirements.md` and `docs/technical-constraints.md` when the project has no existing equivalent documentation structure; otherwise update the established authoritative files. Mark requirements inferred only from source as **pending confirmation**, not approved intent. Discrepancies with standards or user expectations require explicit resolution.

## New projects

There may be no source baseline. Use the user's confirmed goals and agreed technical decisions as the initial basis, and keep unsettled choices distinct from confirmed requirements.

## Shared contracts

A shared interface or protocol should have a clear owner, whether that owner is a file or module inside one Git repository or a separate Git repository. Dependent components should not silently redefine it. The active agent checks affected consumers when making changes; no separate Skill mode is required.

## Documents

Respect existing project locations. Without prior convention, use `docs/` for project-level docs and module directories for module-specific documents. Documentation detail follows project needs and external requirements.
