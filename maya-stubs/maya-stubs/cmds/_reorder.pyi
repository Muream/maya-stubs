from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def reorder(*args: str, back: bool = ..., front: bool = ..., relative: int = ...) -> bool:
    """This command reorders (moves) objects relative to their siblings.For relative moves, both positive and negative numbers may be
    specified.  Positive numbers move the object forward and
    negative numbers move the object backward amoung its
    siblings. When an object is at the end (beginning) of the list
    of siblings, a relative move of 1 (-1) will put the object at
    the beginning (end) of the list of siblings.  That is,
    relative moves will wrap if necessary.If a shape is specified and it is the only child then its parent
    will be reordered.
    Args:
        back (bool?): Move object(s) to back of sibling list.  
                Properties: create
        front (bool?): Move object(s) to front of sibling list.  
                Properties: create
        relative (int?): Move object(s) relative to other siblings.  
                Properties: create

    Returns:
        bool:

    Example:
    """

