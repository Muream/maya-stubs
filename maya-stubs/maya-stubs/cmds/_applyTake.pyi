from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def applyTake(*args: Any, channel: Multiuse[str] = ..., device: Multiuse[str] = ..., filter: Multiuse[str] = ..., preview: bool = ..., recurseChannel: bool = ..., reset: bool = ..., specifyChannel: bool = ..., startTime: int = ...) -> bool:
    """This command takes data in a device (refered to as a take) and converts
    it into a form that may be played back and reviewed. The take can either
    be imported through the readTake action, or recorded by the recordDevice
    action. The take is either converted into animation curves or if the
    -preview flag is used, into blendDevice nodes.The command looks for animation curves attached to the target attributes
    of a device attachment. If animation curves exist, the take is
    pasted over the existing curves. If the curves do not exist, new
    animation curves are created.If devices are not specified, all of the devices with take data and that
    are enabled for applyTake, will have their data applied.See also: recordDevice, enableDevice, readTake, writeTake
    Args:
        channel (Multiuse[str]?): This flag overrides the set channel enable value.  
                If a channel is specified, it will be enabled.   
                C: The default is all applyTake enabled channels for the device(s).  
                Properties: create, multiuse
        device (Multiuse[str]?): Specifies which device contains the take.   
                C: The default is all applyTake enabled devices.  
                Properties: create, multiuse
        filter (Multiuse[str]?): This flag specifies the filters to use during the  
                applyTake. If this flag is used multiple times, the ordering  
                of the filters is from left to right.   
                C: The default is no filters.  
                Properties: create, multiuse
        preview (bool?): Applies the take to blendDevice nodes attached to the target  
                attributes connected to the device attachments. Animation curves  
                attached to the attributes will not be altered, but for the time  
                that preview data is defined, the preview data will be the data  
                used during playback.   
                C: The default is to not preview.  
                Properties: create
        recurseChannel (bool?): When this flag is used, the children of the channel(s)  
                specified by -c/channel are also applied.  
                C: The default is all of the enabled channels.  
                Properties: create
        reset (bool?): Resets the blendDevice nodes affected by -preview. The preview data  
                is removed and if animation curves exist, they are used during  
                playback.  
                Properties: create
        specifyChannel (bool?): This flag is used with -c/channel flag. When used, applyTake  
                will only work on the channels listed with the -c/channel flag.   
                C: The default is all of the enabled channels.  
                Properties: create
        startTime (int?): The default start time for a take is determined at record time.  
                The startTime option sets the starting time of the take in the  
                current animation units.   
                C: The default is the first time stamp of the take. If a time  
                stamp does not exist for the take, 0 is used.  
                Properties: create

    Returns:
        bool:

    Example:
    """

