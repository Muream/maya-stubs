from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setParent(arg0: str = ..., /, *, query: bool = ..., defineTemplate: str = ..., menu: bool = ..., topLevel: bool = ..., upLevel: bool = ..., useTemplate: str = ...) -> Union[str, bool]:
    """This command changes the default parent to be the specified parent.
    Two special parents are "|" which indicates the top level layout of the
    window hierarchy, or ".." which indicates one level up in the hierarchy.
    Trying to move above the top level has no effect.A control must be parented to a control layout.  A control layout may
    be parented to another control layout or a window.  A menu may be parented
    to a window or a menu bar layout.  For all of these cases
    thecommand (with no flags) will indicate the current
    default parent.A menu item must be parented to a menu.  To specify the default menu
    parent use the command.  Note that all menu item
    objects created using themay also be treated as menu
    objects.The default parent is ignored by any object that explicitly sets theflag when it is created.
    Args:
        defineTemplate (str?): Put a command in a mode where any other flags and args  
                are parsed and added to the command template with the given name.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        menu (bool?): Parent menu for menu items.  
                Properties: create, query
        topLevel (bool?): Move to the top level layout in the hierarchy. Equivalent to use "|"  
                Properties: create
        upLevel (bool?): Move up one level in the hierarchy. Equivalent to use ".."  
                Properties: create
        useTemplate (str?): Will force the command to use a command template given by the name other than  
                the current one.  
                Properties: create

    Returns:
        str: Name of the parent if the parent changes. Empty string if the parent
            doesn't change.

    Example:
    """

