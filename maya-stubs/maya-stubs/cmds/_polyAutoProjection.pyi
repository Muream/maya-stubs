from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyAutoProjection(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., createNewMap: bool = ..., insertBeforeDeformers: bool = ..., layout: Queryable[int] = ..., name: str = ..., nodeState: Queryable[int] = ..., optimize: Queryable[int] = ..., percentageSpace: Queryable[float] = ..., planes: Queryable[int] = ..., projectBothDirections: bool = ..., scaleMode: Queryable[int] = ..., skipIntersect: bool = ..., uvSetName: str = ..., worldSpace: bool = ..., layoutMethod: Queryable[int] = ..., pivot: Queryable[Tuple[float, float, float]] = ..., pivotX: Queryable[float] = ..., pivotY: Queryable[float] = ..., pivotZ: Queryable[float] = ..., rotate: Queryable[Tuple[float, float, float]] = ..., rotateX: Queryable[float] = ..., rotateY: Queryable[float] = ..., rotateZ: Queryable[float] = ..., scale: Queryable[Tuple[float, float, float]] = ..., scaleX: Queryable[float] = ..., scaleY: Queryable[float] = ..., scaleZ: Queryable[float] = ..., translate: Queryable[Tuple[float, float, float]] = ..., translateX: Queryable[float] = ..., translateY: Queryable[float] = ..., translateZ: Queryable[float] = ...) -> Union[str, bool, int, float, Tuple[float, float, float]]:
    """Projects a map onto an object, using several orthogonal projections
    simultaneously.
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
        createNewMap (bool?): Set to true if a new map should be created  
                Properties: create
        insertBeforeDeformers (bool?): Set to true if the new node created should inserted before any deformer nodes.  
                Properties: create
        layout (Queryable[int]?): What layout algorithm should be used:  
                0 UV pieces are set to no layout.  
                1 UV pieces are aligned along the U axis.  
                2 UV pieces are moved in a square shape.  
                Properties: create, query, edit
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
        projectBothDirections (bool?): This flag specifies which reference to use.  
                If "on" : projections are mirrored on directly opposite faces.  
                If "off" : projections are not mirrored on opposite faces.  
                C: Default is "off".  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        scaleMode (Queryable[int]?): How to scale the pieces, after projections:  
                0 No scale is applied.  
                1 Uniform scale to fit in unit square.  
                2 Non proportional scale to fit in unit square.  
                Properties: create, query, edit
        skipIntersect (bool?): When on, self intersection of UV pieces are not  
                tested. This makes the projection faster and produces fewer pieces,  
                but may lead to overlaps in UV space.  
                Properties: create, query, edit
        uvSetName (str?): Name of the UV set to be created  
                Properties: create
        worldSpace (bool?): This flag specifies which reference to use.  
                If "on" : all geometrical values are taken in world reference.  
                If "off" : all geometrical values are taken in object reference.  
                C: Default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        layoutMethod (Queryable[int]?): Set which layout method to use:  
                0 Block Stacking.  
                1 Shape Stacking.  
                Properties: create, query, edit
        pivot (Queryable[Tuple[float, float, float]]?): This flag specifies the pivot for scaling and rotation.  
                C: Default is 0.0 0.0 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        pivotX (Queryable[float]?): This flag specifies the X pivot for scaling and rotation.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        pivotY (Queryable[float]?): This flag specifies the Y pivot for scaling and rotation.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        pivotZ (Queryable[float]?): This flag specifies the Z pivot for scaling and rotation.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        rotate (Queryable[Tuple[float, float, float]]?): This flag specifies the rotation angles around X, Y, Z.  
                C: Default is 0.0 0.0 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        rotateX (Queryable[float]?): This flag specifies the rotation angle around X.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        rotateY (Queryable[float]?): This flag specifies the rotation angle around Y.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        rotateZ (Queryable[float]?): This flag specifies the rotation angle around Z.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        scale (Queryable[Tuple[float, float, float]]?): This flag specifies the scaling vector.  
                C: Default is 1.0 1.0 1.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        scaleX (Queryable[float]?): This flag specifies X for scaling vector.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        scaleY (Queryable[float]?): This flag specifies Y for scaling vector.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        scaleZ (Queryable[float]?): This flag specifies Z for scaling vector.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        translate (Queryable[Tuple[float, float, float]]?): This flag specifies the translation vector.  
                C: Default is 0.0 0.0 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        translateX (Queryable[float]?): This flag specifies the X translation vector.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        translateY (Queryable[float]?): This flag specifies the Y translation vector.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        translateZ (Queryable[float]?): This flag specifies the Z translation vector.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

