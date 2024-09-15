from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyListComponentConversion(*args: str, border: bool = ..., fromEdge: bool = ..., fromFace: bool = ..., fromUV: bool = ..., fromVertex: bool = ..., fromVertexFace: bool = ..., internal: bool = ..., toEdge: bool = ..., toFace: bool = ..., toUV: bool = ..., toVertex: bool = ..., toVertexFace: bool = ..., uvShell: bool = ..., vertexFaceAllEdges: bool = ...) -> List[str]:
    """This command converts poly components from one or more types
    to another one or more types, and returns the list of the
    conversion. It does not change anything of the current database.
    Args:
        border (bool?): Indicates that the converted components must  
                be on the border of the selection. If it is not provided, the  
                converted components will be the related ones.  
                Properties: create
        fromEdge (bool?):   
                Properties: create
        fromFace (bool?):   
                Properties: create
        fromUV (bool?):   
                Properties: create
        fromVertex (bool?):   
                Properties: create
        fromVertexFace (bool?): Indicates the component type to convert from.  
                If none of them is provided, it is assumed to be  
                all of them, including poly objects.  
                Properties: create
        internal (bool?): Indicates that the converted components must  
                be totally envolved by the source components. E.g.  
                a converted face must have all of its surrounding  
                vertices being given. If it is not provided, the  
                converted components will be the related ones.  
                Properties: create
        toEdge (bool?):   
                Properties: create
        toFace (bool?):   
                Properties: create
        toUV (bool?):   
                Properties: create
        toVertex (bool?):   
                Properties: create
        toVertexFace (bool?): Indicates the component type to convert to.  
                If none of them is provided, it is assumed to  
                the object.  
                Properties: create
        uvShell (bool?): Will return UV components within the same UV shell. Only works with -tuv and -fuv flags.  
                Properties: create
        vertexFaceAllEdges (bool?): When converting from face vertices to edges, indicates  
                that all edges with an end at the face vertex should be included.  
                Without this flag, the default behaviour is to only include  
                one edge per face vertex.  
                Properties: create

    Returns:
        List[str]: List of poly components

    Example:
    """

