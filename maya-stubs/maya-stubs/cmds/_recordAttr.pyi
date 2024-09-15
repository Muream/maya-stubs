from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def recordAttr(*args: str, query: bool = ..., attribute: Multiuse[str] = ..., delete: bool = ...) -> bool:
    """This command sets up an attribute to be recorded.  When
    the record command is executed, any changes to this attribute
    are recorded.  When recording stops these changes are turned
    into keyframes.If no attributes are specified all attributes of the node
    are recorded.When the query flag is used, a list of the attributes being recorded will be returned.
    Args:
        attribute (Multiuse[str]?): specify the attribute to record  
                Properties: create, multiuse
        delete (bool?): Do not record the specified attributes  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

