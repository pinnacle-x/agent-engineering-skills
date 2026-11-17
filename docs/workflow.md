# Continuous Design Confirmation → Direct Agent Execution

The agent is the direct engineering executor. The purpose of Grill/Wayfinder is to help settle consequential design questions **whenever they emerge**, not merely at the beginning of a project. The purpose of project documentation is to let the agent find the **currently effective confirmed scheme**.

## 1. Establish the starting context

- **Greenfield:** identify user goals, confirmed constraints, available decisions and open design questions. There is no source baseline to invent.
- **Existing project:** inspect actual source, build/runtime configuration, hardware and interface artifacts, test evidence and revision state. Source is the factual baseline of the current implementation. Then establish/update confirmed requirements and technical constraints; mark inferred intentions for confirmation rather than declaring them approved.

`$project-bootstrap` can create/reconcile the project entry and discoverable document index. Re-running it is not required for every later design decision.

## 2. Iterate at meaningful design decision points

```text
New phase / new requirement / unresolved architecture or interface decision
                           ↓
    Focused issue → grill-with-docs
    Large ambiguous multi-stage issue → wayfinder
                           ↓
               Proposed scheme and alternatives
                           ↓
          User/project authority confirms direction
                           ↓
      Update effective scheme documentation + doc index
                           ↓
            Active agent executes the scope directly
                           ↓
     Evidence/feedback/new uncertainty → repeat as needed
```

Grill/Wayfinder can be used repeatedly across project phases, but they are **not gates for every minor modification**. Complexity alone is not a reason to rerun discovery when an accepted design already covers the task.

Do not mistake a tool's proposal for approval. Keep decisions marked pending until the user or an authorized project owner confirms them. If implementation reveals that a design is wrong or obsolete, return to a suitable design discussion and update the effective documentation after confirmation.

## 3. How the agent finds documents

Root `AGENTS.md` points to the **project document index** (default `docs/README.md`, or the real established path). The index lists **actual paths** for current implementation evidence, confirmed requirements/constraints, effective architecture/decision records and unresolved/superseded designs.

The agent should:

1. Read `AGENTS.md`, the document index, applicable project rules under `.agents/rules/` (when present), and relevant source.
2. Select **Active / Confirmed** documents applicable to the task; never treat an obsolete alternative or unaccepted draft as the implementation instruction.
3. Compare the selected scheme with current source and external controlling requirements. If they disagree, surface and resolve the mismatch before making an irreversible assumption.
4. After a meaningful accepted design change, maintain the authoritative document and index, including retiring replaced documents, without rewriting `AGENTS.md` each time.

Document index mechanics and example: [Document Discovery](document-discovery.md).

## 4. System checks and delivery

The agent handles ordinary checks and affected-module analysis directly. When integration traceability or versioned delivery warrants it:

```text
$engineering-governance verify
$engineering-governance release
```

Verification should compare the product against **effective confirmed requirements and design** as well as the actual code. Single-Git verification identifies one revision; multi-Git verification identifies exact revisions of all included repositories.

## 5. Project rules remain independent

`AGENTS.md` also mentions only the `.agents/rules/` directory. It is not created during bootstrap. A confirmed, repeated agent mistake may lead to `$project-bootstrap add-rule` with approval. Individual rule updates and any optional rule index stay inside the rules directory.
