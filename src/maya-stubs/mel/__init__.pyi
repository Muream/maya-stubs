from __future__ import annotations

from typing import *

Unknown = Any

def createMelWrapper(
    fn: Unknown,
    types: List[Any] = [],
    retType: str = "void",
    ignoreDefaultArgs: bool = True,
    returnCmd: bool = False,
    outDir: Unknown = None,
) -> Any:
    """@brief Create a wrapper mel proc for a python function

    When the mel proc is invoked, it will call the python function,
    passing any arguments it receives, and then return the function's
    result.

    Example:
        - I need a mel proc with signature: proc string[] fn(int $a, string $b)
        - I've created a python function to do the work in 'mymod.py' which looks like:
        - def fn(a,b): return [b]*a
        python>> import mymod
        python>> maya.mel.createMelWrapper(mymod.fn,types=['int','string'], retType='string[]')
        # Result: /users/username/maya/scripts/fn.mel #
        mel>> rehash;
        mel>> string $as[] = fn(3,"a");
        // Result: a a a //

    @param fn the function to wrap, must be a function.
    @param types string list of mel argument types to use,
    defaults to all 'string'.
    @param retType mel return type of the function, must be convertible to
    what fn actually returns. None means return type is 'void'.
    @param ignoreDefaultArgs  True means arguments with default values will be
    ignored when creating the mel wrapper proc.
    @param returnCmd True means return the generated mel code that defines the
    wrapper proc, False means write it to a mel file.
    @param outDir The directory to write the generated file to.  None means
    prompt for the directory.
    @return path to generated mel proc OR generated mel code, depending on
    returnCmd.
    """

def eval(*args: Unknown, **kwargs: Unknown) -> Any:
    """Takes as input a string containing MEL code, evaluates it, and returns the result.

    This function takes a string which contains MEL code and evaluates it using
    the MEL interpreter. The result is converted into a Python data type and is
    returned.

    If an error occurs during the execution of the MEL script, a Python exception
    is raised with the appropriate error message.
    """
