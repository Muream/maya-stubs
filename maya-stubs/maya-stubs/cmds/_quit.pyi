from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def quit(*, abort: bool = ..., exitCode: int = ..., force: bool = ...) -> bool:
    """This command is used to exit the application.
    Args:
        abort (bool?): Will quit without saving like -force, but will also prevent  
                preferences/hotkeys/colors from being saved.  Use at  
                your own risk.  
                Properties: create
        exitCode (int?): Specifies the exit code to be returned once the application  
                exits.  The default exit code is 0.  
                Properties: create
        force (bool?): If specified, this flag will force a quit without saving  
                or prompting for saving changes. Use at  
                your own risk.  
                Properties: create

    Returns:
        bool:

    Example:
    """

