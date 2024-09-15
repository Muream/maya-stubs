from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def openGLExtension(*args: str, extension: str = ..., renderer: bool = ..., vendor: bool = ..., version: bool = ...) -> str:
    """Command returns the extension name depending on whether a given
    OpenGL extension is supported or not. The input is the
    extension string to the -extension flag.
    If the -extension flag is not used, or if
    the string argument to this flag is an empty string
    than all extension names are returned in a single string.
    If the extension exists it is not necessary true that
    the extension is supported.
    This command can only be used when a modeling
    view has been created. Otherwise no extensions
    will have been initialized and the resulting
    string will always be the empty string.OpenGL, GL, extensions
    Args:
        extension (str?): Specifies the OpenGL extension to query.  
                Properties: create
        renderer (bool?): Specifies to query the OpenGL renderer.  
                Properties: create
        vendor (bool?): Specifies to query the company responsible for the OpenGL implementation.  
                Properties: create
        version (bool?): Specifies to query the OpenGL version.  
                Properties: create

    Returns:
        str: The supported string(s)

    Example:
    """

