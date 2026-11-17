# Existing project — source facts, evolving confirmed scheme

Suppose an industrial-device repository contains one Git root with `Firmware/`, `PC/`, `Protocol/` and `Hardware/`, but the docs are outdated.

```text
$project-bootstrap
```

1. Inspect actual source, build/project settings, the protocol definitions, hardware files, tests and working state. Record concrete evidence for the **current implementation**.
2. Build or update confirmed requirements and technical constraints without silently promoting implementation details to approved intent. If no suitable documents exist, use `docs/requirements.md` and `docs/technical-constraints.md`.
3. Establish a project **document index** (default `docs/README.md`), linking these records and applicable existing architecture/decision docs. Root `AGENTS.md` points to the index.
4. Example: the source's register table declares a temperature setpoint; this is **observed behavior**. A requirement that customers may change that setpoint remotely is **Confirmed** only when backed by a user-approved requirement, authoritative contract or standard. Otherwise it is **Pending confirmation**.
5. When a new feature requests a different register scheme, a **focused Grill round** can clarify important interface tradeoffs. For wider hardware/software redesign with unclear boundaries, **Wayfinder** can clarify a multi-stage direction.
6. After user/project confirmation, update the effective source document and document index. Mark the old design superseded when replaced; the agent then directly changes the relevant PC/Firmware/Protocol code and runs appropriate checks.
7. Repeat when a new consequential design decision emerges. Do not rerun Grill/Wayfinder solely because a line of code is modified.

The index helps the next session find the **current approved scheme**, while source remains the factual baseline of what the device has actually implemented.
