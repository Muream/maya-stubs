from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def commandLogging(*, query: bool = ..., historySize: Queryable[int] = ..., logCommands: bool = ..., logFile: Queryable[str] = ..., recordCommands: bool = ..., resetLogFile: bool = ...) -> Union[bool, int, str]:
    """This command controls logging of Maya commands,
    in memory and on disk.Note that if commands are logged in memory, they will
    be available to the crash reporter and appear in crash logs.
    Args:
        historySize (Queryable[int]?): Sets the number of entries  
                in the in-memory command history.  
                Properties: create, query
        logCommands (bool?): Enables or disables the on-disk logging  
                of commands.  
                Properties: create, query
        logFile (Queryable[str]?): Sets the filename to use for the on-disk log.  
                If logging is active, the current file will be closed  
                before the new one is opened.  
                Properties: create, query
        recordCommands (bool?): Enables or disables the in-memory logging  
                of commands.  
                Properties: create, query
        resetLogFile (bool?): Reset the log filename to the default  
                ('mayaCommandLog.txt' in the application folder,  
                alongside 'Maya.env' and the default projects folder).  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

