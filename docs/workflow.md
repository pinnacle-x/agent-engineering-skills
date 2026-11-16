# Portable Agent Workflow

Use `project-bootstrap` once for repository instruction setup. Use the regular agent and engineering Skills for most project work. Use `praxflow` only when cross-repository governance is required.

## 1. Initialize or reconcile the repository

```text
$project-bootstrap
```

This creates or reconciles root `AGENTS.md` and explicitly indexed `.agents/rules/` without overwriting existing project conventions. Repeat only when initial rules need repair or adaptation. See [bootstrap guide](project-bootstrap.md).

## 2. Normal engineering work

Use the active agent and available companion Skills directly to inspect code/PDFs, reason about requirements, perform domain modeling, plan, implement, test and review.

Call `grill-with-docs` when important unresolved **design questions** require an interactive decision process and durable ADRs. Grill determines what the contract should mean; it does not by itself assign owners and consumers or enforce a multi-repository rollout.

## 3. Public interface changes across repositories

Before modifying a public contract consumed by independent repositories:

```text
$praxflow interface-change
```

This mode records ownership, consumers, compatibility, migration, owner-first order and required verification in `docs/changes/IC-XXXX-<slug>.md` in the designated system/product repository.

If the interface design is unresolved, run Grill first, then use the agreed design in the interface-change record. Do not use this mode for repository-local refactors.

## 4. Exact-revision integrated verification

After owner and consumer repositories are implemented and locally tested:

```text
$praxflow system-verify
```

Record each repository's commit SHA and the actual integration and hardware/manual evidence in `docs/verification/VER-<id>.md`. Unperformed manual/hardware checks remain `MANUAL_PENDING`.

## 5. Reproducible release

Only when verification is `PASS`:

```text
$praxflow manifest-release
```

Pin the exact verified revisions in an immutable release manifest (for example `releases/vX.Y.Z.xml` and `releases/vX.Y.Z.md`).

## Summary

```text
Project bootstrap (once) → AGENTS.md + .agents/rules
             ↓
Read project rules → normal engineering agent work
             ↓
Unresolved design? → grill-with-docs → approved design
             ↓
Cross-repo contract change? → praxflow interface-change
             ↓
Implement owner first → implement consumers → local tests
             ↓
Cross-repo system? → praxflow system-verify
             ↓
PASS only → praxflow manifest-release
```

Policies: one semantic owner per public contract; owner changes first; actual test evidence is required; release manifests record the exact verified revision set.
