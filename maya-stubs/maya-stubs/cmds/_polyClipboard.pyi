from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyClipboard(*args: str, clear: bool = ..., color: bool = ..., copy: bool = ..., paste: bool = ..., shader: bool = ..., uvCoordinates: bool = ...) -> bool:
    """The command allows the user to copy and paste certain polygonal
    attributes to a clipboard. These attributes are:
     1) Shader (shading engine) assignment.
     2) Texture coordinate (UV) assignment.
     3) Color value assignment.
    Any combination of attributes can be chosen for the copy or
    paste operation. If the attribute has not been copied
    to the clipboard, then naturally it cannot be pasted from
    the clipboard.
    The copy option will copy the attribute assignments from
    a single source polygonal dag object or polygon component.
    If the source does not have the either UV or color attributes,
    then nothing will be copied to the clipboard.
    The paste option will paste the attribute assignments to
    one or more polygon components or polygonal dag objects.
    If the destination does not have either UV or color attributes,
    then new values will be assigned as needed.
    Additionally, there is the option to clear the clipboard
    contentspoly, clipboard, uv, color, shaders
    Args:
        clear (bool?): When used, will mean to clear the specified attribute argument(s).  
                Properties: create
        color (bool?): When used, will be to copy or paste color attributes  
                Properties: create
        copy (bool?): When used, will mean to copy the specified attribute argument(s).  
                Properties: create
        paste (bool?): When used, will mean to paste the specified attribute argument(s).  
                Properties: create
        shader (bool?): When used, will be to copy or paste shader attributes  
                Properties: create
        uvCoordinates (bool?): When used, will be to copy or paste texture coordinate attributes  
                Properties: create

    Returns:
        bool: Success or Failure

    Example:
    """

