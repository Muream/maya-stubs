from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyAppend(*args: str, edit: bool = ..., query: bool = ..., append: Multiuse[Union[Tuple[()], Tuple[float, float, float]]] = ..., constructionHistory: bool = ..., edge: Multiuse[int] = ..., hole: Multiuse[bool] = ..., name: str = ..., point: Multiuse[Tuple[float, float, float]] = ..., subdivision: Queryable[int] = ..., texture: Queryable[int] = ...) -> Union[str, bool, int]:
    """Appends a new face to the selected polygonal object.
    The first argument must be a border edge.
    The new face will be automatically closed.Only works with one object selected.
    Args:
        append (Multiuse[Union[Tuple[()], Tuple[float, float, float]]]?): Appends to the given polygon object.  The append flag should be used  
                multiple times to specify the edges, points, and holes that make up the new  
                face that is being added.  
              
                You may specify an edge by passing a single argument which will be the edges  
                index.  A point is specified with three arguments which are the coordinates  
                of the point in the objects local space.  Pass no arguments indicates that  
                the values which follow shall specify a hole.  In Python, pass an empty  
                tuple to specify no arguments.  
                Properties: create, multiuse
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        edge (Multiuse[int]?): Adds the given edge of the selected object to the new face.  
                This edge must be a border, which will be then shared by the  
                new face and the neighboring one. The new face is oriented according  
                to the orientation of the given edge(s).  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass one argument.  
                Properties: create, multiuse
        hole (Multiuse[bool]?): Add a hole. The following points and edges will define a hole.  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass an empty tuple ().  
                Properties: create, multiuse
        name (str?): Give a name to the resulting node.  
                Properties: create
        point (Multiuse[Tuple[float, float, float]]?): Adds a new point to the new face.  
                Coordinates of free points are given in the local object reference.  
              
                Note that this flag should be avoided in Python.  You may use the "append"  
                flag instead and pass three arguments.  
                Properties: create, multiuse
        subdivision (Queryable[int]?): This flag specifies the level of subdivisions.  
                Automatically subdivides new edges into the given number of edges.  
                Existing edges cannot be subdivided.  
                C : Default is 1 (no subdivision).  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        texture (Queryable[int]?): Specifies how new faces are mapped.  
                 0. None; 1. Normalize; 2. Unitize  
                C: Default is 0 (no mapping).  
                Q: When queried, this flag returns an int  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

