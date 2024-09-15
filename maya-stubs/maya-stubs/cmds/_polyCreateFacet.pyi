from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCreateFacet(*args: str, edit: bool = ..., query: bool = ..., constructionHistory: bool = ..., hole: Multiuse[bool] = ..., name: str = ..., point: Multiuse[Union[Tuple[()], Tuple[float, float, float]]] = ..., subdivision: Queryable[int] = ..., texture: Queryable[int] = ...) -> Union[List[str], bool, int]:
    """Create a new polygonal object with the specified face, which will be closed.
    List of arguments must have at least 3 points.
    Args:
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        hole (Multiuse[bool]?): Add a hole. The following points will define a hole.  
                Holes can be defined either clockwise or counterclockwise.  
              
                Note that this flag is not recommended for use in Python.  When specifying facets  
                with the point flag in Python, pass in an empty point "()" when you want to  
                start specifying a hole.  
                Properties: create, multiuse
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        point (Multiuse[Union[Tuple[()], Tuple[float, float, float]]]?): Adds a new point to the face.  
                Coordinates of points are given in world reference.  
              
                The point flag may also be passed with no arguments.  That indicates that the  
                following points will specify a hole.  Passing the point flag with no  
                arguments is the same as using the "hole" flag, except that it will work  
                in Python.  
                Properties: create, multiuse
        subdivision (Queryable[int]?): This flag specifies the level of subdivision.  
                Subdivides edges into the given number of edges.  
                C: Default is 1 (no subdivision).  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        texture (Queryable[int]?): Specifies how the face is mapped.  
                 0. None; 1. Normalize; 2. Unitize  
                C: Default is 0 (no mapping).  
                Q: When queried, this flag returns an int  
                Properties: create, query, edit

    Returns:
        List[str]: Object name and node name.

    Example:
    """

