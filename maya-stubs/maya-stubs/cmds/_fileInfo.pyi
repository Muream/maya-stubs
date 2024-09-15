from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fileInfo(arg0: str = ..., arg1: str = ..., /, *, query: bool = ..., referenceNode: str = ..., remove: Queryable[str] = ...) -> Union[List[str], str]:
    """fileInfo provides a mechanism for keeping information related
    to a Maya scene file.
    Each invocation of the command consists of a keyword/value pair,
    where both the keyword and the associated value are strings.
    The command may be invoked multiple times with different keywords.
    Maya emits this command several times into each file it creates,
    primarily to provide details such as
    which productization or packaging of the program was used
    (e.g "Complete", "Unlimited"), the specific version and build identification
    that was run, and the operating system on which it was run.
    Maya may make use of this information when present in files it reads.
    All keyword/value pairs defined by use of the fileInfo command are
    preserved when Maya saves the scene, whether to an ASCII or binary file.file, version
    Args:
        referenceNode (str?): Specify the name of a referenceNode to indicate the scene file to query.  
                This flag is only valid during query.  
                			In query mode, this flag needs a value.  
                Properties: query
        remove (Queryable[str]?): If the remove flag is specified, the string following it is a keyword to  
                remove from the list of fileInfo to be saved with the scene file.  
                Properties: create, query

    Returns:
        List[str]: Command result

    Example:
    """

