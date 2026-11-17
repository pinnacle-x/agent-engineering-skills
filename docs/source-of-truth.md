# Sources of Truth

## Current implementation and intended behavior

- **Current implemented behavior:** source files, build configurations and observed tests.
- **Intended behavior:** user-approved requirements, external standards, protocols, hardware specifications, and accepted product decisions.
- **Integration and delivery evidence:** actual test results, artifact identities and immutable Git revision(s).
- **Architectural rationale:** existing project documents and decisions where they remain relevant.

Conflicts between code and a requirement are discrepancies to resolve, not permission to silently rewrite the requirement.

## Shared contracts across modules or repositories

Each shared contract should have a clear semantic owner (a file/module within one Git or an independently versioned repository). Consumers should use or reference that owner instead of maintaining competing definitions.

When a public contract changes, identify the owner, affected consumers, compatibility and necessary tests. In one Git, owner and consumers can change together. In multiple Git repositories, coordinate agreed owner-first updates and verify the exact combined revisions.

Use `$engineering-governance change-impact` only where the impact merits it. The Skill does not prescribe documents, issue trackers or a mandatory Spec/ADR pipeline.

## Documentation

Respect the project's existing locations. Without prior convention, project-level documentation defaults to `docs/` and module docs live near the modules. The active agent determines appropriate content, structure and level of detail for project needs.
