from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def affects(arg0: str = ..., /, *args: str, by: bool = ..., type: str = ...) -> str:
    """This command returns the list of attributes on a node or node type which
    affect the named attribute.attribute, node, class, dg
    Args:
        by (bool?): Show attributes that are affected by the given one rather than the  
                ones that affect it.  
                Properties: create
        type (str?): static node type from which to get 'affects' information  
                Properties: create

    Returns:
        str: List of affected/affecting attributes

    Example:
    """

