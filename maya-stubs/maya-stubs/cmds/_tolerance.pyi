from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def tolerance(*, query: bool = ..., angular: Queryable[float] = ..., linear: Queryable[float] = ...) -> Union[bool, float]:
    """This command sets tolerances used by modelling operations
    that require a tolerance, such as surface fillet.
    Linear tolerance is also known as "positional" tolerance.
    Angular tolerance is also known as "tangential" tolerance.
    Args:
        angular (Queryable[float]?): Sets the angular, or "tangential" tolerance.  
                Properties: create, query
        linear (Queryable[float]?): Sets the linear, or "positonal" tolerance.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

