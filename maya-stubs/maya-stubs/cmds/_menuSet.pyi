from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def menuSet(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addMenu: str = ..., allMenuSets: bool = ..., currentMenuSet: Queryable[str] = ..., exists: str = ..., hotBoxVisible: bool = ..., insertMenu: Tuple[str, int] = ..., label: Queryable[str] = ..., menuArray: Queryable[List[str]] = ..., moveMenu: Tuple[str, int] = ..., moveMenuSet: Tuple[str, int] = ..., numberOfMenuSets: bool = ..., numberOfMenus: bool = ..., permanent: bool = ..., removeMenu: str = ..., removeMenuSet: str = ...) -> Union[str, bool, List[str]]:
    """Create a menu set which is used to logically order menus for display
    in the main menu bar.  Such menu sets can be edited and reordered
    dynamically.
    Args:
        addMenu (str?): Appends a menu onto the end of the current menu set.  
                Properties: create
        allMenuSets (bool?): Returns an array of the all the menu set object names in use.  Query returns string array.  
                Properties: query
        currentMenuSet (Queryable[str]?): The currently active menu set under which all operations affect (append, insert, remove, etc.).  Query returns string.  
                Properties: create, query
        exists (str?): Returns whether the specified menu set exists.  This query flag supports string arguments.  
                ie. menuSet -q -exists animationMenuSet;  
                      In query mode, this flag needs a value.  
                Properties: query
        hotBoxVisible (bool?): Whether this menu set should be displayed in the hotbox as well as in the main menubar.  
                Properties: create, query, edit
        insertMenu (Tuple[str, int]?): Inserts a menu into a specified index in the current menu set.  
                Properties: create
        label (Queryable[str]?): The label of the current menu set.  Query returns string.  
                Properties: create, query
        menuArray (Queryable[List[str]]?): An array of menu names (strings) in the current menu set.  Query returns string array.  
                Properties: create, query
        moveMenu (Tuple[str, int]?): Moves a specified menu from the current menu set to a new position.  
                Properties: create
        moveMenuSet (Tuple[str, int]?): Moves a specified menu set to another index.  
                Properties: create
        numberOfMenuSets (bool?): Number of menuSets in total.  Query returns int.  
                Properties: query
        numberOfMenus (bool?): The mumber of menus in the current menu set.  Query returns int.  
                Properties: query
        permanent (bool?): Whether this menu set can be removed.  
                Properties: create, query, edit
        removeMenu (str?): Removes a specified menu from the current menu set.  
                Properties: create
        removeMenuSet (str?): Removes the specified menu set object from the list of all menu sets.  
                Properties: create

    Returns:
        str: Name of resulting menu set.  (If there are no menu sets left, an empty string is returned)

    Example:
    """

