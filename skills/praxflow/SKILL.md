---
name: praxflow
description: Unified PraxFlow product-engineering workflow for multi-repository systems. Use for repository bootstrap, PDF evidence ingestion, system discovery, specification materialization/validation, protocol validation, cross-repository interface changes, system verification, and manifest releases.
---

# PraxFlow

PraxFlow is one Agent Skill with multiple workflow modes. It coordinates repeatable product engineering across independent system, protocol, PC, controller, module, hardware, and manifest repositories.

Use one mode at a time unless the user explicitly asks to continue across stages. Preserve each mode's stop conditions and human gates. Do not silently skip from evidence gathering into design, from design into implementation, or from verification into release.

## Invocation

Preferred explicit form:

```text
$praxflow <mode> [arguments]
```

Supported modes:

- `repo-bootstrap`
- `pdf-ingest`
- `system-discovery`
- `spec-materialize`
- `spec-validate`
- `protocol-validate`
- `interface-change`
- `system-verify`
- `manifest-release`

If the user invokes `$praxflow` without a mode, infer the mode only when the requested action maps unambiguously to one mode. Otherwise ask once for the intended stage. Natural-language requests such as "bootstrap this controller repo with PraxFlow" or "validate the protocol spec with PraxFlow" are equivalent.

## Global rules

Apply these rules in every mode:

- One fact has one owner repository.
- Consumers reference owner specifications instead of maintaining divergent copies.
- Unknown or conflicting facts are never guessed.
- Evidence extraction, product decisions, specifications, implementation, verification, and release are distinct stages.
- Production implementation requires an approved implementation source.
- Public-interface semantics are changed owner-first.
- `HIGH` and `CRITICAL` unresolved decisions are not silently resolved.
- Manual/hardware tests are never marked `PASS` without explicit evidence from a human or test system.
- Release manifests pin immutable tested revisions.
- Preserve existing `AGENTS.md` rules and metadata from other installed engineering workflows unless they directly conflict with an explicit PraxFlow requirement.

## Recommended lifecycle

```text
repo-bootstrap
  -> pdf-ingest
  -> system-discovery
  -> resolve HIGH/CRITICAL decisions when needed
  -> create canonical specification source
  -> spec-materialize
  -> spec-validate
  -> protocol-validate (protocol repositories only)
  -> human approval
  -> implementation / TDD / review using the environment's engineering tools
  -> interface-change before shared contract changes
  -> system-verify
  -> manifest-release
```

PraxFlow does not replace general-purpose design review, specification drafting, TDD, implementation, diagnosis, or code review skills. It defines product-level ownership, evidence, gates, and cross-repository workflow.

---

# Mode: `repo-bootstrap`

Bootstrap a repository for PraxFlow. Use when starting or standardizing a system, protocol, PC, controller, module, hardware, or manifest repository.

## Inputs

Require or infer exactly one repository role:

- `system`
- `protocol`
- `pc`
- `controller`
- `module`
- `hardware`
- `manifest`

If the role cannot be inferred safely, ask once.

## Preconditions

- The current directory is a Git repository.
- Preserve an existing `AGENTS.md`; edit it instead of replacing unrelated rules.

## Actions

1. Detect the repository role and current structure.
2. Ensure `AGENTS.md` contains concise PraxFlow sections for:
   - repository role and ownership
   - required reading order
   - source-of-truth references
   - cross-repository boundaries
   - PDF handling rules when applicable
   - implementation gates
   - build/test expectations when known
   - prohibited actions
3. Create only directories appropriate to the role.
4. Do not create speculative `CONTEXT.md`, `CONTEXT-MAP.md`, ADRs, or formal specs.

## Role scaffolds

### system

Create: `input/`, `docs/raw/`, `docs/system/`, `docs/adr/`, `docs/spec/`, `docs/changes/`, `docs/verification/`, `tools/`.

### protocol

Create: `input/`, `docs/raw/`, `docs/adr/`, `docs/spec/`, `tools/`, `tests/`.

### pc/controller/module

Create: `docs/adr/`, `docs/spec/`, `src/`, `tests/`, `tools/`. Add `input/` only when this repo owns source documents.

### hardware

Create: `input/`, `docs/raw/`, `docs/spec/`, `docs/verification/`.

### manifest

Create: `releases/`, `docs/`; create `default.xml` only if repository membership is already known.

## Required AGENTS.md policy

PraxFlow rules must state:

- One fact has one owner repository.
- Consumers reference owner specs instead of maintaining divergent copies.
- Unknown or conflicting facts are never guessed.
- Production implementation requires an approved implementation source.
- Cross-repository interface changes use `$praxflow interface-change`.
- Release combinations are recorded by the manifest repository.

## Output and stop condition

