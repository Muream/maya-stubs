from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def group(*args: str, absolute: bool = ..., empty: bool = ..., name: str = ..., parent: str = ..., relative: bool = ..., useAsGroup: str = ..., world: bool = ...) -> str:
    """This command groups the specified objects under a new group
    and returns the name of the new group.If the -em flag is specified, then an empty group (with no
    objects) is created.If the -w flag is specified then the new group is placed under the
    world, otherwise if -p is specified it is placed under the
    specified node. If neither -w or -p is specified the new group is
    placed under the lowest common group they have in common. (or the
    world if no such group exists)If an object is grouped with another object that has the same name
    then one of the objects will be renamed by this command.
    Args:
        absolute (bool?): preserve existing world object transformations  
                (overall object transformation is preserved  
                by modifying the objects local transformation)  
                [default]  
                Properties: create
        empty (bool?): create an empty group (with no objects in it)  
                Properties: create
        name (str?): Assign given name to new group node.  
                Properties: create
        parent (str?): put the new group under the given parent  
                Properties: create
        relative (bool?): preserve existing local object transformations  
                (relative to the new group node)  
                Properties: create
        useAsGroup (str?): Use the specified node as the group node. The specified node must be  
                derived from the transform node and must not have any existing parents  
                or children.  
                Properties: create
        world (bool?): put the new group under the world  
                Properties: create

    Returns:
        str: - name of the group node

    Example:
    """

