from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def alignSurface(arg0: str = ..., arg1: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., curvatureContinuity: bool = ..., curvatureScale1: Queryable[float] = ..., curvatureScale2: Queryable[float] = ..., directionU: bool = ..., joinParameter: Queryable[float] = ..., nodeState: Queryable[int] = ..., positionalContinuity: bool = ..., positionalContinuityType: Queryable[int] = ..., reverse1: bool = ..., reverse2: bool = ..., swap1: bool = ..., swap2: bool = ..., tangentContinuity: bool = ..., tangentContinuityType: Queryable[int] = ..., tangentScale1: Queryable[float] = ..., tangentScale2: Queryable[float] = ..., twist: bool = ..., attach: bool = ..., constructionHistory: bool = ..., keepMultipleKnots: bool = ..., name: str = ..., object: bool = ..., replaceOriginal: bool = ...) -> Union[List[str], bool, float, int]:
    """The surface align command is used to align surfaces in maya. The main
    alignment options are positional, tangent and curvature continuity.
    Curvature continuity implies tangent continuity.NOTE: this tool is based on Studio's align tool.Positional continuity means the surfaces (move) or the ends of the
    surfaces (modify) are changed.Tangent continuity means one of the surfaces is modified to be tangent
    at the points where they meet.Curvature continuity means one of the surfaces is modified to be
    curvature continuous as well as tangent.The default behaviour, when no surfaces or flags are passed, is to only
    do positional and tangent continuity on the active list with the end
    of the first surface and the start of the other surface used for
    alignment.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        curvatureContinuity (bool?): Curvature continuity is on if true and off otherwise.  
                Default: false  
                Properties: create, query, edit
        curvatureScale1 (Queryable[float]?): Curvature scale applied to curvature of first surface for curvature continuity.  
                Default: 0.0  
                Properties: create, query, edit
        curvatureScale2 (Queryable[float]?): Curvature scale applied to curvature of second surface for curvature continuity.  
                Default: 0.0  
                Properties: create, query, edit
        directionU (bool?): If true use U direction of surface and V direction otherwise.  
                Default: true  
                Properties: create, query, edit
        joinParameter (Queryable[float]?): Parameter on reference surface where modified surface is to be aligned to.  
                Default: 123456.0  
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
        positionalContinuity (bool?): Positional continuity is on if true and off otherwise.  
                Default: true  
                Properties: create, query, edit
        positionalContinuityType (Queryable[int]?): Positional continuity type legal values:  
                1. move first surface,  
                2. move second surface,  
                3. move both surfaces,  
                4. modify first surface,  
                5. modify second surface,  
                6. modify both surfaces  
                Default: 1  
                Properties: create, query, edit
        reverse1 (bool?): If true, reverse the direction (specified by directionU) of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.  
                Default: false  
                Properties: create, query, edit
        reverse2 (bool?): If true, reverse the direction (specified by directionU) of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.  
                Default: false  
                Properties: create, query, edit
        swap1 (bool?): If true, swap the UV directions of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.  
                Default: false  
                Properties: create, query, edit
        swap2 (bool?): If true, swap the UV directions of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.  
                Default: false  
                Properties: create, query, edit
        tangentContinuity (bool?): Tangent continuity is on if true and off otherwise.  
                Default: true  
                Properties: create, query, edit
        tangentContinuityType (Queryable[int]?): Tangent continuity type legal values:  
                1. do tangent continuity on first surface,  
                2. do tangent continuity on second surface  
                Default: 1  
                Properties: create, query, edit
        tangentScale1 (Queryable[float]?): Tangent scale applied to tangent of first surface for tangent continuity.  
                Default: 1.0  
                Properties: create, query, edit
        tangentScale2 (Queryable[float]?): Tangent scale applied to tangent of second surface for tangent continuity.  
                Default: 1.0  
                Properties: create, query, edit
        twist (bool?): If true, reverse the second surface in the opposite direction (specified by directionU) before doing align. This will avoid twists in the aligned surfaces. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.  
                Default: false  
                Properties: create, query, edit
        attach (bool?): Should surfaces be attached after alignment?  
                Properties: create
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        keepMultipleKnots (bool?): Should multiple knots be kept?  
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

