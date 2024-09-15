from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def spaceLocator(*args: str, edit: bool = ..., query: bool = ..., absolute: bool = ..., name: str = ..., position: Queryable[Tuple[float, float, float]] = ..., relative: bool = ...) -> Union[List[str], Tuple[float, float, float]]:
    """The command creates a locator at the specified position
    in space. By default it is created at (0,0,0).
    Args:
        absolute (bool?): If set, the locator's position is in world space.  
                Properties: create, edit
        name (str?): Name for the locator.  
                Properties: create, edit
        position (Queryable[Tuple[float, float, float]]?): Location in  3. dimensional space where locator is to be created.  
                Properties: create, query, edit
        relative (bool?): If set, the locator's position is relative to its local space. The locator is created in relative mode by default.  
                Properties: create, edit

    Returns:
        List[str]: The name for the new locator in space.

    Example:
    """

