from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyHelix(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., coils: Queryable[float] = ..., constructionHistory: bool = ..., createUVs: Queryable[int] = ..., direction: Queryable[int] = ..., height: Queryable[float] = ..., name: str = ..., nodeState: Queryable[int] = ..., object: bool = ..., radius: Queryable[float] = ..., roundCap: bool = ..., subdivisionsAxis: Queryable[int] = ..., subdivisionsCaps: Queryable[int] = ..., subdivisionsCoil: Queryable[int] = ..., texture: Queryable[int] = ..., useOldInitBehaviour: bool = ..., width: Queryable[float] = ...) -> Union[List[str], bool, float, int]:
    """The polyHelix command creates a new polygonal helix.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        coils (Queryable[float]?): Number of coils.  
                Default: 3  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        createUVs (Queryable[int]?): Create UVs or not.  
                0. No UVs  
                1. No Normalization  
                2. Normalize  
                3. Normalize and Preserve Aspect Ratio  
                Default: 2  
                Properties: create, query, edit
        direction (Queryable[int]?): What should be the direction of the coil.  
                0=Clockwise; 1=Counterclockwise  
                Default: 1  
                Properties: create, query, edit
        height (Queryable[float]?): Height of the helix.  
                Default: 2.0  
                Properties: create, query, edit
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
        radius (Queryable[float]?): Radius of tube.  
                Default: 0.4  
                Properties: create, query, edit
        roundCap (bool?): To indicate whether we need a round cap  
                Default: false  
                Properties: create, query, edit
        subdivisionsAxis (Queryable[int]?): Subdivisions around the axis.  
                Default: 8  
                Properties: create, query, edit
        subdivisionsCaps (Queryable[int]?): Subdivisions along the thickness caps.  
                Default: 0  
                Properties: create, query, edit
        subdivisionsCoil (Queryable[int]?): Subdivisions along the coil.  
                Default: 50  
                Properties: create, query, edit
        texture (Queryable[int]?): What texture mechanism to be applied  
                0=No textures; 1=Object; 2=Faces  
                Default: 2  
                Properties: create, query, edit
        useOldInitBehaviour (bool?): Create the helix with base on the origin as in Maya V8.0 and below  
                Otherwise create helix centred at origin  
                Default: false  
                Properties: create, query, edit
        width (Queryable[float]?): Width of the helix.  
                Default: 2.0  
                Properties: create, query, edit

    Returns:
        List[str]: Object name and node name.

    Example:
    """

