from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def snapMode(*, query: bool = ..., curve: bool = ..., distanceIncrement: Queryable[float] = ..., edgeMagnet: Queryable[int] = ..., edgeMagnetTolerance: Queryable[float] = ..., grid: bool = ..., liveFaceCenter: bool = ..., livePoint: bool = ..., meshCenter: bool = ..., pixelCenter: bool = ..., pixelSnap: bool = ..., point: bool = ..., tolerance: Queryable[int] = ..., useTolerance: bool = ..., uvTolerance: Queryable[int] = ..., viewPlane: bool = ...) -> Union[bool, float, int]:
    """The snapMode command is used to control snapping.  It toggles the
    snapping modes in effect and sets information used for snapping.
    Args:
        curve (bool?): Set curve snap mode  
                Properties: create, query
        distanceIncrement (Queryable[float]?): Set the distance for the snapping to objects such as a lines or planes.  
                Properties: create, query
        edgeMagnet (Queryable[int]?): Number of extra magnets to snap onto, regularly spaced  
                along the edge.  
                Properties: create, query
        edgeMagnetTolerance (Queryable[float]?): Precision for edge magnet snapping.  
                Properties: create, query
        grid (bool?): Set grid snap mode  
                Properties: create, query
        liveFaceCenter (bool?): While moving on live polygon objects, snap to its  
                face centers.  
                Properties: create, query
        livePoint (bool?): While moving on live polygon objects, snap to its  
                vertices.  
                Properties: create, query
        meshCenter (bool?): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.  
                Properties: create, query
        pixelCenter (bool?): Snap UV to the center of the pixel instead of the corner.  
                Properties: create, query
        pixelSnap (bool?): Snap UVs to the nearest pixel center or corner.  
                Properties: create, query
        point (bool?): Set point snap mode  
                Properties: create, query
        tolerance (Queryable[int]?): Tolerance defines the size of the square region  
                in which points must lie in order to be snapped to. The  
                tolerance value is the distance from the cursor position  
                to the boundary of the square (in all four directions).  
                Properties: create, query
        useTolerance (bool?): If useTolerance is set, then point snapping  
                is limited to points that are within a square region  
                surrounding the cursor position. The size of the square  
                is determined by the tolerance value.  
                Properties: create, query
        uvTolerance (Queryable[int]?): uvTolerance defines the size of the square region  
                in which points must lie in order to be snapped to, in the  
                UV Editor.  The tolerance value is the distance  
                from the cursor position to the boundary of the square  
                (in all four directions).  
                Properties: create, query
        viewPlane (bool?): Set view-plane snap mode  
                Properties: create, query

    Returns:
        bool: if command is a query

    Example:
    """

