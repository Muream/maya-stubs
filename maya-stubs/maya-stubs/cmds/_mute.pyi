from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mute(*args: str, query: bool = ..., disable: bool = ..., force: bool = ...) -> List[str]:
    """The mute command is used to disable and enable playback on a channel. When a channel is muted, it retains the value that it was at prior to being muted.mute, animation, channels
    Args:
        disable (bool?): Disable muting on the channels  
                Properties: create
        force (bool?): Forceable disable of muting on the channels. If there are keys on the mute channel,  
                the animation and mute node will both be removed.  If this flag is not set, then  
                mute nodes with animation will only be disabled.  
                Properties: create

    Returns:
        List[str]: Name(s) of the mute node(s)

    Example:
    """

