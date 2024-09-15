from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def contextInfo(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., c: bool = ..., escapeContext: bool = ..., exists: bool = ..., image1: bool = ..., image2: bool = ..., image3: bool = ..., title: bool = ...) -> str:
    """This command allows you to get information on named contexts.
    Args:
        c (bool?): Return the class type of the named context.  
                Properties: create
        escapeContext (bool?): Return the command string that will allow you to exit the current tool.  
                Properties: create
        exists (bool?): Return true if the context exists, false if it does not  
                exists (or is internal and therefore untouchable)  
                Properties: create
        image1 (bool?): Returns the name of an xpm associated with the named context.  
                Properties: create
        image2 (bool?): Returns the name of an xpm associated with the named context.  
                Properties: create
        image3 (bool?): Returns the name of an xpm associated with the named context.  
                Properties: create
        title (bool?): Return the title string of the named context.  
                Properties: create

    Returns:
        str: Info requested

    Example:
    """

