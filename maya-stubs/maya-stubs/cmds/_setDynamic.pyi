from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setDynamic(*args: str, allOnWhenRun: bool = ..., disableAllOnWhenRun: bool = ..., setAll: bool = ..., setOff: bool = ..., setOn: bool = ...) -> str:
    """setDynamic sets the isDynamic attribute of particle objects
    on or off.  If no objects are specified, it sets the
    attribute for any selected objects.  If -all is thrown, it
    sets the attribute for all particle objects in the scene.
    By default it sets the attribute true (on); if the -off flag is
    thrown, it sets the attribute false (off).WARNING: setDynamic is obsolescent.  This is the last version of
    Maya in which it will be supported.
    Args:
        allOnWhenRun (bool?): Obsolete, no longer suppported or necessary.  
                Properties: create
        disableAllOnWhenRun (bool?): Obsolete, no longer suppported or necessary.  
                Properties: create
        setAll (bool?): Set for all objects.  
                Properties: create
        setOff (bool?): Sets isDynamic false.  
                Properties: create
        setOn (bool?): Sets isDynamic true.  This flag is set by default.  
                Properties: create

    Returns:
        str: array

    Example:
    """

