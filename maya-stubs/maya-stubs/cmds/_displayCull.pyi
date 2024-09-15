from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayCull(*args: str, query: bool = ..., backFaceCulling: bool = ...) -> bool:
    """This command is responsible for setting the display culling
    property of back faces of surfaces.
    Args:
        backFaceCulling (bool?): Enable/disable culling of back faces.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

