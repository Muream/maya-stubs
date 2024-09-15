from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def reorderContainer(*args: str, edit: bool = ..., query: bool = ..., back: bool = ..., front: bool = ..., relative: Queryable[int] = ...) -> Union[bool, int]:
    """This command reorders (moves) objects relative to their siblings in
    a container.For relative moves, both positive and negative numbers may be
    specified.  Positive numbers move the object forward and
    negative numbers move the object backward amoung its
    siblings. When an object is at the end (beginning) of the list
    of siblings, a relative move of 1 (-1) will put the object at
    the beginning (end) of the list of siblings.  That is,
    relative moves will wrap if necessary.Only nodes within one container can be moved at a time.
    Note: The container command's -nodeList flag will return a sorted list of
    contained nodes. To see the effects of reordering, use the -unsortedOrder flag
    in conjunction with the -nodeList flag.node, container, reorder
    Args:
        back (bool?): Move object(s) to back of container contents list  
                Properties: create, query, edit
        front (bool?): Move object(s) to front of container contents list  
                Properties: create, query, edit
        relative (Queryable[int]?): Move object(s) relative to other container contents  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

