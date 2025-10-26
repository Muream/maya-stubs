# Contributing

There are two ways into which you can contribute to this:

1. Improve the Generated Stubs.
    See [Generating the stubs](#generating-the-stubs)
2. Manually provide signatures for some members.

## How to contribute

- Fork and clone the repo
- Do your thing
- Push to your Fork and submit a Pull Request

### Project structure
The project is setup as an `uv` workspace where:

- The root package is the actual package for the maya stubs (which are in `src/maya-stubs`)
  The stubs are automatically generated and should not be modified manually.

- the `packages` folder contains two different packages:
  - `maya-stubgen`: This is the library that generates the stubs
    - `cli.py` creates the command line interface for maya-stubgen
    - `stubgen.py` contains the functions used to generate the stubs
    - `parsers/` is where all the different parsers are.
      A "Parser" is a class that generates `Docspec` objects for a python module  
      Here are the different parsers:
        - `BuiltinParser`: "Parses" a builtin module by introspecting it at runtime.
        This does not give the best results but works on everything.
        This parser is used as a fallback when other parsers can't be used.
        - `MayaParser`: Does not actually parse anything but is in charge of calling the best parser for the different maya modules
        - `CmdsParser`: Just like `MayaParser` it is responsible to call the correct parser for each of the maya commands.
        - `CmdsSynopsisParser`: parses the result of `cmds.help("MyCommand")`.  
            This parser generally will only produce accurate flag types but has the benefit of working for _all_ commands available in the maya session. 
            Including plug-in commands which are not on the HTML docs and generally not included in other stubs.
        - `CmdsDocsParser`: Parses the html documentation of the maya commands
          This parser is generally able to get pretty accurate stubs including return types, flag types, docstrings and examples.
          It is the one used for most commands.
      Note: There is no dedicated parser for OpenMaya 1.0 and 2.0 yet.
      These are generated using the BuiltinParser.
  - `docspec-to-jinja` which is used by `maya-stubgen` to generate the stubs content from the docspec objects.


## Generating the stubs

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- Maya 2023 or above

### Generate the stubs

- (Optional) Set the environment variable `MAYA_LOCATION` to the maya install dir of the version you want to generate the stubs for.
  - Windows: `C:\Program Files\Autodesk\Maya2026`
  - macOS: `/Applications/Autodesk/maya2026`
  - Linux: `/usr/autodesk/maya2026`
  - If `MAYA_LOCATION` is not set, the tool will automatically search for Maya installations in the default platform-specific locations, preferring the newest version found (current year + 2 down to Maya 2023).
- Generate the stubs with `uv run maya-stubgen generate-stubs src/`.
- After the first run, you can re-use the docspec cache with `uv run maya-stubgen generate-stubs src/ --reuse-cache`.
    This is useful if you're not making any changes to the parsers but only to the code generation side of things.
- You can generate stubs for specific modules or members by specifying the `-m/--module` and/or `--members` options:
  ```
  uv run maya-stubgen generate-stubs src/ -m maya.cmds --members "(currentTime|playblast)$"
  ```
  This will only create stubs for the `currentTime` and `playblast` Python commands; useful for quickly testing changes.
