from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyBevel3(*args: str, edit: bool = ..., query: bool = ..., angleTolerance: Queryable[float] = ..., autoFit: bool = ..., caching: bool = ..., chamfer: bool = ..., constructionHistory: bool = ..., depth: Queryable[float] = ..., fillNgons: bool = ..., mergeVertexTolerance: Queryable[float] = ..., mergeVertices: bool = ..., miterAlong: Queryable[int] = ..., mitering: Queryable[int] = ..., miteringAngle: Queryable[float] = ..., name: str = ..., nodeState: Queryable[int] = ..., offset: Queryable[float] = ..., offsetAsFraction: bool = ..., roundness: Queryable[float] = ..., segments: Queryable[int] = ..., smoothingAngle: Queryable[float] = ..., uvAssignment: Queryable[int] = ..., worldSpace: bool = ...) -> Union[str, float, bool, int]:
    """Bevel edges.
    Args:
        angleTolerance (Queryable[float]?): Angular tolerance for creation of extra triangles  
                Note this attribute is for compatability only and should not be modified in Maya 7.0 files  
                Default: 20.0  
                Properties: create, query, edit
        autoFit (bool?): If autoFit is on, it computes a smooth roundness :  new facets round off a smooth angle.  
                Default: true  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        chamfer (bool?): If chamfer is on, the surface is smoothed out at bevels. When it is off, the shape of the surface remains the same.  
                Default: true  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        depth (Queryable[float]?): The depth of bevel. One means a smooth surface, -1 means maximum depth.  
                Default: 1.0  
                Properties: create, query, edit
        fillNgons (bool?): Subdivide new faces with more than 4 edges  
                Default: false  
                Properties: create, query, edit
        mergeVertexTolerance (Queryable[float]?): Tolerance within which to merge vertices  
                Default: 0.0  
                Properties: create, query, edit
        mergeVertices (bool?): Merge vertices within a tolerance  
                Default: false  
                Properties: create, query, edit
        miterAlong (Queryable[int]?): Controls in which direction new vertices should we offseted.  
                Default: 0  
                Properties: create, query, edit
        mitering (Queryable[int]?): Controls how the topology should look like at corners.  
                Default: 0  
                Properties: create, query, edit
        miteringAngle (Queryable[float]?): Miter faces that have angles less than this value  
                Default: 0.0  
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
        offset (Queryable[float]?): The offset for bevel.  
                Default: 0.2  
                Properties: create, query, edit
        offsetAsFraction (bool?): If on, the offset value is treated as a fraction between zero and one.  
                Default: false  
                Properties: create, query, edit
        roundness (Queryable[float]?): The roundness of bevel, it is taken into account when autoFit is off.  
                Default: 0.5  
                Properties: create, query, edit
        segments (Queryable[int]?): The number of segments used for beveling.  
                Default: 1  
                Properties: create, query, edit
        smoothingAngle (Queryable[float]?): Create new edges as hard edges if the angle between adjacent faces exceeds this value  
                Default: 0.0  
                Properties: create, query, edit
        uvAssignment (Queryable[int]?): Technique used to compute UVs on new faces  
                0 computes new UVs by projecting along surface normal of original mesh onto new mesh  
                1 computes new UVs by projecting along surface normal of new mesh onto original mesh  
                Default: 0  
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

