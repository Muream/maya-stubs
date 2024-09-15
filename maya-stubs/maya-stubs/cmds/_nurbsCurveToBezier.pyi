from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsCurveToBezier() -> List[str]:
    """The nurbsCurveToBezier command attempts to convert an existing NURBS curve
    to a Bezier curve.
    Returns:
        List[str]: (object name and node name)

    Example:
    """

