from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def openCLInfo(*args: str, query: bool = ..., limitMinimumVerts: bool = ..., minVertexBuffer: Queryable[int] = ..., supportsDoublePrecision: bool = ..., valid: bool = ...) -> Union[bool, int]:
    """Query OpenCL information.OpenCL, debug
    Args:
        limitMinimumVerts (bool?): Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration  
                determines a certain minimum size for geometries to be allowed on GPU.  
                When this flag is on this limit is obeyed. When this flag is off this limit is ignored.  
                This is only used for debugging purposes and is not saved to the file or any preferences.  
                Properties: create, query
        minVertexBuffer (Queryable[int]?): Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network  
                with qualifying geometries).  
                This is only used for debugging purposes and is not saved to the file or any preferences.  
                Properties: create, query
        supportsDoublePrecision (bool?): Specifies whether double precision can be used in OpenCL. If the platform can not  
                allow double precision this can not be set to "on".  
                Properties: create, query
        valid (bool?): Valid in query mode only. Checks if OpenCL is initialized.  
                Properties: query

    Returns:
        bool: The state of whether OpenCL is initialized or not (with the 'valid' flag)

    Example:
    """

