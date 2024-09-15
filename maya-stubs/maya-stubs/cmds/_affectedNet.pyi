from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def affectedNet(*args: str, edit: bool = ..., query: bool = ..., type: str = ...) -> bool:
    """This command gets the list of attributes on a node or node type and
    creates nodes of type TdnAffect, one for each attribute, that are
    connected iff the source node's attribute affects the destination node's
    attribute.
    Args:
        type (str?): Get information from the given node type instead of one node  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

