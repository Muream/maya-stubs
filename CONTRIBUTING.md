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
The Project contains a few different sub-projects:

- `maya-stubgen` is the library that generates the stubs.
  the most interesting bits are tucked under `maya_stubgen/cli/generate_stubs/docspec_parser` where you'll find:
    - `docspec_from_builtin.py`: This module generates a `docspec.Module` for any python module.
      Since it works with introspection, it is able work with builtin modules.
      This is the fallback if any of the other parsers fail.
    - `docspec_from_cmds`: This package generates a `docspec.Module` for `maya.cmds` specifically.
      It contains two different parsers:
        - `html_parser.py`: which parses the html documentation 
          This parser is generally able to get pretty accurate stubs including return types, flag types, docstrings and examples.
        - `synopsis_parser.py`: which parses the result of `cmds.help("MyCommand")`.
          This parser generally will only produce accurate flag types but has the benefit of working for _all_ commands available in the maya session. 
          Including plug-in commands which are not on the HTML docs and generally not included in other stubs.
    - `docspec_from_api1`: Doesn't exist yet but this is where the dedicate API 1.0 parser will live
    - `docspec_from_api2`: Doesn't exist yet but this is where the dedicate API 2.0 parser will live
- `docspec-to-jinja`: This library converts the docspec objects to `pyi` and `md` files through jinja2 templates (it is a dependency of `maya-stubgen`)
- `maya-docs` kinda deprecated, this is a project that contains generated documentation from the maya-stubgen docspec
- `maya-stubs` is where the stubs are stored.
    All of the content of this project is meant to be automatically generated.
    This project is compatible with python >3.7 so it can be installed in projects using any of these python versions.
    This is the project that actually gets pushed to pypi.

## Generating the stubs

### Prerequisites

- [Poetry](https://python-poetry.org/)
- Maya 2023 or 2024

### Generate the stubs

- Tell poetry to use `mayapy` using `poetry env use`; the path to use depends on your OS, see examples for Maya 2024 using default install paths below:
    - Linux:
      ```sh
      poetry env use /usr/autodesk/maya2024/bin/mayapy
      ```
    - macOS:
      ```sh
      # mayapy cannot be used directly, use the framework distribution instead
      poetry env use /Applications/Autodesk/maya2024/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3
      ```
    - Windows:
      ```bat
      :: we have to create an alias for mayapy.exe for it to work with venv
      cd "C:\Program Files\Autodesk\Maya2024\bin"
      mklink python.exe mayapy.exe
      :: then use the alias as the base interpreter for poetry
      cd C:\path\to\maya-stubs
      poetry env use "C:\Program Files\Autodesk\Maya2024\bin\python.exe"
      ```
- Run `poetry install`.
    - If you want to generate stubs for another Maya version, simply select the correct `mayapy` using `poetry env use` again, and rerun `poetry install`.
- Generate the stubs with `poetry run generate-stubs generate-stubs`.
    - After the first run, you can re-use the docspec cache with `poetry run generate-stubs generate-stubs --reuse-cache`.
    - You can generate stubs for specific modules or members by specifying the `-m/--module` and/or `--members` options:
      ```
      poetry run generate-stubs generate-stubs -m maya.cmds --members "(currentTime|playblast)$"
      ```
      This will only create stubs for the `currentTime` and `playblast` Python commands; useful for quickly testing changes.
