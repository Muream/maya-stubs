from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyDuplicateAndConnect(*args: str, removeOriginalFromShaders: bool = ..., renameChildren: bool = ...) -> bool:
    """This command duplicates the input polygonal object, connects
    up the outMesh attribute of the original polygonal shape to
    the inMesh attribute of the newly created duplicate shape and
    copies over the shader assignments from the original shape
    to the new duplicated shape.The command will fail if no objects are selected or sent as
    argument or if the object sent as argument is not a polygonal
    object.
    Args:
        removeOriginalFromShaders (bool?): Used to specify if the original object should be removed from  
                the shaders (shadingGroups) that it is a member of. The shader  
                associations will get transferred to the duplicated object, before  
                they are removed from the original. If this flag is specified  
                then the original polygonal object will be drawn in wireframe  
                mode even if all objects are being drawn in shaded mode.  
                Properties: create
        renameChildren (bool?): rename the children nodes of the hierarchy, to make them unique.  
                Properties: create

    Returns:
        bool:

    Example:
    """

