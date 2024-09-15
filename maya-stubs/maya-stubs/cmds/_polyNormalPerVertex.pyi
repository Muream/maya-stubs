from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyNormalPerVertex(*args: str, edit: bool = ..., query: bool = ..., allLocked: bool = ..., deformable: bool = ..., freezeNormal: bool = ..., normalX: Queryable[float] = ..., normalXYZ: Queryable[Multiuse[Tuple[float, float, float]]] = ..., normalY: Queryable[float] = ..., normalZ: Queryable[float] = ..., relative: bool = ..., unFreezeNormal: bool = ...) -> Union[bool, float, Multiuse[Tuple[float, float, float]]]:
    """Command associates normal(x, y, z) with vertices on polygonal objects.
    When used with the query flag, it returns the normal associated with the
    specified components. However, when queried, the command returns all
    normals (all vtx-face combinations) on the vertex, regardless of whether
    they are shared or not.poly, userNormals, polyNormals, setNormal, vertexNormal, vertex
    Args:
        allLocked (bool?): Queries if all normals on the selected vertices are locked (frozen) or not  
                Properties: create, query, edit
        deformable (bool?): DEFAULT  true  
                OBSOLETE flag. This flag will be removed in the next release.  
                Properties: create, query, edit
        freezeNormal (bool?): Specifies that the normal values be frozen (locked) at the current value.  
                Properties: create, query, edit
        normalX (Queryable[float]?): Specifies the x value normal  
                Properties: create, query, edit
        normalXYZ (Queryable[Multiuse[Tuple[float, float, float]]]?): Specifies the xyz values normal  
                If this flag is used singly, the specified normal xyz values are  
                used for all selected components.  
                If the flag is used multiple times, the number of uses must match  
                the number of selected components, and each use specifies  
                the normal of one component.  
                Properties: create, query, edit, multiuse
        normalY (Queryable[float]?): Specifies the y value normal  
                Properties: create, query, edit
        normalZ (Queryable[float]?): Specifies the z value normal  
                Properties: create, query, edit
        relative (bool?): When used, the normal values specified are added relative to the current value.  
                Properties: create, query, edit
        unFreezeNormal (bool?): Specifies that the normal values that were frozen at the current value be  
                un-frozen (un-locked).  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

