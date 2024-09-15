from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyAxis(*args: str, edit: bool = ..., query: bool = ..., arrowType: Queryable[int] = ..., axis: Queryable[Tuple[float, float, float]] = ..., caching: bool = ..., constructionHistory: bool = ..., frameType: Queryable[int] = ..., lengthX: Queryable[float] = ..., lengthY: Queryable[float] = ..., lengthZ: Queryable[float] = ..., materialTemplate: str = ..., name: str = ..., nodeState: Queryable[int] = ..., object: bool = ..., radius: Queryable[float] = ..., rightHanded: bool = ..., scale: Queryable[float] = ..., subdivisionsAxis: Queryable[int] = ...) -> Union[List[str], int, Tuple[float, float, float], bool, float]:
    """The polyAxis command creates a new polygonal shape representing a coordinate system.
    Args:
        arrowType (Queryable[int]?): This flag specifies the shape at the ends of the axis  
                The valid values are 0, 1 and 2.  
                0 means a flat end shape.  
                1 means a rounded end shape.  
                2 means a cone end shape.  
              
                C: Default is the cone end shape  
                Properties: create, query, edit
        axis (Queryable[Tuple[float, float, float]]?): This flag specifies the primitive axis used to build the frame. This is the axis that will point up.  
                Q: When queried, this flag returns a float[3].  
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
        frameType (Queryable[int]?): This flag allows a specific frame type to be created  
                The valid values are 0 and 1.  
                0 implies an axis shape will be created.  
                1 implies an wedge shape will be created.  
              
                C: Default is the axis shape  
                Properties: create, query, edit
        lengthX (Queryable[float]?): This flag specifies the length of the x-axis.  
                Properties: create, query, edit
        lengthY (Queryable[float]?): This flag specifies the length of the y-axis.  
                Properties: create, query, edit
        lengthZ (Queryable[float]?): This flag specifies the length of the z-axis.  
                Properties: create, query, edit
        materialTemplate (str?): Assign the specified material template to geoemtry. If it does  
                not exist one will be created with materials assigned to each  
                axis  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
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
        object (bool?): Create the result, or just the dependency node (where applicable).  
                Properties: create
        radius (Queryable[float]?): This flag specifies the radius of the axis.  
                Properties: create, query, edit
        rightHanded (bool?): When this is set to true the result will be a shape representing a right handed coordinate system  
                Properties: create, query, edit
        scale (Queryable[float]?): This flag specifies the overall scale of the frame shape.  
                Properties: create, query, edit
        subdivisionsAxis (Queryable[int]?): This specifies the number of subdivisions for the axis.  
                Properties: create, query, edit

    Returns:
        List[str]: Object name and node name.

    Example:
    """

