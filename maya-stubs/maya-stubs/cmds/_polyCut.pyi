from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCut(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., cutPlaneCenter: Queryable[Tuple[float, float, float]] = ..., cutPlaneCenterX: Queryable[float] = ..., cutPlaneCenterY: Queryable[float] = ..., cutPlaneCenterZ: Queryable[float] = ..., cutPlaneHeight: Queryable[float] = ..., cutPlaneRotate: Queryable[Tuple[float, float, float]] = ..., cutPlaneRotateX: Queryable[float] = ..., cutPlaneRotateY: Queryable[float] = ..., cutPlaneRotateZ: Queryable[float] = ..., cutPlaneSize: Queryable[Tuple[float, float]] = ..., cutPlaneWidth: Queryable[float] = ..., cuttingDirection: str = ..., deleteFaces: bool = ..., extractFaces: bool = ..., extractOffset: Queryable[Tuple[float, float, float]] = ..., extractOffsetX: Queryable[float] = ..., extractOffsetY: Queryable[float] = ..., extractOffsetZ: Queryable[float] = ..., name: str = ..., nodeState: Queryable[int] = ..., onObject: bool = ..., worldSpace: bool = ...) -> Union[str, bool, Tuple[float, float, float], float, Tuple[float, float], int]:
    """This command splits a mesh, or a set of poly faces, along a plane.
    The position and orientation of the plane can be adjusted using the
    appropriate flags listed above.  In addition, the cut operation can
    also delete the faces lying on one side of the cutting plane, or
    extract those faces by an offset amount.
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
        cutPlaneCenter (Queryable[Tuple[float, float, float]]?): The position of the cutting plane.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        cutPlaneCenterX (Queryable[float]?): Cutting plane center X coord.  
                Properties: create, query, edit
        cutPlaneCenterY (Queryable[float]?): Cutting plane center Y coord.  
                Properties: create, query, edit
        cutPlaneCenterZ (Queryable[float]?): Cutting plane center Z coord.  
                Properties: create, query, edit
        cutPlaneHeight (Queryable[float]?): The height of the cutting plane  
                Properties: create, query, edit
        cutPlaneRotate (Queryable[Tuple[float, float, float]]?): The orientation of the cutting plane.  
                Default: 0.0, 0.0, 0.0  
                Properties: create, query, edit
        cutPlaneRotateX (Queryable[float]?): cutting plane X rotate angle.  
                Properties: create, query, edit
        cutPlaneRotateY (Queryable[float]?): cutting plane Y rotate angle.  
                Properties: create, query, edit
        cutPlaneRotateZ (Queryable[float]?): cutting plane Z rotate angle.  
                Properties: create, query, edit
        cutPlaneSize (Queryable[Tuple[float, float]]?): The width and the height of the cutting plane  
                Default: 1.0, 1.0  
                Properties: create, query, edit
        cutPlaneWidth (Queryable[float]?): The width of the cutting plane  
                Properties: create, query, edit
        cuttingDirection (str?): This flag specifies the direction of the cutting plane.  
                Valid values are "x", "y", "z"  
                A value of "x" will cut the object along the YZ plane  
                cutting through the center of the bounding box.  
                A value of "y" will cut the object along the ZX plane  
                cutting through the center of the bounding box.  
                A value of "z" will cut the object along the XY plane  
                cutting through the center of the bounding box.  
                Properties: create
        deleteFaces (bool?): whether to delete the one-half of the cut-faces  
                of the poly.  If true, they are deleted.  
                Default: false  
                Properties: create, query, edit
        extractFaces (bool?): whether to extract the cut-faces of the poly  
                into a separate shell.  If true, they are extracted.  
                Default: false  
                Properties: create, query, edit
        extractOffset (Queryable[Tuple[float, float, float]]?): The displacement offset of the cut faces.  
                Default: 0.5, 0.5, 0.5  
                Properties: create, query, edit
        extractOffsetX (Queryable[float]?): The X-displacement offset of the cut faces.  
                Properties: create, query, edit
        extractOffsetY (Queryable[float]?): The Y-displacement offset of the cut faces.  
                Properties: create, query, edit
        extractOffsetZ (Queryable[float]?): The Z-displacement offset of the cut faces.  
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
        onObject (bool?): whether to act on the entire polyObject  
                or its selected face components  
                Default: true  
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

