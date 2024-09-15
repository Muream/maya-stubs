from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyBoolOp(arg0: str = ..., arg1: str = ..., /, *, edit: bool = ..., query: bool = ..., faceAreaThreshold: Queryable[float] = ..., operation: Queryable[int] = ..., preserveColor: bool = ..., useThresholds: bool = ..., vertexDistanceThreshold: Queryable[float] = ..., caching: bool = ..., mergeUVSets: Queryable[int] = ..., nodeState: Queryable[int] = ...) -> Union[List[str], float, int, bool]:
    """This command creates a new poly as the result of a boolean
    operation on input polys : union, intersection, difference.Only for difference, the order of the selected objects is
    important :result = object1 - object2.If no objects are specified in the command line, then the
    objects from the active list are used.
    Args:
        faceAreaThreshold (Queryable[float]?): Area threshold to determine whether faces should  
                be collapsed before boolean. Attribute is ignored unless  
                useThresholds is set to true  
                Default: 0.0001  
                Properties: create, query, edit
        operation (Queryable[int]?): Boolean operation type. 1=union, 2=difference, 3=intersection.  
                Default type is union.  
                Default: kBoolOpUnion  
                Properties: create, query, edit
        preserveColor (bool?): If true, boolean op will compute color for the  
                new mesh. If false, the new mesh won't have any color  
                set.  
                Default: false  
                Properties: create, query, edit
        useThresholds (bool?): If true, merge vertices with separations less then  
                vertexDistanceThreshold and collapse faces with areas  
                less then faceAreaThreshold. If false, do not merge  
                vertices or collapse faces  
                Default: false  
                Properties: create, query, edit
        vertexDistanceThreshold (Queryable[float]?): Tolerance to determine whether vertices (and edges) should  
                be merged before boolean operation is applied. Attribute is  
                ignored unless useThresholds is set to true  
                Default: 0.001  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        mergeUVSets (Queryable[int]?): Specify how UV sets will be merged on the output mesh.  
              
                0 = "No Merge": Each UV set on each mesh will become a new UV set in the output.  
                1 = "Merge By Name": UV sets with the same name will be merged.  
                2 = "Merge By UV Links": UV sets will be merged so that UV linking on the input meshes continues to work.  
              
                The default is merge by name.  
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

    Returns:
        List[str]: Object name and node name.

    Example:
    """

