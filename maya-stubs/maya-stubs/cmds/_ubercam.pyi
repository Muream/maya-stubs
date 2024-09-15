from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ubercam(arg0: str = ..., /) -> str:
    """Use this command to create a "ubercam" with equivalent behavior
    to all cameras used by shots in the sequencer.sequencer, shot, camera
    Returns:
        str: Ubercam name

    Example:
    """

