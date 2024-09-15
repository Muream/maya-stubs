from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def loadUI(*, listTypes: bool = ..., uiFile: str = ..., uiString: str = ..., verbose: bool = ..., workingDirectory: str = ...) -> str:
    """loadUI lets you generate a Maya user interface from a Qt user interface (.ui) file.
    While creating the interface, if a Qt widgetâ€™s class is recognized, and a Maya-equivalent exists,
    the Maya-equivalent widget will be used.
    Any dynamic widget properties starting with a â€˜-â€™ will be treated as a MEL key/value pair.
    Widget properties starting with a â€˜+â€™ will be treated as a Python key/value pair.
    Properties will be applied to the widget upon creation.
    For additional details about ui files, please refer to Qt docs.
    Args:
        listTypes (bool?): Returns the list of recognized UI types and their associated Maya command.  
                Properties: create
        uiFile (str?): Full path to a user interface file to load.  
                Properties: create
        uiString (str?): Load UI from a formated string.  
                Properties: create
        verbose (bool?): Extra information about created controls will be printed.  
                Properties: create
        workingDirectory (str?): Sets the working directory, the loader looks for resources  
                such as icons and resouce files in paths relative to this directory.  
                Properties: create

    Returns:
        str: Full path name to the root control.

    Example:
    """

