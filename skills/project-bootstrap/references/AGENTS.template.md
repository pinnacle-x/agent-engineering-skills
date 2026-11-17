# Project Agent Instructions

Adapt to the existing project. Do not invent technical facts or change unrelated instructions.

## Orientation

- Read relevant source, current build/test instructions, README and existing project guidance before changes.
- Treat code and observed tests as evidence for implemented behavior while respecting standards, approved requirements and authoritative contracts.
- Let the active agent choose appropriate specification, TDD, implementation and documentation approaches.

## Documentation

- Use existing project documentation conventions.
- Without an established location, put project-wide documents in `docs/` and module-specific documents near their modules.
- Create and maintain the documentation warranted by user/project needs; no fixed document count or detail limit.

## Project Rules

- Project-specific rules are stored in `.agents/rules/`. The directory is created on demand and can be absent.
- When it exists, inspect its contents and read the rules relevant to the task; when absent, proceed without extra project-specific rules.
- Do not assume the runtime automatically loads rules from that directory.
- Adding, modifying, merging or deleting rules is handled **inside that directory**; this `AGENTS.md` does not enumerate rules or their applicability.

## Completion

- Run applicable checks and report actual results, including checks not performed.
- Keep relevant project documentation, source and requirements consistent; surface conflicts.
