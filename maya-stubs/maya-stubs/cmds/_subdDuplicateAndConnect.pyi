from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdDuplicateAndConnect(*args: str) -> bool:
    """This command duplicates the input subdivision surface object, connects
    up the outSubdiv attribute of the original subd shape to
    the create attribute of the newly created duplicate shape and
    copies over the shader assignments from the original shape
    to the new duplicated shape.The command will fail if no objects are selected or sent as
    argument or if the object sent as argument is not a subdivision surface
    object.
    Returns:
        bool:

    Example:
    """

