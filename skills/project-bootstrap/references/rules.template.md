# Optional task-specific project rule format

This is a format example for **approved, problem-driven rules**, not a bundle of defaults. Bootstrap does not create `.agents/rules/` until an actual rule is needed.

## Rule file: `.agents/rules/<topic>.md`

```markdown
# Rule: <specific recurring failure being prevented>

## Applies when
<affected task, module, conditions or file types>

## Confirmed problem
<observed repeated failures and verified root cause>

## Required check or behavior
<one actionable, scoped instruction the agent can verify>

## Exceptions and limitations
<when this rule must not be applied>
```

Do not reference each rule from root `AGENTS.md`. That file only describes the `.agents/rules/` directory; the agent lists and reads relevant files when it exists.

## Optional index: `.agents/rules/INDEX.md`

For multiple rules that benefit from a compact map, use an index **inside** the rules directory:

```markdown
# Rule Index

| Rule file | Applies when |
| --- | --- |
| stm32-dma.md | Changing STM32 DMA / cache code |
| modbus-registers.md | Changing Modbus register definitions |
```

These entries are **illustrations, not files to pre-create**. When rules are added, revised, merged, renamed or deleted, reconcile the index with the actual files. If the directory contains only a few obvious rules, omit the index.

Prefer revising or removing obsolete rules instead of growing an unbounded rule collection. Never apply a rule outside its stated scope or claim automatic Harness loading.
