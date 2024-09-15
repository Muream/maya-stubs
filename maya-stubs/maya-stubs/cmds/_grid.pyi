from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def grid(*args: str, query: bool = ..., default: bool = ..., displayAxes: bool = ..., displayAxesBold: bool = ..., displayDivisionLines: bool = ..., displayGridLines: bool = ..., displayOrthographicLabels: bool = ..., displayPerspectiveLabels: bool = ..., divisions: Queryable[int] = ..., orthographicLabelPosition: Queryable[str] = ..., perspectiveLabelPosition: Queryable[str] = ..., reset: bool = ..., size: Queryable[float] = ..., spacing: Queryable[float] = ..., style: Queryable[int] = ..., toggle: bool = ...) -> Union[bool, int, str, float]:
    """This command changes the size and spacing of lines on the ground
    plane displayed in the perspective and orthographic views.This command lets you reset the ground plane, change its size
    and grid line spacing, grid subdivisions and display options.
    Args:
        default (bool?): Used to specify/query default values.  
                Properties: query
        displayAxes (bool?): Specify true to display the grid axes.  
                Properties: query
        displayAxesBold (bool?): Specify true to accent the grid axes by drawing them with a  
                thicker line.  
                Properties: query
        displayDivisionLines (bool?): Specify true to display the subdivision lines between  
                grid lines.  
                Properties: query
        displayGridLines (bool?): Specify true to display the grid lines.  
                Properties: query
        displayOrthographicLabels (bool?): Specify true to display the grid line numeric labels in  
                the orthographic views.  
                Properties: query
        displayPerspectiveLabels (bool?): Specify true to display the grid line numeric labels in  
                the perspective view.  
                Properties: query
        divisions (Queryable[int]?): Sets the number of subdivisions between major grid lines.  
                The default is 10. If the spacing is 10 units, setting  
                divisions to 10 will cause division lines to appear 1 unit  
                apart.  
                Properties: query
        orthographicLabelPosition (Queryable[str]?): The position of the grid's numeric labels in orthographic  
                views. Valid values are    "axis" and "edge".  
                Properties: query
        perspectiveLabelPosition (Queryable[str]?): The position of the grid's numeric labels in perspective  
                views. Valid values are    "axis" and "edge".  
                Properties: query
        reset (bool?): Resets the ground plane to its default values
        size (Queryable[float]?): Sets the size of the grid in linear units.  The default is  
                12 units.  
                Properties: query
        spacing (Queryable[float]?): Sets the spacing between major grid lines in linear units.  
                The default is 10 units.  
                Properties: query
        style (Queryable[int]?): This flag is obsolete and should not be used.  
                Properties: query
        toggle (bool?): Turns the ground plane display off in all windows, including  
                orthographic windows.  Default is true.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

