from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def suitePrefs(*, applyToSuite: str = ..., installedAsSuite: bool = ..., isCompleteSuite: bool = ...) -> bool:
    """This command sets the mouse and keyboard interaction mode
    for Maya and other Suites applications (if Maya is part of
    a Suites install).
    Args:
        applyToSuite (str?): Apply the mouse and keyboard interaction settings  
                for the given application to all applications in the  
                Suite (if Maya is part of a Suites install). Valid  
                values are "Maya", "3dsMax", or "undefined", which  
                signifies that each app is to use their own settings.  
                Properties: create
        installedAsSuite (bool?): Returns true if Maya is part of a Suites install, false  
                otherwise.  
                Properties: create
        isCompleteSuite (bool?): Returns true if the Suites install contains all Entertainment  
                Creation Suite products, false otherwise.  
                Properties: create

    Returns:
        bool:

    Example:
    """

