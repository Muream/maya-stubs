from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyColorBlindData(*args: Any, aboveMaxColorBlue: Multiuse[float] = ..., aboveMaxColorGreen: Multiuse[float] = ..., aboveMaxColorRed: Multiuse[float] = ..., attrName: Multiuse[str] = ..., belowMinColorBlue: Multiuse[float] = ..., belowMinColorGreen: Multiuse[float] = ..., belowMinColorRed: Multiuse[float] = ..., clashColorBlue: float = ..., clashColorGreen: float = ..., clashColorRed: float = ..., colorBlue: Multiuse[float] = ..., colorGreen: Multiuse[float] = ..., colorRed: Multiuse[float] = ..., dataType: Multiuse[str] = ..., enableFalseColor: bool = ..., maxColorBlue: Multiuse[float] = ..., maxColorGreen: Multiuse[float] = ..., maxColorRed: Multiuse[float] = ..., maxValue: Multiuse[float] = ..., minColorBlue: Multiuse[float] = ..., minColorGreen: Multiuse[float] = ..., minColorRed: Multiuse[float] = ..., minValue: Multiuse[float] = ..., mode: Multiuse[int] = ..., noColorBlue: float = ..., noColorGreen: float = ..., noColorRed: float = ..., numIdTypes: Multiuse[int] = ..., queryMode: bool = ..., typeId: Multiuse[int] = ..., useMax: Multiuse[bool] = ..., useMin: Multiuse[bool] = ..., value: Multiuse[str] = ...) -> List[str]:
    """This command applies false color to the selected polygonal components
    and objects, depending on whether or not blind data exists for the
    selected components (or, in the case of poly objects, dynamic
    attributes), and, depending on the color mode indicated, what the
    values are. It is possible to color objects based on whether or not
    the data exists, if the data matches a specific value or range of
    values, or grayscale color the data according to what the actual value
    is in relation to the specified min and max. This command also has a
    query mode in which the components and/or objects are returned in a
    string array to allow for selection filtering.color, query, blind, data
    Args:
        aboveMaxColorBlue (Multiuse[float]?): Specifies blue component of color to use for data that is above max  
                Properties: create, multiuse
        aboveMaxColorGreen (Multiuse[float]?): Specifies green component of color to use for data that is above max  
                Properties: create, multiuse
        aboveMaxColorRed (Multiuse[float]?): Specifies red component of color to use for data that is above max  
                Properties: create, multiuse
        attrName (Multiuse[str]?): Specifies the name of the data that is being examined by this command.  
                Properties: create, multiuse
        belowMinColorBlue (Multiuse[float]?): Specifies blue component of color to use for data that is below min  
                Properties: create, multiuse
        belowMinColorGreen (Multiuse[float]?): Specifies green component of color to use for data that is below min  
                Properties: create, multiuse
        belowMinColorRed (Multiuse[float]?): Specifies red component of color to use for data that is below min  
                Properties: create, multiuse
        clashColorBlue (float?): Specifies blue component color to use for data which clashes  
                Properties: create
        clashColorGreen (float?): Specifies green component color to use for data which clashes  
                Properties: create
        clashColorRed (float?): Specifies red component color to use for data which clashes  
                Properties: create
        colorBlue (Multiuse[float]?): Specifies blue component of color to use for given data  
                Properties: create, multiuse
        colorGreen (Multiuse[float]?): Specifies green component of color to use for given data  
                Properties: create, multiuse
        colorRed (Multiuse[float]?): Specifies red component of color to use for given data  
                Properties: create, multiuse
        dataType (Multiuse[str]?): Specifies the type for this id  
                Properties: create, multiuse
        enableFalseColor (bool?): Turns false coloring on or off for all poly objects in the scene  
                Properties: create
        maxColorBlue (Multiuse[float]?): Specifies blue component of color to use for max value for grayscale  
                Properties: create, multiuse
        maxColorGreen (Multiuse[float]?): Specifies green component of color to use for max value for grayscale  
                Properties: create, multiuse
        maxColorRed (Multiuse[float]?): Specifies red component of color to use for max value for grayscale  
                Properties: create, multiuse
        maxValue (Multiuse[float]?): Specifies the max value for grayscale or discrete range data  
                Properties: create, multiuse
        minColorBlue (Multiuse[float]?): Specifies blue component of color to use for min value for grayscale  
                Properties: create, multiuse
        minColorGreen (Multiuse[float]?): Specifies green component of color to use for min value for grayscale  
                Properties: create, multiuse
        minColorRed (Multiuse[float]?): Specifies red component of color to use for min value for grayscale  
                Properties: create, multiuse
        minValue (Multiuse[float]?): Specifies the min value for grayscale or discrete range data  
                Properties: create, multiuse
        mode (Multiuse[int]?): Specifies the mode:  
              
                0. binary - only components and objects that have the data will be colored  
                1. discrete value - a value is specified. Data that matches this value will be colored  
                2. discrete range - values that fall within the given range will be colored  
                3. unsigned set mode - if ( givenValue & actualValue ) then data will be colored  
                4. unsigned not set mode - if ( !(givenValue & actualValue) ) then data will be colored  
                5. unsigned equal mode - if ( givenValue == actualValue ) then data will be colored  
                6. grayscale mode - a min value, max value, min color, max color, below min color, and  
                    above max color are given. Data is colored according to how it relates to these values.  
                7. as color mode - if the blind data consists of 3 doubles, ranged 0. 1, the components are colored as the data specifies  
                Properties: create, multiuse
        noColorBlue (float?): Specifies blue component of color to use for no data assigned  
                Properties: create
        noColorGreen (float?): Specifies green component of color to use for no data assigned  
                Properties: create
        noColorRed (float?): Specifies red component of color to use for no data assigned  
                Properties: create
        numIdTypes (Multiuse[int]?): Specifies how many attrs are in this id type  
                Properties: create, multiuse
        queryMode (bool?): If on, do not color and return selection as string array instead.  
                Any data that would be colored normally (except for 'no color' and  
                out of range colors) is returned  
                Properties: create
        typeId (Multiuse[int]?): Specifies the typeId of the BlindData type being created  
                Properties: create, multiuse
        useMax (Multiuse[bool]?): Specifies whether the max should be used for discrete ranges  
                Properties: create, multiuse
        useMin (Multiuse[bool]?): Specifies whether the min should be used for discrete ranges  
                Properties: create, multiuse
        value (Multiuse[str]?): The value of the data  
                Properties: create, multiuse

    Returns:
        List[str]: Command result

    Example:
    """

