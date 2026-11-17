# System verification (optional record)

Create this file only when a persistent record is warranted by project process, risk or user request.

- Scope: single Git / multiple Git repositories
- Verification goal: <goal or release candidate>
- Result: PASS | FAIL | BLOCKED | MANUAL_PENDING

## Revision(s)

| Git repository | Commit SHA | Affected modules / notes |
|---|---|---|
| <repo> | <exact SHA> | <scope> |

For single-Git projects, **one row** is sufficient. For multi-Git releases, include each required repository. Record uncommitted changes explicitly.

## Automated and integration evidence

<commands actually run, results, logs/artifacts, interfaces checked>

## Hardware/manual evidence

<required check, actual status, evidence or pending reason>

## Known limitations

<missing coverage, failures, unresolved risks>
