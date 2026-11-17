---
name: engineering-governance
description: Optional integrated verification and reproducible release coordination for single-Git or multi-Git products. The agent directly assesses change effects and performs engineering work; this Skill has verify and release modes only.
---

# Engineering Governance

Use this Skill only when a product-level integration verification or reproducible release merits coordinated evidence. One Git repository can contain several tightly coupled modules; multiple Git repositories need independently pinned revisions.

The **active agent** handles ordinary analysis, including the effects of changes on dependent modules, and executes engineering tasks directly. Do not introduce a separate change-impact invocation or a required planning ceremony.

## Invocation

```text
$engineering-governance
$engineering-governance verify
$engineering-governance release
```

Without a mode, choose verify or release from the user's request; for routine engineering work, say the Skill is unnecessary. If shorthand is not supported, request the Skill by name in natural language.

## Scope and sources

1. Inspect actual Git roots, module boundaries, current source, authoritative requirements, interfaces, build instructions and current evidence. Folders named PC/Firmware/Protocol do **not** necessarily mean separate Git repositories.
2. Source and observed results establish present engineering facts. Approved requirements, standards and external contracts remain authoritative for intended behavior. Escalate conflicts, do not silently rewrite either side.
3. The agent identifies affected modules and contracts as part of direct engineering work, regardless of whether this Skill is invoked.
4. Follow existing documentation locations and project processes. Do not force numbered change records, issue trackers, XML or a fixed number of documents.

## Mode: verify

Use when the user wants **integrated evidence** for an affected system or release candidate; this does not replace ordinary local checks.

1. Discover test/build instructions and required system, interface, deployment and hardware acceptance conditions from real project artifacts.
2. **Single Git:** identify the exact commit SHA (plus any dirty/uncommitted state) and all affected modules. Run or review relevant integration and module checks for that revision.
3. **Multi Git:** identify each included repository's exact commit SHA and check interface and dependency compatibility for that concrete combination.
4. Record **actual** commands, evidence and outcomes. Use `PASS`, `FAIL`, `BLOCKED`, `MANUAL_PENDING` or `NOT_APPLICABLE` for each required check. Never turn an unperformed manual/hardware check into `PASS`.
5. Present results in the response or existing project reports; create a verification document only when required for the project's verification, traceability or delivery. `templates/SYSTEM_VERIFICATION.md` is an optional reference.
6. Overall verification passes only when all required checks are `PASS` or genuinely `NOT_APPLICABLE`. Explicitly report uncertainty and blockers.

## Mode: release

Only use when an actual release is requested. Confirm version, revision scope and the verification evidence required by the project's acceptance criteria.

1. Confirm that the release revision(s) exactly match the verified revision(s). Reject unrecorded or dirty workspace state where it would prevent reproducibility.
2. **Single Git:** pin one immutable commit SHA, with a project tag if appropriate. Do not generate a multi-repository manifest for a single Git project.
3. **Multi Git:** pin the exact verified SHA per included repository in the existing/preferred product-composition format; introduce a manifest only when needed for reproducible combination releases.
4. Preserve existing releases; do not overwrite a published version silently or replace immutable revisions with floating branch names.
5. Produce the documentation and artifacts warranted by actual project requirements, with no artificial restrictions on detail or count. Report required checks not yet performed; do not label the release verified if required checks remain pending.

## Separation

`project-bootstrap` covers new and existing project entry points, evidence-backed requirements and constraints, and approved project rules. Neither Skill requires the other. Grill and Wayfinder may clarify important unresolved decisions when useful; **the agent executes approved solutions directly**.
