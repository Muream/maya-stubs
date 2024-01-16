# Maya Stubs

Type Annotated Stubs for Autodesk Maya's python APIs

## Goals

Provide fully type annotated stubs for maya.cmds and OpenMaya 1.0 & 2.0


## Status

Note that is very much in progress and it is unlikely that the stubs will ever be perfect.  
At this point, even if some of the `maya.cmds` annotations are wrong/misleading, I would consider it a better experience than using the stubs from the devkit.
The stubs from OpenMaya 1.0 and 2.0 are very minimal and only have `*args, **kwargs` signatures, which should be pretty close to the devkit stubs.

- 🚧 maya.cmds: In Progress
  - [x] Stubs for all commands.
  - [x] Accurate Arguments signatures for most commands.
    Parsed from the HTML Docs or the synopsys from `cmds.help("command")`
  - [x] Accurate Positional Only Arguments for most command.
  - [x] Accurate Return types on most commands
  - [x] Docstrings.
  - [ ] Accurate Arguments signatures all commands.
  - [ ] Accurate Return types all most commands
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


## Installation

You can get the stubs with one of two ways:

1. Run `pip install maya-stubs` from the python executable used by your IDE.
2. Download them manually from the [Github releases](https://github.com/Muream/maya-stubs/releases) and let your IDE know of their location.

## Notes

### PyCharm maya.cmds completion

PyCharm users may not see code completion for `maya.cmds` as the editor limits code insight features by default on files over 2.5 MB for performance reasons. Currently the cmds stub is over this limit.

This value can be increased in [PyCharm's properties](https://www.jetbrains.com/help/pycharm/file-idea-properties.html), accessible via the `Help > Edit Custom Properties` menu.

Code completion should work after adding the line below to the properties file and restarting PyCharm. This example overrides the default value from 2.5 MB to 10 MB. The value may be customized as needed, but keep in mind it can affect editor performance.

```
idea.max.intellisense.filesize = 10000
```
