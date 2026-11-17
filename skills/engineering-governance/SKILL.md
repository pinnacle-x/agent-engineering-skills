---
name: engineering-governance
description: Optional integrated verification and reproducible releases for single-Git or multi-Git products, using current code evidence and the effective approved design discoverable from the project's document index.
---

# Engineering Governance

Use for product-level integration evidence or reproducible releases. It does not manage ordinary engineering execution or act as a separate change-impact process. The active agent implements the current approved design directly.

## Invocation

```text
$engineering-governance
$engineering-governance verify
$engineering-governance release
```

If called without a mode, choose verify or release based on the user's actual goal. If the task is ordinary project work, this Skill may be unnecessary. Alternative Harnesses may require invocation by name.

## Before verification or release

1. Inspect the actual Git root(s), changed modules, source/build/test commands, hardware constraints, and any pending workspace changes.
2. Read the project's **document index** linked from `AGENTS.md` (normally `docs/README.md`, or the existing equivalent). Identify the **active/confirmed** requirements, technical constraints, current approved scheme, authoritative interface and acceptance criteria relevant to this release or system test.
3. Distinguish **what is implemented** (source and observed evidence) from **what was approved** (current effective requirements/design). Do not treat stale/superseded proposals as release requirements, or silently rewrite approved requirements to match code.
4. If an important acceptance requirement or scheme remains unconfirmed, report that gap and obtain the required decision. Grill/Wayfinder may help resolve major new design choices before work resumes; they are not a mandatory verification tool.
5. One repository can contain several components without multiple Git histories. Follow existing document and verification conventions rather than imposing fixed filenames or extra reports.

## Mode: verify

1. Discover actual commands and needed system/interface/hardware checks from the current effective project requirements, scheme and build/test artifacts.
2. **Single Git:** identify one exact commit SHA and all relevant modules, noting dirty/uncommitted state; run or assess integrated checks for that code revision.
3. **Multi Git:** identify the exact commit SHA of each participating repository and verify contract compatibility for that version combination.
4. Record commands, observed evidence, and per-check results: `PASS`, `FAIL`, `BLOCKED`, `MANUAL_PENDING` or `NOT_APPLICABLE`. Never mark an unperformed manual/hardware test as passed.
5. Use current project reporting conventions; a dedicated report such as `templates/SYSTEM_VERIFICATION.md` is optional unless required by project needs.
6. Overall PASS requires all **required** checks to pass or genuinely not apply. Highlight acceptance/design discrepancies and unresolved requirements.

## Mode: release

1. Confirm a requested version, release scope and required verification evidence for the **effective approved scheme**.
2. Ensure exact release revisions match successful verification. Dirty or untracked source that prevents reproducibility is a blocker.
3. **Single Git:** use a verified SHA and an appropriate tag if used by the project; no default multi-repository manifest.
4. **Multi Git:** pin the actually tested SHA per included repo in the established/preferred composition format. Use a manifest when necessary for a reproducible multi-repository release.
5. Do not silently rewrite published release versions or substitute floating branch names for immutable revisions.
6. Deliver documentation and artifacts warranted by project/contract requirements, without an artificial limit on documentation depth.

## Separation

`project-bootstrap` establishes a project entry, evidence-backed baseline and a document index. **The active agent maintains approved design documents and that index throughout the project**, including after repeated Grill/Wayfinder rounds; governance only consumes the current effective scheme when verifying or releasing. Neither Skill depends on the other being installed.
