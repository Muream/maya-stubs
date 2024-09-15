from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def resourceManager(*, nameFilter: str = ..., saveAs: Tuple[str, str] = ...) -> bool:
    """List resources matching certain properties.resources, file
    Args:
        nameFilter (str?): List only resources matching the name. Argument may contain ? and *  
                characters.  
                Properties: create
        saveAs (Tuple[str, str]?): Saves a copy of the resource (first parameter) as a separate file (second parameter).  
                Properties: create

    Returns:
        bool:

    Example:
    """

