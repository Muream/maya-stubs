from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCheck(*args: str, edge: bool = ..., face: bool = ..., faceOffset: bool = ..., openFile: str = ...) -> int:
    """Dumps a description of internal memory representation of poly objects.If no objects are specified in the command line, the
    objects from the active list are used.Default behaviour is to print only a summary. Use the flags
    above to get more details on a specific part of the object.
    Args:
        edge (bool?): Check edge descriptions.  
                If no flag is set, a complete check is performed.  
                Properties: create
        face (bool?): Check face descriptions.  
                If no flag is set, a complete check is performed.  
                Properties: create
        faceOffset (bool?): Check face offset descriptions.  
                If no flag is set, a complete check is performed.  
                Properties: create
        openFile (str?): Opens a file that contains a poly description,  
                as dumped out by the debug commands.  
                Properties: create

    Returns:
        int: The number of errors.

    Example:
    """

