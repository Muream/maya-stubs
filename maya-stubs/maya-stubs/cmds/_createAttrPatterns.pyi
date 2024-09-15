from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createAttrPatterns(*, patternDefinition: str = ..., patternFile: str = ..., patternType: str = ...) -> str:
    """Create a new instance of an attribute pattern given a pattern type (e.g. XML) and a string or data file
    containing the description of the attribute tree in the pattern's format.attribute, pattern
    Args:
        patternDefinition (str?): Hardcoded string containing the pattern definition, for simpler formats that  
                don't really need a separate file for definition.  
                Properties: create
        patternFile (str?): File where the pattern information can be found  
                Properties: create
        patternType (str?): Name of the pattern definition type to use in creating this instance  
                of the pattern.  
                Properties: create

    Returns:
        str: Name of created pattern

    Example:
    """

