from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def allNodeTypes(*, includeAbstract: bool = ...) -> List[str]:
    """This command returns a list containing the type names of every kind of
    creatable node registered with the system. Note that some node types are
    abstract and cannot be created. These will not show up on this list.
    (e.g. transform and polyShape both inherit from dagObject, but dagObject
     cannot be created directly so it will not appear on this list.)debug, node, type, graph
    Args:
        includeAbstract (bool?): Show every node type, even the abstract ones which cannot be created  
                via the 'createNode' command. These will have the suffix "(abstract)" appended  
                to them in the list.  
                Properties: create

    Returns:
        List[str]: List of node types

    Example:
    """

