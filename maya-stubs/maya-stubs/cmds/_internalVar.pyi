from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def internalVar(*, mayaInstallDir: bool = ..., userAppDir: bool = ..., userBitmapsDir: bool = ..., userHotkeyDir: bool = ..., userMarkingMenuDir: bool = ..., userPrefDir: bool = ..., userPresetsDir: bool = ..., userScriptDir: bool = ..., userShelfDir: bool = ..., userTmpDir: bool = ..., userWorkspaceDir: bool = ...) -> str:
    """This command returns the values of internal variables.  No modification
    of these variables is supported.
    Args:
        mayaInstallDir (bool?): Return the Maya installation directory.  
                Properties: create
        userAppDir (bool?): Return the user application directory.  
                Properties: create
        userBitmapsDir (bool?): Return the user bitmaps prefs directory.  
                Properties: create
        userHotkeyDir (bool?): Return the user hotkey directory.  
                Properties: create
        userMarkingMenuDir (bool?): Return the user marking menu directory.  
                Properties: create
        userPrefDir (bool?): Return the user preference directory.  
                Properties: create
        userPresetsDir (bool?): Return the user presets directory.  
                Properties: create
        userScriptDir (bool?): Return the user script directory.  
                Properties: create
        userShelfDir (bool?): Return the user shelves directory.  
                Properties: create
        userTmpDir (bool?): Return a temp directory.  Will check for TMPDIR environment variable,  
                otherwise will return the current directory.  
                Properties: create
        userWorkspaceDir (bool?): Return the user workspace directory  
                (also known as the projects directory).  
                Properties: create

    Returns:
        str: The value of the variable specified by the flag use.

    Example:
    """