Report repository role, files/directories created or changed, unresolved bootstrap assumptions, and the next recommended step.

Stop after bootstrap. Do not begin product design or implementation.

---

# Mode: `pdf-ingest`

Transform repository-owned PDFs into faithful, traceable raw artifacts. This mode extracts evidence; it does not design the product or generate production code.

## Inputs

Accept one or more PDF paths, normally under `input/`. If no path is provided, discover PDFs in `input/`.

## Preferred execution

For ordinary text-heavy PDFs, resolve the bundled helper relative to this skill directory and run:

```bash
python scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --json
```

For schematics, circuit diagrams, engineering drawings, layout-dependent tables, or other PDFs whose meaning depends on spatial relationships:

```bash
python scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --schematic --json
```

Equivalent explicit form:

```bash
python scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --render-images all --dpi 180 --json
```

When installed outside the target repository, resolve `scripts/extract_pdf.py` from the installed `praxflow` skill directory rather than assuming the target repository contains a `skills/` folder.

The helper tries PyMuPDF first and then pypdf for text extraction. Page rendering requires PyMuPDF. It deliberately does not OCR pages automatically.

## Extraction strategy

1. Classify each PDF as text, table-heavy, scanned, schematic/drawing, or mixed.
2. Prefer the existing PDF text layer for textual evidence.
3. Use the bundled helper or equivalent local extraction tools.
4. For schematics/drawings, render all relevant pages and treat page images as primary visual evidence for spatial relationships.
5. For ordinary PDFs, the default candidate rendering path should cover pages with little/no extractable text.
6. Inspect visually important tables, diagrams, symbols, wires, labels, and spatial relationships when text extraction is insufficient.
7. Use OCR only for pages that cannot be reliably extracted otherwise and only when textual transcription is needed.
8. Preserve page boundaries and source file identity.
9. Preserve headings, numbering, tables, units, hexadecimal values, signs, decimal points, and data types.
10. Never silently normalize an ambiguous token.

## Schematic and drawing rule

- Do not infer electrical connectivity from extracted labels alone.
- Prefer netlist/native structured design data when exact connectivity is required.
- If the active model cannot consume images, retain rendered artifacts and add `TODO_VERIFY` for visual relationships that cannot be established from text alone.

## Uncertainty rule

For unclear or conflicting content, write `TODO_VERIFY` with source file, page number, observed interpretation, and candidate interpretations when useful. Do not choose a candidate without evidence.

## Outputs

For each input PDF create:

```text
docs/raw/<stem>_raw.md
docs/raw/<stem>_extraction_report.md
docs/raw/<stem>_images/page_NNN.png   # when rendering is enabled
```

The raw file must preserve source-page markers. The extraction report must include page count, extraction method, render mode/DPI, rendered image list, OCR candidates, low-confidence/failed pages, `TODO_VERIFY` items, and one overall result: `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`.

## Prohibited actions and stop condition

Do not create product requirements from implied meaning, convert guesses into facts, create ADRs, create implementation specs, modify source PDFs, generate production code, or claim exact wire/net connectivity from nearby text.

Stop after extraction, required visual follow-up, and report generation.

---

# Mode: `system-discovery`

Analyze existing product evidence without inventing architecture. Separate established facts from unresolved decisions and classify unresolved decisions by impact.

## Read first

- `AGENTS.md`
- `docs/raw/*`
- existing `CONTEXT.md` if present
- existing `CONTEXT-MAP.md` if present
- `docs/adr/*`
- `docs/spec/*`
- workspace repository list when visible
- `manifest/default.xml` when available

## Actions

1. Identify product-level contexts/subsystems explicitly supported by evidence.
2. Identify owner repositories for facts/interfaces when known.
3. Extract established responsibilities and interface directions.
4. Separate facts from assumptions.
5. Create/update a context map.
6. Create/update the open-decision register.
7. Classify every unresolved decision as `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`.

## Decision severity

- `LOW`: local, cheap to reverse, little downstream impact.
- `MEDIUM`: meaningful design choice mainly contained within one repository.
- `HIGH`: cross-repository, public-interface, real-time, compatibility, or expensive-to-reverse choice.
- `CRITICAL`: safety, hazardous behavior, irreversible product behavior, or system-integrity decision requiring explicit human approval.

For each `HIGH` or `CRITICAL` item, recommend an interactive deep-design review but do not start one automatically. A compatible companion skill such as `grill-with-docs` may implement the review, but PraxFlow remains independent of any one review tool.

## Outputs

Create/update:

- `CONTEXT-MAP.md`
- `docs/system/SYSTEM_FACTS.md`
- `docs/system/OPEN_DECISIONS.md`

`CONTEXT-MAP.md` records contexts, repository mapping, responsibilities, owned interfaces, and dependencies without duplicating subsystem contexts.

