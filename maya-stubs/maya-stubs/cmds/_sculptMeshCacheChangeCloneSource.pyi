from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sculptMeshCacheChangeCloneSource(*args: Any, edit: bool = ..., query: bool = ..., blendShape: Queryable[str] = ..., target: Queryable[str] = ...) -> Union[bool, str]:
    """This command changes the source blend shape and target for the
    clone target tool. Used internally for undo/redo, and should not be called directly.
    Args:
        blendShape (Queryable[str]?): Set which blend shape should be used as the source when using the clone tool. When queried,  
                returns the current blend shape name as a string.  
                Properties: create, query, edit
        target (Queryable[str]?): Set which blend shape should be used as the target when using the clone tool. When queried,  
                returns the current blend shape target name as a string.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

