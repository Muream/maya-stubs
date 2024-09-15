from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsSelect(*args: str, borderSelection: bool = ..., bottomBorder: bool = ..., growSelection: int = ..., leftBorder: bool = ..., rightBorder: bool = ..., shrinkSelection: int = ..., topBorder: bool = ...) -> bool:
    """Performs selection operations on NURBS objects.If any of the border flags is set, then the appropriate borders are
    selected. Otherwise the current CV selection is used, or all CVs if
    the surfaces is selected as an object.The growSelection, shrinkSelection, borderSelection flags are then applied
    in that order.In practice, it is recommended to use one flag at a time, except for
    the border flags.texture, uv, image
    Args:
        borderSelection (bool?): Extract the border of the current CV selection.  
                Properties: create
        bottomBorder (bool?): Selects the bottom border of the surface (V=0).  
                Properties: create
        growSelection (int?): Grows the CV selection by the given number of CV  
                Properties: create
        leftBorder (bool?): Selects the left border of the surface (U=0).  
                Properties: create
        rightBorder (bool?): Selects the right border of the surface (U=MAX).  
                Properties: create
        shrinkSelection (int?): Shrinks the CV selection by the given number of CV  
                Properties: create
        topBorder (bool?): Selects the top border of the patches (V=MAX).  
                Properties: create

    Returns:
        bool:

    Example:
    """

