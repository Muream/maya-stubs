from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listInputDevices(*args: Any, free: bool = ..., primary: bool = ..., secondary: bool = ...) -> List[str]:
    """This command lists all input devices that maya knows about.
    Args:
        free (bool?): List the free devices  
                Properties: create
        primary (bool?): List the primary devices  
                Properties: create
        secondary (bool?): List the secondary devices  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

