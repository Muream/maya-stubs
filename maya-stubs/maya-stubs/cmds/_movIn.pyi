from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def movIn(*args: str, file: str = ..., startTime: int = ...) -> bool:
    """Imports a .mov file into animation curves connected to  the listed
    attributes. The attribute must be writable, since an animation curve
    will be created and connected to the attribute. If an animation curve
    already is connected to the attribute, the imported data is pasted onto
    that curve.The starting time used for the .mov file importation is the current time
    when the command is executed.Valid attribute types are numeric attributes; time attributes; linear
    attributes; angular attributes; compound attributes made of the types
    listed previously; and multi attributes composed of the types listed
    previously. If an unsuppoted attribute type is requested, the command
    will fail and no data will be imported. It is important that your
    user units are set to the same units used in the .mov file, otherwise
    linear and angular values will be incorrect.To export a .mov file, use the movOut command.
    Args:
        file (str?): The name of the .mov file. If no extension is used, a .mov will be  
                added.  
                Properties: create
        startTime (int?): The default start time for importing the .mov file is the  
                current time. The startTime option sets the starting time for  
                the .mov data in the current time unit.  
                Properties: create

    Returns:
        bool:

    Example:
    """

