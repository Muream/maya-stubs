from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sysFile(arg0: str = ..., /, *, copy: str = ..., delete: bool = ..., makeDir: bool = ..., move: str = ..., removeEmptyDir: bool = ..., rename: str = ...) -> bool:
    """This command provides a system independent way to create a directory
    or to rename or delete a file.
    Args:
        copy (str?): Copy the file to the name given by the newFileName paramter.  
                Properties: create
        delete (bool?): Deletes the file.  
                Properties: create
        makeDir (bool?): Create the directory path given in the parameter.  
                This will create the entire path if more than one  
                directory needs to be created.  
                Properties: create
        move (str?): Behaves identically to the -rename flag and remains for  
                compatibility with old scripts  
                Properties: create
        removeEmptyDir (bool?): Delete the directory path given in the parameter if  
                the directory is empty. The command will not delete a directory  
                which is not empty.  
                Properties: create
        rename (str?): Rename the file to the name given by the newFileName parameter.  
                Properties: create

    Returns:
        bool: True if successful, false otherwise.

    Example:
    """

