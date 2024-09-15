from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setFluidAttr(*args: str, addValue: bool = ..., attribute: str = ..., clear: bool = ..., floatRandom: float = ..., floatValue: float = ..., lowerFace: bool = ..., reset: bool = ..., vectorRandom: Tuple[float, float, float] = ..., vectorValue: Tuple[float, float, float] = ..., xIndex: int = ..., xvalue: bool = ..., yIndex: int = ..., yvalue: bool = ..., zIndex: int = ..., zvalue: bool = ...) -> bool:
    """Sets values of built-in fluid attributes such as density, velocity, etc.,
    for individual grid cells or for all cells in the grid.fluid
    Args:
        addValue (bool?): Add specified value to attribute
        attribute (str?): Specifies the fluid attribute for which to set values.  Valid  
                attributes are "velocity", "density", "fuel", "color", "falloff", and "temperature".  
                Properties: create
        clear (bool?): Set this attribute to 0
        floatRandom (float?): If this was a scalar (e.g. density) attribute, use a random value in +-VALUE  
                If fv is specified, it is used as the base value and combined with the  
                random value. If the fv flag is not specified, the  base is assumed to be 0.
        floatValue (float?): If this was a scalar (e.g. density) attribute, use this value
        lowerFace (bool?): Only valid with "-at velocity".  Since velocity values are stored on the edges  
                of each voxel and not at the center, using voxel based indices to set velocity  
                necessarily affects neighboring voxels.  Use this flag to only set velocity  
                components on the lower left three faces of a voxel, rather than all six.  
                Properties: create
        reset (bool?): Set this attribute to default value
        vectorRandom (Tuple[float, float, float]?): If this was a vector (e.g. velocity) attribute, use a random value in +-VALUE  
                If vv is specified, it is used as the base value and combined with the  
                random value. If the vv flag is not specified, the  base is assumed to be 0,0,0.
        vectorValue (Tuple[float, float, float]?): If this was a vector (e.g. velocity) attribute, use this value
        xIndex (int?): Only return values for cells with this X index  
                Properties: create
        xvalue (bool?): Only set the first component of the vector-valued attribute specified by  
                the "-at/attribute" flag.
        yIndex (int?): Only return values for cells with this Y index  
                Properties: create
        yvalue (bool?): Only set the second component of the vector-valued attribute specified by  
                the "-at/attribute" flag.
        zIndex (int?): Only return values for cells with this Z index  
                Properties: create
        zvalue (bool?): Only set the third component of the vector-valued attribute specified by  
                the "-at/attribute" flag.

    Returns:
        bool:

    Example:
    """

