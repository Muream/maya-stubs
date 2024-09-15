from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rebuildSurface(arg0: str = ..., arg1: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., degreeU: Queryable[int] = ..., degreeV: Queryable[int] = ..., direction: Queryable[int] = ..., endKnots: Queryable[int] = ..., fitRebuild: Queryable[int] = ..., keepControlPoints: bool = ..., keepCorners: bool = ..., keepRange: Queryable[int] = ..., nodeState: Queryable[int] = ..., rebuildType: Queryable[int] = ..., spansU: Queryable[int] = ..., spansV: Queryable[int] = ..., tolerance: Queryable[float] = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., polygon: int = ..., replaceOriginal: bool = ...) -> Union[List[str], bool, int, float]:
    """This command rebuilds a surface by modifying its parameterization.
    In some cases the shape of the surface may also change. The
    rebuildType (-rt) attribute determines how the surface is rebuilt.The optional second surface can be used to specify a reference
    parameterization.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        degreeU (Queryable[int]?): The degree of the resulting surface in the u direction  
                0. maintain current,  
                1. linear,  
                2. quadratic,  
                3. cubic,  
                5. quintic,  
                7. heptic  
                Default: 3  
                Properties: create, query, edit
        degreeV (Queryable[int]?): The degree of the resulting surface in the v direction  
                0. maintain current,  
                1. linear,  
                2. quadratic,  
                3. cubic,  
                5. quintic,  
                7. heptic  
                Default: 3  
                Properties: create, query, edit
        direction (Queryable[int]?): The direction in which to rebuild:  
                0. U,  
                1. V,  
                2. Both U and V  
                Default: 2  
                Properties: create, query, edit
        endKnots (Queryable[int]?): End conditions for the surface  
                0. uniform end knots,  
                1. multiple end knots,  
                Default: 0  
                Properties: create, query, edit
        fitRebuild (Queryable[int]?): Specify the type of rebuild method to be used:  
                0. Convert Classic, the default and original convert method.  
                1. Fit using the least squares fit method.  
                2. Convert Match, alternate matching convert method.  
                3. Convert Grid, uses a grid-based fit algorithm.  
                Default: 0  
                Properties: create, query, edit
        keepControlPoints (bool?): Use the control points of the input surface.  
                This forces uniform parameterization unless rebuildType is 2 (match knots)  
                Default: false  
                Properties: create, query, edit
        keepCorners (bool?): The corners of the resulting surface will not change from the corners of the input surface.  
                Default: true  
                Properties: create, query, edit
        keepRange (Queryable[int]?): Determine the parameterization for the resulting surface.  
                0. reparameterize the resulting surface from 0 to 1;  
                1. keep the original surface parameterization;  
                2. reparameterize the result from 0 to number of spans  
                Default: 1  
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
        rebuildType (Queryable[int]?): The rebuild type:  
                0. uniform,  
                1. reduce spans,  
                2. match knots,  
                3. remove multiple knots,  
                4. force non rational  
                5. rebuild ends  
                6. trim convert (uniform)  
                7. into Bezier mesh  
                Default: 0  
                Properties: create, query, edit
        spansU (Queryable[int]?): The number of spans in the u direction in resulting surface. Used only when rebuildType is 0. uniform. If 0, keep the same number of spans as the original surface.  
                Default: 4  
                Properties: create, query, edit
        spansV (Queryable[int]?): The number of spans in the v direction in resulting surface. Used only when rebuildType is 0. uniform. If 0, keep the same number of spans as the original surface.  
                Default: 4  
                Properties: create, query, edit
        tolerance (Queryable[float]?): The tolerance with which to rebuild  
                Default: 0.01  
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
        replaceOriginal (bool?): Create "in place" (i.e., replace).  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

