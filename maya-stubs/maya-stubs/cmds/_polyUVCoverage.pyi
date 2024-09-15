from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyUVCoverage(*args: str, uvRange: Tuple[float, float, float, float] = ...) -> List[float]:
    """Return the UV space coverage of the specified components.If no objects are specified in the command line, then components from selection list will be used.
    Args:
        uvRange (Tuple[float, float, float, float]?): UV space range for calculating the coverage  
                The 4 values specify the minimum U, V and maximum U, V in that order. Default is 0.0 0.0 1.0 1.0.  
                Properties: create

    Returns:
        List[float]: UV space coverage percentage

    Example:
    """

