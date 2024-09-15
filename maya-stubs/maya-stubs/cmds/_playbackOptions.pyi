from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def playbackOptions(*, edit: bool = ..., query: bool = ..., animationEndTime: Queryable[int] = ..., animationStartTime: Queryable[int] = ..., blockingAnim: bool = ..., by: Queryable[float] = ..., framesPerSecond: bool = ..., loop: Queryable[str] = ..., maxPlaybackSpeed: Queryable[float] = ..., maxTime: Queryable[int] = ..., minTime: Queryable[int] = ..., playbackSpeed: Queryable[float] = ..., selectionEndTime: Queryable[int] = ..., selectionStartTime: Queryable[int] = ..., selectionVisible: bool = ..., stepLoop: bool = ..., view: Queryable[str] = ...) -> Union[str, int, bool, float]:
    """This command sets/queries certain values associated
    with playback: looping style, start/end times, etc.
    Only commands modifying the -minTime/maxTime,
    the -animationStartTime/animationEndTime,
    the -selectionStartTime/selectionEndTime/selectionVisible
    or the -by value are undoable.
    Args:
        animationEndTime (Queryable[int]?): Sets the end time of the animation.  Query returns a float.  
                Properties: create, query, edit
        animationStartTime (Queryable[int]?): Sets the start time of the animation.  Query returns a float.  
                Properties: create, query, edit
        blockingAnim (bool?): All tangents playback as stepped so that animation can be viewed in pure pose-to-pose form  
                Properties: create, query
        by (Queryable[float]?): Increment between times viewed during playback. (Default 1.0)  
                Properties: create, query, edit
        framesPerSecond (bool?): Queries the actual playback rate.  Query returns a float.  
                Properties: create, query
        loop (Queryable[str]?): Controls if and how playback repeats.  Valid values are  
                "once," "continuous," and "oscillate."  Query returns string.  
                Properties: create, query, edit
        maxPlaybackSpeed (Queryable[float]?): Sets the desired maximum playback speed.  Query returns a float. The  
                maxPlaybackSpeed is only used by Maya when your playbackSpeed is 0  
                (play every frame). The maxPlaybackSpeed will clamp the maximum  
                playback rate to prevent it from going more than a certain amount. A  
                maxPlaybackSpeed of 0 will give free (unclamped) playback.  
                Properties: create, query, edit
        maxTime (Queryable[int]?): Sets the end of the playback time range.  Query returns a float.  
                Properties: create, query, edit
        minTime (Queryable[int]?): Sets the start of the playback time range.  Query returns a float.  
                Properties: create, query, edit
        playbackSpeed (Queryable[float]?): Sets the desired playback speed.  Query returns a float.  
                Properties: create, query, edit
        selectionEndTime (Queryable[int]?): Sets the end time of the selection.  Query returns a float.  
                Properties: create, query, edit
        selectionStartTime (Queryable[int]?): Sets the start time of the selection.  Query returns a float.  
                Properties: create, query, edit
        selectionVisible (bool?): Sets the selection visibility. Query returns current visibility.  
                Properties: create, query, edit
        stepLoop (bool?): Turns on/off looping back to the start or end of the play range for step forward/backward one frame and step forward/backward one key.  
                Properties: create, query
        view (Queryable[str]?): Controls how many modelling views update during playback.  
                Valid values are "all" and "active".  Query returns a string.  
                Properties: create, query, edit

    Returns:
        str: or float
            Query of edited option.

    Example:
    """

