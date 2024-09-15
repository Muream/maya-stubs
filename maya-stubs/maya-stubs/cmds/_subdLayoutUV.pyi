from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdLayoutUV(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., nodeState: Queryable[int] = ..., constructionHistory: bool = ..., flipReversed: bool = ..., layout: Queryable[int] = ..., layoutMethod: Queryable[int] = ..., name: str = ..., percentageSpace: Queryable[float] = ..., rotateForBestFit: Queryable[int] = ..., scale: Queryable[int] = ..., separate: Queryable[int] = ..., worldSpace: bool = ...) -> Union[str, bool, int, float]:
    """Move UVs in the texture plane to avoid overlaps.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
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
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        flipReversed (bool?): If this flag is turned on, the reversed UV pieces are fliped.  
                Properties: create, query, edit
        layout (Queryable[int]?): How to move the UV pieces, after cuts are applied:  
                0 No move is applied.  
                1 Layout the pieces along the U axis.  
                2 Layout the pieces in a square shape.  
                Properties: create, query, edit
        layoutMethod (Queryable[int]?): Which layout method to use:  
                0 Block Stacking.  
                1 Shape Stacking.  
                Properties: create, query, edit
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        percentageSpace (Queryable[float]?): When layout is set to square, this value is a percentage of  
                the texture area which is added around each UV piece. It can be  
                used to ensure each UV piece uses different pixels in the texture.  
                Maximum value is 5 percent.  
                Properties: create, query, edit
        rotateForBestFit (Queryable[int]?): 0 No rotation is applied.  
                1 Only allow 90 degree rotations.  
                2 Allow free rotations.  
                Properties: create, query, edit
        scale (Queryable[int]?): How to scale the pieces, after move and cuts:  
                0 No scale is applied.  
                1 Uniform scale to fit in unit square.  
                2 Non proportional scale to fit in unit square.  
                Properties: create, query, edit
        separate (Queryable[int]?): Which UV edges should be cut:  
                0 No cuts.  
                1 Cut only along folds.  
                2 Make all necessary cuts to avoid all intersections.  
                Properties: create, query, edit
        worldSpace (bool?): If true, performs the operation in world space coordinates as  
                opposed to local space.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

