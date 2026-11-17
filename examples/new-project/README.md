# New project — Grill/Wayfinder and current architecture

A new industrial-device product needs an MCU, communication protocol and temperature-control architecture, but no established product source exists.

1. Use `$project-bootstrap` to record known goals/constraints and stable project entry guidance. Do not create fictional architecture files just to fill a template.
2. Use upstream `/setup-matt-pocock-skills` once with **Local Markdown** as the issue tracker (when not using GitHub Issues).
3. Invoke `/grill-with-docs` for focused choices. If the scope is too broad for one session, invoke `/wayfinder`: it stores a local decision Map and child tickets under configured `.scratch/` locations.
4. After extensive accepted decisions, optionally invoke `/to-spec` to write `.scratch/<feature>/spec.md`. Retain ADRs for qualifying long-lived design decisions. Confirm what was actually persisted; Grill does not promise a file for every agreed detail.
5. Once an architecture is approved and sufficiently concrete, `$project-bootstrap update-design` can establish or update `docs/architecture.md` and `docs/design-overview.md` (or the project's existing locations), **without copying the entire tracker/spec**.
6. `AGENTS.md` references the current long-lived design and configured tracker/domain paths. No `docs/README.md` index is required unless the project already uses one or needs it.
7. The Agent executes the approved scope directly. As code is built, it checks and syncs affected architecture/overview sections, clearly distinguishing current implementation from future accepted targets.
8. Revisit Grill/Wayfinder only for important new decisions. Check `.gitignore` before relying on local `.scratch/` on another machine.

An accepted Wayfinder Map is a decision record; an optional task spec is a snapshot; current architecture and high-level design remain living project documentation.
