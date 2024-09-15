from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def copyAttr(*args: str, edit: bool = ..., query: bool = ..., attribute: Multiuse[str] = ..., containerParentChild: bool = ..., inConnections: bool = ..., keepSourceConnections: bool = ..., outConnections: bool = ..., renameTargetContainer: bool = ..., values: bool = ...) -> bool:
    """Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes.
    The attributes flag can be used to specify a list of attributes to be
    processed. If the attributes flag is unused, all attributes will be
    processed. For dynamic attributes, the values and/or connections will only
    be transferred if the attributes names on both nodes match.
    This command does not support geometry shape nodes such as meshes, subds and
    nurbs. This command does not support transfer of multi-attribute values such
    as weight arrays.node, connection, copy, container
    Args:
        attribute (Multiuse[str]?): The name of the attribute(s) for which connections and/or values will be  
                transferred. If no attributes are specified, then all attributes will be  
                transferred.  
                Properties: create, multiuse
        containerParentChild (bool?): For use when copying from one container to another only. This option indicates  
                that the published parent and/or child relationships on the original container  
                should be transferred to the target container if the published names match.  
                Properties: create
        inConnections (bool?): Indicates that incoming connections should be transferred.  
                Properties: create
        keepSourceConnections (bool?): For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out connections on the source node will be broken and made to the target node.  
                Properties: create
        outConnections (bool?): Indicates that outgoing connections should be transferred.  
                Properties: create
        renameTargetContainer (bool?): For use when copying from one container to another only. This option will  
                rename the target container to the name of the original container, and  
                rename the original container to its old name + "Orig". You would want to  
                use this option if your original container was referenced and edited,  
                and you want those edits from the main scene to now apply to the  
                new container.  
                Properties: create
        values (bool?): Indicates that values should be transferred.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

