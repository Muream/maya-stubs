from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def webBrowserPrefs(arg0: str = ..., /) -> None:
    """This command is obsolete and will be removed in a future version of Maya.
    The internal web browser of Maya has been replaced by a plug-in which allows your own browser to connect with Maya.
    Please refer help for information on how to setup communication of Maya with external web browser application.
    """

