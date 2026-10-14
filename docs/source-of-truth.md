# Source of Truth

PraxFlow uses explicit ownership only to prevent **cross-repository semantic drift**.

## Principle

A public fact or contract has one semantic owner repository. Consumers reference that owner rather than independently redefining the same meaning.

PraxFlow does not prescribe how ordinary project facts, PDFs, specifications, or implementation documents must be stored. Follow each repository's existing `AGENTS.md`, documentation, tracker, and source layout.

## Typical ownership

| Information | Typical owner |
|---|---|
| Product/system-level contract | system/product repository |
| Shared communication protocol | protocol/contract repository |
| PC internals | PC repository |
| Controller internals | controller repository |
| Module internals | corresponding module repository |
| Repository composition | manifest/product-composition repository |
| Immutable released composition | manifest/product-composition repository |

These are defaults, not mandatory directory names. Existing project ownership rules win.

## Consumer rule

A consumer may cache or generate a local representation for build convenience, but it must not silently become a second semantic owner.

When a public contract changes:

1. identify the owner;
2. record affected consumers;
3. update/approve the owner contract first;
4. update consumers afterward;
5. verify the exact combined repository revisions.

Use `$praxflow interface-change` for this process.

## Conflict handling

If owner/consumer definitions disagree, record the conflict and resolve it through the owner or an explicit human design decision. Do not silently choose whichever version is easier to implement.
