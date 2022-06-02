# Maya Stubs
Stubs for Autodesk Maya

The goal of this is to get as fully typed stubs for all maya APIs.
This is not a small feat so the stubs will improve over time.

# Usage
You can get the stubs with one of two ways:
1. Download them manually from the [Github releases](https://github.com/Muream/maya-stubs/releases) and let your IDE know of their location.
2. Run `pip install maya-stubs` from the python executable used by your IDE.

# Status:
- 🚧 maya.cmds: Incomplete
    - [x] Stubs for all commands.
    - [x] Accurate Arguments signatures for most commands (parsed from `cmds.help("command")`).
    - [x] Implicit first argument(s) for most command.
    - [ ] Accurate Arguments signatures all commands.
    - [ ] Return Types.
    - [ ] Docstrings.
- 🚧 OpenMaya 1.0: Incomplete
    - [x] Stubs for all members
    - [ ] Accurate Argument Signatures
    - [ ] Return Types
    - [ ] Docstrings.
- 🚧 OpenMaya 2.0: Incomplete
    - [x] Stubs for all members
    - [ ] Accurate Argument Signatures
    - [ ] Return Types
    - [x] Docstrings.