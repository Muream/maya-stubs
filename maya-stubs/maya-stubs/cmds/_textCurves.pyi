from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def textCurves(*args: str, edit: bool = ..., query: bool = ..., font: str = ..., name: str = ..., object: bool = ..., text: str = ...) -> List[str]:
    """The textCurves command creates NURBS curves from a text string
    using the specified font.A single letter can be made up of more than one NURBS curve.
    The number of curves per letter varies with the font.
    Args:
        font (str?): The font to use.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        text (str?): The string to create the curves for.  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

