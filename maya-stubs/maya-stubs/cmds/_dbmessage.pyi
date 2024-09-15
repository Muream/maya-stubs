from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dbmessage(*, file: str = ..., list: bool = ..., monitor: bool = ..., type: str = ...) -> bool:
    """Thecommand is used to install monitors for certain
    message types, dumping debug information as they are sent so that the
    flow of messages can be examined.debug, message, filter
    Args:
        file (str?): Destination file of the message monitoring information.  Use the special names  
                stdout and stderr to redirect to your command window.  As  
                well, the special name msdev is available on NT to direct your  
                output to the debug tab in the output window of Developer Studio.  
                Default value is stdout.  
                Properties: create
        list (bool?): List all available message types and their current enabled status.  
                Properties: create
        monitor (bool?): Set the monitoring state of the message type ('on' to enable, 'off' to disable).  
                Returns the list of all message types being monitored after the change in state.  
                Properties: create
        type (str?): Monitor only the messages whose name matches this keyword (default is all).  
                Properties: create

    Returns:
        bool:

    Example:
    """

