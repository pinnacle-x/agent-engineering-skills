# Optional task-specific rule format

This is a **format reference**, not a list of rules to create during bootstrap.

Only persist rules after repeated, evidenced problems with confirmed causes, after checking existing project guidance and obtaining user approval. A precise user request authorizing the exact rule also suffices.

## Recommended file

`.agents/rules/<topic>.md`

```markdown
# Rule: <specific failure being prevented>

## Applies when
<concrete task, affected module or file pattern>

## Verified problem
<brief evidence from repeated failures and confirmed cause>

## Required check or behavior
<one actionable, scoped instruction the agent can verify>

## Exceptions / limitations
<conditions where the rule does not apply>
```

After creating the file, add a link from the root `AGENTS.md` with a matching **when-to-read** condition. Do not insert a generic wildcard or claim the directory loads automatically. Prefer revising or removing obsolete rules over indefinitely accumulating them.

## Example (do not copy blindly)

For repeated STM32 DMA/cache coherency bugs, the rule can require checking the actual buffer memory region, cacheability, access direction, cache-line alignment and needed cache maintenance. It must **not** blanket-disable caching for every DMA operation.
