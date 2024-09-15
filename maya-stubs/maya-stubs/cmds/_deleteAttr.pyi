from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deleteAttr(*args: str, edit: bool = ..., query: bool = ..., attribute: str = ...) -> bool:
    """This command is used to delete a dynamic attribute
    from a node or nodes. The attribute can be specified
    by using either the long or short name. Only one
    dynamic attribute can be deleted at a time. Static
    attributes cannot be deleted. Children of a compound
    attribute cannot be deleted. You must delete the
    complete compound attribute. This command has no
    edit capabilities. The only query ability is to list
    all the dynamic attributes of a node.
    Args:
        attribute (str?): Specify either the long or short name of the attribute.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

