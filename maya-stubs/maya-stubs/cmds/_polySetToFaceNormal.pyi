from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySetToFaceNormal(*args: str, setUserNormal: bool = ...) -> str:
    """This command takes selected polygonal vertices or vertex-faces and changes
    their normals. If the optionis used, the new normal
    values will be the face normals arround the vertices/vertex-faces. Otherwise
    the new normal values will be default values according to the internal
    calculation.poly, userNormal, polyNormals, setToFaceNormal, setNormal, vertexNormal
    Args:
        setUserNormal (bool?): when this flag is presented, user normals will be created on each vertex  
                face and the values will be the face normal value. Otherwise the normal  
                values will be the internal computing results. Default is false.  
                Properties: create

    Returns:
        str: of the node name

    Example:
    """

