# Single-Git change impact example

A product has one `.git` root and three modules: `Firmware/`, `PC/` and `Protocol/`. A Modbus register meaning changes.

```text
$engineering-governance change-impact
goal: Assess changing the approved Modbus register across Firmware, PC and Protocol.
```

The Skill identifies the authoritative protocol definition, both consumers, compatibility, migration and checks. It **does not** demand separate Git repositories, approval IDs, ADR files or `docs/changes/`. For a straightforward change it may answer in the conversation or existing PR.

The active agent then edits the affected code and appropriate documentation/tests. Integrated verification can use **one exact Git SHA**, plus any necessary hardware evidence.
