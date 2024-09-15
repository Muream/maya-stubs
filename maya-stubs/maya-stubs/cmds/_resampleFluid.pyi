from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def resampleFluid(*args: str, edit: bool = ..., query: bool = ..., resampleDepth: Queryable[int] = ..., resampleHeight: Queryable[int] = ..., resampleWidth: Queryable[int] = ...) -> Union[bool, int]:
    """A command to extend the fluid grid, keeping the voxels the same size,
    and keeping the existing contents of the fluid in the same place. Note
    that the fluid transform is also modified to make this possible.fluid
    Args:
        resampleDepth (Queryable[int]?): Change depth resolution to this value  
                Properties: create, query, edit
        resampleHeight (Queryable[int]?): Change height resolution to this value  
                Properties: create, query, edit
        resampleWidth (Queryable[int]?): Change width resolution to this value  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

