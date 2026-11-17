# Examples

- [Existing project bootstrap](existing-project/README.md): derive confirmed requirements and technical constraints after inspecting an actual codebase.
- [Release](release/README.md): single-Git vs multi-Git traceability.

The agent directly handles normal code changes, including related-module analysis. There is no separate impact-analysis Skill command.

`project-bootstrap` creates `.agents/rules/` only when adding an approved project rule; any rule index stays inside that directory.
