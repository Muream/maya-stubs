from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def recordDevice(*args: Any, query: bool = ..., cleanup: bool = ..., data: bool = ..., device: Multiuse[str] = ..., duration: Queryable[int] = ..., playback: bool = ..., state: bool = ..., wait: bool = ...) -> Union[bool, int]:
    """Starts and stops server side device recording. The data is recorded
    at the device rate. Once recorded, the data may be brought into Maya
    with the applyTake command.See also: enableDevice, applyTake, readTake, writeTake
    Args:
        cleanup (bool?): Removes the recorded data from the device.  
                Properties: create
        data (bool?): Specifies if the device has recorded data. If the device is  
                recording at the time of query, the flag will return false.   
                Q: When queried, this flag returns an int.  
                Properties: query
        device (Multiuse[str]?): Specifies which device(s) to start record recording.  
                The listed device(s) will start recording regardless of their record  
                enable state.   
                C: The default is to start recording all devices that are  
                record enabled.  
                Properties: create, multiuse
        duration (Queryable[int]?): Duration (in seconds) of the recording. When the duration  
                expires, the device will still be in a recording state and must  
                be told to stop recording.   
                C: The default is 60.   
                Q: When queried, this flag returns an int.  
                Properties: create, query
        playback (bool?): If any attribute is connected to an animation curve, the  
                animation curve will play back while recording the device(s)  
                including any animation curves attached to attributes being  
                recorded.   
                C: The default is false.   
                Q: When queried, this flag returns an int.  
                Properties: create, query
        state (bool?): Start or stop device recording.   
                C: The default is true.   
                Q: When queried, this flag returns an int.  
                Properties: create, query
        wait (bool?): If -p/playback specified, wait until playback completion before  
                returning control to the user. This flag is ignored if -p is not used.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

