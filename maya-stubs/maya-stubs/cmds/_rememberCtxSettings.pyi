from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rememberCtxSettings(arg0: str = ..., /) -> bool:
    """This command restores a tool to its saved settings. This command must
    only be called once for each tool created and should be called at the
    point the tool is created.
    Returns:
        bool:

    Example:
    """

