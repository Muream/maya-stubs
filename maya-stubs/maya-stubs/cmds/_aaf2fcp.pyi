from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def aaf2fcp(*, deleteFile: bool = ..., dstPath: str = ..., getFileName: int = ..., progress: int = ..., srcFile: str = ..., terminate: int = ..., waitCompletion: int = ...) -> str:
    """This command is used to convert an aff file to a Final Cut Pro (fcp) xml file
    The conversion process can take several seconds to complete and the command is meant
    to be run asynchronouslyutility, aaf, fcp
    Args:
        deleteFile (bool?): Delete temporary file. Can only be used with the terminate option  
                Properties: create
        dstPath (str?): Specifiy a destination path  
                Properties: create
        getFileName (int?): Query output file name  
                Properties: create
        progress (int?): Request progress report  
                Properties: create
        srcFile (str?): Specifiy a source file  
                Properties: create
        terminate (int?): Complete the task  
                Properties: create
        waitCompletion (int?): Wait for the conversion process to complete  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

