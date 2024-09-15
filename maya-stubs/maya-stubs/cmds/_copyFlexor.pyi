from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def copyFlexor(*args: str) -> str:
    """This command copies an existing bone or joint flexor from one
    bone (joint) to another.  The attributes of the flexor and their
    connections as well as any tweaks in on the latticeFfd are copied
    from the original to the new flexor.  If the selected bone (joint)
    appears to be a mirror reflection of the bone (joint) of the
    existing flexor then the transform of the ffd lattice group gets
    reflected to the new bone (joint).  The arguments for the command
    are the name of the ffd Lattice and the name of the destination joint.
    If they are not specified at the command line, they will be picked
    up from the current selection list.
    Returns:
        str: The name of the new flexor node

    Example:
    """

