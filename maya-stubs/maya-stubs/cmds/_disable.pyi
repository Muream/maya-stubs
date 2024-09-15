from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def disable(arg0: str = ..., /, *, value: bool = ...) -> bool:
    """This command enables or disables the control passed as argument.
    Args:
        value (bool?): If true, this command disables the control.  
                If false, this command enables the control.  
                Default value is true (disable)  
                Properties: create

    Returns:
        bool:

    Example:
    """

