from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def squareSurface(arg0: str = ..., arg1: str = ..., arg2: str = ..., arg3: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., continuityType1: Queryable[int] = ..., continuityType2: Queryable[int] = ..., continuityType3: Queryable[int] = ..., continuityType4: Queryable[int] = ..., curveFitCheckpoints: Queryable[int] = ..., endPointTolerance: Queryable[float] = ..., nodeState: Queryable[int] = ..., rebuildCurve1: bool = ..., rebuildCurve2: bool = ..., rebuildCurve3: bool = ..., rebuildCurve4: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., polygon: int = ...) -> Union[List[str], bool, int, float]:
    """This command produces a square surface given 3 or 4 curves.
    This resulting square surface is created within the intersecting
    region of the selected curves. The order of selection is important
    and the curves must intersect or their ends must meet.You must specify one continuity type flag for each selected curve.
    If continuity type is 1 (fixed, no tangent continuity) then the
    curveFitCheckpoints flag () is not required.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        continuityType1 (Queryable[int]?): Continuity type legal values for curve 1. 1. fixed boundary  
                2. tangent continuity  
                3. implied tangent continuity  
                Default: 2  
                Properties: create, query, edit
        continuityType2 (Queryable[int]?): Continuity type legal values for curve 2. 1. fixed boundary  
                2. tangent continuity  
                3. implied tangent continuity  
                Default: 2  
                Properties: create, query, edit
        continuityType3 (Queryable[int]?): Continuity type legal values for curve 3. 1. fixed boundary  
                2. tangent continuity  
                3. implied tangent continuity  
                Default: 2  
                Properties: create, query, edit
        continuityType4 (Queryable[int]?): Continuity type legal values for curve 4. 1. fixed boundary  
                2. tangent continuity  
                3. implied tangent continuity  
                Default: 2  
                Properties: create, query, edit
        curveFitCheckpoints (Queryable[int]?): The number of points per span to check the tangency deviation between the boundary curve and the created tangent square surface. Only available for the tangent continuity type.  
                Default: 5  
                Properties: create, query, edit
        endPointTolerance (Queryable[float]?): Tolerance for end points, only used if endPoint attribute is true.  
                Default: 0.1  
                Properties: create, query, edit
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
        rebuildCurve1 (bool?): A boolean to determine if input curve 1 should be rebuilt (with curvature continuity).  
                Default: false  
                Properties: create, query, edit
        rebuildCurve2 (bool?): A boolean to determine if input curve 2 should be rebuilt (with curvature continuity).  
                Default: false  
                Properties: create, query, edit
        rebuildCurve3 (bool?): A boolean to determine if input curve 3 should be rebuilt (with curvature continuity).  
                Default: false  
                Properties: create, query, edit
        rebuildCurve4 (bool?): A boolean to determine if input curve 4 should be rebuilt (with curvature continuity).  
                Default: false  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        polygon (int?): The value of this argument controls the type of the object  
                created by this operation  
              
                 0. nurbs surface  
                 1. polygon (use nurbsToPolygonsPref to set the parameters for the conversion)  
                 2. subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)  
                 3. Bezier surface  
                 4. subdivision surface solid (use nurbsToSubdivPref to set the  
                parameters for the conversion)  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

