# Existing source project — keep current design documents aligned

A single Git repository holds `Firmware/`, `PC/`, `Protocol/` and `Hardware/`. The current README describes an older implementation.

1. Invoke `$project-bootstrap` to inspect real current source/project config, interface definitions, tests and state. The actual implementation is the baseline for what presently exists.
2. Preserve accepted external standards and user-confirmed behavior as intended requirements; don't promote observed source behavior to approved design without confirmation. Update existing requirement/constraint docs, or `docs/requirements.md` and `docs/technical-constraints.md` if needed.
3. If using upstream Grill, choose **Local Markdown** in `/setup-matt-pocock-skills`. Read configured `docs/agents/domain.md` and `docs/agents/issue-tracker.md` (or real existing equivalents), applicable ADRs and task-linked Map/spec when present.
4. Reconcile existing system architecture/high-level design (or `docs/architecture.md` and `docs/design-overview.md` when appropriate) using actual implementation evidence and accepted targets. The `AGENTS.md` entry points to those stable files and upstream configuration, without needing an additional mandatory index.
5. Example: a new Modbus register changes firmware and PC parsing. If the public interface decision is unresolved, use Grill. Once accepted, Agent edits the code directly, then syncs affected overview/interface flow and architecture sections only if changed.
6. At any point, request `$project-bootstrap update-design` to review and synchronize stale architecture/overview documentation. A routine internal bug fix with no design effect should not force edits.
7. If source contradicts an accepted design, report the mismatch as pending rather than rewriting the requirement or claiming the target is implemented.
8. Check whether `.scratch/` is ignored or untracked before assuming that task specs will survive a fresh clone. Upstream map/spec locations are not automatically project-wide permanent documentation.

This approach treats the source as current engineering evidence, ADRs and task specs as confirmed decision context, and architecture/overview documents as living representations of the project.
