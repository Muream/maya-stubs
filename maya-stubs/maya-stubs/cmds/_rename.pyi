from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rename(arg0: str = ..., arg1: str = ..., /, *, ignoreShape: bool = ..., uuid: bool = ...) -> str:
    """Renames the given object to have the new name. If only one
    argument is supplied the command will rename the (first) selected
    object. If the new name conflicts with an existing name, the
    object will be given a unique name based on the supplied name.
    It is not legal to rename an object to the empty string.When a transform is renamed then any shape nodes beneath the
    transform that have the same prefix as the old transform name
    are renamed. For example, "rename nurbsSphere1 ball" would
    rename "nurbsSphere1|nurbsSphereShape1" to "ball|ballShape".If the new name ends in a single '#' then the rename command
    will replace the  trailing '#' with a number that ensures
    the new name is unique.If the name has an absolute namespace part, it will be considered.
    Namespaces that do not exist will be created automatically as needed.
    If the name has a relative namespace part, it will be ignored.
    In that case, the object will be put under the current namespace.
    (see example below).
    Args:
        ignoreShape (bool?): Indicates that renaming of shape nodes below  
                transform nodes should be prevented.  
                Properties: create
        uuid (bool?): Indicates that the new name is actually a UUID,  
                and that the command should change the node's UUID.  
                (In which case its name remains unchanged.)  
                Properties: create

    Returns:
        str: The new name. When undone returns original name.

    Example:
    """

