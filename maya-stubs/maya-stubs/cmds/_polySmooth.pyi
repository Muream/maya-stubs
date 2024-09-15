from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySmooth(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., name: str = ..., nodeState: Queryable[int] = ..., continuity: Queryable[float] = ..., degree: int = ..., divisions: Queryable[int] = ..., divisionsPerEdge: int = ..., keepBorder: bool = ..., keepHardEdge: bool = ..., keepMapBorders: int = ..., keepSelectionBorder: bool = ..., keepTesselation: bool = ..., keepTessellation: bool = ..., method: int = ..., osdCreaseMethod: Queryable[int] = ..., osdFvarBoundary: Queryable[int] = ..., osdFvarPropagateCorners: bool = ..., osdSmoothTriangles: bool = ..., osdVertBoundary: Queryable[int] = ..., propagateEdgeHardness: bool = ..., pushStrength: float = ..., roundness: float = ..., smoothUVs: bool = ..., subdivisionLevels: int = ..., subdivisionType: Queryable[int] = ...) -> Union[str, bool, int, float]:
    """Smooth a polygonal object. This command works on polygonal objects
    or faces.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        name (str?): Give a name to the resulting node.  
                Properties: create
        nodeState (Queryable[int]?): Maya dependency nodes have 6 possible states.  
                The Normal (0), HasNoEffect (1), and Blocking (2) states can be  
                used to alter how the graph is evaluated.  
              
              
              
                The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)  
                are for internal use only. They temporarily shut off parts of the graph during interaction  
                (e.g., manipulation). The understanding is that once the operation is done,  
                the state will be reset appropriately, e.g. Waiting-Blocking will reset  
                back to Blocking.  
              
              
              
                The Normal and Blocking cases apply to all nodes, while  
                HasNoEffect is node specific; many nodes do not support this option.  
                Plug-ins store state in the MPxNode::state attribute. Anyone can set  
                it or check this attribute.  Additional details about each of these 3 states follow.  
              
              
              
              
                State  
                Description  
              
              
                Normal  
                The normal node state. This is the default.  
              
              
                HasNoEffect  
              
              
                The HasNoEffect option (a.k.a. pass-through), is used in cases where  
                there is an operation on an input producing an output of the same data type.  
                Nearly all deformers support this state, as do a few other nodes.  
                As stated earlier, it is not supported by all nodes.  
              
              
                Itâ€™s typical to implement support for the HasNoEffect state in  
                the nodeâ€™s compute method and to perform appropriate operations.  
                Plug-ins can also support HasNoEffect.  
              
              
                The usual implementation of this state is to copy the input directly to the  
                matching output without applying the algorithm in the node. For deformers,  
                applying this state leaves the input geometry undeformed on the output.  
              
              
              
              
                Blocking  
              
              
                This is implemented in the depend node base class and applies to all nodes.  
                Blocking is applied during the evaluation phase to connections.  
                An evaluation request to a blocked connection will return as failures,  
                causing the destination plug to retain its current value. Dirty propagation  
                is indirectly affected by this state since blocked connections are never cleaned.  
              
              
                When a node is set to Blocking the behavior is supposed to be the same as  
                if all outgoing connections were broken. As long as nobody requests evaluation  
                of the blocked node directly it wonâ€™t evaluate after that. Note that a blocked  
                node will still respond to getAttr requests but a getAttr on a  
                downstream node will not reevaluate the blocked node.  
              
              
                Setting the root transform of a hierarchy to Blocking wonâ€™t automatically  
                influence child transforms in the hierarchy. To do this, youâ€™d need to  
                explicitly set all child nodes to the Blocking state.  
              
              
                For example, to set all child transforms to Blocking, you could use the  
                following script.  
              
              
              
                import maya.cmds as cmds  
                def blockTree(root):  
                nodesToBlock = []  
                for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():  
                nodesToBlock += cmds.listConnections(node, source=True, destination=True )  
                for node in {source:1 for source in nodesToBlock}.keys():  
                cmds.setAttr( '%s.nodeState' % node, 2 )  
              
              
              
                Applying this script would continue to draw objects but things would not be animated.  
              
              
              
              
                Default: kdnNormal  
                Properties: create, query, edit
        continuity (Queryable[float]?): This flag specifies the smoothness parameter. The minimum value of 0.0  
                specifies that the faces should only be subdivided. Maximum value of 1.0 smooths  
                the faces as much as possible.  
                C: Default is 1.0  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        degree (int?): Degree of the resulting limit surface  
                Properties: create
        divisions (Queryable[int]?): This flag specifies the number of recursive smoothing steps.  
                C: Default is 1.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        divisionsPerEdge (int?): Number of subdivisions along one edge for each step.  
                Properties: create
        keepBorder (bool?): If on, the border of the object will not move during smoothing operation.  
                C: Default is "on".  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        keepHardEdge (bool?): If true, vertices on hard edges will not be modified.  
                C: Default is false.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepMapBorders (int?): Treatment of UV map borders  
                0. all map border edges will be smoothed  
                1. map borders that are also geometry borders will be smoothed  
                2. no map borders will be smoothed  
                Properties: create
        keepSelectionBorder (bool?): If true, vertices on border of the selection will not be modified.  
                C: Default is false.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepTesselation (bool?): If true: the object will be smoothed consistently from frame to frame.  
                This is best when the object is being deformed or animated .  
                If false: non-starlike faces will be triangulated before being  
                smoothed.  This avoids self-overlapping faces, but could lead to a  
                change in topology (number of vertices/faces) from frame to frame,  
                during an animated deformation.  
                Properties: create
        keepTessellation (bool?): If true: the object will be smoothed consistently from frame to frame.  
                This is best when the object is being deformed or animated .  
                If false: non-starlike faces will be triangulated before being  
                smoothed.  This avoids self-overlapping faces, but could lead to a  
                change in topology (number of vertices/faces) from frame to frame,  
                during an animated deformation.  
                Properties: create
        method (int?): Type of smoothing algorithm to use  
                0. exponential - traditional smoothing  
                1. linear - number of faces per edge grows linearly  
                Properties: create
        osdCreaseMethod (Queryable[int]?): Controls how boundary edges and vertices are interpolated.  
                Properties: create, query, edit
        osdFvarBoundary (Queryable[int]?): Controls how boundaries are treated for face-varying data (UVs and Vertex Colors).  
                Properties: create, query, edit
        osdFvarPropagateCorners (bool?):   
                Properties: create, query, edit
        osdSmoothTriangles (bool?): Apply a special subdivision rule be applied to all triangular faces  
                that was empirically determined to make triangles subdivide more smoothly.  
                Properties: create, query, edit
        osdVertBoundary (Queryable[int]?): Controls how boundary edges and vertices are interpolated.  
                Properties: create, query, edit
        propagateEdgeHardness (bool?): If true, edges which are a result of smoothed edges will be given  
                the same value for their edge hardness.  New subdivided edges will  
                always be smooth.  
                C: Default is false.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        pushStrength (float?): COMMENT 0.0 is approximation, 1.0 is interpolation scheme  
                Properties: create
        roundness (float?): When 1.0, push vectors are renormalized to keep length constant  
                Properties: create
        smoothUVs (bool?): If true: UVs as well as geometry will be smoothed  
                Properties: create
        subdivisionLevels (int?): Number of times the subdivide and smooth operation is run.  
                Properties: create
        subdivisionType (Queryable[int]?): The subdivision method used for smoothing.  
                C: Default is 0.  
                0. Maya Catmull-Clark  
                1. OpenSubdiv Catmull-Clark  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

