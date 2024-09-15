from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def runup(*, cache: bool = ..., fromPreviousFrame: bool = ..., fromStartFrame: bool = ..., maxFrame: int = ..., state: bool = ...) -> str:
    """runup plays the scene through a frame of frames, forcing
    dynamic objects to evaluate as it does so.   If no max frame
    is specified, runup runs up to the current time.
    Args:
        cache (bool?): Cache the state after the runup.  
                Properties: create
        fromPreviousFrame (bool?): Run up the animation from the previously evaluated frame.  
                If no flag is supplied this is the default.  
                Properties: create
        fromStartFrame (bool?): Run up the animation from the start frame.  
                If no flag is supplied -fromPreviousFrame is the default.  
                Properties: create
        maxFrame (int?): Ending time for runup, in current user time units.  
                The runup will always start at the  
                minimum start frame for all dynamic objects.  
                Properties: create
        state (bool?): Turns runup and cache on/off.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

