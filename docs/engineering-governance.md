# Engineering Governance — Integrated Verification and Release

`engineering-governance` provides optional `verify` and `release` modes when a system needs traceable integration results or reproducible delivery. The agent **directly** investigates effects on modules/interfaces while performing project work; governance does not duplicate that work.

| Situation | Verification scope | Release evidence |
| --- | --- | --- |
| One Git, isolated task | Normal agent checks; governance generally unnecessary | Existing project process |
| One Git, coupled modules | Integrated checks associated with **one** immutable Git SHA | That revision and optional project tag |
| Multiple independent Git repositories | Compatibility and integration checks against **each** included repo SHA | Verified immutable revision combination in a suitable manifest |

A project containing `Firmware/`, `PC/` and `Protocol/` can still have a single `.git` root. Directory count does not determine Git count.

## Verify

```text
$engineering-governance verify
```

Review the actual project’s required checks and run/coordinate relevant integration verification. Record commands, test results, exact revision(s), hardware/manual acceptance evidence and remaining unknowns. Unperformed required checks stay pending; do not label them as passing.

A lasting verification document can use `templates/SYSTEM_VERIFICATION.md` when justified by actual project requirements, not as a mandatory file for every change.

## Release

```text
$engineering-governance release
```

Confirm release version, required verification and exact matching tested revision(s).

- **Single Git:** use the verified commit SHA and existing tag/release conventions. Do not generate multi-repository XML.
- **Multi Git:** pin the exact verified SHA of each included repository, using the existing/preferred product-composition format. A manifest is appropriate when a product combines independently versioned repositories.

Do not silently replace published releases, use moving branch names as fixed versions or pretend missing hardware checks passed. Preserve documentation and delivery evidence appropriate to project requirements.

## Relationship to project bootstrap

For an **existing** project, `project-bootstrap` establishes source-evidenced current state and the confirmed requirements and technical constraints. Those artifacts inform verification requirements; the agent resolves cross-module effects directly. No other Skill is a mandatory prerequisite.
