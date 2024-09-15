from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deleteAttrPattern(*, allPatterns: bool = ..., patternName: str = ..., patternType: str = ...) -> str:
    """After a while the list of attribute patterns could become cluttered.
    This command provides a way to remove patterns from memory so that only
    the ones of interest will show.attribute, pattern
    Args:
        allPatterns (bool?): If specified it means delete all known attribute patterns.  
                Properties: create
        patternName (str?): The name of the pattern to be deleted.  
                Properties: create
        patternType (str?): Delete all patterns of the given type.  
                Properties: create

    Returns:
        str: Name(s) of deleted pattern(s)

    Example:
    """

