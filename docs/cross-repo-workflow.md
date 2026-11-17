# Cross-Repository Public Contract Coordination

Use `cross-repo-governance` only for approved public contracts consumed by independent repositories. It handles **coordination**, not semantic design.

For example, a `StartTest` command impacts a protocol owner plus controller and PC consumers.

## 0. Resolve substantive design decisions first

If command semantics, compatibility strategy or other high-impact decisions are not agreed, use `grill-with-docs` first. Record the decision/ADR. Do not repeat the interview in Cross-Repo Governance.

## 1. Coordinate the approved change

```text
$cross-repo-governance interface-change
goal: Coordinate the approved StartTest command across repositories.
approved_contract: <owner contract or ADR reference>
```

The record `docs/changes/IC-0001-start-test-command.md` names the contract owner, consumers, compatibility/migration impacts, owner-first implementation order, and required verification.

## 2. Owner first

```text
approved owner contract → owner implementation
                        → consumer implementations
                        → repository-local tests
```

Consumers must not invent a separate public contract. Unresolved design conflicts return to the contract owner/Grill.

## 3. Verify exact repository revisions

```text
$cross-repo-governance system-verify
change: IC-0001
```

Record exact commits and actual integration/manual evidence.

## 4. Release verified composition

Only after verification `PASS`:

```text
$cross-repo-governance manifest-release
```

The immutable manifest pins the exact verified commit set, never floating branch names.
