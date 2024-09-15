from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def assignInputDevice(*args: Any, query: bool = ..., clutch: str = ..., continuous: bool = ..., device: str = ..., immediate: bool = ..., multiple: bool = ...) -> str:
    """This command associates a command string (i.e. a mel script)
    with the input device.  When the device moves or a button on
    the device is pressed, the command string is executed as if
    you typed it into the window.  If the command string contains
    the names of buttons or axes of the device, the current value
    of these buttons/axes are substituted in.  Buttons are reported
    as booleans and axes as doubles.This command is most useful for associating buttons on a device
    with commands.  For using a device to capture continous movements
    it is much more efficient to attach the device directly into
    the dependency graph.
    Args:
        clutch (str?): specify a clutch button.  This button must be down  
                for the command string to be executed.  
                If no clutch is specified the command string is  
                executed everytime the device state changes  
                Properties: create
        continuous (bool?): if this flag is set the command string is continously  
                (once for everytime the device changes state).  By  
                default if a clutch button is specified the command  
                string is only executed once when the button is  
                pressed.  
                Properties: create
        device (str?): specify which device to assign the command string.  
                Properties: create
        immediate (bool?): Immediately executes the command, without using the queue.  
                Properties: create
        multiple (bool?): if this flag is set the other command strings  
                associated with this device are not deleted.  
                By default, when a new command string is attached  
                to the device, all other command strings are deleted.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

