# New project — repeated design decisions

A new industrial-device product has no existing source code. The user has confirmed a temperature-control goal but has not chosen the MCU, communications interface or control architecture.

```text
$project-bootstrap
```

1. Establish confirmed requirements and initial constraints; record the important choices still open.
2. If the project's overall boundaries are ambiguous, a Wayfinder round can clarify scope and system priorities. Use Grill for a focused high-impact choice such as MCU/system architecture.
3. A **user-accepted** decision becomes an effective project design document. Place the record in the project's chosen location (for example `docs/architecture.md`) and link it under **Active approved designs** in the document index (for example `docs/README.md`).
4. Root `AGENTS.md` points to that **index**, not to every individual design record.
5. The agent reads the relevant approved design and directly builds the agreed scope.
6. When a new subsystem or interface decision emerges, use Grill/Wayfinder again as appropriate, confirm the outcome and update the design document and index. Replace or mark obsolete plans `Superseded`; avoid two competing active schemes.

This is **an iterative loop**, not a single upfront workshop and not a mandatory new meeting for every small code change.
