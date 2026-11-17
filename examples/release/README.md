# Release examples

## One Git

```text
$engineering-governance release
version: 1.0.0
scope: one Git repository with Firmware, PC and Protocol modules
```

Use the verified commit SHA and, if the project uses them, Git tag `v1.0.0`, normal build outputs and required release documents. Do **not** generate a multi-repo XML manifest.

## Multiple Git repositories

```text
$engineering-governance release
version: 1.0.0
scope: separately versioned Firmware, PC and Protocol Git repositories
```

Use the product's existing/preferred composition manifest to pin the **verified SHA of each included repository**. Preserve actual verification evidence; do not claim pending hardware checks passed. The manifest is warranted by independent revision combinations, not by folder names.
