from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def applyAttrPattern(*args: str, nodeType: str = ..., patternName: str = ...) -> int:
    """Take the attribute structure described by a pre-defined pattern and apply it either to a
    node (as dynamic attributes) or a node type (as extension attributes). The same pattern
    can be applied more than once to different nodes or node types as the operation duplicates
    the attribute structure described by the pattern.  See the 'createAttrPatterns' command
    for a description of how to create a pattern.attribute, pattern
    Args:
        nodeType (str?): Name of the node type to which the attribute pattern is to be applied. This flag  
                will cause a new extension attribute tree to be created, making the new attributes  
                available on all nodes of the given type. If it is not specified then either a node  
                name must be specified or a node must be selected for application of dynamic  
                attributes.  
                Properties: create
        patternName (str?): The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.  
                Properties: create

    Returns:
        int: Number of nodes or node types to which the attribute were added

    Example:
    """

