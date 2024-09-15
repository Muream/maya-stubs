from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySphere(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., name: str = ..., nodeState: Queryable[int] = ..., object: bool = ..., axis: Queryable[Tuple[float, float, float]] = ..., createUVs: int = ..., radius: Queryable[float] = ..., subdivisionsAxis: Queryable[int] = ..., subdivisionsHeight: Queryable[int] = ..., subdivisionsX: Queryable[int] = ..., subdivisionsY: Queryable[int] = ..., texture: int = ...) -> Union[List[str], bool, int, Tuple[float, float, float], float]:
    """The sphere command creates a new polygonal sphere.
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
        axis (Queryable[Tuple[float, float, float]]?): This flag specifies the primitive axis used to build the sphere.  
                Q: When queried, this flag returns a float[3].  
                Properties: create, query, edit
        createUVs (int?): This flag alows a specific UV mechanism to be selected, while creating the sphere.  
                The valid values are 0, 1, or 2.  
                0 implies that no UVs will be generated (No texture to be applied).  
              
                1 implies UVs are created with pinched at poles  
              
                2 implies UVs are created with sawtooth at poles  
              
                  For better understanding of these options, you may have to open the  
                     texture view window  
              
                C: Default is 2  
                Properties: create
        radius (Queryable[float]?): This flag specifies the radius of the sphere.  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        subdivisionsAxis (Queryable[int]?): Subdivisions around the axis.  
                Properties: create, query, edit
        subdivisionsHeight (Queryable[int]?): Subdivisions along the height of the sphere.  
                Properties: create, query, edit
        subdivisionsX (Queryable[int]?): This specifies the number of subdivisions in the X direction for the sphere.  
                C: Default is 20.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        subdivisionsY (Queryable[int]?): This flag specifies the number of subdivisions in the Y direction for the sphere.  
                C: Default is 20.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        texture (int?): This flag is obsolete and will be removed in the next release.  
                The -cuv/createUVs flag should be used instead.  
                Properties: create

    Returns:
        List[str]: Object name and node name.

    Example:
    """

