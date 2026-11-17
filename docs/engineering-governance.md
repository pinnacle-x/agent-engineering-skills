# Engineering Governance: Single Git and Multi Git

Use `engineering-governance` when an interface change, coupled modules, integrated verification or a reproducible release justifies extra coordination.

| Scope | Change impact | Verification | Release |
|---|---|---|---|
| Single Git, isolated change | Ordinary agent work | Local checks | Existing project convention |
| Single Git, coupled modules | Shared module/file contracts | One commit SHA + integrated checks | One SHA, optional Git tag; no multi-repo XML |
| Multiple Git repositories | Cross-repo contract owner and consumers | Exact SHA per included repository | Verified SHA combination in an existing/preferred manifest |

Directory names do **not** determine Git repository count. A tree containing `Firmware/` and `PC/` can still be a single repository.

## Change impact (optional)

```text
$engineering-governance change-impact
```

Inspect the authoritative shared interface (e.g. Modbus register definition), affected PC/firmware consumers, compatibility, migration and verification obligations. In a single Git repository, the owner definition and consumers may be committed together. In multiple repos, coordinate owner-first changes when there is a separately maintained contract.

Resolve genuine design uncertainty through the active agent; optional Grill/Wayfinder can help. **Do not force ADR approval or numbered change documents.** Use `templates/CHANGE_IMPACT.md` only when durable coordination records are genuinely useful.

## Verify (optional)

```text
$engineering-governance verify
```

Run relevant actual checks, identify the exact Git revision(s), and record uncommitted state and any unperformed hardware checks. A single Git needs **one SHA**; multiple repos require one for each participating repository. Do not mark unperformed physical tests as passed. Use existing test logs or `templates/SYSTEM_VERIFICATION.md` where a persistent report is needed.

## Release (on request)

```text
$engineering-governance release
```

A single Git project usually uses its tested commit, project version/tag and normal release artifacts. A multi-repo product may require a manifest pinning exactly the tested repository SHAs. Preserve whichever format the project already uses. Never require an XML manifest or a new documentation hierarchy for single-Git projects.

Do not release an unverified revision set; record missing required checks and blockers. Documentation is produced and maintained to meet **the project's actual needs**, not a mandatory minimum or maximum.

## Source ownership

Implementation truth lives in code and verified tests. Approved requirements, standards and public protocol contracts still define **what should be implemented**; they may live inside one repository or in a separately owned repository. Do not silently replace them with consumer copies.
