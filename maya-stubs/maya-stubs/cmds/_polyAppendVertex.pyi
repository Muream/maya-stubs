from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyAppendVertex(*args: str, edit: bool = ..., query: bool = ..., append: Multiuse[Union[Tuple[()], Tuple[float, float, float]]] = ..., constructionHistory: bool = ..., hole: Multiuse[bool] = ..., name: str = ..., point: Multiuse[Tuple[float, float, float]] = ..., texture: Queryable[int] = ..., vertex: Multiuse[int] = ...) -> Union[str, bool, int]:
    """Appends a new face to the selected polygonal object. The direction
    of the normal is given by the vertex order: the face normal points
    towards the user when the vertices rotate counter clockwise. Note
    that holes must be described in the opposite direction.Only works with one object selected.
    Args:
        append (Multiuse[Union[Tuple[()], Tuple[float, float, float]]]?): Append a vertex or a point to the selected object, or mark the start of a  
                hole.  
              
                This flag may also be used in place of the "hole", "vertex" and "point" flags.  
                If no argument is passed to the "append" flag, then it marks the beginning of a  
                hole (use an empty tuple in Python '()').  If one argument is passed, then the  
                argument is considered to be an index into the vertices of the selected  
                object, as with the "vertex" flag.  If three arguments are passed, then it is  
                interpreted as the coordinates of a new point which will be inserted, as with  
                the "point" flag.  
                Properties: create, multiuse
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        hole (Multiuse[bool]?): Add a hole. The following points and edges will define a hole.  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass an empty tuple '()' to specify the start of a hole.  
                Properties: create, multiuse
        name (str?): Give a name to the resulting node.  
                Properties: create
        point (Multiuse[Tuple[float, float, float]]?): Adds a new point to the new face.  
                Coordinates of free points are given in the local object reference.  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass three arguments.  
                Properties: create, multiuse
        texture (Queryable[int]?): Specifies how new faces are mapped.  
                0. None; 1. Normalize; 2. Unitize  
                C: Default is 0 (no mapping).  
                Q: When queried, this flag returns an int  
                Properties: create, query, edit
        vertex (Multiuse[int]?): Adds the given vertex of the selected object to the new face.  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass one argument.  
                Properties: create, multiuse

    Returns:
        str: The node name.

    Example:
    """

