from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def readTake(*args: Any, angle: str = ..., device: str = ..., frequency: float = ..., linear: str = ..., noTime: bool = ..., take: str = ...) -> bool:
    """This action reads a take (.mov) file to a defined device.See also: writeTake, applyTake
    Args:
        angle (str?): Sets the angular unit used in the take. Valid strings are  
                "deg", "degree", "rad", and "radian".   
                C: The default is the current user angular unit.  
                Properties: create
        device (str?): Specifies the device into which the take data is read. This is a  
                required argument.  
                Properties: create
        frequency (float?): The timestamp is ignored and the specified frequency is used. If  
                timeStamp data is not in the .mov file, the -noTimestamp flag  
                should also be used. This flag resample, instead  
                the data is assumed to be at the specified frequency.   
                C: If the take file does not use time stamps, the default frequency  
                is 60Hz.  
                Properties: create
        linear (str?): Sets the linear unit used in the take. Valid strings are  
                "mm", "millimeter", "cm", "centimeter", "m", "meter", "km",  
                "kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi",  
                and "mile".   
                C: The default is the current user linear unit.  
                Properties: create
        noTime (bool?): Specifies if the take (.mov) file contains time stamps.   
                C: The default is to assume time stamps are part of the take file.  
                Properties: create
        take (str?): Reads the specified take file. It is safest to pass the full  
                path to the flag.  
                Properties: create

    Returns:
        bool:

    Example:
    """

