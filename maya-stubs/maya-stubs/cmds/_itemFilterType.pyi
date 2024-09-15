from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def itemFilterType(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., text: Queryable[str] = ..., type: bool = ...) -> Union[str, List[str], bool]:
    """This command queries a named itemFilter object.  This object
    can be attached to selectionConnection objects, or to editors,
    in order to filter the item lists going through them.  Using
    union and intersection filters, complex composite filters can
    be created.
    Args:
        text (Queryable[str]?): Defines an annotation string to be stored with the filter  
                Properties: query, edit
        type (bool?): Query the type of the filter object. Possible return values are:  
                itemFilter, attributeFilter, renderFilter, or unknownFilter.  
                Properties: query

    Returns:
        str: Single command result
        List[str]: Multiple command result

    Example:
    """

