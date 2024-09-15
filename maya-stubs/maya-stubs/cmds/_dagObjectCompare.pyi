from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dagObjectCompare(*args: str, attribute: bool = ..., bail: str = ..., connection: bool = ..., namespace: str = ..., relative: bool = ..., short: bool = ..., type: bool = ...) -> bool:
    """dagObjectCompare can be used to compare to compare objects based on:dag, compare
    Args:
        attribute (bool?): Compare dag object attributes  
                Properties: create
        bail (str?): Bail on first error or bail on category. Legal values are  
                "never", "first", and "category".  
                Properties: create
        connection (bool?): Compare dag connections  
                Properties: create
        namespace (str?): The baseline namespace  
                Properties: create
        relative (bool?): dag relatives  
                Properties: create
        short (bool?): Compress output to short form (not as verbose)  
                Properties: create
        type (bool?): Compare based on dag object type  
                Properties: create

    Returns:
        bool:

    Example:
    """

