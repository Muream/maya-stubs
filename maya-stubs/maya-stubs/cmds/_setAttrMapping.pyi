from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setAttrMapping(*args: Any, query: bool = ..., absolute: bool = ..., attribute: Multiuse[str] = ..., axis: str = ..., clutch: str = ..., device: str = ..., offset: float = ..., relative: bool = ..., scale: float = ..., selection: bool = ...) -> bool:
    """This command applies an offset and scale to a specified device
    attachment. This command is different than the setInputDeviceMapping
    command, which applies a mapping to a device axis.The value from the device is multiplied by the scale and the
    offset is added to this product. With an absolute mapping, the
    attached attribute gets the resulting value. If the mapping is
    relative, the resulting value is added to the previous calculated
    value. The calculated value will also take into account the
    setInputDeviceMapping, if it was defined.As an example, if the space ball is setup with absolute attachment
    mappings, pressing in one direction will cause the
    attached attribute to get a constant value. If a relative mapping
    is used, and the spaceball is pressed in one direction, the
    attached attribute will get a constantly increasing (or constantly
    decreasing) value.Note that the definition of relative is different than the definition
    used by the setInputDeviceMapping command. In general, both
    a relative attachment mapping (this command) and a relative
    device mapping (setInputDeviceMapping) should not be used together
    one the same axis.
    Args:
        absolute (bool?): Make the mapping absolute.  
                Properties: create
        attribute (Multiuse[str]?): The attribute used in the attachment.  
                Properties: create, multiuse
        axis (str?): The axis on the device used in the attachment.  
                Properties: create
        clutch (str?): The clutch button used in the attachment.  
                Properties: create
        device (str?): The device used in the attachment.  
                Properties: create
        offset (float?): Specify the offset value.  
                Properties: create
        relative (bool?): Make the mapping relative.  
                Properties: create
        scale (float?): Specify the scale value.  
                Properties: create
        selection (bool?): This flag specifies the mapping should be on the selected  
                objects  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

