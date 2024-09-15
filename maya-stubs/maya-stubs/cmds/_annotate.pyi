from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def annotate(*args: str, point: Tuple[float, float, float] = ..., text: str = ...) -> str:
    """This command is used to create an annotation to be attached to the
    specified objects at the specified point.
    Args:
        point (Tuple[float, float, float]?): Specifies the point about which the annotation text is to be  
                centered.  
                Properties: create
        text (str?): Specifies the annotation text.  
                Properties: create

    Returns:
        str: Annotation added

    Example:
    """

