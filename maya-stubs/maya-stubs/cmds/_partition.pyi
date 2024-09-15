from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def partition(*args: str, edit: bool = ..., query: bool = ..., addSet: str = ..., name: str = ..., removeSet: str = ..., render: bool = ...) -> Union[str, bool]:
    """This command is used to create, query or add/remove sets to a
    partition. If a partition name needs to be specified, it is the first
    argument, other arguments represent the set names.Without any flags, the command will create a
    partition with a default name.  Any sets which are arguments
    to the command will be added to the partition.A set can be added to a partition only if none of its members
    are in any of the other sets in the partition. If the -re/render
    flag is specified when the partition is created, only 'renderable'
    sets can be added to the partition.Sets can be added and removed from a partition by using the
    -addSet or -removeSet flags.If a set is already selected, and the partition command is
    executed, the set will be added to the created partition.
    Args:
        addSet (str?): Adds the list of sets to the named partition.  
                Properties: create
        name (str?): Assigns the given name to new partition. Valid only for create mode.  
                Properties: create
        removeSet (str?): Removes the list of sets from the named partition.  
                Properties: create
        render (bool?): New partition can contain render sets.  
                For use in creation mode only. Default is false.  Can also  
                be used with query flag - returns boolean.  
                Properties: create, query

    Returns:
        str: Name of the partition that was created or edited

    Example:
    """

