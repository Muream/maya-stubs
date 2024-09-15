from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def movOut(*args: str, comment: bool = ..., file: str = ..., precision: int = ..., time: NullableRange[float] = ...) -> bool:
    """Exports a .mov file from the listed attributes. Valid attribute types
    are numeric attributes; time attributes; linear attributes; angular
    attributes; compound attributes made of the types listed previously;
    and multi attributes composed of the types listed previously.Length, angle, and time values will be written to the file in the
    user units.If an unsupported attribute type is requested, the action will fail.
    The .mov file may be read back into Maya using the movIn command.
    Args:
        comment (bool?): If true, the attributes written to the .mov file will be listed  
                in a commented section at the top of the .mov file. The default is  
                false.  
                Properties: create
        file (str?): The name of the .mov file. If no extension is used, a .mov will be  
                added.  
                Properties: create
        precision (int?): Sets the number of digits to the right of the decimal place in  
                the .mov file.  
                C: The default is 6.  
                Properties: create
        time (NullableRange[float]?): The time range to save as a .mov file. The default is the current  
                time range.  
                Properties: create

    Returns:
        bool:

    Example:
    """

