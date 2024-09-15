from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def stroke(*, name: str = ..., pressure: bool = ..., seed: int = ...) -> str:
    """The stroke command creates a new Paint Effects stroke node.
    Args:
        name (str?): Sets the name of the stroke to the input string  
                Properties: create
        pressure (bool?): On creation, allows the copying of the pressure  
                mapping settings from the Paint Effects Tool. Default  
                is false.  
                Properties: create
        seed (int?): Sets the random seed for this stroke.  
                Properties: create

    Returns:
        str: (The path to the new stroke or the replaced stroke)

    Example:
    """

