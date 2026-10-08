# PraxFlow Skill Reference

PraxFlow is maintained as one Agent Skill:

```text
skills/praxflow/SKILL.md
```

The Skill exposes multiple workflow modes through one entrypoint.

## `repo-bootstrap`

**Invocation:**

```text
$praxflow repo-bootstrap
role: system
```

**Use when:** creating or standardizing a system, protocol, PC, controller, module, hardware, or manifest repository.

**Reads:** current repository structure, existing `AGENTS.md`, existing agent metadata.

**Does:** establishes repository role, ownership rules, durable folders, implementation gates, and source-of-truth references.

**Does not:** invent requirements or create speculative `CONTEXT.md`, ADRs, or formal specs.

## `pdf-ingest`

**Invocation:**

```text
$praxflow pdf-ingest input/DeviceManual.pdf
```

**Does:** extracts PDF evidence, preserves source file/page, identifies weak extraction/OCR candidates, renders visual page artifacts when required, and marks uncertainty instead of guessing.

**Writes:**

```text
docs/raw/<stem>_raw.md
docs/raw/<stem>_extraction_report.md
docs/raw/<stem>_images/page_NNN.png   # rendered pages
```

For schematics and engineering drawings, use rendered page images with a vision-capable model. Do not infer exact electrical connectivity from extracted labels alone; prefer a netlist/native structured source when exact connectivity matters.

## `system-discovery`

**Invocation:**

```text
$praxflow system-discovery
```

**Use in:** the system repository after relevant source ingestion.

**Does:** identifies evidence-backed contexts, responsibilities, interface ownership, and unresolved product decisions.

**Writes:**

```text
CONTEXT-MAP.md
docs/system/SYSTEM_FACTS.md
docs/system/OPEN_DECISIONS.md
```

**Decision policy:** classify unresolved decisions `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`. Recommend deep design review for `HIGH`/`CRITICAL`; do not invoke it automatically.

## `spec-materialize`

**Invocation:**

```text
$praxflow spec-materialize
source: issue #123
```

**Does:** converts a concrete reviewed/draft specification source into repository-owned structured files without changing meaning.

**Writes:** role-specific files under `docs/spec/` plus `SPEC_SOURCE.json`.

## `spec-validate`

**Invocation:**

```text
$praxflow spec-validate
```

**Checks:** completeness, unresolved `TODO_VERIFY`, source ownership, contradictions with ADRs, testability, and implementation readiness.

**Writes:** `docs/spec/VALIDATION_REPORT.md`.

**Result:** `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`.

## `protocol-validate`

**Invocation:**

```text
$praxflow protocol-validate
```

**Use in:** protocol repositories.

**Checks:** addresses, function/command codes, frame lengths, CRC, endianness, signedness, scale/offset, units, permissions, enumerations, error codes, source pages, and unresolved verification markers.

**Writes:** `docs/spec/PROTOCOL_VALIDATION_REPORT.md`.

## `interface-change`

**Invocation:**

```text
$praxflow interface-change
goal: Add StartTest command.
```

**Does:** identifies owner repository, affected consumers, compatibility risk, required update order, and verification plan.

**Writes:** `system/docs/changes/IC-XXXX-<slug>.md`.

**Rule:** owner spec first; consumers never redefine a shared contract locally.

## `system-verify`

**Invocation:**

```text
$praxflow system-verify
change: IC-0001
```

**Does:** records exact repository SHAs, runs/records repository tests, integration checks, and separates automated from manual/hardware evidence.

**Writes:** `system/docs/verification/VER-<id>.md`.

**Per-check status:** `PASS`, `FAIL`, `BLOCKED`, `MANUAL_PENDING`, or `NOT_APPLICABLE`.

## `manifest-release`

**Invocation:**

```text
$praxflow manifest-release
version: 1.0.0
verification: system/docs/verification/VER-RC-001.md
```

**Precondition:** system verification is `PASS`.

**Writes:**

```text
releases/vX.Y.Z.xml
releases/vX.Y.Z.md
```

The XML pins the tested repository revisions so the complete product can be reproduced.

## Mode routing

If the user invokes `$praxflow` without naming a mode, the Agent may infer the mode only when the requested action is unambiguous. Otherwise it asks once which workflow stage is intended.

Each mode retains its own stop condition. PraxFlow must not silently continue from evidence extraction into design, from design into implementation, or from verification into release.
