from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def buttonManip(arg0: Callable[..., Any] = ..., arg1: str = ..., /, *, icon: str = ...) -> bool:
    """This creates a button manipulator. This manipulator has a position in
    space and a triad manip for positioning. When you click on the top
    part of the manip, the command defined by the first argument is
    executed. The command is associated with the manipulator when it is
    created.If a dag object is included on the command line, the manip will be
    parented to the object. This means moving the object will move the
    manip. You can move the manip independently of the object using its
    triad.Note that a buttonManip may not be parented to more than one object.
    Args:
        icon (str?): Specify an icon to represent the manipulator.  
                Properties: create

    Returns:
        bool:

    Example:
    """

