# Cross-Repository Public Interface Workflow

Use PraxFlow only when one product change modifies a public contract consumed by multiple independent repositories.

Example: adding a `StartTest` command affects a protocol owner plus controller and PC consumers.

## 1. Plan the contract change

From a workspace that can inspect the relevant repositories:

```text
$praxflow interface-change
goal: Add StartTest command.
```

Expected record:

```text
system/docs/changes/IC-0001-start-test-command.md
```

The plan identifies the owner, consumers, compatibility impact, implementation order, migration/versioning needs, and verification requirements.

## 2. Owner first

The owner contract must be updated and approved through the project's normal process before consumers change the public semantics.

```text
owner contract update + approval
  -> owner implementation when applicable
  -> consumer implementations
  -> local tests in each repository
  -> integrated system verification
```

PraxFlow does not dictate how the owner contract is written or validated. Use the active agent and the repository's normal engineering process.

## 3. Verify the exact combination

After all affected repositories are ready:

```text
$praxflow system-verify
change: IC-0001
```

The verification record must capture exact commit SHAs and manual/hardware evidence.

## 4. Release only the verified combination

Only after verification is `PASS`:

```text
$praxflow manifest-release
```

The release manifest pins the exact verified revisions, not floating branch names.
