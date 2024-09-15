from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listDeviceAttachments(*args: Any, attribute: str = ..., axis: str = ..., clutch: str = ..., device: str = ..., file: str = ..., selection: bool = ..., write: bool = ...) -> str:
    """This command lists the current set of device attachments.
    The listing is in the form of the commands required to
    recreate them.  This includes both attachments and device
    mappings.
    Args:
        attribute (str?): specify the attribute attachments to list  
                Properties: create
        axis (str?): specify the axis attachments to list  
                Properties: create
        clutch (str?): List only attachment clutched with this button  
                Properties: create
        device (str?): specify which device attachments to list  
                Properties: create
        file (str?): Specify the name of the file to write out device  
                attachments.  
                Properties: create
        selection (bool?): This flag list only attachments on selection  
                Properties: create
        write (bool?): Write out device attachments to a file specified  
                by the -f flag, is set.  If -f is not set, it'll  
                write out to a file named for the device.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

