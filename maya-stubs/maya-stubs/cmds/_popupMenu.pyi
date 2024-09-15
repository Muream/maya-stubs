from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def popupMenu(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowOptionBoxes: bool = ..., altModifier: bool = ..., button: Queryable[int] = ..., ctrlModifier: bool = ..., defineTemplate: str = ..., deleteAllItems: bool = ..., exists: bool = ..., itemArray: bool = ..., markingMenu: bool = ..., numberOfItems: bool = ..., parent: str = ..., postMenuCommand: Callable[..., Any] = ..., postMenuCommandOnce: bool = ..., shiftModifier: bool = ..., useTemplate: str = ...) -> Union[str, bool, int]:
    """This command creates a popup menu and attaches it to the current
    control if no parent is specified.  The popup menu is posted with the
    right mouse button by default.Popup menus can be added to any kind of control, however,
    on some widgets, only the standard menu button (3rd mouse button)
    can be used to trigger popup menus. This is to meet generally
    accepted UI guidelines that assign the 3rd mouse button and only
    this one to popup menus, and also to prevent unexpected behavior
    of controls like text fields, that expect 1st and 2nd button to be
    reserved for contextual operations like text or item selection...
    Args:
        allowOptionBoxes (bool?): Indicate whether the menu will be able to support option box  
                menu items.  An error results if an option box item is added to a  
                menu that doesn't allow them.  This flag may be queried and must be  
                specified when the popup menu is created.  The default value is  
                false.  
                Properties: create, query
        altModifier (bool?): Specify this flag if the Alt modifier must be pressed when  
                posting the popup menu.  
                Properties: create, query, edit
        button (Queryable[int]?): Indicate which button posts the popup menu.  Valid values  
                range from 1 to 3 where 1 is the left most button on the mouse.  
                Properties: create, query, edit
        ctrlModifier (bool?): Specify this flag if the Cntl modifier must be pressed when  
                posting the popup menu.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteAllItems (bool?): Delete all the items in this menu.  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        itemArray (bool?): Return string array of the menu item names.  
                Properties: query
        markingMenu (bool?): Set the marking menu state of this popup menu.  
                Properties: create, query, edit
        numberOfItems (bool?): Return number of items in the menu.  
                Properties: query
        parent (str?): Specify the control that the popup menu will appear in.  
                Properties: create
        postMenuCommand (Callable[..., Any]?): Specify a script to be executed when the popup menu is about  
                to be shown.  
                Properties: create, edit
        postMenuCommandOnce (bool?): Indicate the -pmc/postMenuCommand should only be  
                invoked once.  Default value is false, ie.  
                the -pmc/postMenuCommand is invoked every time the popup menu is  
                shown.  
                Properties: create, query, edit
        shiftModifier (bool?): Specify this flag if the Shift modifier must be pressed  
                when posting the popup menu.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: Full path name to the menu.

    Example:
    """

