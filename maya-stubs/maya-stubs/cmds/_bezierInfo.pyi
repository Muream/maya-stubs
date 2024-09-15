from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bezierInfo(*, anchorFromCV: int = ..., cvFromAnchor: int = ..., isAnchorSelected: bool = ..., isTangentSelected: bool = ..., onlyAnchorsSelected: bool = ..., onlyTangentsSelected: bool = ...) -> int:
    """This command provides a queryable interface for Bezier curve shapes.
    Args:
        anchorFromCV (int?): Returns the Bezier anchor index from a given CV index  
                Properties: create
        cvFromAnchor (int?): Returns the CV index for a given Bezier anchor index  
                Properties: create
        isAnchorSelected (bool?): Returns 1 if an anchor CV is currently selected. 0, otherwise.  
                Properties: create
        isTangentSelected (bool?): Returns 1 if a tangent CV is currently selected. 0, otherwise.  
                Properties: create
        onlyAnchorsSelected (bool?): Returns 1 if the only CV components selected are anchor CVs. 0, otherwise.  
                Properties: create
        onlyTangentsSelected (bool?): Returns 1 if the only CV components selected are tangent CVs. 0, otherwise.  
                Properties: create

    Returns:
        int: Queried value

    Example:
    """

