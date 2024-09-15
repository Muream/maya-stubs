from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dimWhen(arg0: str = ..., arg1: str = ..., /, *, clear: bool = ..., false: bool = ..., true: bool = ...) -> bool:
    """This method attaches the named UI object (first argument) to the named
    condition (second argument) so that the object will be dimmed when the
    condition is in a particular state.This command will fail if the object does not exist. If the condition
    does not exist (yet), that's okay --- a placeholder will be used until
    such a condition comes into existence.The UI object should be one of two things, either a control or a menu
    item.
    Args:
        clear (bool?): Remove the condition on the specified dimmable.  
                Properties: create
        false (bool?): Dim the object when the condition is false.  
                Properties: create
        true (bool?): Dim the object when the condition is true. (default)  
                Properties: create

    Returns:
        bool:

    Example:
    """

