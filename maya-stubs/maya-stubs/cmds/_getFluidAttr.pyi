from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getFluidAttr(*args: str, attribute: str = ..., lowerFace: bool = ..., xIndex: int = ..., xvalue: bool = ..., yIndex: int = ..., yvalue: bool = ..., zIndex: int = ..., zvalue: bool = ...) -> bool:
    """Returns values of built-in fluid attributes such as density,
    velocity, etc., for individual grid cells or for all cells in the grid.fluid
    Args:
        attribute (str?): Specifies the fluid attribute for which to display values.  Valid  
                attributes are "force", "velocity", "density", "falloff",  
                "fuel", "color", and "temperature".  (Note that getting force values is an  
                alternate way of getting velocity values at one time step.)  
                Properties: create
        lowerFace (bool?): Only valid with "-at velocity".  Since velocity values are stored on the edges  
                of each voxel and not at the center, using voxel based indices to set velocity  
                necessarily affects neighboring voxels.  Use this flag to only set velocity  
                components on the lower left three faces of a voxel, rather than all six.  
                Properties: create
        xIndex (int?): Only return values for cells with this X index  
                Properties: create
        xvalue (bool?): Only get the first component of the vector-valued attribute specified by  
                the "-at/attribute" flag.
        yIndex (int?): Only return values for cells with this Y index  
                Properties: create
        yvalue (bool?): Only get the second component of the vector-valued attribute specified by  
                the "-at/attribute" flag.
        zIndex (int?): Only return values for cells with this Z index  
                Properties: create
        zvalue (bool?): Only get the third component of the vector-valued attribute specified by  
                the "-at/attribute" flag.

    Returns:
        bool:

    Example:
    """

