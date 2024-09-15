from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setRenderPassType(*args: str, defaultDataType: bool = ..., numChannels: int = ..., type: str = ...) -> bool:
    """This command will set the passID of a renderPass node and
    create the custom attributes specified by the corresponding render pass
    definition.  If the render pass
    node already has a passID assigned to it, attributes that are no longer
    required become hidden, and new attributes are unhidden and/or created as
    needed.  This allows passIDs to be changed back and forth without losing
    attribute data.  It also allows common attributes to be transported from one
    render pass type to another.render, layer,, pass
    Args:
        defaultDataType (bool?): If set, the render pass will use its default data type.  
                Properties: create
        numChannels (int?): Specify the number of channels to use in the render pass. Note that  
                this flag is only valid if there is an implementation supporting the  
                requested number of channels.  
                Properties: create
        type (str?): Specify the pass type to assign to the pass node(s).  
                Properties: create

    Returns:
        bool: true/false

    Example:
    """

