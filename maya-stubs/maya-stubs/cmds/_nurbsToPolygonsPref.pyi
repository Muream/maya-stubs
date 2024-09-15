from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsToPolygonsPref(*, query: bool = ..., chordHeight: Queryable[float] = ..., chordHeightRatio: Queryable[float] = ..., delta3D: Queryable[float] = ..., edgeSwap: bool = ..., format: Queryable[int] = ..., fraction: Queryable[float] = ..., matchRenderTessellation: Queryable[int] = ..., merge: Queryable[int] = ..., mergeTolerance: Queryable[float] = ..., minEdgeLen: Queryable[float] = ..., polyCount: Queryable[int] = ..., polyType: Queryable[int] = ..., uNumber: Queryable[int] = ..., uType: Queryable[int] = ..., useChordHeight: bool = ..., useChordHeightRatio: bool = ..., vNumber: Queryable[int] = ..., vType: Queryable[int] = ...) -> Union[bool, float, int]:
    """This command sets the values used by the nurbs-to-polygons
    (or "tesselate") preference.  This preference is used by
    Maya menu items and is saved between Maya sessions.
    To query any of the flags, use the "-query" flag.
    For more information on the flags, see the node documentation for
    the "nurbsTessellate" node.
    Args:
        chordHeight (Queryable[float]?):   
                Properties: create, query
        chordHeightRatio (Queryable[float]?):   
                Properties: create, query
        delta3D (Queryable[float]?):   
                Properties: create, query
        edgeSwap (bool?):   
                Properties: create, query
        format (Queryable[int]?): Valid values are 0, 1 and 2.  
                Properties: create, query
        fraction (Queryable[float]?):   
                Properties: create, query
        matchRenderTessellation (Queryable[int]?):   
                Properties: create, query
        merge (Queryable[int]?):   
                Properties: create, query
        mergeTolerance (Queryable[float]?):   
                Properties: create, query
        minEdgeLen (Queryable[float]?):   
                Properties: create, query
        polyCount (Queryable[int]?):   
                Properties: create, query
        polyType (Queryable[int]?):   
                Properties: create, query
        uNumber (Queryable[int]?):   
                Properties: create, query
        uType (Queryable[int]?):   
                Properties: create, query
        useChordHeight (bool?):   
                Properties: create, query
        useChordHeightRatio (bool?):   
                Properties: create, query
        vNumber (Queryable[int]?):   
                Properties: create, query
        vType (Queryable[int]?):   
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

