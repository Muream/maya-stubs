from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def error(*args: str, noContext: bool = ..., showLineNumber: bool = ...) -> bool:
    """The error command is provided so that the user can issue
    error messages from his/her scripts and
    control execution in the event of runtime errors.The string argument is displayed in the command window
    (or stdout if running in batch mode) after
    being prefixed with an error message heading and
    surrounded by //.The error command also causes execution to terminate with an error.
    Using error is like raising an exception because the error will
    propagate up through the call chain. You can use catch to
    handle the error from the caller side. If you don't want
    execution to end, then you probably want to use the warning
    command instead.debug, information, echo
    Args:
        noContext (bool?): Do not include the context information with the error message.  
                Properties: create
        showLineNumber (bool?): Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the  
                script editor that enables line number display instead.  
                Properties: create

    Returns:
        bool:

    Example:
    """

