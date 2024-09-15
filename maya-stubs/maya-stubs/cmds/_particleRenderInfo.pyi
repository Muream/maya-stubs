from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def particleRenderInfo(*, query: bool = ..., attrList: Queryable[int] = ..., attrListAll: bool = ..., name: Queryable[int] = ..., renderTypeCount: bool = ...) -> Union[bool, int]:
    """This action provides information access to the particle
    render subclasses. These are derived from TdynRenderBase.
    This action is used primarily by the Attribute Editor to
    gather information about attributes used for rendering.
    Args:
        attrList (Queryable[int]?): Return the list of attributes used by this render type.  
                Properties: query
        attrListAll (bool?): Return a complete list of all render attributes used by the  
                particle object. This also includes the per particle attributes.  
                Properties: query
        name (Queryable[int]?): Return the name of the render subclass using the render type.  
                Properties: query
        renderTypeCount (bool?): Return the count of registered render classes for particle.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

