# Engineering Governance — Integrated Verification and Release

`engineering-governance` remains optional for `verify` and `release` in single- or multi-Git products. The Agent performs ordinary engineering work and affected-module analysis itself.

## Read current source and approved design

Before system verification, consult `AGENTS.md` for existing current architecture/high-level design documents and upstream domain/tracker configuration. Read relevant approved requirements, ADRs and the **identified task spec or resolved decision Map** when available. Do not assume an unapproved Map or an old local spec describes the current target. Cross-check source revision, build configuration and observed results.

| Product shape | Evidence |
| --- | --- |
| Single Git, routine change | Agent's normal checks; governance may not be warranted |
| Single Git, coupled modules | One exact SHA, applicable system/interface/hardware evidence |
| Multiple Git repositories | Exact SHA of every participating repository, checked together |

## Verify

```text
$engineering-governance verify
```

Review actual checks against **current implementation facts and accepted target requirements**. Use existing project verification reports or optional `templates/SYSTEM_VERIFICATION.md`. Unperformed hardware/manual checks remain `MANUAL_PENDING` or `BLOCKED`, not `PASS`.

## Release

```text
$engineering-governance release
```

Release only a verified immutable revision or revision combination. Follow existing version/tag/documentation conventions; use a multi-repository composition manifest only when a product actually spans independently versioned repositories.

After a material code change, the Agent should also assess whether long-lived architecture/overview documents need updating. A release should identify known unresolved design/implementation discrepancies rather than silently treating a stale document as a passed requirement.
