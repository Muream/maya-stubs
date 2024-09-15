from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fluidVoxelInfo(*args: str, checkBounds: bool = ..., inBounds: Tuple[int, int, int] = ..., objectSpace: bool = ..., radius: float = ..., voxel: Tuple[float, float, float] = ..., voxelCenter: bool = ..., xIndex: int = ..., yIndex: int = ..., zIndex: int = ...) -> bool:
    """Provides basic information about the mapping of a fluid voxel grid into world- or object space of the fluid.  Use this command to determine the center point of a voxel, or to find the voxel containing a given point, among other things.fluid
    Args:
        checkBounds (bool?): If this flag is on, and the voxel index of a point that is out of bounds is requested,  
                then we return nothing.  
                Properties: create
        inBounds (Tuple[int, int, int]?): Are the three ints representing the x, y, z indices of a voxel within the bounds of the fluid's voxel grid?  True if yes, false if not.  (For 2D fluids, pass in z=0 for the third argument.  See examples.)  
                Properties: create
        objectSpace (bool?): Whether the queried value should be returned in object space (TRUE),  
                or world space (FALSE, the default).  
                Properties: create
        radius (float?): Modifier for the -voxel flag.  Returns a list of  
                index triples identifying voxels that fall within  
                the given radius of the point specified by the  
                -voxel flag.  
                Properties: create
        voxel (Tuple[float, float, float]?): Returns array of three ints representing the x, y, z indices of the voxel within which the given point position is contained.  
                If the checkBounds flag is on, and the point is out of bounds, we return nothing. Otherwise, even if the point is out of bounds, index values are returned.  
                When combined with the -radius flag, returns an array of index triples  
                representing a list of voxels within a given radius of the given point position.  
                Properties: create
        voxelCenter (bool?): The center position of the specified voxels.  Returns an array of floats (three for each of the indices in the query).  (Valid only with the -xIndex, -yIndex, and -zIndex flags.)  
                Properties: create
        xIndex (int?): Only return values for cells with this X index  
                Properties: create
        yIndex (int?): Only return values for cells with this Y index  
                Properties: create
        zIndex (int?): Only return values for cells with this Z index  
                Properties: create

    Returns:
        bool:

    Example:
    """

