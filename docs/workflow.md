# Portable Agent Workflow

Use the active agent and general engineering Skills for routine work. Use Grill for important unresolved design choices. Only use the two independent Skills here for their specific missing capabilities.

## 1. Bootstrap a repository (once, or to reconcile existing instructions)

```text
$project-bootstrap
```

Read the current files first; create or reconcile `AGENTS.md` and explicit `.agents/rules/` links. Preserve current code, docs, configuration and Git state. Do not repeat engineering issue-tracker/domain-doc setup.

## 2. Normal engineering and Grill

The active agent and engineering Skills handle requirements, reading code/PDFs, architecture, specifications, implementation, local tests and review.

When an important choice remains unresolved, use `grill-with-docs` for design interviews, comparison of options and ADRs. This includes decisions about what a public API or protocol means. Skip Grill when a design is already approved.

## 3. Shared public contract across repositories (only when needed)

After design is approved and **before** consumer semantic changes:

```text
$cross-repo-governance interface-change
```

Record contract owner, consumers, the approved contract/ADR reference, compatibility, owner-first rollout, migration and required verification. The governance record `docs/changes/IC-XXXX-<slug>.md` is not a duplicate API specification.

## 4. Exact-revision integrated verification

After affected repositories have local tests:

```text
$cross-repo-governance system-verify
```

Record the actual commit SHA of each included repository and evidence for automated, integration, and hardware/manual checks. Unperformed manual/hardware checks remain `MANUAL_PENDING`.

## 5. Immutable multi-repository release composition

Only when integrated verification is `PASS`:

```text
$cross-repo-governance manifest-release
```

Pin exactly the previously verified revision set, not moving branch names.

## Summary

```text
project-bootstrap → AGENTS.md + explicitly indexed rules
         ↓
active agent + Grill when important design is unresolved
         ↓
cross-repo-governance interface-change (if shared contract)
         ↓
owner implementation → consumer implementation → local tests
         ↓
cross-repo-governance system-verify → PASS → manifest-release
```
