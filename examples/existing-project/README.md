# Existing project — example adoption

Suppose a legacy industrial device project contains one Git root with `Firmware/`, `PC/`, `Protocol/` and `Hardware/` folders, but its documentation is outdated.

```text
$project-bootstrap
```

The agent first inspects actual source, project/build configuration, protocol definitions, hardware constraints and available verification. It records the present baseline with concrete evidence.

Then it creates/updates project documents, using existing authoritative equivalents or (if no convention exists):

```text
docs/requirements.md
docs/technical-constraints.md
```

Examples of the distinction:

- **Observed in code:** the current register table declares a temperature setpoint field (cite the real file). This is evidence of *existing behavior*.
- **Confirmed requirement:** the setpoint must be configurable over Modbus only if an approved requirement, interface contract, standard or user confirms it; otherwise mark it *pending confirmation*.
- **Technical constraint:** a particular MCU, interface or toolchain is configured in the real project files (cite them). Explain whether it is a proven current-system constraint or an approved target for future changes.

The agent continues directly once relevant decisions are established. No extra execution workflow is invoked, and no project rule directory is created unless an approved rule is actually needed.
