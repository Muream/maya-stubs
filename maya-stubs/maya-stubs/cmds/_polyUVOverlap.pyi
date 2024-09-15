from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyUVOverlap(*args: str, nonOverlappingComponents: bool = ..., overlappingComponents: bool = ...) -> List[str]:
    """Return the required result on the specified components.If no objects are specified in the command line, then components from selection list will be used.
    Args:
        nonOverlappingComponents (bool?): Return non-overlapping components based on selected/specified components  
                Properties: create
        overlappingComponents (bool?): Return overlapping components based on selected/specified components  
                Properties: create

    Returns:
        List[str]: List of poly components

    Example:
    """

