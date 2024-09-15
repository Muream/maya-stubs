from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attrCompatibility(arg0: str = ..., arg1: str = ..., /, *, addAttr: bool = ..., clear: bool = ..., dumpTable: bool = ..., enable: bool = ..., nodeRename: str = ..., pluginNode: str = ..., renameAttr: str = ..., removeAttr: bool = ..., type: str = ..., version: str = ...) -> None: ...
