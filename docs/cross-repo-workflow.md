# Cross-Repository Public Contract Coordination

Use PraxFlow only when an **approved** public contract must be changed across independent repositories. Grill determines the design where substantive choices remain; PraxFlow coordinates its safe implementation by the contract owner and consumers.

Example: adding a new `StartTest` protocol command affects a protocol owner plus firmware and PC consumers.

## 0. Resolve semantics with Grill when needed

If the interface semantics, tradeoffs, migration strategy, or expected behavior are not agreed, use `grill-with-docs` first and record the decision/ADR. **Do not** recreate the design discussion in PraxFlow. If no such open decision exists, skip Grill.

## 1. Coordinate the agreed change

From a workspace that can inspect the relevant repositories:

```text
$praxflow interface-change
goal: Coordinate the approved StartTest command across the protocol owner,
      controller, and PC repositories.
approved_contract: [path or ADR reference]
```

Output: `docs/changes/IC-0001-start-test-command.md` in the designated product/system repository.

The record identifies contract owner, consumers, approved contract reference, compatibility effects, owner-first rollout order, migration and validation requirements. It is not a rival contract or second ADR.

## 2. Update owner first

```text
approved owner contract
  → owner implementation
  → consumer implementations
  → local tests in each repository
```

Do not change consumer semantics before the approved owner contract is updated. Use the active agent and normal engineering Skills for implementation and local tests.

## 3. Verify the exact combined revisions

```text
$praxflow system-verify
change: IC-0001
```

Record exact commit SHAs for each repository and actual automated, integration and manual/hardware evidence.

## 4. Release only a verified combination

Only after verification is `PASS`:

```text
$praxflow manifest-release
```

The immutable manifest pins the exact verified revisions. If there is no cross-repository change or release requirement, skip unnecessary PraxFlow modes.
