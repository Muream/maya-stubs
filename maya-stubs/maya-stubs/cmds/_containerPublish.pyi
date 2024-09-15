from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def containerPublish(*args: str, edit: bool = ..., query: bool = ..., bindNode: Queryable[Tuple[str, str]] = ..., bindTemplateStandins: bool = ..., inConnections: bool = ..., mergeShared: bool = ..., outConnections: bool = ..., publishNode: Queryable[Tuple[str, str]] = ..., unbindNode: Queryable[str] = ..., unpublishNode: Queryable[str] = ...) -> Union[bool, Tuple[str, str], str]:
    """This is an accessory command to the container command which is used
    for some advanced publishing operations on the container. For example,
    the "publishConnections" flag on the container will publish all the
    connections, but this command can be used to publish just the inputs,
    outputs, or to collapse the shared inputs into a single attribute
    before publishing.publish, container
    Args:
        bindNode (Queryable[Tuple[str, str]]?): Bind the specified node to the published node name.  
                Properties: create, query, edit
        bindTemplateStandins (bool?): This flag will create a temporary stand-in attribute for any  
                attributes that exist in the template but are not already bound.  
                This enables you to set values for unbound attributes.  
                Properties: create, query, edit
        inConnections (bool?): Specifies that the unpublished connections to nodes in the container  
                from external nodes should be published.  
                Properties: create
        mergeShared (bool?): For use with the inConnections flag. Indicates that when an external  
                attribute connects to multiple internal attributes within the container, a  
                single published attribute should be used to correspond to all of the  
                internal attributes.  
                Properties: create
        outConnections (bool?): Specifies that the unpublished connections from nodes in the container  
                to external nodes should be published.  
                Properties: create
        publishNode (Queryable[Tuple[str, str]]?): Publish a name and type. When first published, nothing will be bound.  
                To bind a node to the published name, use the bindNode flag.  
                Properties: create, query, edit
        unbindNode (Queryable[str]?): Unbind the node that is published with the name specified by the flag.  
                Properties: create, query, edit
        unpublishNode (Queryable[str]?): Unpublish the specified published node name.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

