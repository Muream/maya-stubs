from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pairBlend(*args: str, edit: bool = ..., query: bool = ..., attribute: Multiuse[str] = ..., input1: bool = ..., input2: bool = ..., node: str = ...) -> Union[str, bool]:
    """The pairBlend node allows a weighted combinations of 2 inputs to be blended together. It is created automatically when keying or constraining an attribute which is already connected.Alternatively, the pairBlend command can be used to connect a pairBlend node to connected attributes of a node. The previously existing connections are rewired to input1 of the pairBlend node. Additional connections can then be made manually to input2 of the pairBlend node.The pairBlend command can also be used to query the inputs to an existing pairBlend node.blend, animation, constraints
    Args:
        attribute (Multiuse[str]?): The name of the attribute(s) which the blend will drive. This flag is required when creating the blend.  
                Properties: create, multiuse
        input1 (bool?): Returns a string array of the node(s) connected to input 1.  
                Properties: query
        input2 (bool?): Returns a string array of the node(s) connected to input 2.  
                Properties: query
        node (str?): The name of the node which the blend will drive. This flag is required when creating the blend.  
                Properties: create

    Returns:
        str: name of pairBlend node

    Example:
    """

