# Agent-Led Engineering Workflow

## Default: the agent works directly

```text
User goal → agent inspects current code and requirements
          → agent chooses design/specification/TDD/implementation approach
          → agent updates code, tests and appropriate documentation
          → actual verification results and Git revisions
```

The agent decides task decomposition, test strategy, document detail and location based on existing conventions and requirements. **No mandatory chain of Grill → Spec → Tickets → TDD → Review**.

Optional `grill-with-docs` can assist major undecided design, and `wayfinder` can assist large ambiguous, multi-session problems. Neither is a prerequisite for implementing a clear task.

## When instructions need initialization or repair

```text
$project-bootstrap
```

Create/reconcile `AGENTS.md`; do not create `.agents/rules/` by default. If an agent repeatedly makes the same confirmed error, use:

```text
$project-bootstrap add-rule
```

Only persist the scoped rule with approval and index its task-specific loading condition in `AGENTS.md`.

## When system-level risk warrants it

For coupled modules or repositories, shared contract changes, integration readiness or versioned delivery:

```text
$engineering-governance change-impact
$engineering-governance verify
$engineering-governance release
```

The Skill chooses **single-Git** vs **multi-Git** strategy based on actual Git roots, not folder count. Routine single-module changes stay with the agent. Results can live in the response, existing project records or additional documents where the work requires them.

## Examples

- **Single Git, small code change:** agent edits/tests; governance generally unnecessary.
- **One Git with PC + Firmware + Protocol:** agent manages the code; governance can check shared protocol impact and integrated verification using one Git SHA.
- **Separate PC/Firmware/Protocol Git repositories:** governance can coordinate contract ownership, check compatibility across exact SHAs and pin a multi-repository release composition.

See [Engineering Governance](engineering-governance.md).
