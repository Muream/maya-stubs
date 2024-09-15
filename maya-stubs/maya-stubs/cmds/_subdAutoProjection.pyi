from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdAutoProjection(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., nodeState: Queryable[int] = ..., constructionHistory: bool = ..., layout: Queryable[int] = ..., layoutMethod: Queryable[int] = ..., name: str = ..., optimize: Queryable[int] = ..., percentageSpace: Queryable[float] = ..., planes: Queryable[int] = ..., scale: Queryable[int] = ..., skipIntersect: bool = ..., worldSpace: bool = ...) -> Union[str, bool, int, float]:
    """Projects a texture map onto an object, using several orthogonal projections
    simultaneously.The argument is a face selection list.
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
        layout (Queryable[int]?): What layout algorithm should be used:  
                0 UV pieces are aligned along the U axis.  
                1 UV pieces are moved in a square shape.  
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
        optimize (Queryable[int]?): Use two different flavors for the cut generation.  
                0 Every face is assigned to the best plane. This optimizes the  
                map distortion.  
                1 Small UV pieces are incorporated into larger ones, when the  
                extra distortion introduced is reasonable. This tends to produce fewer  
                UV pieces.  
                Properties: create, query, edit
        percentageSpace (Queryable[float]?): When layout is set to square, this value is a percentage of  
                the texture area which is added around each UV piece. It can be  
                used to ensure each UV piece uses different pixels in the texture.  
                Maximum value is 5 percent.  
                Properties: create, query, edit
        planes (Queryable[int]?): Number of intermediate projections used. Valid numbers  
                are 4, 5, 6, 8, and 12.  
                C: Default is 6.  
                Properties: create, query, edit
        scale (Queryable[int]?): How to scale the pieces, after projections:  
                0 No scale is applied.  
                1 Uniform scale to fit in unit square.  
                2 Non proportional scale to fit in unit square.  
                Properties: create, query, edit
        skipIntersect (bool?): When on, self intersection of UV pieces are not  
                tested. This makes the projection faster and produces fewer pieces,  
                but may lead to overlaps in UV space.  
                Properties: create, query, edit
        worldSpace (bool?): This flag specifies which reference to use.  
                If "on" : all geometrical values are taken in world reference.  
                If "off" : all geometrical values are taken in object reference.  
                C: Default is "off".  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

