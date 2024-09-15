from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deleteUI(*args: str, collection: bool = ..., control: bool = ..., editor: bool = ..., layout: bool = ..., menu: bool = ..., menuItem: bool = ..., panel: bool = ..., panelConfig: bool = ..., radioMenuItemCollection: bool = ..., toolContext: bool = ..., uiTemplate: bool = ..., window: bool = ...) -> bool:
    """This command deletes UI objects such as windows and controls.  Deleting
    a layout or window will also delete all of its children.  If a flag
    is used then all objects being deleted must be of the specified type.
    This command may not be edited or queried.NOTE: it is recommended that the type flags be used to disambiguate
    different kinds of objects with the same name.
    Args:
        collection (bool?): Object names for deletion are all radio or tool collections.  
                Properties: create
        control (bool?): Object names for deletion are all controls.  
                Properties: create
        editor (bool?): Object names for deletion are all editors.  
                Properties: create
        layout (bool?): Object names for deletion are all layouts.  
                Properties: create
        menu (bool?): Object names for deletion are all menus.  
                Properties: create
        menuItem (bool?): Object names for deletion are all menu items.  
                Properties: create
        panel (bool?): Object names for deletion are all panels.  
                Properties: create
        panelConfig (bool?): Object names for deletion are panel configurations.  
                Properties: create
        radioMenuItemCollection (bool?): Object names for deletion are all radio menu item collections.  
                Properties: create
        toolContext (bool?): Object names for deletion are all tool contexts.  
                Properties: create
        uiTemplate (bool?): Object names for deletion are all UI templates.  
                Properties: create
        window (bool?): Object names for deletion are all windows.  
                Properties: create

    Returns:
        bool:

    Example:
    """

