from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def surfaceShaderList(*args: str, edit: bool = ..., query: bool = ..., add: str = ..., remove: str = ...) -> bool:
    """Add/Remove a relationship between an object and the
    current shading group.
    Args:
        add (str?): add object(s) to shader group list.  
                Properties: create
        remove (str?): remove object(s) to shader group list.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

