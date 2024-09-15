from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setXformManip(*args: Any, query: bool = ..., showUnits: bool = ..., suppress: bool = ..., useRotatePivot: bool = ..., worldSpace: bool = ...) -> bool:
    """This command changes some of the settings of the xform manip,
    to control its appearance.
    Args:
        showUnits (bool?): If set to true, the xform manip displays current units;  
                otherwise, the manip hides them.  
                Properties: query
        suppress (bool?): If set to true, the xform manip is suppressed and therefore  
                not visible or usable.  
                Properties: query
        useRotatePivot (bool?): If set to true, the xform manip uses the rotate pivot;  
                otherwise, the manip uses the bounding-box center. Defaults false.  
                Properties: query
        worldSpace (bool?): If set to true, the xform manip is always in world space.  
                If false, the manip is in object space. (Note: when multiple  
                objects are selected the manip is always in world space, no  
                matter what this is set to)  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

