from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def distanceDimension(*args: str, endPoint: Tuple[float, float, float] = ..., startPoint: Tuple[float, float, float] = ...) -> str:
    """This command is used to create a distance dimension to display the
    distance between two specified points.
    Args:
        endPoint (Tuple[float, float, float]?): Specifies the point to measure distance to, from the startPoint.  
                Properties: create
        startPoint (Tuple[float, float, float]?): Specifies the point to start measuring distance from.  
                Properties: create

    Returns:
        str: - the shape name of the DAG node created.

    Example:
    """

