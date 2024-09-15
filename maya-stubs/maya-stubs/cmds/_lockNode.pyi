from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lockNode(*args: str, query: bool = ..., ignoreComponents: bool = ..., lock: bool = ..., lockName: bool = ..., lockUnpublished: bool = ...) -> Union[None, List[bool], bool]:
    """Locks or unlocks one or more dependency nodes. A locked node is restricted
    in the following ways:Note that an unlocked attribute of a locked node may still have its value
    set, or connections to it made or broken. For more information on attribute
    locking, see thecommand.If no node names are specified then the current selection list is used.There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on unconnected
    attributes may not be modified. Parenting is allowed to change on members of locked
    containers that have been published as parent or child anchors.node, dependency, graph, lock
    Args:
        ignoreComponents (bool?): Normally, the presence of a component in the list of objects to be locked  
                will cause the command to fail with an error. But if this flag is supplied  
                then components will be silently ignored.  
                Properties: create, query
        lock (bool?): Specifies the new lock state for the node. The default is true.  
                Properties: create, query
        lockName (bool?): Specifies the new lock state for the node's name.  
                Properties: create, query
        lockUnpublished (bool?): Used in conjunction with the lock flag. On a container, lock or unlock all  
                unpublished attributes on the members of the container. For non-containers,  
                lock or unlock unpublished attributes on the specified node.  
                Properties: create, query

    Returns:
        None: For regular command execution.
        List[bool]: For query execution.

    Example:
    """

