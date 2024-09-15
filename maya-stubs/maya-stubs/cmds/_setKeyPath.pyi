from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setKeyPath(*args: str) -> List[str]:
    """The setKeyPath command either creates or edits the path (a nurbs curve)
    based on the current position of the selected object at the current time.
    Returns:
        List[str]: (Names of the created curve node and motionPath node)

    Example:
    """