`SYSTEM_FACTS.md` contains only evidence-backed facts and source references.

`OPEN_DECISIONS.md` gives every item a stable ID (`OD-001`, ...), status, severity, affected contexts/repos, why unresolved, candidate options when known, impact, and recommended next action.

## Stop condition

Stop after discovery. Do not create production code and do not silently resolve `HIGH` or `CRITICAL` decisions. If no major decisions remain, state that the project can proceed to specification.

---

# Mode: `spec-materialize`

Convert a concrete specification source into repository-local structured specification files without changing its meaning.

## Read first

- `AGENTS.md`
- repository role
- `CONTEXT.md` if present
- relevant `CONTEXT-MAP.md`
- `docs/adr/*`
- `docs/raw/*` when the spec depends on extracted evidence

## Source requirement

Require a concrete source identifier or file. Record it; do not fabricate one.

## Role-specific outputs

### system

Create/update under `docs/spec/`:

- `SYSTEM_SPEC.md`
- `SUBSYSTEM_ALLOCATION.md`
- `INTERFACE_CATALOG.md`
- `SYSTEM_TEST_PLAN.md`
- `SPEC_SOURCE.json`

### protocol

Create/update:

- `PROTOCOL.md`
- `REGISTER_MAP.json`
- `COMMANDS.json`
- `ERROR_CODES.json`
- `TEST_VECTORS.json`
- `SPEC_SOURCE.json`

### pc

Create/update:

- `PC_SPEC.md`
- `UI_REQUIREMENTS.md`
- `DATA_MODEL.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

### controller

Create/update:

- `CONTROLLER_SPEC.md`
- `STATE_MACHINE.md`
- `IO_MAP.md`
- `SAFETY_REQUIREMENTS.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

### module

Create/update:

