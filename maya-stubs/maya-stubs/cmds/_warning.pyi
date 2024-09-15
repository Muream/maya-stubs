from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def warning(*args: str, noContext: bool = ..., showLineNumber: bool = ...) -> bool:
    """The warning command is provided so that the user can issue warning
    messages from his/her scripts.
    The string argument is displayed in the command window (or stdout if
    running in batch mode) after being prefixed with a warning message heading
    and surrounded by the appropriate language separators
    (# for Python, // for Mel).debug, information, echo
    Args:
        noContext (bool?): Do not include the context information with the warning message.  
                Properties: create
        showLineNumber (bool?): Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the  
                script editor that enables line number display instead.  
                Properties: create

    Returns:
        bool:

    Example:
    """

