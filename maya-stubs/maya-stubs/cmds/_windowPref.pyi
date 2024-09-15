from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def windowPref(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., enableAll: bool = ..., exists: bool = ..., height: Queryable[int] = ..., leftEdge: Queryable[int] = ..., loadAll: bool = ..., maximized: bool = ..., parentMain: bool = ..., remove: bool = ..., removeAll: bool = ..., restoreMainWindowState: str = ..., saveAll: bool = ..., saveMainWindowState: str = ..., topEdge: Queryable[int] = ..., topLeftCorner: Queryable[Tuple[int, int]] = ..., width: Queryable[int] = ..., widthHeight: Queryable[Tuple[int, int]] = ...) -> Union[bool, int, Tuple[int, int]]:
    """Create or modify preferred window attributes.  The size and position
    of a window is retained during and between application sessions.  A
    default window preference is created when a window is closed.  Window
    preferences must be named and, consequently, only affect the window
    with a matching name.Note that window preferences are not applied to the main Maya window
    nor the Command window.
    Args:
        enableAll (bool?): Enable/disable all window preferences.  Preferences are enabled  
                by default.  Set this flag to false and window's will ignore all  
                preference values.  
                Properties: create, query
        exists (bool?): Returns true|false depending upon whether the specified object  
                exists. Other flags are ignored.  
                Properties: create
        height (Queryable[int]?): Height of the window.  
                Properties: create, query, edit
        leftEdge (Queryable[int]?): Left edge position of the window.  
                Properties: create, query, edit
        loadAll (bool?): Reads in file with window attributes from disk.  
                Properties: create
        maximized (bool?): Maximize the window.  
                Properties: create, query, edit
        parentMain (bool?): Set whether window is parented to main application window. Windows only.  
                Properties: create, query
        remove (bool?): Remove a window preference.  
                Properties: create
        removeAll (bool?): Remove all window preferences.  
                Properties: create
        restoreMainWindowState (str?): Reads in file with main window state (positions of toolbars and dock controls).  
                Properties: create
        saveAll (bool?): Writes out file with window attributes.  
                Properties: create
        saveMainWindowState (str?): Writes out file with main window state (positions of toolbars and dock controls).  
                Properties: create
        topEdge (Queryable[int]?): Top edge position of the window.  
                Properties: create, query, edit
        topLeftCorner (Queryable[Tuple[int, int]]?): Top and left edge position of the window.  
                Properties: create, query, edit
        width (Queryable[int]?): Width of the window.  
                Properties: create, query, edit
        widthHeight (Queryable[Tuple[int, int]]?): Width and height of the window.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

