from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fileDialog(*, application: bool = ..., defaultFileName: str = ..., directoryMask: str = ..., mode: int = ..., title: str = ...) -> str:
    """The fileBrowserDialog and fileDialog commands have now been deprecated.
    Both commands are still callable, but it is recommended that the fileDialog2 command
    be used instead.  To maintain some backwards compatibility, both fileBrowserDialog and
    fileDialog will convert the flags/values passed to them into the appropriate flags/values
    that the fileDialog2 command uses and will call that command internally.  It is not
    guaranteed that this compatibility will be able to be maintained in future versions so
    any new scripts that are written should use fileDialog2.See below for an example of how to change a script to use fileDialog2.
    Args:
        application (bool?): This is a "Mac" only flag. This brings up the dialog which  
                selects only the application bundle.  
                Properties: create
        defaultFileName (str?): Set default file name. This flag is available under "write" mode  
                Properties: create
        directoryMask (str?): This can be used to specify what directory and file names  
                will be displayed in the dialog.  If not specified, the  
                current directory will be used, with all files displayed.  
                The string may contain a path name, and must contain a  
                wild-carded file specifier. (eg "*.cc" or "/usr/u/*") If  
                just a path is specified, then the last directory in the  
                path is taken to be a file specifier, and this will not  
                produce the desired results.  
                Properties: create
        mode (int?): Defines the mode in which to run the file dialog:  
              
                0 for read  
                1 for write  
              
                Write mode can not be used in conjunction with the -application flag.  
                Properties: create
        title (str?): Set title text. The default value under "write" mode is "Save As". The default value under "read" mode is "Open".  
                Properties: create

    Returns:
        str: Name of dialog

    Example:
    """

