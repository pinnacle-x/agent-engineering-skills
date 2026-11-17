# Optional rule file examples

Create only the rule files justified by the project, one file per heading below. These are examples, not inferred facts. If existing repository instructions already cover a topic, link to those instead of copying them.

## `.agents/rules/general.md`

- Keep changes within the requested task.
- Inspect existing files and related documentation before editing.
- Preserve existing conventions, verified decisions, and intentionally configured behavior.
- Do not invent specifications, project status, test results or tool availability.
- Surface important ambiguity or conflicts rather than silently redefining the project.

## `.agents/rules/development.md` (optional)

- Read the affected module and its callers before editing.
- Prefer minimal changes that follow the project's established architecture.
- Do not change public interfaces without identifying affected consumers and approvals.
- Follow project-specific formatting/build guidance if it exists; do not invent commands.

## `.agents/rules/testing.md` (optional)

- Use existing test and build commands when available.
- Report exactly which checks were run and their actual outcomes.
- Keep hardware/manual checks as pending until evidence exists.
- Do not mark unperformed tests as passing.

## `.agents/rules/documentation.md` (optional)

- Update documents that are made inaccurate by the change.
- Preserve stable decisions and maintain references to the source of truth.
- Avoid creating placeholder docs or duplicate requirement definitions.
- Do not change version numbers unless the project's release policy or task requires it.
