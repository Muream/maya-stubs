from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nameCommand(arg0: str = ..., /, *, annotation: str = ..., command: Callable[..., Any] = ..., data1: str = ..., data2: str = ..., data3: str = ..., default: bool = ..., sourceType: str = ...) -> str:
    """This command creates a nameCommand object. Each nameCommand object
    can be connected to a hotkey. Thereafter, the nameCommand's command
    string will be executed whenever the hotkey is pressed (or released,
    as specified by the user).
    Args:
        annotation (str?): A description of the command.  
                Properties: create
        command (Callable[..., Any]?): The command that is executed  
                when the nameCommand is invoked.  
                Properties: create
        data1 (str?):   
                Properties: create
        data2 (str?):   
                Properties: create
        data3 (str?): These are optional, user-defined data strings that  
                are attached to the nameCommand object.  They can be  
                edited or queried using the assignCommand command.  
                Properties: create
        default (bool?): Indicate that this name command is a default command.  
                Default name commands will not be saved to preferences.  
                Properties: create
        sourceType (str?): Sets the language type for the command script. Can only be used in conjunction with the -command flag.  
                Valid values are "mel" (enabled by default), and "python".  
                Properties: create

    Returns:
        str: The name of the nameCommand object created

    Example:
    """

