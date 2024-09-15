from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCutUVCtx(*args: Any, edit: bool = ..., query: bool = ..., loopSpeed: Queryable[int] = ..., mapBordersColor: Queryable[Tuple[float, float, float]] = ..., showCheckerMap: bool = ..., showTextureBorders: bool = ..., showUVShellColoring: bool = ..., steadyStroke: bool = ..., steadyStrokeDistance: Queryable[float] = ..., symmetry: Queryable[int] = ...) -> Union[bool, float, int, Tuple[float, float, float]]:
    """Create a new context to cut UVs on polygonal objects
    Args:
        loopSpeed (Queryable[int]?): Edit the speed of loop cutting.  
                Properties: query, edit
        mapBordersColor (Queryable[Tuple[float, float, float]]?): Color of UV map border edges in 3d view.  
                Properties: query, edit
        showCheckerMap (bool?): Display checker map.  
                Properties: query, edit
        showTextureBorders (bool?): Display texture border edges.  
                Properties: query, edit
        showUVShellColoring (bool?): Turn on UV shell coloring or not.  
                Properties: query, edit
        steadyStroke (bool?): Turn on steady stroke or not.  
                Properties: query, edit
        steadyStrokeDistance (Queryable[float]?): The distance for steady stroke.  
                Properties: query, edit
        symmetry (Queryable[int]?): Symmetric modeling.  
                Properties: query, edit

    Returns:
        bool: Whether steady stroke is on or not, when querying the steadyStroke flag.
        float: The distance for a steady stroke, when querying the steadyStrokeDistance flag.

    Example:
    """

