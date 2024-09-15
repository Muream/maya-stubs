from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdListComponentConversion(*args: Any, border: bool = ..., fromEdge: bool = ..., fromFace: bool = ..., fromUV: bool = ..., fromVertex: bool = ..., internal: bool = ..., toEdge: bool = ..., toFace: bool = ..., toUV: bool = ..., toVertex: bool = ..., uvShell: bool = ..., uvShellBorder: bool = ...) -> List[str]:
    """This command converts subdivision surface components from one or
    more types to another one or more types, and returns the list of the
    conversion. It does not change the currently selected objects.Use the "-in/internal" flag to specify conversion to
    "connected" vs. "contained" components.  For example,
    if the internal flag is specified when converting
    from subdivision surface vertices to faces, then
    only faces that are entirely contained by the vertices
    will be returned.  If the internal flag is not specified,
    then all faces that are connected to the vertices will
    be returned.
    Args:
        border (bool?): Convert to a border.  
                Properties: create
        fromEdge (bool?): Indicates the component type to convert  
                from: Edges  
                Properties: create
        fromFace (bool?): Indicates the component type to convert  
                from: Faces  
                Properties: create
        fromUV (bool?): Indicates the component type to convert  
                from: UVs  
                Properties: create
        fromVertex (bool?): Indicates the component type to convert  
                from: Vertex  
                Properties: create
        internal (bool?): Applicable when converting from  
                "smaller" component types to larger ones.  
                Specifies conversion to "connected" vs.  
                "contained" components.  
                See examples below.  
                Properties: create
        toEdge (bool?): Indicates the component type to convert  
                to: Edges  
                Properties: create
        toFace (bool?): Indicates the component type to convert  
                to: Faces  
                Properties: create
        toUV (bool?): Indicates the component type to convert  
                to: UVs  
                Properties: create
        toVertex (bool?): Indicates the component type to convert  
                to: Vertices  
                Properties: create
        uvShell (bool?): Will return UV components within the same UV  
                shell. Only works with -tuv and -fuv flags.  
                Properties: create
        uvShellBorder (bool?): Will return UV components on the border  
                within the same UV shell. Only works with  
                -tuv and -fuv flags.  
                Properties: create

    Returns:
        List[str]: List of subdivision surface components

    Example:
    """

