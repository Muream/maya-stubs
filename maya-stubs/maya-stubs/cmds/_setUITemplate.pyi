from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setUITemplate(arg0: str = ..., /, *, query: bool = ..., popTemplate: bool = ..., pushTemplate: bool = ...) -> str:
    """This command sets the current(default) command template
    for the ELF commands.  The special name NONE can be used to set no templates
    current. See "uiTemplate" command also.
    Args:
        popTemplate (bool?): Pop the current template off of the stack and sets the next template  
                on the stack to be current.  
                Properties: create
        pushTemplate (bool?): Push the current template onto a stack that can later be popped.  
                Properties: create

    Returns:
        str: The name of the currently selected command template.

    Example:
    """

