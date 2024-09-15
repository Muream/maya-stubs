from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toolPropertyWindow(*, edit: bool = ..., query: bool = ..., field: Queryable[str] = ..., helpButton: Queryable[str] = ..., icon: Queryable[str] = ..., inMainWindow: bool = ..., location: Queryable[str] = ..., noviceMode: bool = ..., resetButton: Queryable[str] = ..., restore: bool = ..., selectCommand: Queryable[str] = ..., showCommand: Queryable[str] = ...) -> Union[bool, str]:
    """End users should only call this command as 1. a query (in the
    custom tool property sheet code) or 2. with no arguments
    to create the default tool property sheet.  The more complex
    uses of it are internal.
    Args:
        field (Queryable[str]?): Sets/returns the name of the text field used to store the  
                tool name in the property sheet.  
                Properties: query, edit
        helpButton (Queryable[str]?): Sets/returns the name of the button used to show help  
                on the tool in the property sheet.  
                Properties: query, edit
        icon (Queryable[str]?): Sets/returns the name of the static picture object (used to display the  
                tool icon in the property sheet).  
                Properties: query, edit
        inMainWindow (bool?): Specify true if you want the tool settings to appear in the main  
                window rather than a separate window.  
                Properties: create
        location (Queryable[str]?): Sets/returns the location of the current tool property sheet, or an empty  
                string if there is none.  
                Properties: query, edit
        noviceMode (bool?): Sets/returns the 'novice mode' flag.(unused at the moment)  
                Properties: query, edit
        resetButton (Queryable[str]?): Sets/returns the name of the button used to restore the  
                tool settings in the property sheet.  
                Properties: query, edit
        restore (bool?): Reopens the tool settings window.  
                This flag can be used with the flag inMainWindow for the fall back location if the tool settings can't be restored.  
                Properties: create
        selectCommand (Queryable[str]?): Sets/returns the property sheet's select command.  
                Properties: query, edit
        showCommand (Queryable[str]?): Sets/returns the property sheet's display command.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

