# Contributing:
There are two ways into which you can contribute to this:
1. Improve the Generated Stubs.  
    See [Generating the stubs](#generating-the-stubs)
2. Manually provide signatures for some members.

## How to contribute
- Fork and clone the repo
- Do your thing
- Push to your Fork and submit a Pull Request


# Project structure
- `maya_stubgen` is the library that generates the stubs
- `maya-stubs` is where the stubs are stored.  
    It contains two kinds of stubs:
    - The generated ones, suffixed with `_generated`. Eg: `OpenMaya_generated.pyi`
    - The hand made ones, which are importing the generated ones.  
    You can re-define any member of the generated stubs in here to provide a better signature that can't be automatically generated properly.


# Generating the stubs
## Prerequisites
- [Poetry](https://python-poetry.org/)
- Python 3.9.7 (I recommend [pyenv](https://github.com/pyenv/pyenv) - or [pyenv-win](https://github.com/pyenv-win/pyenv-win) on Windows - to easily install multiple python versions)
- Maya 2023


## Generate the stubs
- Run `poetry install`.  
  Note: This will create a `.venv` virtualenv inside of the repository with all the development dependencies.
- Generate the stubs with `/path/to/mayapy -m maya_stubgen generate-stubs`.
  Note: This might fail the first time  as mayapy seems to struggle creating a new MAYA_APP_DIR the 
