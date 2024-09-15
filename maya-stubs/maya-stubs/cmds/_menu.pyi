from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def menu(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowOptionBoxes: bool = ..., defineTemplate: str = ..., deleteAllItems: bool = ..., docTag: Queryable[str] = ..., enable: bool = ..., exists: bool = ..., familyImage: Queryable[str] = ..., helpMenu: bool = ..., itemArray: bool = ..., label: Queryable[str] = ..., mnemonic: Queryable[str] = ..., numberOfItems: bool = ..., parent: str = ..., postMenuCommand: Callable[..., Any] = ..., postMenuCommandOnce: bool = ..., scrollable: bool = ..., tearOff: bool = ..., useTemplate: str = ..., version: Queryable[str] = ..., visible: bool = ...) -> Union[str, bool]:
    """This command creates a new menu and adds it to the default window's
    menubar if no parent is specified.  The menu can be enabled/disabled.
    Note that this command may also be used on menu objects created using
    the command
    Args:
        allowOptionBoxes (bool?): Deprecated. All menus now always allow option boxes.  
                Indicate whether the menu will be able to support option box  
                menu items.  
                Properties: create, query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteAllItems (bool?): Delete all the items in this menu.  
                Properties: create, edit
        docTag (Queryable[str]?): Attaches a tag to the menu.  
                Properties: create, query, edit
        enable (bool?): Enables/disables the menu.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        familyImage (Queryable[str]?): The filename of the icon associated with the menu. This  
                icon will be used if a menu item does not have an icon image  
                defined.  
                Properties: create, query, edit
        helpMenu (bool?): Indicates that this menu is the help menu and will be the  
                right most menu in the menu bar. On Unix systems the help menu  
                is also right justified in the menu bar.  
                Properties: create, query, edit
        itemArray (bool?): Return string array of the menu item names.  
                Properties: query
        label (Queryable[str]?): The text that is displayed for the menu.  If no label is  
                supplied then the menuName will be used.  
                Properties: create, query, edit
        mnemonic (Queryable[str]?): Set the Alt key to post that menu.  The character  
                specified must match the case of its corresponding character in  
                the menu item text, but selection from the keyboard is case  
                insensitive.  
                Properties: create, query, edit
        numberOfItems (bool?): Return number of items in the menu.  
                Properties: query
        parent (str?): Specify the window that the menu will appear in.  
                Properties: create
        postMenuCommand (Callable[..., Any]?): Specify a script to be executed when the menu is about to be  
                shown.  
                Properties: create, edit
        postMenuCommandOnce (bool?): Indicate the -pmc/postMenuCommand should only be  
                invoked once.  Default value is false, ie.  
                the -pmc/postMenuCommand is invoked every time the menu is  
                shown.  
                Properties: create, query, edit
        scrollable (bool?): Make the popup menus support scrolling. Default value is false.  
                Properties: create, query, edit
        tearOff (bool?): Makes the menu tear-off-able.  
                Properties: create
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        version (Queryable[str]?): Specify the version that this menu feature was introduced.  
                The argument should be given as a string of the version number  
                (e.g. "2014", "2015"). Currently only accepts major version  
                numbers (e.g. 2014.5 should be given as "2014").  
                Properties: create, query, edit
        visible (bool?): Shows/hides the menu.  
                Properties: create, query, edit

    Returns:
        str: Full path name to the menu.

    Example:
    """

