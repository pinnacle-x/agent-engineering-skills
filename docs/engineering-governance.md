# Engineering Governance — Verification and Release

`engineering-governance` is optional and limited to integrated `verify` and `release` for single-Git or multi-Git products.

The active agent determines and handles affected code/interfaces directly. It can return to Grill/Wayfinder when a new consequential design decision is unresolved; accepted outcomes are written into the project's authoritative documents and discoverable via the document index.

## Verification reads the effective scheme

Before integrated verification, consult the actual project document index referenced by `AGENTS.md`. Read current **Active / Confirmed** requirements, technical constraints, interfaces and accepted architecture relevant to the target system. Compare them with the actual code revision and observed results. Do **not** treat an old design draft as a specification for verification.

| Project type | Evidence needed |
| --- | --- |
| Single Git, local work | Routine agent checks, governance often unnecessary |
| Single Git with coupled modules | One exact SHA, module/interface checks, required hardware acceptance evidence |
| Multiple Git repositories | Exact SHA of each participating repo and compatibility tests for the combination |

## Verify

```text
$engineering-governance verify
```

Run/review actual appropriate integration checks. Record commands and outcomes; keep required unperformed manual/hardware checks pending. Use existing project reporting conventions or an optional `templates/SYSTEM_VERIFICATION.md` when a persistent record is warranted.

## Release

```text
$engineering-governance release
```

Use the exact verified revision(s) and the current effective approved scheme. A single Git typically needs a SHA/tag, not a multi-repo XML. Multi-Git composition can require a manifest pinning exact verified SHAs.

Do not silently reuse superseded schemes, publish unverified combinations or misstate pending hardware tests. The agent handles ordinary engineering execution directly.
