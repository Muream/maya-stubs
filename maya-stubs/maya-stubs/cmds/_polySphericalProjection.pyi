from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySphericalProjection(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., createNewMap: bool = ..., insertBeforeDeformers: bool = ..., keepImageRatio: bool = ..., mapDirection: str = ..., name: str = ..., nodeState: Queryable[int] = ..., perInstance: bool = ..., smartFit: bool = ..., worldSpace: bool = ..., imageCenter: Queryable[Tuple[float, float]] = ..., imageCenterX: Queryable[float] = ..., imageCenterY: Queryable[float] = ..., imageScale: Queryable[Tuple[float, float]] = ..., imageScaleU: Queryable[float] = ..., imageScaleV: Queryable[float] = ..., projectionCenter: Queryable[Tuple[float, float, float]] = ..., projectionCenterX: Queryable[float] = ..., projectionCenterY: Queryable[float] = ..., projectionCenterZ: Queryable[float] = ..., projectionHorizontalSweep: Queryable[float] = ..., projectionScale: Queryable[Tuple[float, float]] = ..., projectionScaleU: Queryable[float] = ..., projectionScaleV: Queryable[float] = ..., radius: Queryable[float] = ..., rotate: Queryable[Tuple[float, float, float]] = ..., rotateX: Queryable[float] = ..., rotateY: Queryable[float] = ..., rotateZ: Queryable[float] = ..., rotationAngle: Queryable[float] = ..., seamCorrect: bool = ...) -> Union[str, bool, int, Tuple[float, float], float, Tuple[float, float, float]]:
    """TpolyProjCmdBase is a base class for the command to create a mapping on the selected polygonal faces.
    Projects a spherical map onto an object.
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
        createNewMap (bool?): This flag when set true will create a new map with  
                a the name passed in, if the map does not already exist.  
                Properties: create, query
        insertBeforeDeformers (bool?): This flag specifies if the projection node should be inserted before  
                or after deformer nodes already applied to the shape. Inserting the  
                projection after the deformer leads to texture swimming during  
                animation and is most often undesirable.  
                C: Default is on.  
                Properties: create
        keepImageRatio (bool?): True means keep any image ratio  
                Properties: create
        mapDirection (str?): This flag specifies the mapping direction.  
                'x', 'y' and 'z' projects the map along the corresponding axis.  
                'c' projects along the current camera viewing direction.  
                'p' does perspective projection if current camera is perspective.  
                'b' projects along the best plane fitting the objects selected.  
                Properties: create
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
        perInstance (bool?): True if the new map is per-instance, otherwise it is shared.  
                Properties: create
        smartFit (bool?): True means use the smart fit algorithm  
                Properties: create
        worldSpace (bool?): This flag specifies which reference to use.  
                If "on" : all geometrical values are taken in world reference.  
                If "off" : all geometrical values are taken in object reference.  
                C: Default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        imageCenter (Queryable[Tuple[float, float]]?): This flag specifies the center point of the 2D model layout.  
                C: Default is 0.5 0.5.  
                Q: When queried, this flag returns a float[2].  
                Properties: create, query, edit
        imageCenterX (Queryable[float]?): This flag specifies X for the center point of the 2D model layout.  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        imageCenterY (Queryable[float]?): This flag specifies Y for the center point of the 2D model layout.  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        imageScale (Queryable[Tuple[float, float]]?): This flag specifies the UV scale : Enlarges or reduces the 2D version of the model in U  
                or V space relative to the 2D centerpoint.  
                C: Default is 1.0 1.0.  
                Q: When queried, this flag returns a float[2].  
                Properties: create, query, edit
        imageScaleU (Queryable[float]?): This flag specifies the U scale : Enlarges or reduces the 2D version of the model in U space relative to the 2D centerpoint.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        imageScaleV (Queryable[float]?): This flag specifies the V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        projectionCenter (Queryable[Tuple[float, float, float]]?): This flag specifies the origin point from which the map is projected.  
                C: Default is 0.0 0.0 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        projectionCenterX (Queryable[float]?): This flag specifies X for the origin point from which the map is projected.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        projectionCenterY (Queryable[float]?): This flag specifies Y for the origin point from which the map is projected.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        projectionCenterZ (Queryable[float]?): This flag specifies Z for the origin point from which the map is projected.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        projectionHorizontalSweep (Queryable[float]?): The angle swept horizontally by the projection.  The range is [0, 360].  
                Properties: create, query, edit
        projectionScale (Queryable[Tuple[float, float]]?): This flag specifies the width and the height of the map relative to the 3D projection axis.  
                C: Default is 180.0 90.0.  
                Q: When queried, this flag returns a float[2].  
                Properties: create, query, edit
        projectionScaleU (Queryable[float]?): This flag specifies the width of the map relative to the 3D projection axis : the scale aperture. The range is [0, 360].  
                C: Default is 180.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        projectionScaleV (Queryable[float]?): This flag specifies the height of the map relative to the 3D projection axis : the scale height.  
                C: Default is 90.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        radius (Queryable[float]?): Used by the UI : Manipulator.  
                Properties: create, query, edit
        rotate (Queryable[Tuple[float, float, float]]?): This flag specifies the mapping rotate angles.  
                C: Default is 0.0 0.0 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        rotateX (Queryable[float]?): This flag specifies X mapping rotate angle.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        rotateY (Queryable[float]?): This flag specifies Y mapping rotate angle.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        rotateZ (Queryable[float]?): This flag specifies Z mapping rotate angle.  
                C: Default is 0.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        rotationAngle (Queryable[float]?): This flag specifies the rotation angle in the mapping space.  
                When the angle is positive, then the map rotates  
                counterclockwise on the mapped model, whereas when it is  
                negative then the map rotates clockwise on the mapped model.  
                C: Default is 10.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        seamCorrect (bool?): This flag specifies to perform a seam correction  
                on the mapped faces.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

