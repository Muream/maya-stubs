from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def weightsColor(*args: Any, query: bool = ..., colorRamp: Queryable[str] = ..., deformer: Queryable[str] = ..., falseColor: bool = ..., outOfRangeColor: Queryable[Tuple[float, float, float]] = ..., rampMaxColor: Queryable[Tuple[float, float, float]] = ..., rampMinColor: Queryable[Tuple[float, float, float]] = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ...) -> Union[List[str], str, bool, Tuple[float, float, float]]:
    """Controls the coloring of deformer weights.
    Args:
        colorRamp (Queryable[str]?): Allows a user defined color ramp to be used to map values to colors.  
                Properties: query
        deformer (Queryable[str]?): Specify the deformer that needs to be visualized.  
                Properties: query
        falseColor (bool?): Enable or disable false color display on the geometry.  
                Properties: query
        outOfRangeColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used for the areas outside the deformers subset.  
                Properties: query
        rampMaxColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is greater than or equal to  
                the maximum value.  
                Properties: query
        rampMinColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is less than or equal to the  
                minimum value.  
                Properties: query
        useColorRamp (bool?): Specifies whether the user defined color ramp should be used to map values  
                from to colors. If this is turned off, the default greyscale feedback  
                will be used.  
                Properties: query
        useMaxMinColor (bool?): Specifies whether the out of range colors should be used.  See rampMinColor  
                and rampMaxColor flags for further details.  
                Properties: query

    Returns:
        List[str]: For query operation

    Example:
    """

