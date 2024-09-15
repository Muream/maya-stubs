from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def stitchSurfacePoints(*args: str, edit: bool = ..., query: bool = ..., bias: Queryable[float] = ..., caching: bool = ..., cvIthIndex: Queryable[Multiuse[int]] = ..., cvJthIndex: Queryable[Multiuse[int]] = ..., fixBoundary: bool = ..., nodeState: Queryable[int] = ..., parameterU: Queryable[Multiuse[float]] = ..., parameterV: Queryable[Multiuse[float]] = ..., positionalContinuity: Queryable[Multiuse[bool]] = ..., stepCount: Queryable[Multiuse[int]] = ..., tangentialContinuity: Queryable[Multiuse[bool]] = ..., togglePointNormals: bool = ..., togglePointPosition: bool = ..., toggleTolerance: Queryable[Multiuse[bool]] = ..., tolerance: Queryable[Multiuse[float]] = ..., cascade: bool = ..., constructionHistory: bool = ..., equalWeight: bool = ..., keepG0Continuity: bool = ..., keepG1Continuity: bool = ..., name: str = ..., object: bool = ..., replaceOriginal: bool = ...) -> Union[List[str], float, bool, Multiuse[int], int, Multiuse[float], Multiuse[bool]]:
    """The stitchSurfacePoints command aligns two or more surface points
    along the boundaries together to a single point. In the process, a
    node to average the points is created. The points are averaged
    together in a weighted fashion. The points may be control vertices
    along the boundaries. If the points are CVs then they are stitched
    together only with positional continuity.Note: No two points can lie on the same surface.
    Args:
        bias (Queryable[float]?): Blend CVs in between input surface and result from stitch. A value of 0.0 returns the input surface.  
                Default: 1.0  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        cvIthIndex (Queryable[Multiuse[int]]?): The ith boundary CV index on the input surface.  
                Default: -1  
                Properties: create, query, edit, multiuse
        cvJthIndex (Queryable[Multiuse[int]]?): The jth boundary CV index on the input surface.  
                Default: -1  
                Properties: create, query, edit, multiuse
        fixBoundary (bool?): Fix Boundary CVs while solving for any G1 constraints.  
                Default: false  
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
        parameterU (Queryable[Multiuse[float]]?): The U parameter value on surface for a point constraint.  
                Default: -10000  
                Properties: create, query, edit, multiuse
        parameterV (Queryable[Multiuse[float]]?): The V parameter value on surface for a point constraint.  
                Default: -10000  
                Properties: create, query, edit, multiuse
        positionalContinuity (Queryable[Multiuse[bool]]?): Toggle on (off) G0 continuity at edge corresponding to multi index.  
                Default: true  
                Properties: create, query, edit, multiuse
        stepCount (Queryable[Multiuse[int]]?): Step count for the number of discretizations.  
                Default: 20  
                Properties: create, query, edit, multiuse
        tangentialContinuity (Queryable[Multiuse[bool]]?): Toggle on (off) G1 continuity across edge corresponding to multi index.  
                Default: false  
                Properties: create, query, edit, multiuse
        togglePointNormals (bool?): Toggle on (off) normal point constraints on the surface.  
                Default: false  
                Properties: create, query, edit
        togglePointPosition (bool?): Toggle on (off) position point constraints on the surface.  
                Default: true  
                Properties: create, query, edit
        toggleTolerance (Queryable[Multiuse[bool]]?): Toggle on (off) so as to use Tolerance or specified steps for discretization.  
                Default: false  
                Properties: create, query, edit, multiuse
        tolerance (Queryable[Multiuse[float]]?): Tolerance to use while discretizing the edge.  
                Default: 0.1  
                Properties: create, query, edit, multiuse
        cascade (bool?): Cascade the created stitch node. (Only if the surface has a stitch  
                history)  
                Default is 'false'.  
                Properties: create
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        equalWeight (bool?): Assign equal weights to all the points being stitched together.  
                Default is 'true'. If false, the first point is assigned a weight of  
                1.0 and the rest are assigned 0.0.  
                Properties: create
        keepG0Continuity (bool?): Stitch together the points with positional continuity.  
                Default is 'true'.  
                Properties: create
        keepG1Continuity (bool?): Stitch together the points with tangent continuity.  
                Default is 'false'.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        replaceOriginal (bool?): Create "in place" (i.e., replace).  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

