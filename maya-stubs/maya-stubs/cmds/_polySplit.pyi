from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySplit(*args: str, edit: bool = ..., query: bool = ..., constructionHistory: bool = ..., name: str = ..., adjustEdgeFlow: Queryable[float] = ..., detachEdges: bool = ..., edgepoint: Multiuse[Tuple[int, float]] = ..., facepoint: Multiuse[Tuple[int, float, float, float]] = ..., insertWithEdgeFlow: bool = ..., insertpoint: Multiuse[Union[Tuple[int, float], Tuple[int, float, float, float]]] = ..., projectedCurve: Multiuse[str] = ..., projectedCurveTolerance: float = ..., smoothingangle: float = ..., subdivision: Queryable[int] = ...) -> Union[str, bool, float, int]:
    """Split facets/edges of a polygonal object.The first and last arguments must be edges. Intermediate points
    may lie on either a shared face or an edge which neighbors the previous point.
    Args:
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        adjustEdgeFlow (Queryable[float]?): The weight value of the edge vertices to be positioned.  
                Properties: create, query, edit
        detachEdges (bool?): Value of the detachEdges attribute for the resulting poly split node.  
                Properties: create
        edgepoint (Multiuse[Tuple[int, float]]?): The given edge is split into two new edges  
                by inserting a new vertex located the given percentage  
                along the edge.  
              
                Note: This flag is not recommended for use from Python.  See the  
                insertpoint flag instead.  
                Properties: create, multiuse
        facepoint (Multiuse[Tuple[int, float, float, float]]?): A new vertex is inserted,  
                lying at the given coordinates inside the given face.  
                Coordinates are given in the local object space.  
              
                Note: This flag is not recommended for use from Python.  See the  
                insertpoint flag instead.  
                Properties: create, multiuse
        insertWithEdgeFlow (bool?): True to enable edge flow. Otherwise, the edge flow is disabled.  
                Properties: create, query, edit
        insertpoint (Multiuse[Union[Tuple[int, float], Tuple[int, float, float, float]]]?): This flag allows the caller to insert a new vertex into an edge or a face.  
              
                To insert a new vertex in an edge, pass the index of the edge and a percentage  
                along the edge at which to insert the new vertex.  When used to insert a  
                vertex into an edge, this flag takes two arguments.  
              
                To insert a new vertex into a face, pass the index of the face and three values  
                which define the coordinates for the insertion in local object space.  When  
                used to insert a vertex into a face, this flag takes four arguments.  
              
                This flag replaces the edgepoint and facepoint flags.  
                Properties: create, multiuse
        projectedCurve (Multiuse[str]?): Curves to be projected.  
                Properties: create, multiuse
        projectedCurveTolerance (float?): Tolerance for curve projection.  
                Properties: create
        smoothingangle (float?): Subdivide new edges will be soft if less then this angle.  
                C: Default is 0.0  
                Properties: create
        subdivision (Queryable[int]?): Subdivide new edges into the given number of sections.  
                Edges involving free points won't be subdivided.  
                C: Default is 1 (no subdivision).  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

