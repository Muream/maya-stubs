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

- Create a virtualenv with `uv` that uses mayapy as its base interpreter
  You should use the mayapy version for the stubs you want to generate.
    - Windows:
      Because of a (bug)[https://github.com/astral-sh/uv/issues/7521] in `uv` we can't use mayapy directly as the base interpreter for our virtualenv  
      ```bat
      :: we have to create an alias for mayapy.exe for it to work with venv
      cd "C:\Program Files\Autodesk\Maya2024\bin"
      mklink python.exe mayapy.exe
      :: then use the alias as the base interpreter for poetry
      cd C:\path\to\maya-stubs
      uv venv --python "C:\Program Files\Autodesk\Maya2024\bin\mayapy.exe"
      ```
    - Linux
      ```bash
      uv venv --python /usr/autodesk/maya2024/bin/mayapy
      ```
    - MacOS
      ```bash
      # mayapy cannot be used directly, use the framework distribution instead
      uv venv --python /Applications/Autodesk/maya2024/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3
      ```
    Note: I don't use Linux or MacOS so I can't say that this will work for sure.
- Generate the stubs with `uv run maya-stubgen generate-stubs src/maya-stubs`.
    - After the first run, you can re-use the docspec cache with `uv run maya-stubgen generate-stubs src/maya-stubs --reuse-cache`.
    - You can generate stubs for specific modules or members by specifying the `-m/--module` and/or `--members` options:
      ```
      uv run maya-stubgen generate-stubs src/maya-stubs -m maya.cmds --members "(currentTime|playblast)$"
      ```
      This will only create stubs for the `currentTime` and `playblast` Python commands; useful for quickly testing changes.
