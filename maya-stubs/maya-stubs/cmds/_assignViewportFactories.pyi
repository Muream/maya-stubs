from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def assignViewportFactories(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., materialFactory: Queryable[str] = ..., nodeType: Queryable[str] = ..., textureFactory: Queryable[str] = ...) -> Union[bool, str]:
    """Sets viewport factories for displays as materials or textures.assignViewportFactories, registration
    Args:
        materialFactory (Queryable[str]?): Set or query the materialFactory for the node type.  
                Properties: create, query, edit
        nodeType (Queryable[str]?): The node type.  
                Properties: create, query, edit
        textureFactory (Queryable[str]?): Set or query the textureFactory for the node type.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

