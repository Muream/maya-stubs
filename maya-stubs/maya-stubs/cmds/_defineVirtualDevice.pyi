from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def defineVirtualDevice(*args: Any, query: bool = ..., axis: int = ..., channel: str = ..., clear: bool = ..., create: bool = ..., device: str = ..., parent: str = ..., undefine: bool = ..., usage: str = ...) -> bool:
    """This command defines a virtual device. Virtual devices act like real
    devices and are useful to manipulate/playback data when an command
    device is not connected to the computer.
    Args:
        axis (int?): Specifies the axis number of the channel. All children have their  
                axis number determined by their parent's axis number and the width  
                of the parent channel. If this flag is not used, the order of the  
                channel determines the axis number.  
                Properties: create
        channel (str?): After a -create is started, channels may be added to the device  
                definition. The channel string wil be the name of the channel  
                being added to the device. The -channel flag must also be  
                accompanied by the -usage flag and optionally by the -axis flag.  
                Properties: create
        clear (bool?): The -clear option will end a device definition and throw away  
                any defined channels.  
                Properties: create
        create (bool?): Start defining a virtual device. If a device is currently being  
                defined, the -create flag will produce an error.  
                Properties: create
        device (str?): The -device flag ends the device definition. All of the channels  
                between the -create flag and the -device flag are added to  
                the specified device. If that device already exists, the command  
                will fail and the device should be redefined with another device  
                name. To see the currently defined devices, use the listInputDevices  
                command. The -device flag is also used with -undefine to undefine a  
                virtual device.  
                Properties: create
        parent (str?): Specified the parent channel of the channel being defined. If the  
                channel does not exist, or is an incompatible type, the command  
                will fail.  
                Properties: create
        undefine (bool?): Undefines the device specified with the -device flag.  
                Properties: create
        usage (str?): The -usage option is required for every -channel flag. It  
                describes what usage type the defined channel is. The usage  
                types are:  
              
              
                unknownscalar  
              
                posrot  
                posRotquaternionposQuaternion  
              
                rotXYZrotYZXrotZXY  
                rotXZYrotYXZrotZYX  
              
                posRotXYZposRotYZXposRotZXY  
                posRotXZYposRotXZYposRotZYX  
              
                posXposYposZrotX  
                rotYrotZ  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

