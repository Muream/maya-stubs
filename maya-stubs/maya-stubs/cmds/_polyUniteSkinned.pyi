from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyUniteSkinned(*args: str, edit: bool = ..., query: bool = ..., centerPivot: bool = ..., constructionHistory: bool = ..., mergeUVSets: Queryable[int] = ..., objectPivot: bool = ...) -> Union[bool, int]:
    """Command to combine poly mesh objects (as polyUnite)
    while retaining the smooth skinning setup on the
    combined object.skinCluster, poly
    Args:
        centerPivot (bool?): Set the resulting object's pivot to the center of the selected objects bounding box.  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create, query, edit
        mergeUVSets (Queryable[int]?): Specify how UV sets will be merged on the output mesh.  
                The choices are 0 | 1 | 2.  
                0 = Do not merge. Each UV set on each mesh will become a new UV set in the output.  
                1 = Merge by name. UV sets with the same name will be merged.  
                2 = Merge by UV links. UV sets will be merged so that UV linking on the input meshes continues to work.  
                The default is 1 (merge by name).  
                Properties: create, query, edit
        objectPivot (bool?): Set the resulting object's pivot to last selected object's pivot.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

