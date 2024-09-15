from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deviceManager(*args: Any, edit: bool = ..., query: bool = ..., attachment: bool = ..., axisCoordChanges: bool = ..., axisIndex: Queryable[int] = ..., axisName: bool = ..., axisOffset: bool = ..., axisScale: bool = ..., deviceIndex: Queryable[int] = ..., deviceNameFromIndex: Queryable[int] = ..., numAxis: bool = ..., numDevices: bool = ...) -> Union[bool, int]:
    """This command queriers the internal device manager for information on attached devices.device
    Args:
        attachment (bool?): Returns the plugs that a device and axis are attached to.  Expects the -deviceIndex and  
                axisIndex to be used in conjunction.  
                Properties: query
        axisCoordChanges (bool?): Returns whether the axis coordinate changes.  Expects the -deviceIndex and -axisIndex flags to be used  
                in conjunction.  
                Properties: query
        axisIndex (Queryable[int]?): Used usually in conjunction with other flags, to indicate the index of the axis.  
                Properties: create, query, edit
        axisName (bool?): Returns the name of the axis.  Expects the -deviceIndex and -axisIndex flags to be used  
                in conjunction.  
                Properties: query
        axisOffset (bool?): Returns the offset of the axis.  Expects the -deviceIndex and -axisIndex flags to be used  
                in conjunction.  
                Properties: query
        axisScale (bool?): Returns the scale of the axis.  Expects the -deviceIndex and -axisIndex flags to be used  
                in conjunction.  
                Properties: query
        deviceIndex (Queryable[int]?): Used usually in conjunction with other flags, to indicate the index of the device.  
                Properties: create, query, edit
        deviceNameFromIndex (Queryable[int]?): Returns the name of the device with the given index.  
                Properties: query
        numAxis (bool?): Returns the number of axis this device has.  Expects the -deviceIndex flag to be used.  
                Properties: query
        numDevices (bool?): Returns the number of devices currently attached.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

