from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def manipPivot(*, query: bool = ..., bakeOri: bool = ..., moveToolOri: int = ..., ori: Queryable[Tuple[float, float, float]] = ..., oriValid: bool = ..., pinPivot: bool = ..., pos: Queryable[Tuple[float, float, float]] = ..., posValid: bool = ..., reset: bool = ..., resetMode: Queryable[int] = ..., resetOri: bool = ..., resetPos: bool = ..., rotateToolOri: int = ..., scaleToolOri: int = ..., snapOri: bool = ..., snapPos: bool = ..., valid: bool = ...) -> Union[bool, Tuple[float, float, float], int]:
    """Changes transform component pivot used by the move/rotate/scale manipulators.
    Args:
        bakeOri (bool?): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.  
                Properties: create, query
        moveToolOri (int?): Change move tool's axis orientation to the specified mode. This flag is the same  
                as using "manipMoveContext -e -mode" on the Move tool except that this command  
                is undoable.  
                Properties: create
        ori (Queryable[Tuple[float, float, float]]?): Component pivot orientation in world-space.  
                Properties: create, query
        oriValid (bool?): Returns true if component pivot orientation is valid.  
                Properties: query
        pinPivot (bool?): Pin component pivot. Selection changes will not reset the pivot position/orientation  
                when a custom pivot is set and pinning is on.  
                Properties: create, query
        pos (Queryable[Tuple[float, float, float]]?): Component pivot position in world-space.  
                Properties: create, query
        posValid (bool?): Returns true if component pivot position is valid.  
                Properties: query
        reset (bool?): Clear the saved component pivot position and orientation.  
                Properties: create
        resetMode (Queryable[int]?): Specifies the mode used when resetting the pivot position. Available modes are:  
              
                0. Center pivot (on bounding box)  
                1. Zero pivot (object-space origin)  
                Properties: query
        resetOri (bool?): Clear the saved component pivot orientation.  
                Properties: create
        resetPos (bool?): Clear the saved component pivot position.  
                Properties: create
        rotateToolOri (int?): Change rotate tool's axis orientation to the specified mode. This flag is the same  
                as using "manipRotateContext -e -mode" on the Rotate tool except that this command  
                is undoable.  
                Properties: create
        scaleToolOri (int?): Change scale tool's axis orientation to the specified mode. This flag is the same  
                as using "manipScaleContext -e -mode" on the Scale tool except that this command  
                is undoable.  
                Properties: create
        snapOri (bool?): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.  
                Properties: create, query
        snapPos (bool?): Snap pivot position. Modify pivot position when snapping the pivot to a component.  
                Properties: create, query
        valid (bool?): Returns true if component pivot position or orientation is valid.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

