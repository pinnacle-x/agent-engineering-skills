# Repository and Module Boundaries

Engineering Governance adapts to real project structure and does not mandate a number of Git repositories, a directory layout or a separate "system" repository.

## Single Git

Example:

```text
industrial-device/
├── .git/
├── Firmware/
├── PC/
├── Protocol/
├── Hardware/
└── docs/
```

Here firmware, PC and protocol may be separate **modules**, but they share one Git commit history. Coordinate shared interface changes across modules and verify integration using **one commit SHA**. Do not create a multi-repository manifest simply because there are many directories.

## Multiple Git

A product may instead have independent firmware, PC, protocol, hardware and composition repositories. Determine the actual owner of a shared contract; check consumer compatibility and verify an exact revision for each included repository. A release manifest is useful when a product needs to pin several independently versioned repositories.

## Preserve existing design

These are examples, not required project folders. Keep current module boundaries, authoritative contract locations, documentation conventions and delivery policies unless the user explicitly asks to reorganize them.
