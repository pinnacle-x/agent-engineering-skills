# Project Agent Instructions

This is an **example** to adapt when no root `AGENTS.md` exists. Do not paste project-specific claims or add references to absent rule files.

## Entry

- Read this `AGENTS.md` first, then follow the applicable rules listed below.
- Inspect `README.md` if it exists and relevant source files before proposing changes.
- Derive current behavior from actual files and verified documentation; do not invent project state.
- Report conflicting guidance instead of silently choosing a convenient version.

## Rule discovery

Files under `.agents/rules/` are **not assumed to be automatically loaded** by all harnesses.

- Always: `.agents/rules/general.md`
- Changes to implementation: `.agents/rules/development.md` (only when present)
- Testing/verification: `.agents/rules/testing.md` (only when present)
- Updates to documentation or public behavior: `.agents/rules/documentation.md` (only when present)

**When creating AGENTS.md:** delete all rule-index lines for files that have not been created. Prefer explicit condition + file path over wildcard loading.

## Skills

Discover available installed Agent Skills before using them. Use a Skill only if it exists in the active environment. Design review, ordinary implementation, and cross-repository release coordination are distinct tasks; do not assume they use the same Skill.

## Completion

- Run applicable checks; distinguish passing tests from tests that were not performed.
- Update affected project documentation, but do not bump versions or change release records without a project requirement.
- Summarize changed files, verification evidence and remaining blockers.
