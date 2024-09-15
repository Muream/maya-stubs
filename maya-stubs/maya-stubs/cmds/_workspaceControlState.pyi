from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def workspaceControlState(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., defaultTopLeftCorner: Queryable[Tuple[int, int]] = ..., defaultWidthHeight: Queryable[Tuple[int, int]] = ..., exists: bool = ..., height: Queryable[int] = ..., leftEdge: Queryable[int] = ..., maximized: bool = ..., remove: bool = ..., topEdge: Queryable[int] = ..., topLeftCorner: Queryable[Tuple[int, int]] = ..., width: Queryable[int] = ..., widthHeight: Queryable[Tuple[int, int]] = ...) -> Union[bool, Tuple[int, int], int]:
    """Create or modify preferred window attributes for workspace controls.
    The size and position of a workspace control is retained during application
    sessions (although position only applies to workspace controls that are
    alone in a floating workspace docking panel). A default workspace control
    state is created when a workspace control is closed. Workspace control
    states must be named and, consequently, only affect the workspace control
    with a matching name.
    Args:
        defaultTopLeftCorner (Queryable[Tuple[int, int]]?): Top and left edge position that the window will have when "Remember size and position" is off and when the panel is first opened.  
                The values will be DPI scaled on edit and the value in query is returned unscaled.  
                This value will only be used if the default width and height are also valid.  
                Properties: create, query, edit
        defaultWidthHeight (Queryable[Tuple[int, int]]?): Width and height that the window will have when "Remember size and position" is off and when the panel is first opened.  
                The values will be DPI scaled on edit and the value in query is returned unscaled.  
                The position used in that case is defaultTopLeftCorner.  
                Properties: create, query, edit
        exists (bool?): Returns true|false depending upon whether the specified object  
                exists. Other flags are ignored.  
                Properties: create
        height (Queryable[int]?): Height of the window.  
                Properties: create, query, edit
        leftEdge (Queryable[int]?): Left edge position of the window.  
                Properties: create, query, edit
        maximized (bool?): Maximize the window.  
                Properties: create, query, edit
        remove (bool?): Remove a window preference.  
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

