from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setInfinity(*args: str, edit: bool = ..., query: bool = ..., attribute: Multiuse[str] = ..., controlPoints: bool = ..., hierarchy: str = ..., postInfinite: Queryable[str] = ..., preInfinite: Queryable[str] = ..., shape: bool = ...) -> Union[bool, str]:
    """Set the infinity type before (after) a paramCurve's first
    (last) keyframe.
    Args:
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        controlPoints (bool?): This flag explicitly specifies whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        postInfinite (Queryable[str]?): Set the infinity type after a paramCurve's last keyframe. Valid  
                values are "constant", "linear", "cycle", "cycleRelative", "oscillate".  
                Properties: create, query
        preInfinite (Queryable[str]?): Set the infinity type before a paramCurve's first keyframe. Valid  
                values are "constant", "linear", "cycle", "cycleRelative", "oscillate".  
                Properties: create, query
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

