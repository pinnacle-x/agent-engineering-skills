# Document Discovery and Design Lifecycle

The goal is to ensure the agent can find an **effective, currently confirmed design** after a new session, after multiple Grill/Wayfinder discussions, or when picking up an older repository.

## Two stable entry points

Root `AGENTS.md` should contain:

```markdown
## Project Documentation
- Project document index: [docs/README.md](docs/README.md) (if present).
- Before engineering work, consult the index and read the relevant Active / Confirmed documents.
- After an important design decision is accepted or superseded, update the authoritative document and the index.
- Pending or superseded proposals are not implementation instructions.

## Project Rules
- Project rules live in `.agents/rules/` and are created only when needed.
- If it exists, inspect and read applicable rules. Do not assume runtime auto-loading.
```

Replace `docs/README.md` with the project's established index path if different. **Do not list every design document in AGENTS.md**. Document files, Grill/Wayfinder output paths and their statuses are maintained in the project index.

The agent must not assume the index exists just because the default path is named. If an actual project document exists but has no index, establish one with working links; avoid empty placeholders.

## What the document index tracks

Each entry should have enough metadata to choose the right document without loading the entire repository:

| Category | Recommended information |
| --- | --- |
| Current implementation | Actual source paths, relevant commit/working-state evidence, scope |
| Confirmed requirements | Link to the governing requirement document, scope, confirmation authority |
| Technical constraints | Link to verified or approved constraints, module/system scope |
| Active design | Link to the **currently approved** architecture or scheme, applicable task/area, confirmation reference |
| Pending | Link or short description of unresolved decisions, without portraying drafts as accepted |
| Superseded | Historical design reference and the active replacement; never a current instruction |

A table is optional: existing project indexes may use links/headings. **Valid links, applicability and effective status are essential.** The index is a navigation map, **not a second copy of the detailed architecture**.

## What makes a design record usable

A confirmed design document, whether produced by Grill/Wayfinder or written directly by the agent from an approved decision, should make the agent's task feasible. As applicable, record:

- goal and affected scope;
- decisions and important boundaries/interfaces;
- relevant constraints and accepted tradeoffs;
- unresolved questions and assumptions;
- confirmation source (user acceptance, approved contract or project authority);
- status: `Active` / `Pending` / `Superseded`;
- paths to authoritative implementation/contracts and validation expectations where relevant.

Do not require a fixed ADR format or extensive documentation for each question. Preserve upstream Grill/Wayfinder outputs where useful, and link their actual paths rather than duplicating entire contents.

## When to use Grill or Wayfinder again

Consider another design round when a **new consequential decision** arises: changed requirements, new phase of a broad project, architecture or subsystem boundary choice, significant interface compatibility change, constraint conflict, or implementation evidence invalidating a previous design.

For a focused unresolved design, `grill-with-docs` is a reasonable choice. For broad multi-stage ambiguity, `wayfinder` is a reasonable choice. Neither tool decides approval by itself; the project authority confirms the actual scheme.

A local implementation fix with clear applicable design need not start another Grill/Wayfinder interview.

## After the decision is confirmed

1. Locate the existing authoritative document, or use the confirmed design output as that document.
2. Update the content or link to the new active design. Preserve important decision context, but do not let two contradictory documents both claim to be active.
3. Update the project document index: actual paths, scope, new status, replacement of superseded documents and unresolved questions.
4. The agent reads the relevant active scheme and current source, then **executes directly**.
5. Compare implementation and verification evidence with the accepted scheme; if reality diverges, treat it as a discrepancy and loop back to clarification when needed.

## Existing-source-specific safeguard

Current source and observed behavior are authoritative for **what is currently implemented**, not automatically for intended requirements. Start by establishing the baseline; document and index confirmed requirements/technical constraints only when backed by reliable evidence or approval. Track source-only inferred requirements as pending.

Updating code does not authorize silently rewriting approved project requirements to match the code. Conversely, a stale design document cannot override observed facts about the current implementation. Resolve the divergence explicitly.

## Example layouts (not required)

```text
project/
├── AGENTS.md                      # stable index pointer and rules-directory policy
├── docs/
│   ├── README.md                  # links to actual active/pending/superseded docs
│   ├── requirements.md            # existing project, when no equivalent exists
│   ├── technical-constraints.md   # existing project, when no equivalent exists
│   └── architecture.md            # only if real confirmed architecture is recorded
├── .agents/
│   └── rules/                     # not created by default
└── ... existing source
```

The project may instead use `docs/design/`, module-local docs or a pre-existing index. Preserve those locations; root `AGENTS.md` must point to the **actual** index.
