from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lsUI(*args: str, cmdTemplates: bool = ..., collection: bool = ..., contexts: bool = ..., controlLayouts: bool = ..., controls: bool = ..., dumpWidgets: bool = ..., editors: bool = ..., head: int = ..., long: bool = ..., menuItems: bool = ..., menus: bool = ..., numWidgets: bool = ..., panels: bool = ..., radioMenuItemCollections: bool = ..., tail: int = ..., type: Multiuse[str] = ..., windows: bool = ..., workspaceControls: bool = ...) -> List[str]:
    """This command returns the names of UI objects.
    Args:
        cmdTemplates (bool?): UI command templates created using ELF UI commands.  
                Properties: create
        collection (bool?): Control collections created using ELF UI commands.  
                Properties: create
        contexts (bool?): Tool contexts created using ELF UI commands.  
                Properties: create
        controlLayouts (bool?): Control layouts created using ELF UI commands [e.g. formLayouts, paneLayouts, etc.]  
                Properties: create
        controls (bool?): Controls created using ELF UI commands. [e.g. buttons, checkboxes, etc]  
                Properties: create
        dumpWidgets (bool?): Dump all QT widgets used by Maya.  
                Properties: create
        editors (bool?): All currently existing editors.  
                Properties: create
        head (int?): The parameter specifies the maximum number of elements to be returned  
                from the beginning of the list of items. (Note: each flag  
                will return at most this many items so if multiple flags are specified  
                then the number of items returned will be greater than the value  
                specified).  
                Properties: create
        long (bool?): Use long pathnames instead of short non-path names.  
                Properties: create
        menuItems (bool?): Menu items created using ELF UI commands.  
                Properties: create
        menus (bool?): Menus created using ELF UI commands.  
                Properties: create
        numWidgets (bool?): Reports the number of QT widgets used by Maya.  
                Properties: create
        panels (bool?): All currently existing panels.  
                Properties: create
        radioMenuItemCollections (bool?): Menu item collections created using ELF UI commands.  
                Properties: create
        tail (int?): The parameter specifies the maximum number of elements to be returned  
                from the end of the list of items. (Note: each flag  
                will return at most this many items so if multiple flags are specified  
                then the number of items returned will be greater than the value  
                specified).  
                Properties: create
        type (Multiuse[str]?): List all objects of a certain type specified by the string argument.  
                For example, "window", "menu", "control", or "controlLayout".  
                Properties: create, multiuse
        windows (bool?): Windows created using ELF UI commands.  
                Properties: create
        workspaceControls (bool?): Workspace controls created using ELF UI commands.  
                Properties: create

    Returns:
        List[str]: The names of the object arguments.

    Example:
    """

