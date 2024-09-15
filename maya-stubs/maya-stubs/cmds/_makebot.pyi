from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def makebot(*, checkdepends: bool = ..., checkres: int = ..., input: str = ..., nooverwrite: bool = ..., output: str = ..., verbose: bool = ...) -> bool:
    """The makebot command takes an image file and produces a block
    ordered texture (BOT) file, to be used for texture caching.
    If a relative pathname is specified for the input image file,
    project management rules apply.  If a relative pathname is
    specified for the output BOT file, project management rules
    apply and gets put into the sourceImages directory.
    Args:
        checkdepends (bool?): the BOT file should only be generated if it doesn't already exists,  
                or if it is older than the source file  
                Properties: create
        checkres (int?): the BOT file should only be generated if its resolution (maximum of  
                width and height) is larger than the minimum value specified by the  
                argument  
                Properties: create
        input (str?): input image file  
                Properties: create
        nooverwrite (bool?): If -c and/or -r indicate that the BOT file should be generated but  
                if already exists, then this flag will prevent the file from being  
                overwritten  
                Properties: create
        output (str?): output BOT file  
                Properties: create
        verbose (bool?): Makebot will provide feedback if this flag is specified  
                Properties: create

    Returns:
        bool:

    Example:
    """

