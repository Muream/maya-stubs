from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyAverageNormal(*args: str, allowZeroNormal: bool = ..., distance: float = ..., postnormalize: bool = ..., prenormalize: bool = ..., replaceNormalXYZ: Tuple[float, float, float] = ...) -> str:
    """Set normals of vertices or vertex-faces to an average value when the vertices
    within a given threshold.
    First, it sorts out the containing edges, and set them to be soft, if it is
    possible, so to let the normals appear to be "merged". The remained components
    then are sorted into lumps where vertices in each lump are within the given
    threshold. For all vertices and vertex-faces, set their normals to the average
    normal in the lump.
    Selected vertices may or may not on the same object.
    If objects are selected, it is assumed that all vertices are selected.
    If edges or faces are selected, it is assumed that the related vertex-faces
    are selected.poly, userNormals, polyNormals, averageNormal, setNormal, vertexNormal
    Args:
        allowZeroNormal (bool?): Specifies whether to allow zero normals to be created.  
                By default it is false. If it is false, replaceNormal is needed.  
                Properties: create
        distance (float?): Specifies the distance threshold. All vertices within  
                the threshold are considered when computing an average  
                normal. By default it is 0.0.  
                Properties: create
        postnormalize (bool?): Specifies whether to normalize the resulting normals.  
                By default it is true.  
                Properties: create
        prenormalize (bool?): Specifies whether to normalize the normals before averaging.  
                By default it is true.  
                Properties: create
        replaceNormalXYZ (Tuple[float, float, float]?): If the allowZeroNormal is false, this value is used to  
                replace the zero normals. By default it is (1, 0, 0).  
                Properties: create

    Returns:
        str: of the node name.

    Example:
    """

