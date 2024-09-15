from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sound(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., endTime: Queryable[int] = ..., file: Queryable[str] = ..., length: bool = ..., mute: bool = ..., name: Queryable[str] = ..., offset: Queryable[int] = ..., sourceEnd: Queryable[int] = ..., sourceStart: Queryable[int] = ...) -> Union[str, int, bool]:
    """Creates an audio node which can be used with UI commands such
    as soundControl or timeControl which support sound scrubbing
    and sound during playback.
    Args:
        endTime (Queryable[int]?): Time at which to end the sound.  
                Properties: create, query, edit
        file (Queryable[str]?): Name of sound file.  
                Properties: create, query, edit
        length (bool?): Query the length (in the current time unit) of the sound.  
                Properties: query
        mute (bool?): Mute the audio clip.  
                Properties: create, query, edit
        name (Queryable[str]?): Name to give the resulting audio node.  
                Properties: create, query, edit
        offset (Queryable[int]?): Time at which to start the sound.  
                Properties: create, query, edit
        sourceEnd (Queryable[int]?): Time offset from the start of the sound file at which to end the sound.  
                Properties: create, query, edit
        sourceStart (Queryable[int]?): Time offset from the start of the sound file at which to start the sound.  
                Properties: create, query, edit

    Returns:
        str: Name of resulting audio node

    Example:
    """

