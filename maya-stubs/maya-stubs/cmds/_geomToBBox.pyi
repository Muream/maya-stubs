from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def geomToBBox(*args: str, bakeAnimation: bool = ..., combineMesh: bool = ..., endTime: int = ..., keepOriginal: bool = ..., name: str = ..., nameSuffix: str = ..., sampleBy: int = ..., shaderColor: Tuple[float, float, float] = ..., single: bool = ..., startTime: int = ...) -> bool:
    """Create polygonal mesh bounding boxes for geometry.
    Can also create a single bounding box per hierarchy.bounding, box
    Args:
        bakeAnimation (bool?): Bake the animation. Can be used with startTime, endTime and sampleBy flags.  
                If used alone, the time slider will be used to specify the startTime and endTime.  
                Properties: create
        combineMesh (bool?): Combine resulting bounding boxes.  
                Mutually exclusive with -s/single option.  
                Properties: create
        endTime (int?): Used with bakeAnimation flag. Specifies the end time of the baking process.  
                Properties: create
        keepOriginal (bool?): Do not remove the selected nodes used to create the bounding boxes.  
                Properties: create
        name (str?): Specifies the bounding box name.  
                Properties: create
        nameSuffix (str?): Specifies the bounding box name suffix.  
                Properties: create
        sampleBy (int?): Used with bakeAnimation flag. Specifies the animation evaluation time increment.  
                Properties: create
        shaderColor (Tuple[float, float, float]?): Set the color attribute of the Lambert material associate with the bounding box.  
                The RGB values should be defined between 0 to 1.0.  
                Default value is 0.5 0.5 0.5.  
                Properties: create
        single (bool?): Create a single bounding box per hierarchy selected.  
                Properties: create
        startTime (int?): Used with bakeAnimation flag. Specifies the start time of the baking process.  
                Properties: create

    Returns:
        bool:

    Example:
    """

