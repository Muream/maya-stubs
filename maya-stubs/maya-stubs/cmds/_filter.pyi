from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filter(*args: Any, edit: bool = ..., query: bool = ..., name: Queryable[str] = ..., type: Queryable[str] = ...) -> str:
    """Creates or modifies a filter node.  Filter nodes are used by applyTake
    to modify recorded device data before assigning it to the param curves
    for the attached attributes.
    Args:
        name (Queryable[str]?): Name for created filter  
                Properties: create, query, edit
        type (Queryable[str]?): Filter type to create, One of:  
              
                filterEuler            Euler angle "demangler"  
                filterResample          
                Resamples input data at fixed output rate with several filtering options  
                filterSimplify          
                Combines groups of data points that are almost linear into lines segments  
                filterClosestSample      
                Resamples input data a fixed output rate using the closest sample point  
                Properties: create, query, edit

    Returns:
        str: filter name

    Example:
    """

