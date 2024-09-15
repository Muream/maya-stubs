from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def objectTypeUI(arg0: str = ..., /, *, isType: str = ..., listAll: bool = ..., superClasses: bool = ...) -> str:
    """This command returns the type of UI element such as button, sliders, etc.
    Args:
        isType (str?): Returns true|false if the object is of the specified type.  
                Properties: create
        listAll (bool?): Returns a list of all known UI commands and their respective types.  
                Each entry contains three strings which are the command name, ui type and class name.  
                Note that the class name is internal and is subject to change.  
                Properties: create
        superClasses (bool?): Returns a list of the names of all super classes for the given object.  
                Note that all class names are internal and are subject to change.  
                Properties: create

    Returns:
        str: The type of the specified object.

    Example:
    """

