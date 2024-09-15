from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listAttrPatterns(*, patternType: bool = ..., verbose: bool = ...) -> List[str]:
    """Attribute patterns are plain text descriptions of an entire Maya attribute forest. ("forest"
    because there could be an arbitrary number of root level attributes, it's not restricted to
    having a single common parent though in general that practice is a good idea.)
    This command lists the various pattern types available, usually created via plugin, as well as
    any specific patterns that have already been instantiated. A pattern type is a thing that knows
    how to take some textual description of an attribute tree, e.g. XML or plaintext, and convert it
    into an attribute pattern that can be applied to any node or node type in Maya.attribute, pattern
    Args:
        patternType (bool?): If turned on then show the list of pattern types rather than actual instantiated patterns.  
                Properties: create
        verbose (bool?): If turned on then show detailed information about the patterns or pattern types.  
                The same list of instance or pattern names is returned as for the non-verbose case.  
                Properties: create

    Returns:
        List[str]: List of patterns or pattern instances available

    Example:
    """

