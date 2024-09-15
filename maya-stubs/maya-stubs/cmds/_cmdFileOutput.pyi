from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cmdFileOutput(*, query: bool = ..., close: int = ..., closeAll: bool = ..., open: str = ..., status: Queryable[int] = ...) -> int:
    """This command will open a text file to receive all of the commands
    and results that normally get printed to the Script Editor
    window or console. The file will stay open until an explicit -close
    with the correct file descriptor or a -closeAll, so care should be
    taken not to leave a file open.To enable logging to commence as soon as Maya starts up, the
    environment variable MAYA_CMD_FILE_OUTPUT may be specified prior
    to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to a filename
    will create and output to that given file. To access the descriptor
    after Maya has started, use the -query and -open flags together.
    Args:
        close (int?): Closes the file corresponding to the given descriptor.  
                If -3 is returned, the file did not exist. -1 is returned  
                on error, 0 is returned on successful close.  
                Properties: create
        closeAll (bool?): Closes all open files.  
                Properties: create
        open (str?): Opens the given file for writing (will overwrite if it exists  
                and is writable). If successful, a value is returned to enable  
                status queries and file close. -1 is returned if the file cannot  
                be opened for writing. The -open flag can also be specified in  
                -query mode. In query mode, if the named file is currently opened,  
                the descriptor for the specified file is returned, otherwise -1 is  
                returned. This is an easy way to check if a given file is  
                currently open.  
                      In query mode, this flag needs a value.  
                Properties: create, query
        status (Queryable[int]?): Queries the status of the given descriptor. -3 is returned  
                if no such file exists, -2 indicates the file is not open,  
                -1 indicates an error condition, 0 indicates file is ready  
                for writing.  
                Properties: create, query

    Returns:
        int: : On open, returns a value (descriptor) that can be used to query
            the status or close the file. Otherwise, a status code
            indicating status of file

    Example:
    """

