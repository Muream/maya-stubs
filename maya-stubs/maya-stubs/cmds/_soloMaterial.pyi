from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def soloMaterial(*args: Any, query: bool = ..., attr: Queryable[str] = ..., last: bool = ..., node: Queryable[str] = ..., unsolo: bool = ...) -> Union[bool, str]:
    """Shows a preview of a specified material node output attribute.solo, material, rendering, shaders
    Args:
        attr (Queryable[str]?): The attr flag specifies a node attribute to solo.  
                Properties: create, query
        last (bool?): Whether to solo the last material node and attribute.  
                Properties: create, query
        node (Queryable[str]?): The node flag specifies the node to solo.  
                Properties: create, query
        unsolo (bool?): Whether to remove soloing.  
                Properties: create, query

    Returns:
        bool: Success or Failure

    Example:
    """

