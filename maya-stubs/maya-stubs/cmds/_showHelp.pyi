from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showHelp(arg0: str = ..., /, *, query: bool = ..., absolute: bool = ..., docs: bool = ..., helpTable: bool = ..., version: bool = ...) -> bool:
    """Invokes a web browser to open the on-line documentation and help files.
    It will open the help page for a given topic, or open a browser
    to a specific URL.browse, documentation, web, page, help
    Args:
        absolute (bool?): The specified "URL" is an absolute URL that should be passed directly  
                to the web browser.  
                Properties: create
        docs (bool?): Use this flag to directly specify a help file relative to the  
                on-line documentation root.  
                Properties: create, query
        helpTable (bool?): Use this flag to specify which file will be used to search for help  
                topics when the -d/docs and -a/absolute flags are not used. If only  
                a file name is specified and not a path, then the file is assumed to  
                be in the maya application directory.  
                If this flag does not accept an argument if it is queried.  
                The default value is "helpTable".  
                Properties: create, query
        version (bool?): Use this flag to get the Maya version that the showHelp command uses.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

