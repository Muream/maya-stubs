from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyMultiLayoutUV(*args: str, flipReversed: bool = ..., gridU: int = ..., gridV: int = ..., layout: int = ..., layoutMethod: int = ..., offsetU: float = ..., offsetV: float = ..., percentageSpace: float = ..., prescale: int = ..., rotateForBestFit: int = ..., scale: int = ..., sizeU: float = ..., sizeV: float = ..., uvSetName: str = ...) -> bool:
    """place the UVs of the selected polygonal objects so that they do not overlap.poly, uv, map, placement
    Args:
        flipReversed (bool?): If this flag is turned on, the reversed UV pieces are fliped.  
                Properties: create
        gridU (int?): The U size of the grids.  
                Properties: create
        gridV (int?): The V size of the grids.  
                Properties: create
        layout (int?): How to move the UV pieces, after cuts are applied:  
                0 No move is applied.  
                1 Layout the pieces along the U axis.  
                2 Layout the pieces in a square shape.  
                3 Layout the pieces in grids.  
                4 Layout the pieces in nearest regions.  
                Properties: create
        layoutMethod (int?): // -lm/layoutMethod     layoutMethod  integer  
                //      (C, E, Q) Which layout method to use:  
                //              0 Block Stacking.  
                //              1 Shape Stacking.  
                Properties: create
        offsetU (float?): Offset the layout in the U direction by the given value.  
                Properties: create
        offsetV (float?): Offset the layout in the V direction by the given value.  
                Properties: create
        percentageSpace (float?): When layout is set to square, this value is a percentage of  
                the texture area which is added around each UV piece. It can be  
                used to ensure each UV piece uses different pixels in the texture.  
                Maximum value is 5 percent.  
                Properties: create
        prescale (int?): Prescale the shell before laying it out.  
                0 No scale is applied.  
                1 Object space scaling applied.  
                2 World space scaling applied.  
                Properties: create
        rotateForBestFit (int?): How to rotate the pieces, before move:  
                0 No rotation is applied.  
                1 Only allow 90 degree rotations.  
                2 Allow free rotations.  
                Properties: create
        scale (int?): How to scale the pieces, after move:  
                0 No scale is applied.  
                1 Uniform scale to fit in unit square.  
                2 Non proportional scale to fit in unit square.  
                Properties: create
        sizeU (float?): Scale the layout in the U direction by the given value.  
                Properties: create
        sizeV (float?): Scale the layout in the V direction by the given value.  
                Properties: create
        uvSetName (str?): Specifies the name of the uv set to edit uvs on. If not  
                specified will use the current uv set if it exists.  
                Properties: create

    Returns:
        bool:

    Example:
    """

