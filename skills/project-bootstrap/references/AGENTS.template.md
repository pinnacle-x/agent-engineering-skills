# Project Agent Instructions

Adapt this template to the existing repository. Do not insert absent paths, unverified claims or rules for hypothetical problems.

## Orientation

- Before editing, read relevant source, build/test configuration, README and existing project guidance.
- Treat code and executed tests as evidence of current implementation. Preserve external requirements, standards and approved interface definitions as requirements.
- Let the active agent choose planning, specification, TDD, implementation and documentation approaches appropriate to the task. Do not impose a fixed workflow.
- Keep original conventions when modifying the project.

## Documentation locations

- Follow the project's existing documentation structure.
- If there is no convention, use `docs/` for project-wide documentation and the relevant module's directory for module-specific documents.
- Create or update the documentation justified by the task, user requirements and the need to preserve architectural decisions or interfaces. No fixed limit on detail or document count.

## Task-specific rules (optional)

Files in `.agents/rules/` are **not** universally auto-loaded. Do not create them during normal bootstrap. Once an approved, problem-driven rule file exists, index it here with **an explicit reading condition and exact relative path**.

Example only (omit unless file exists):

```markdown
- When modifying STM32 DMA/cache behavior, read
  [.agents/rules/stm32-dma.md](.agents/rules/stm32-dma.md).
```

To add or revise a lasting rule, request `project-bootstrap add-rule`; confirm repeated evidence and avoid redundant guidance.

## Completion

- Run applicable checks and report their actual results; distinguish unperformed checks.
- Keep documents consistent with relevant code, tests, approved contracts and project requirements.
- Report changed files, important decisions and remaining blockers.
