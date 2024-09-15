from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def writeTake(*args: Any, angle: str = ..., device: str = ..., linear: str = ..., noTime: bool = ..., precision: int = ..., take: str = ..., virtualDevice: str = ...) -> bool:
    """This action writes a take from a device with recorded data to a
    take (.mov) file. The writeTake action can also write the virtual
    definition of a device.See also: recordDevice, readTake, defineVirtualDevice
    Args:
        angle (str?): Sets the angular unit used in the take.  
                Valid strings are [deg|degree|rad|radian].   
                C: The default is the current user angular unit.  
                Properties: create
        device (str?): Specifies the device that contains the take. This is a required  
                argument. If the device does not contain a take, the action will  
                fail.  
                Properties: create
        linear (str?): Sets the linear unit used in the take. Valid strings are  
                [mm|millimeter|cm|centimeter|m|meter|km|kilometer|in|inch|ft|foot|yd|yard|mi|mile]   
                C: The default is the current user linear unit.  
                Properties: create
        noTime (bool?): The take (.mov) file will not contain time stamps.   
                C: The default is to put time stamps in the take file.  
                Properties: create
        precision (int?): Sets the number of digits to the right of the decimal place in  
                the take file.  
                C: The default is 6.  
                Properties: create
        take (str?): Write out the take to a file with the specified name.  
                Properties: create
        virtualDevice (str?): Writes out the virtual device definition to a mel script with the  
                specified file name.  
                Properties: create

    Returns:
        bool:

    Example:
    """

