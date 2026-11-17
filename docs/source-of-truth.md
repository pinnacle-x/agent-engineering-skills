# Sources of Truth — Current State and Effective Scheme

A successful project needs **two different kinds of authority**, neither of which can silently replace the other.

## 1. Current implementation facts

For an existing project, current source, build/deployment configuration, actual hardware/project files and observed test/runtime results determine **what currently exists or happens**. Inspect the relevant revision/workspace and retain file/evidence references.

An older README or remembered design cannot overrule a directly inspected current implementation fact.

## 2. Confirmed requirements and effective design

Accepted user decisions, external standards, signed-off contracts, verified engineering constraints and project-approved design records determine **what should be implemented**.

Start from current code when adopting an existing project, then establish `requirements.md` and `technical-constraints.md` or their actual established equivalents. Code-only inferred intent is **Pending confirmation**; it is not automatically an approved requirement.

For new projects without source, start from confirmed user goals and constraints; use repeated design rounds as needed to establish the first and subsequent schemes.

## 3. Document discoverability and lifecycle

Root `AGENTS.md` links **one actual project document index** (normally `docs/README.md`). The index identifies the current implementation baseline, confirmed requirements/constraints and the **active, approved** design documents. Pending drafts and superseded designs remain distinguishable and cannot silently govern implementation.

After a consequential design decision is confirmed through a Grill/Wayfinder discussion or another accepted project process, **update the authoritative document and index**. The agent then executes against that active scheme and actual source.

Project documents may live in existing docs directories or modules. The index links to their **real paths** and keeps status/application up to date, without forcing a new directory hierarchy.

## 4. Conflicts

If actual code differs from approved design, treat it as a **tracked discrepancy**:

- The code still describes current behavior.
- The accepted requirement/design describes expected behavior.
- Resolve whether to change code, revise design with confirmation, or preserve an intentional compatibility exception.

Do not silently change accepted requirements to match an implementation mistake, or pretend code already implements a design that it does not.

## 5. Shared contracts

A protocol/interface has one semantic owner within a module or repository, even when copied/generated representations exist elsewhere. The agent checks dependent consumers during ordinary engineering work; integration evidence can later use `engineering-governance verify` when necessary.
