from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySlideEdge(*args: str, absolute: bool = ..., direction: int = ..., edgeDirection: float = ..., symmetry: bool = ...) -> bool:
    """Moves an edge loop selection along the edges connected to the sides of
    its vertices.
    Args:
        absolute (bool?): This flag specifies whether or not the command uses absolute mode  
                If in absolute then all vertices will move the same distance (the  
                specified percentage of the smallest edge)  
                C: Default is off  
                Properties: create
        direction (int?): This flag specifies the direction of the slide edge movement  
                0. is left direction (relative)  
                1. is right direction (relative)  
                2. is normal direction (relative)  
                C: Default is 0  
                Properties: create
        edgeDirection (float?): This flag specifies the relative percentage to move along the edges on  
                either side of the vertices along the edge loop  
                C: Default is 0.0  
                Properties: create
        symmetry (bool?): This flag specifies whether or not the command will do a symmetrical slide. Only takes effect  
                when symmetry is enabled.  
                C: Default is off  
                Properties: create

    Returns:
        bool: Success value

    Example:
    """

