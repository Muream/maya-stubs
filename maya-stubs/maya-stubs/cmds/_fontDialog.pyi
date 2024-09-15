from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fontDialog(*, FontList: bool = ..., scalable: bool = ...) -> str:
    """Displays a dialog of available fonts for the user to select from. The
    name of the selected font is returned, or an empty string if no font was selected.When theflag is used, no dialog is displayed. Instead
    the command returns an array of the available fonts.
    Args:
        FontList (bool?): Returns an array of all available font names. No dialog is displayed.  
                Properties: create
        scalable (bool?): Limits the fonts returned or displayed to just those that are scalable.  
                Properties: create

    Returns:
        str: Dialog name

    Example:
    """

