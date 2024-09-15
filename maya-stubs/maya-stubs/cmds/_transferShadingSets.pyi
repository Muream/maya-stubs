from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def transferShadingSets(*args: str, edit: bool = ..., query: bool = ..., sampleSpace: Queryable[int] = ..., searchMethod: Queryable[int] = ...) -> Union[bool, int]:
    """Command to transfer shading set assignments between meshes.
    The last mesh in the list receives the shading assignments from the other meshes.shading, sets
    Args:
        sampleSpace (Queryable[int]?): Selects which space the attribute transfer is performed in.  
                0 is world space, 1 is model space. The default is world space.  
                Properties: create, query, edit
        searchMethod (Queryable[int]?): Specifies which search method to use when correlating points.  
                0 is closest along normal, 3 is closest to point. The default is closest to point.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

