from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyPlatonicSolid(*args: str, edit: bool = ..., query: bool = ..., axis: Queryable[Tuple[float, float, float]] = ..., caching: bool = ..., constructionHistory: bool = ..., createUVs: int = ..., name: str = ..., nodeState: Queryable[int] = ..., object: bool = ..., radius: Queryable[float] = ..., sideLength: Queryable[float] = ..., solidType: int = ..., texture: int = ...) -> Union[List[str], Tuple[float, float, float], bool, int, float]:
    """The polyPlatonicSolid command creates a new polygonal platonic solid.
    Args:
        axis (Queryable[Tuple[float, float, float]]?): This flag specifies the primitive axis used to build the platonic solid.  
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
        createUVs (int?): This flag alows a specific UV mechanism to be selected, while creating.  
                The valid values are 0, 1,  2 ,3 or 4.  
                0 implies that no UVs will be generated (No texture to be applied).  
              
                1 implies UVs should be created for the object as a whole without any normalization.  
                 The solid will be unwrapped and then the texture will be applied  
                 without any distortion.  
                 In the unwrapped solid, the shared edges will have shared UVs.  
              
                2 implies UVs are created separately for each of the faces of the solid.  
              
                3 implies the UVs should be normalized. This will normalize the  
                 U and V direction separately, thereby resulting in distortion of textures.  
              
                4 implies UVs are created so that the texture will not be distorted when applied.  
                 The texture lying outside the UV range will be truncated (since that cannot be  
                 squeezed in, without distorting the texture.  
              
                  For better understanding of these options, you may have to open the  
                     texture view window  
              
                C: Default is 4  
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
        radius (Queryable[float]?): This flag specifies the radius of the platonic solid.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        sideLength (Queryable[float]?): This flag specifies the side length of platonic solid.  
                C: Default is 1.0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        solidType (int?): This flag allows a specific platonic solid to be selected for creation of mesh,  
                The valid values are 0, 1, 2 and 3.  
                0 implies dodecahedron to be created.  
                1 implies icosahedron to be created.  
                2 implies octahedron to be created.  
                3 implies tertrahedron to be created.  
              
                C: Default is 0  
                Properties: create
        texture (int?): This flag is obsolete and will be removed in the next release.  
                The -cuv/createUVs flag should be used instead.  
                Properties: create

    Returns:
        List[str]: Object name and node name.

    Example:
    """

