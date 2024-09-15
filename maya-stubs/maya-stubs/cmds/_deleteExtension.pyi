from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deleteExtension(*, attribute: str = ..., forceDelete: bool = ..., nodeType: str = ...) -> int:
    """This command is used to delete an extension attribute
    from a node type. The attribute can be specified
    by using either the long or short name. Only one
    extension attribute can be deleted at a time.
    Children of a compound attribute cannot be deleted,
    you must delete the complete compound attribute.
    This command has no undo, edit, or query capabilities.attribute, dependency, graph, delete, extension
    Args:
        attribute (str?): Specify either the long or short name of the attribute.  
                Properties: create
        forceDelete (bool?): If this flag is set and turned ON then data values for the extension  
                attributes are all deleted without confirmation. If it's set and turned  
                OFF then any extension attributes that have non-default values set on any  
                node will remain in place. If this flag is not set at all then the user  
                will be asked if they wish to preserve non-default values on this  
                attribute.  
                Properties: create
        nodeType (str?): The name of the node type.  
                Properties: create

    Returns:
        int: Number of nodes with altered data after the delete

    Example:
    """

