from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dbcount(*, enabled: bool = ..., file: str = ..., keyword: str = ..., list: bool = ..., maxdepth: int = ..., quick: bool = ..., reset: bool = ..., spreadsheet: bool = ...) -> bool:
    """Thecommand is used to print and manage a list of statistics
    collected for counting operations.  These statistics are displayed
    as a list of hits on a particular location in code, with added reference
    information for pointers/strings/whatever.
    If -reset is not specified then statistics are printed.debug, count, filter
    Args:
        enabled (bool?): Set the enabled state of the counters ('on' to enable, 'off' to disable).  
                Returns the list of all counters affected.  
                Properties: create
        file (str?): Destination file of the enabled count objects.  Use the special names  
                stdout and stderr to redirect to your command window.  As  
                well, the special name msdev is available on NT to direct your  
                output to the debug tab in the output window of Developer Studio.  
                Properties: create
        keyword (str?): Print only the counters whose name matches this keyword (default is all).  
                Properties: create
        list (bool?): List all available counters and their current enabled status. (The only  
                thing you can do when counters are disabled.)  
                Properties: create
        maxdepth (int?): Maximum number of levels down to traverse and report. 0 is the default and  
                it means continue recursing as many times as are requested.  
                Properties: create
        quick (bool?): Display only a summary for each counter type instead of the full details.  
                Properties: create
        reset (bool?): Reset all counters back to 0 and remove all but the top level counters.  
                Returns the list of all counters affected.  
                Properties: create
        spreadsheet (bool?): Display in spreadsheet format instead of the usual nested braces.  
                This will include a header row that contains 'Count Level1 Level2 Level3...',  
                making the data suitable for opening directly in a spreadsheet table.  
                Properties: create

    Returns:
        bool:

    Example:
    """

