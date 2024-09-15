from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def preferredRenderer(arg0: str = ..., /, *, query: bool = ..., fallback: Queryable[str] = ..., makeCurrent: bool = ...) -> Union[bool, str]:
    """Command to set the preferred renderer. This command can be used
    to query the preferred renderer and to set the current renderer
    as the preferred one. It also allows users to specify a
    preferred fallback renderer.renderer
    Args:
        fallback (Queryable[str]?): Sets the preferred fallback renderer.  
                Properties: create, query
        makeCurrent (bool?): Sets the current renderer as the preferred one.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

