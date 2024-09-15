from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ungroup(*args: str, absolute: bool = ..., parent: str = ..., relative: bool = ..., world: bool = ...) -> bool:
    """This command ungroups the specified objects.The objects will be placed at the same level in the hierarchy the
    group node occupied unless the -w flag is specified, in which case
    they will be placed under the world.If an object is ungrouped and there is an object in the new group
    with the same name then this command will rename the ungrouped
    object.group, parent, instance, duplicate
    Args:
        absolute (bool?): preserve existing world object transformations  
                (overall object transformation is preserved  
                by modifying the objects local transformation)  
                [default]  
                Properties: create
        parent (str?): put the ungrouped objects under the given parent  
                Properties: create
        relative (bool?): preserve existing local object transformations  
                (don't modify local transformation)  
                Properties: create
        world (bool?): put the ungrouped objects under the world  
                Properties: create

    Returns:
        bool:

    Example:
    """

