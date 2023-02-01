from __future__ import annotations

from typing import *

Unknown = Any

def initialize(*args: Any, **kwargs: Any) -> Any:
    """This function initializes Maya within a standalone Python interpreter

    The Python modules that Maya exports (e.g. maya.cmds, maya.OpenMaya, etc.) may
    be used from a standalone Python interpreter.  However, it is necessary to 
    fully initialize Maya within the interpreter before calling any other Maya 
    Python functions.  This call performs that exact function

    This function should never be called from within a Maya process (GUI or batch).
    It should only be required when using an external Python interpreter.

    This function takes one optional argument:
    name - name of the application (defaults to 'python')
    """

def uninitialize(*args: Any, **kwargs: Any) -> Any:
    """This function uninitializes Maya within a standalone Python interpreter"""

