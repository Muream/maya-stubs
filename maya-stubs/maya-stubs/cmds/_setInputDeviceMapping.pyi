from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setInputDeviceMapping(*args: Any, absolute: bool = ..., axis: Multiuse[str] = ..., device: str = ..., offset: float = ..., relative: bool = ..., scale: float = ..., view: bool = ..., world: bool = ...) -> bool:
    """The command sets a scale and offset for all attachments made
    to a specified device axis. Any attachment made to a mapped
    device axis will have the scale and offset applied to its values.The value from the device is multiplied by the scale and the
    offset is added to this product. With an absolute mapping, the
    attached attribute gets the resulting value. If the mapping is
    relative, the final value is the offset added to the scaled
    difference between the current device value and the previous
    device value.This mapping will be applied to the device data before any
    mappings defined by the setAttrMapping command. A typical use
    would be to scale a device's input so that it is within a usable
    range. For example, the device mapping can be used to calibrate
    a spaceball to work in a specific section of a scene.As an example, if the space ball is setup with absolute device
    mappings, constantly pressing in one direction will cause the
    attached attribute to get a constant value. If a relative mapping
    is used, and the spaceball is pressed in one direction, the
    attached attribute will jump a constantly increasing (or constantly
    decreasing) value and will find a rest value equal to the offset.There are important differences between how the relative flag
    is handled by this command and the setAttrMapping command. (See
    the setAttrMapping documentation for specifics on how it calculates
    relative values). In general,
    both a relative device mapping (this command) and a relative
    attachment mapping (setAttrMapping) should not be used together
    on the same axis.
    Args:
        absolute (bool?): report absolute axis values  
                Properties: create
        axis (Multiuse[str]?): specify the axis to map  
                Properties: create, multiuse
        device (str?): specify which device to map  
                Properties: create
        offset (float?): specify the axis offset value  
                Properties: create
        relative (bool?): report the change in axis value since  
                the last sample  
                Properties: create
        scale (float?): specify the axis scale value  
                Properties: create
        view (bool?): translate the device coordinates into the coordinates  
                of the active camera  
                Properties: create
        world (bool?): translate the device coordinates into world space  
                coordinates  
                Properties: create

    Returns:
        bool:

    Example:
    """

