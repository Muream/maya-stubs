from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hotkeySet(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., current: bool = ..., delete: bool = ..., exists: bool = ..., export: str = ..., hotkeySetArray: bool = ..., ip: str = ..., rename: str = ..., source: str = ...) -> Union[str, bool]:
    """Manages hotkey sets in Maya. A hotkey set holds hotkey to command mapping information.
    Default hotkey sets are hotkey sets that are shipped together with Maya. They are locked and cannot be altered.A new hotkey set is always duplicated from an existing hotkey set. In create mode, users can choose to specify
    which hotkey set to duplicate by using the -source flag. A duplicated hotkey set is independent from the source
    hotkey set.
    Args:
        current (bool?): Sets the hotkey set as the current active hotkey set. In query mode, returns the name of  
                the current hotkey set.  
                Properties: create, query, edit
        delete (bool?): Deletes the hotkey set if it exists. Other flags are ignored.  
                Returns true|false depending on the delete operation.  
                Properties: edit
        exists (bool?): Returns true|false depending upon whether the specified object  
                exists. Other flags are ignored.  
                Properties: create
        export (str?): Exports a hotkey set. The argument is used to specify a full path of the output file.  
                Properties: edit
        hotkeySetArray (bool?): Returns a string array of all existing hotkey set names.  
                Properties: query
        ip (str?): Imports a hotkey set. The argument is used to specify a full path of the hotkey set file to import.  
                Properties: edit
        rename (str?): Renames an existing hotkey set. All white spaces will be replaced with '_' during operation.  
                Properties: edit
        source (str?): Specifies the source hotkey set. If flag is not provided, the current active hotkey set is used.  
                Properties: create

    Returns:
        str: The name of the hotkey set.

    Example:
    """

