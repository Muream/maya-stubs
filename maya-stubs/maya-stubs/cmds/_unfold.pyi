from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def unfold(*args: str, applyToShell: bool = ..., areaWeight: float = ..., globalBlend: float = ..., globalMethodBlend: float = ..., iterations: int = ..., optimizeAxis: int = ..., pinSelected: bool = ..., pinUvBorder: bool = ..., scale: float = ..., stoppingThreshold: float = ..., useScale: bool = ...) -> int:
    """Nonepoly, uv, map, border, relax
    Args:
        applyToShell (bool?): Specifies that the selected components should be only work on shells that  
                have something have been selected or pinned.  
                Properties: create
        areaWeight (float?): Surface driven importance. 0 treat all faces equal. 1 gives more importance to large ones.  
                Properties: create
        globalBlend (float?): This allows the user to blend between a local optimization method  
                (globalBlend = 0.0) and a global optimization method  
                (globalBlend = 1.0). The local optimization method looks at the  
                ratio between the triangles on the object and the triangles in UV  
                space.  It has a side affect that it can sometimes introduce tapering  
                problems.  The global optimization is much slower, but takes into  
                consideration the entire object when optimizing uv placement.  
                Properties: create
        globalMethodBlend (float?): The global optimization method uses two functions to compute  
                a minimization.  The first function controls edge  
                stretch by using edges lengths between xyz and uv.  The second  
                function penalizes the first function by preventing  
                configurations where triangles would overlap.  For every surface  
                there is a mix between these two functions that will give the  
                appropriate response. Values closer to 1.0 give more weight to  
                the edge length function. Values closer to 0.0 give more weight to  
                surface area.  The default value of '0.5' is a even mix  
                between these two values.  
                Properties: create
        iterations (int?): Maximum number of iterations for each connected UV piece.  
                Properties: create
        optimizeAxis (int?): Degree of freedom for optimization  
                0=Optimize freely, 1=Move vertically only, 2=Move horzontally only  
                Properties: create
        pinSelected (bool?): Specifies that the selected components should be pinned instead  
                the unselected components.  
                Properties: create
        pinUvBorder (bool?): Specifies that the UV border should be pinned when doing the solve.  
                By default only unselected components are pinned.  
                Properties: create
        scale (float?): Ratio between 2d and 3d space.  
                Properties: create
        stoppingThreshold (float?): Minimum distorsion improvement between two steps in %.  
                Properties: create
        useScale (bool?): Adjust the scale or not.  
                Properties: create

    Returns:
        int: the number of relaxation iterations carried out

    Example:
    """

