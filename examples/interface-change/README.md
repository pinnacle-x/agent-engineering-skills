# Cross-Repository Interface Coordination Example

When the `StartTest` command's semantics are still undecided, resolve them with `grill-with-docs` first and record the approved design/ADR. PraxFlow does **not** repeat that design interview.

Then invoke:

```text
$praxflow interface-change
goal: Coordinate the approved StartTest command across repositories.
approved_contract: <owner contract or ADR reference>
```

Expected output:

```text
system/docs/changes/IC-0001-start-test-command.md
```

The record identifies the owner repository, consumers, compatibility and migration impacts, required owner-first order and verification obligations. The owner contract must be approved before consumer-side semantics change.
