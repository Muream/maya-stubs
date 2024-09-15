from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def detachDeviceAttr(*args: Any, query: bool = ..., all: bool = ..., attribute: str = ..., axis: str = ..., device: str = ..., selection: bool = ...) -> bool:
    """This command detaches connections between device axes and node
    attributes.  The command line arguments are the same as for
    the corresponding attachDeviceAttr except for the clutch argument
    which can not be used in this command.
    Args:
        all (bool?): Delete all attachments on every device.  
                Properties: create
        attribute (str?): The attribute to detach. This flag must be used  
                with the -d/device flag.  
                Properties: create
        axis (str?): The axis to detach. This flag must be used with  
                the -d/device flag.  
                Properties: create
        device (str?): Delete the attachment for this device. If the -ax/axis  
                flag is not used, all of the attachments connected to this  
                device are detached.  
                Properties: create
        selection (bool?): Detaches selection attachments.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

