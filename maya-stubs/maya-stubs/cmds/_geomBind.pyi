from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def geomBind(*args: str, edit: bool = ..., query: bool = ..., bindMethod: int = ..., falloff: Queryable[float] = ..., geodesicVoxelParams: Queryable[Tuple[int, bool]] = ..., maxInfluences: Queryable[int] = ...) -> Union[bool, float, Tuple[int, bool], int]:
    """This command is used to compute weights using geodesic voxel binding algorithm.
    It works by setting the right weights values on an already-existing skinCluster
    node.
    Since this command uses GPU acceleration, it is not supported on headless
    versions of Maya, i.e. batch mode.skinCluster
    Args:
        bindMethod (int?): Specifies which bind algorithm to use. By default, Geodesic Voxel will be used.  
                Available algorithms are:  
                3. Geodesic Voxel  
                Properties: create
        falloff (Queryable[float]?): Falloff controlling the bind stiffness. Valid values range from [0..1].  
                Properties: create, query, edit
        geodesicVoxelParams (Queryable[Tuple[int, bool]]?): Specifies the geodesic voxel binding parameters. This flag is composed of three  
                parameters:  
                0. Maximum voxel grid resolution which must be a power of two. (ie. 64, 128, 256, etc. )  
                1. Performs a post voxel state validation when enabled.  
                Default values are 256 true.  
                Properties: create, query, edit
        maxInfluences (Queryable[int]?): Specifies the maximum influences a vertex can have. By default, all influences  
                are used (-1).  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

