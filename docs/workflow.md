# PraxFlow Workflow

PraxFlow is not a full development lifecycle. It is a thin governance layer used only when work crosses independent repositories.

## Normal work

Use the active agent and general engineering Skills directly for:

- PDF/document reading;
- repository/code discovery;
- domain modeling and design;
- specification work;
- protocol analysis;
- implementation/TDD/debugging/review;
- repository-local build and tests.

Use `grill-with-docs` when an important design choice needs interactive human review and durable design documentation.

## When PraxFlow is needed

### 1. Public interface change

Before changing a contract consumed by multiple repositories:

```text
$praxflow interface-change
```

PraxFlow records ownership, consumers, compatibility impact, owner-first update order, migration/versioning, and required verification.

Output:

```text
system/docs/changes/IC-XXXX-<slug>.md
```

Do not use this mode for repository-local refactors.

### 2. Integrated system verification

After all affected repositories are implemented and locally tested:

```text
$praxflow system-verify
```

PraxFlow records the exact commit SHA of every included repository and binds test/integration/manual evidence to that revision set.

Output:

```text
system/docs/verification/VER-<id>.md
```

Manual/hardware checks remain `MANUAL_PENDING` until explicit evidence exists.

### 3. Reproducible release

Only after integrated verification is `PASS`:

```text
$praxflow manifest-release
```

PraxFlow creates an immutable product-composition record that pins the exact verified revisions.

Typical outputs:

```text
releases/vX.Y.Z.xml
releases/vX.Y.Z.md
```

A non-XML manifest format is also acceptable if it pins the same immutable revision set.

## Compact lifecycle

```text
Agent reads requirements / PDFs / repositories
        ↓
Agent + grill-with-docs when major design choices require review
        ↓
Agent implements and runs repository-local tests
        ↓
Shared/public contract changing?
        └─ yes → $praxflow interface-change BEFORE consumer semantic changes
        ↓
All affected repositories ready
        ↓
$praxflow system-verify
        ↓
PASS + all manual/hardware checks complete
        ↓
$praxflow manifest-release
```

## Core policy

- one public contract has one owner;
- owner changes first, consumers follow;
- verification records exact repository revisions;
- manual/hardware checks require explicit evidence;
- releases pin exactly the revisions that passed verification.
