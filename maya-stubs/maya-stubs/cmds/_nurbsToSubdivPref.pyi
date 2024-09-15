from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsToSubdivPref(*, query: bool = ..., bridge: Queryable[int] = ..., capType: Queryable[int] = ..., collapsePoles: bool = ..., matchPeriodic: bool = ..., maxPolyCount: Queryable[int] = ..., offset: Queryable[float] = ..., reverseNormal: bool = ..., solidType: Queryable[int] = ..., trans00: Queryable[float] = ..., trans01: Queryable[float] = ..., trans02: Queryable[float] = ..., trans10: Queryable[float] = ..., trans11: Queryable[float] = ..., trans12: Queryable[float] = ..., trans20: Queryable[float] = ..., trans21: Queryable[float] = ..., trans22: Queryable[float] = ..., trans30: Queryable[float] = ..., trans31: Queryable[float] = ..., trans32: Queryable[float] = ...) -> Union[bool, int, float]:
    """This command sets the values used by the nurbs-to-subdivision surface
    preference.  This preference is used by the nurbs creation commands
    and is saved between Maya sessions.To query any of the flags, use the "-query" flag.For more information on the flags, see the node documentation for
    the "nurbsToSubdivProc" node.
    Args:
        bridge (Queryable[int]?): Valid values are 0, 1, 2 or 3.  
                Properties: create, query
        capType (Queryable[int]?): Valid values are 0 or 1.  
                Properties: create, query
        collapsePoles (bool?):   
                Properties: create, query
        matchPeriodic (bool?):   
                Properties: create, query
        maxPolyCount (Queryable[int]?):   
                Properties: create, query
        offset (Queryable[float]?):   
                Properties: create, query
        reverseNormal (bool?):   
                Properties: create, query
        solidType (Queryable[int]?): Valid values are 0, 1 or 2.  
                Properties: create, query
        trans00 (Queryable[float]?):   
                Properties: create, query
        trans01 (Queryable[float]?):   
                Properties: create, query
        trans02 (Queryable[float]?):   
                Properties: create, query
        trans10 (Queryable[float]?):   
                Properties: create, query
        trans11 (Queryable[float]?):   
                Properties: create, query
        trans12 (Queryable[float]?):   
                Properties: create, query
        trans20 (Queryable[float]?):   
                Properties: create, query
        trans21 (Queryable[float]?):   
                Properties: create, query
        trans22 (Queryable[float]?):   
                Properties: create, query
        trans30 (Queryable[float]?):   
                Properties: create, query
        trans31 (Queryable[float]?):   
                Properties: create, query
        trans32 (Queryable[float]?):   
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

