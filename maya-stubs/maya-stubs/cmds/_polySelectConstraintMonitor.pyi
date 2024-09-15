from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySelectConstraintMonitor(*args: Any, changeCommand: Tuple[str, str] = ..., create: bool = ..., delete: bool = ...) -> bool:
    """Manage the window to display/edit the polygonal selection constraint
    parameters
    Args:
        changeCommand (Tuple[str, str]?): Specifies the mel callback to refresh the window. First argument is  
                the callback, second is the window name.  
                Properties: create
        create (bool?): Specifies the Monitor should be created  
                Properties: create
        delete (bool?): Specifies that the Monitor should be removed  
                Properties: create

    Returns:
        bool:

    Example:
    """