- `MODULE_SPEC.md`
- `IO_MAP.md`
- `COMMUNICATION_REQUIREMENTS.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

## Traceability

Every specification item derived from source PDFs must preserve source file/page when available. Machine-readable protocol artifacts should carry source metadata per item.

`SPEC_SOURCE.json` records source type, source identifier, repository role, status (`draft` or `approved`), and materialized timestamp when available.

## Rules and stop condition

Do not add requirements absent from the source, resolve `TODO_VERIFY` by guessing, override approved ADR decisions, duplicate public interfaces outside their owner repository, or generate production code.

Stop when local spec artifacts faithfully represent the source.

---

# Mode: `spec-validate`

Validate `docs/spec/` before implementation. This is a gate, not a design session.

## Read first

- `AGENTS.md`
- `CONTEXT.md` if present
- relevant `CONTEXT-MAP.md`
- `docs/adr/*`
- `docs/spec/*`
- relevant `docs/raw/*`

## Checks

At minimum verify:

- required role-specific spec files exist
- source-of-truth ownership is correct
- external owner interfaces are not duplicated/redefined
- unresolved `TODO_VERIFY` is not hidden
- externally derived facts have traceability when available
- no direct conflict exists with ADRs/context definitions
- test/verification expectations exist for implementable behavior
- acceptance criteria are observable
- dependencies on other repositories are explicit
- safety-related requirements are clearly marked and not inferred

## Result and output

Return exactly one overall result:

- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`

`BLOCKED` is mandatory when unresolved uncertainty could lead to incorrect or unsafe implementation.

Create/update `docs/spec/VALIDATION_REPORT.md` with repository role, checked files, overall result, blocking findings, warnings, traceability gaps, ownership issues, unresolved decisions/TODOs, and recommended next action.

Do not fix product decisions by guessing or generate production code. Minor mechanical formatting fixes may be proposed; semantic fixes require the owner or human decision.

---

# Mode: `protocol-validate`

Perform protocol-specific validation in the protocol owner repository. This is stricter than generic spec validation.

## Read first

- `AGENTS.md`
- `CONTEXT.md` if present
- `docs/raw/*`
- `docs/adr/*`
- `docs/spec/PROTOCOL.md`
- `docs/spec/REGISTER_MAP.json`
- `docs/spec/COMMANDS.json`
- `docs/spec/ERROR_CODES.json`
- `docs/spec/TEST_VECTORS.json`

## Required checks

Check at least:

- duplicate/overlapping addresses
- address syntax/ranges
- function/opcode uniqueness
- request/response mapping
- frame length rules
- CRC/checksum definition and known vectors
- byte order and word order
- signed/unsigned types
- scale and offset
- units
- access mode (`R`, `W`, `RW`)
- enum completeness
- error/exception codes
- broadcast behavior
- timeout/retry semantics when protocol-owned
- reserved ranges
- version/compatibility rules when present
- source file/page traceability
- unresolved `TODO_VERIFY`
- consistency between human-readable and machine-readable forms

Where the source defines enough information, ensure `TEST_VECTORS.json` includes independently checkable examples. Do not generate expected values merely by reusing the same implementation algorithm without an independent source.

## Result and output

Return exactly one: `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`.

Create/update `docs/spec/PROTOCOL_VALIDATION_REPORT.md` and list every blocking ambiguity explicitly. Do not mutate consumer repositories or invent missing protocol semantics.

---

# Mode: `interface-change`

Create an owner-first plan for a public interface change before production implementation.

## Read order

When visible, read:

1. `system/AGENTS.md`
2. `system/CONTEXT-MAP.md`
3. `system/docs/spec/*`
4. owner repository `AGENTS.md` and `docs/spec/*`
5. affected consumer repository `AGENTS.md`, `CONTEXT.md`, and relevant specs
6. `manifest/default.xml`

If running inside a single repository, use cross-repository references declared in `AGENTS.md`.

## Actions

1. Identify the interface owner repository.
2. Identify all consumers/affected repositories.
3. Classify the change as compatible, conditionally compatible, or breaking.
4. Identify specification changes required before implementation.
5. Identify implementation order.
6. Identify migration/versioning requirements.
7. Identify automated, integration, and hardware verification needed.
8. Detect `HIGH`/`CRITICAL` unresolved decisions and recommend human design review when needed.

## Output

Create in the system owner repository:

```text
docs/changes/IC-XXXX-<slug>.md
```

Choose the next available numeric ID without rewriting existing IDs. Include goal, owner, affected repositories, current/proposed contract, compatibility impact, required spec updates, implementation order, tests, manual/hardware checkpoints, unresolved decisions, and approval status.

## Owner-first rule and stop condition

Public-interface semantics must be updated and approved in the owner repository before consumers implement them.

Do not implement consumer code, silently alter protocol semantics inside a consumer, or mark a breaking change compatible without evidence.

Stop after the change plan and recommended next action.

---

# Mode: `system-verify`

Verify an integrated multi-repository product change after affected repositories have implemented and reviewed it.

## Inputs

Accept a change ID, release-candidate identifier, or explicit verification goal.

## Read first

- `system/AGENTS.md`
- `system/docs/spec/SYSTEM_TEST_PLAN.md`
- related `system/docs/changes/IC-*.md`
- affected repository `AGENTS.md`
- affected repository test/build instructions
- `manifest/default.xml` when available

## Actions

1. Record current branch/tag/commit SHA for every affected repository.
2. Run repository-local automated build/test commands when available.
3. Run integration tests defined by the system test plan.
4. Check public interface/spec versions match the verified revisions.
5. List hardware/manual tests that cannot be performed automatically.
6. Never mark a manual/hardware test `PASS` without explicit evidence.

## Status values

For each check use:

- `PASS`
- `FAIL`
- `BLOCKED`
- `MANUAL_PENDING`
- `NOT_APPLICABLE`

Overall verification is `PASS` only when all required automatic and manual checks are `PASS` or `NOT_APPLICABLE`.

## Output

Create in the system repository:

```text
docs/verification/VER-<id>.md
```

Include verification goal/change ID, exact repository revisions, spec/interface revisions, commands executed, automatic results, integration results, hardware/manual results, failures/blockers, overall result, and evidence references.

Do not create a release manifest when overall result is not `PASS`.

---

# Mode: `manifest-release`

Create a reproducible product release by pinning exact verified repository revisions in the manifest repository.

## Preconditions

Require:

- requested product version
- system verification artifact with overall result `PASS`
- exact repository revisions used by that verification

If any required verification is `FAIL`, `BLOCKED`, or `MANUAL_PENDING`, stop.

## Read first

- manifest repository `AGENTS.md`
- `default.xml`
- existing `releases/*`
- referenced system verification artifact

## Actions

1. Validate each release revision matches the successful verification record.
2. Refuse dirty/unrecorded workspace state when it would make the release non-reproducible.
3. Generate a release manifest pinning exact immutable revisions (commit SHA or approved immutable tag).
4. Generate a human-readable release record.
5. Preserve `default.xml` as the development manifest unless the user explicitly requests a development-baseline update.

## Outputs

Create:

```text
releases/v<version>.xml
releases/v<version>.md
```

The Markdown record includes product version, source verification artifact, repositories/paths/pinned revisions, protocol/interface versions when applicable, known limitations, release date when available, and reproducibility instructions.

## Rules and stop condition

- Never point a release manifest at moving branches such as `develop` or `main` unless the user explicitly requests a clearly marked non-reproducible snapshot.
- Never create a release from unverified revisions.
- Never rewrite an existing released version without explicit user approval.

Stop after creating release artifacts and reporting the exact pinned revisions.
