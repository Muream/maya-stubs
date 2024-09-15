from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ctxTraverse(*, down: bool = ..., left: bool = ..., right: bool = ..., up: bool = ...) -> bool:
    """This command tells the current context to do a traversal.Some contexts will ignore this command. Individual contexts
    determine what up/down left/right mean.
    Args:
        down (bool?): Move "down" as defined by the current context.  
                Properties: create
        left (bool?): Move "left" as defined by the current context.  
                Properties: create
        right (bool?): Move "right" as defined by the current context.  
                Properties: create
        up (bool?): Move "up" as defined by the current context.  
                Properties: create

    Returns:
        bool:

    Example:
    """

