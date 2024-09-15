from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def xpmPicker(*args: Any, fileName: str = ..., parent: str = ...) -> str:
    """Open a dialog and ask you to choose a xpm file
    Args:
        fileName (str?): default filename to display in dialog  
                Properties: create
        parent (str?): parent window for modal dialog  
                Properties: create

    Returns:
        str: The full name of the xpm file

    Example:
    """

