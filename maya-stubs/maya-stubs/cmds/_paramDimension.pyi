from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def paramDimension(*args: str) -> str:
    """This command is used to create a param dimension to display the
    parameter value of a curve/surface at a specified point on the
    curve/surface.
    Returns:
        str: Name of the paramDimension shape node created

    Example:
    """

