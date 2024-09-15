from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyChipOff(*args: str, edit: bool = ..., query: bool = ..., attraction: Queryable[float] = ..., caching: bool = ..., constructionHistory: bool = ..., duplicate: bool = ..., gain: Queryable[Multiuse[float]] = ..., gravity: Queryable[Tuple[float, float, float]] = ..., gravityX: Queryable[float] = ..., gravityY: Queryable[float] = ..., gravityZ: Queryable[float] = ..., keepFacesTogether: bool = ..., keepFacetTogether: bool = ..., localCenter: Queryable[int] = ..., localDirection: Queryable[Tuple[float, float, float]] = ..., localDirectionX: Queryable[float] = ..., localDirectionY: Queryable[float] = ..., localDirectionZ: Queryable[float] = ..., localRotate: Queryable[Tuple[float, float, float]] = ..., localRotateX: Queryable[float] = ..., localRotateY: Queryable[float] = ..., localRotateZ: Queryable[float] = ..., localScale: Queryable[Tuple[float, float, float]] = ..., localScaleX: Queryable[float] = ..., localScaleY: Queryable[float] = ..., localScaleZ: Queryable[float] = ..., localTranslate: Queryable[Tuple[float, float, float]] = ..., localTranslateX: Queryable[float] = ..., localTranslateY: Queryable[float] = ..., localTranslateZ: Queryable[float] = ..., magnX: Queryable[float] = ..., magnY: Queryable[float] = ..., magnZ: Queryable[float] = ..., magnet: Queryable[Tuple[float, float, float]] = ..., name: str = ..., nodeState: Queryable[int] = ..., offset: Queryable[float] = ..., pivot: Queryable[Tuple[float, float, float]] = ..., pivotX: Queryable[float] = ..., pivotY: Queryable[float] = ..., pivotZ: Queryable[float] = ..., random: Queryable[float] = ..., scale: Queryable[Tuple[float, float, float]] = ..., scaleX: Queryable[float] = ..., scaleY: Queryable[float] = ..., scaleZ: Queryable[float] = ..., translate: Queryable[Tuple[float, float, float]] = ..., translateX: Queryable[float] = ..., translateY: Queryable[float] = ..., translateZ: Queryable[float] = ..., weight: Queryable[float] = ..., worldSpace: bool = ...) -> Union[str, float, bool, Multiuse[float], Tuple[float, float, float], int]:
    """Extract facets. Faces can be extracted separately or together, and
    manipulations can be performed either in world or object space.
    Args:
        attraction (Queryable[float]?): Attraction, related to magnet.  
                The range is [-2.0, 2.0].  
                Default: 0.0  
                Properties: create, query, edit
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
        duplicate (bool?): If "on", facets are duplicated, otherwise original facets are removed.  
                C: Default is "on".  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        gain (Queryable[Multiuse[float]]?): Gain factor per component. Can be painted using Artisan.  
                Default: 1.0  
                Properties: create, query, edit, multiuse
        gravity (Queryable[Tuple[float, float, float]]?): The gravity vector.  
                Default: 0.0, -1.0, 0.0  
                Properties: create, query, edit
        gravityX (Queryable[float]?): Gravity X coord.  
                Properties: create, query, edit
        gravityY (Queryable[float]?): Gravity Y coord.  
                Properties: create, query, edit
        gravityZ (Queryable[float]?): Gravity Z coord.  
                Properties: create, query, edit
        keepFacesTogether (bool?): How to extrude edges.  
                If "on", extruded faces produced from the edges being extruded  
                will be kept together. Otherwise they are pulled independently.  
                Default: true  
                Properties: create, query, edit
        keepFacetTogether (bool?): How to extrude edges.  
                If "on", extruded faces produced from the edges being extruded  
                will be kept together. Otherwise they are pulled independently.  
                Default: true  
                Properties: create, query, edit
        localCenter (Queryable[int]?): Local center on the edge : 0=Middle point, 1=Start point, 2=End point.  
                Default: 0  
                Properties: create, query, edit
        localDirection (Queryable[Tuple[float, float, float]]?): Direction to determine X axis for local space.  
                Default: 1.0, 0.0, 0.0  
                Properties: create, query, edit
        localDirectionX (Queryable[float]?): X coord of the X axis.  
                Properties: create, query, edit
        localDirectionY (Queryable[float]?): Y coord of the X axis.  
                Properties: create, query, edit
        localDirectionZ (Queryable[float]?): Z coord of the X axis.  
                Properties: create, query, edit
        localRotate (Queryable[Tuple[float, float, float]]?): The local rotations.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        localRotateX (Queryable[float]?): Local rotate X coord.  
                The range is [0, 360].  
                Properties: create, query, edit
        localRotateY (Queryable[float]?): Local rotate Y coord.  
                The range is [0, 360].  
                Properties: create, query, edit
        localRotateZ (Queryable[float]?): Local rotate Z coord : Rotation along the normal.  
                The range is [0, 360].  
                Properties: create, query, edit
        localScale (Queryable[Tuple[float, float, float]]?): Local Scale.  
                Default: 1.0, 1.0, 1.0  
                Properties: create, query, edit
        localScaleX (Queryable[float]?): Scale X coord.  
                Properties: create, query, edit
        localScaleY (Queryable[float]?): Scale Y coord.  
                Properties: create, query, edit
        localScaleZ (Queryable[float]?): Scale Z coord.  
                Properties: create, query, edit
        localTranslate (Queryable[Tuple[float, float, float]]?): Local translate.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        localTranslateX (Queryable[float]?): Local translation X coord.  
                Properties: create, query, edit
        localTranslateY (Queryable[float]?): Local translation Y coord.  
                Properties: create, query, edit
        localTranslateZ (Queryable[float]?): Local translation Z coord : Move along the normal.  
                Properties: create, query, edit
        magnX (Queryable[float]?): Magnet X coord.  
                Properties: create, query, edit
        magnY (Queryable[float]?): Magnet Y coord.  
                Properties: create, query, edit
        magnZ (Queryable[float]?): Magnet Z coord.  
                Properties: create, query, edit
        magnet (Queryable[Tuple[float, float, float]]?): The magnet vector.  
                Default: 0.0, 0.0, 0.0  
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
        offset (Queryable[float]?): Local offset. Faces are moved this distance towards the inside of the face.  
                Default: 0.0  
                Properties: create, query, edit
        pivot (Queryable[Tuple[float, float, float]]?): The pivot for scaling and rotation.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        pivotX (Queryable[float]?): Pivot X coord.  
                Properties: create, query, edit
        pivotY (Queryable[float]?): Pivot Y coord.  
                Properties: create, query, edit
        pivotZ (Queryable[float]?): Pivot Z coord.  
                Properties: create, query, edit
        random (Queryable[float]?): Random value for all parameters.  
                Default: 0.0  
                Properties: create, query, edit
        scale (Queryable[Tuple[float, float, float]]?): Scaling vector.  
                Default: 1.0, 1.0, 1.0  
                Properties: create, query, edit
        scaleX (Queryable[float]?): Scale X coord.  
                Properties: create, query, edit
        scaleY (Queryable[float]?): Scale Y coord.  
                Properties: create, query, edit
        scaleZ (Queryable[float]?): Scale Z coord.  
                Properties: create, query, edit
        translate (Queryable[Tuple[float, float, float]]?): Translation vector.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        translateX (Queryable[float]?): Translation X coord.  
                Properties: create, query, edit
        translateY (Queryable[float]?): Translation Y coord.  
                Properties: create, query, edit
        translateZ (Queryable[float]?): Translation Z coord.  
                Properties: create, query, edit
        weight (Queryable[float]?): The weight, related to gravity.  
                Default: 0.0  
                Properties: create, query, edit
        worldSpace (bool?): This flag specifies which reference to use.  
                If "on" : all geometrical values are taken in world reference.  
                If "off" : all geometrical values are taken in object reference.  
                C: Default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

