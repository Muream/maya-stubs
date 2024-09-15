from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attachDeviceAttr(*args: Any, query: bool = ..., attribute: Multiuse[str] = ..., axis: str = ..., camera: bool = ..., cameraRotate: bool = ..., cameraTranslate: bool = ..., clutch: str = ..., device: str = ..., selection: bool = ...) -> bool:
    """This command associates a device/axis pair with a node/attribute pair.
    When the device axis moves, the value of the attribute is set to the
    value of the axis. This value can be scaled and offset using
    the setAttrScale command.
    Args:
        attribute (Multiuse[str]?): specify the attribute to attach to  
                Properties: create, multiuse
        axis (str?): specify the axis to attach from.  
                Properties: create
        camera (bool?): This flag attaches the device/axis to the current camera.  
                The mapping between device axes and camera controls is  
                uses a heuristic based on the device descripton.  
                The interaction is a copy of the mouse camera navigation  
                controls.  
                Properties: create
        cameraRotate (bool?): This flag attaches the device/axis to the current cameras  
                rotation controls.  
                Properties: create
        cameraTranslate (bool?): This flag attaches the device/axis to the current cameras  
                translate controls.  
                Properties: create
        clutch (str?): specify a clutch button.  This button must be down  
                for the command string to be executed.  
                If no clutch is specified the command string is  
                executed everytime the device state changes  
                Properties: create
        device (str?): specify which device to assign the command string.  
                Properties: create
        selection (bool?): This flag attaches to the nodes in the selection list.  
                This is different from the default arguments of the command  
                since changing the selection will change the attachments.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

