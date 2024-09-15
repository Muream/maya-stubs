from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def workspacePanel(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., defineTemplate: str = ..., exists: bool = ..., mainWindow: bool = ..., useTemplate: str = ...) -> Union[str, bool]:
    """Workspace panel.
    Args:
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        mainWindow (bool?): Main window for the application.  The main window  
                has an 'Exit' item in the Window Manager menu.  By default, the  
                first created window becomes the main window.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: Full path name to the workspace panel.

    Example:
    """

