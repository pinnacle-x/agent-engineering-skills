---
name: engineering-governance
description: Optional risk-based engineering change impact, integrated verification, and reproducible releases for single-Git or multi-Git products. Detect repository scope; avoid imposing multi-repo manifests or governance files on routine single-repo development.
---

# Engineering Governance

Use this Skill only when change impact across modules, public interfaces, integrated verification, or a reproducible release merits additional coordination. **The number of Git repositories is not itself a reason to activate governance.**

The active agent owns requirements analysis, specifications, design, coding, TDD where useful, tests, review and task-appropriate documentation. Grill and Wayfinder are optional helpers for unresolved design and unusually ambiguous long-running projects; they are not prerequisites.

## Invocation

```text
$engineering-governance
$engineering-governance change-impact
$engineering-governance verify
$engineering-governance release
```

Without a mode, inspect the user's goal and choose the relevant mode(s), or report that normal agent work suffices. If the Harness does not recognize shorthand, request the installed Skill by name and state the goal.

## First: identify scope and risk

1. Inspect existing source/build/test instructions and Git roots; do not assume that module folders are independent Git repositories.
2. Classify: **single Git, simple change**; **single Git, coupled modules**; or **multiple Git repositories**. A project can have multiple components without multiple `.git` roots.
3. Check whether the proposed change touches public contracts, compatibility, deployed devices, safety-relevant behavior, integration or release composition.
4. If the change is routine and contained within a single module, **do not require governance records**; let the agent implement and test normally.
5. Follow existing repositories' conventions and documentation locations. Never require fixed governance directory names, ticket IDs, Spec formats or a fixed number of documents.

## Mode: change-impact

Use for a materially shared interface or coupled behavior change, in **one or multiple Git repositories**.

1. Identify the actual contract or behavior owner (file/module/repository), its consumers, and relevant external requirements. Existing code is evidence of implementation, not authority to override approved standards or contracts.
2. Read the existing contract and affected consumers. Assess compatible, conditionally compatible, or breaking effects; flag uncertain cases instead of inventing semantics.
3. Coordinate authoritative change before dependent consumer changes **when a distinct shared contract is maintained**. In one Git repository, this may mean updating the protocol definition and all module consumers together in a single commit; it does **not** mandate separate owner and consumer repositories.
4. Describe required migration, compatibility and appropriate tests based on impact. Agent handles implementation and tests.
5. Use an existing issue/PR/plan or a brief response to record impact. **Only create a persistent change record when required** by the project's process, its risk or the user. `templates/CHANGE_IMPACT.md` is optional.
6. If important design decisions are unresolved, let the active agent clarify or use Grill/Wayfinder if helpful. Do not force design interviews or ADRs.

## Mode: verify

Use when the user wants **integrated evidence** for an affected system or release candidate; do not duplicate routine repository-local tests.

1. Discover the existing build/test commands and required integration/hardware checkpoints from actual project files and requirements.
2. For a **single Git repository**, identify one commit SHA plus affected modules and any uncommitted state; run or review relevant module and integration checks.
3. For **multiple Git repositories**, identify the exact commit SHA per participating repository and verify owner/consumer compatibility for that version combination.
4. Record commands and outcomes actually observed. Use `PASS`, `FAIL`, `BLOCKED`, `MANUAL_PENDING` or `NOT_APPLICABLE` per required check; never claim unperformed/manual/hardware checks passed.
5. Present results in the response, existing test reports or normal project records. Create a dedicated verification document **only when appropriate**; `templates/SYSTEM_VERIFICATION.md` is optional.
6. A release gate passes only if all **required** checks are passed or genuinely not applicable. Note remaining risks and unknowns explicitly.

## Mode: release

Use only when a release is actually requested. Confirm version, release scope and appropriate verification before creating release artifacts.

- **Single Git:** use an immutable commit SHA and, when the project uses them, an appropriate Git tag. Existing build artifacts, changelog and documentation follow the project's conventions. **Do not create a multi-repository manifest or XML by default.**
- **Multiple Git:** pin the actually tested SHA of every included repository in the project's preferred product-composition format (e.g. an existing manifest). Only introduce a manifest format if it is needed for a reproducible multi-repository release.
- In all cases: confirm the released revision(s) match required successful verification; identify dirty/uncommitted state; do not invent tests, silently overwrite an existing release/version, or use moving branch names as immutable revision identifiers.
- Produce or update release notes and other documents according to the project's real documentation and delivery requirements; there is **no minimum-documentation restriction**.

## Output philosophy

Return a concise, evidence-based result by default, but provide the documentation and traceability that the project's scope, requirements or user request warrant. Rules and templates are aids, **not mandatory bureaucracy**.

## Separation from project-bootstrap

`project-bootstrap` manages portable `AGENTS.md` and confirmed, opt-in project-specific rules. This Skill does not create them, and neither Skill requires the other to be installed.
