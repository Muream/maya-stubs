from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def play(*, query: bool = ..., forward: bool = ..., playSound: bool = ..., record: bool = ..., sound: Queryable[str] = ..., state: bool = ..., wait: bool = ...) -> Union[bool, str]:
    """This command starts and stops playback.
    In order to change the frame range of playback,
    see the playbackOptions command.
    Args:
        forward (bool?): When true, play back the animation from the  
                currentTime to the maximum of the playback range.  
                When false, play back from the currentTime to the  
                minimum of the playback range.  When queried,  
                returns an int.  
                Properties: create, query
        playSound (bool?): Specify whether or not sound should be used during playback  
                Properties: create, query
        record (bool?): enable the recording system and start one playback loop  
                Properties: create, query
        sound (Queryable[str]?): Specify the sound node to be used during playback  
                Properties: create, query
        state (bool?): start or stop playing back  
                Properties: create, query
        wait (bool?): Wait till completion before returning control to  
                command Window.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

