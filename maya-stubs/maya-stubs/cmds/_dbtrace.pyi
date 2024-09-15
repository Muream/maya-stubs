from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dbtrace(*, query: bool = ..., filter: Queryable[str] = ..., info: bool = ..., keyword: Queryable[Multiuse[str]] = ..., mark: bool = ..., off: bool = ..., output: Queryable[str] = ..., timed: bool = ..., title: str = ..., verbose: bool = ...) -> Union[bool, str, Multiuse[str]]:
    """Thecommand is used to manipulate trace objects.
              The keyword is the only mandatory argument, indicating which trace
              object is to be altered.You can use the query mode to find out which keywords are currently
              active (query with no arguments) or inactive (query with theargument).
              You can enhance that query with or without a keyword argument to find
              out where their output is going (query with theargument), out what filters are currently applied (query with theargument), or if their output will be
              timestamped (query with theargument).debug, trace, filter
    Args:
        filter (Queryable[str]?): Set the filter object for these trace objects (see 'dgfilter')  
                Properties: create, query
        info (bool?): In query mode return a brief description of the trace object.  
                Properties: query
        keyword (Queryable[Multiuse[str]]?): Keyword of the trace objects to affect  
                			In query mode, this flag can accept a value.  
                Properties: create, query, multiuse
        mark (bool?): Display a mark for all outputs of defined trace objects  
                Properties: create
        off (bool?): Toggle the traces off.  If omitted it will turn them on.  
                Properties: create
        output (Queryable[str]?): Destination file of the affected trace objects.  Use the special names  
                stdout and stderr to redirect to your command window.  
                The special name msdev is available on Windows to direct your  
                output to the debug tab in the output window of Visual Studio.  
                Properties: create, query
        timed (bool?): Turn on/off timing information in the output of the specified trace objects.  
                Properties: create, query
        title (str?): Display a title mark for all outputs of defined trace objects  
                Properties: create
        verbose (bool?): Include all traces in output and filter queries, not just those turned on.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

