from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def artAttrTool(*args: Any, query: bool = ..., add: str = ..., exists: Queryable[str] = ..., remove: str = ...) -> Union[bool, str]:
    """The artAttrTool command manages the list of tool types which are
            used for attribute painting. This command supports querying the
            list contents as well as adding new tools to the list. Note that
            there is a set of built-in tools. The list of built-ins can
            be queried by starting Maya and doing an "artAttrTool -q".The tools which are managed by this command are all intended for
            attribute painting via Artisan: when you create a new context via
            artAttrCtx you specify the tool name via artAttrCtx'sflag. Typically the user may wish to simply use one of the built-in
            tools. However, if you need to have custom Properties and Values sheets
            asscociated with your tool, you will need to define a custom tool
            via. For an example of a custom
            attribute painting tool, see the devkit example customtoolPaint.mel.artisan, attribute, paint, context
    Args:
        add (str?): Adds the named tool to the internal list of tools.  
                Properties: create
        exists (Queryable[str]?): Checks if the named tool exists, returning true if found, and false otherwise.  
                Properties: create, query
        remove (str?): Removes the named tool from the internal list of tools.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

