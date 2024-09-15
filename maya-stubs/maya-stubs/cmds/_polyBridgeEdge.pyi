from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyBridgeEdge(*args: str, edit: bool = ..., query: bool = ..., bridgeOffset: Queryable[int] = ..., caching: bool = ..., constructionHistory: bool = ..., curveType: Queryable[int] = ..., divisions: Queryable[int] = ..., inputCurve: str = ..., name: str = ..., nodeState: Queryable[int] = ..., smoothingAngle: Queryable[float] = ..., startVert1: Queryable[int] = ..., startVert2: Queryable[int] = ..., taper: Queryable[float] = ..., taperCurve_FloatValue: Queryable[float] = ..., taperCurve_Interp: Queryable[int] = ..., taperCurve_Position: Queryable[float] = ..., twist: Queryable[float] = ..., worldSpace: bool = ...) -> Union[str, int, bool, float]:
    """Bridges two sets of edges.
    Args:
        bridgeOffset (Queryable[int]?): Add offset to which vertices are connected.  
                Default: 0  
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
        curveType (Queryable[int]?): Format: 0. Linear, 1. Blend, 2. Curve  
                Default: TdnpolyBridgeEdge::Linear  
                Properties: create, query, edit
        divisions (Queryable[int]?): The number of subdivisions in the bridging faces  
                (resulting in (divisions+1) row of faces).  
                Default: 1  
                Properties: create, query, edit
        inputCurve (str?): This flag specifies the name of the curve to be used as input for the operation.  
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
        smoothingAngle (Queryable[float]?): Angle below which new edges will be smoothed  
                Default: kPi/6.0  
                Properties: create, query, edit
        startVert1 (Queryable[int]?): The start vertex from the first set of edges  
                Default: -1  
                Properties: create, query, edit
        startVert2 (Queryable[int]?): The start vertex from the second set of edges  
                Default: -1  
                Properties: create, query, edit
        taper (Queryable[float]?): Taper or Scale along the extrusion path  
                Default: 1.0  
                Properties: create, query, edit
        taperCurve_FloatValue (Queryable[float]?): Value for taperCurve;  
                Curve control for taper along extrusion  
                Using this curve, the taper along extrusion  
                can be changed from a simple linear scaling to  
                custom scaling along the extrusion path.  
                Properties: create, query, edit
        taperCurve_Interp (Queryable[int]?): Interpolation type for taperCurve;  
                Curve control for taper along extrusion  
                Using this curve, the taper along extrusion  
                can be changed from a simple linear scaling to  
                custom scaling along the extrusion path.  
                Properties: create, query, edit
        taperCurve_Position (Queryable[float]?): Position for taperCurve;  
                Curve control for taper along extrusion  
                Using this curve, the taper along extrusion  
                can be changed from a simple linear scaling to  
                custom scaling along the extrusion path.  
                Properties: create, query, edit
        twist (Queryable[float]?): Twist or Rotation along the extrusion path  
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

