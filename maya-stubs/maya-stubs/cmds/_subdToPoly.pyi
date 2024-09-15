from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdToPoly(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., applyMatrixToResult: bool = ..., caching: bool = ..., copyUVTopology: bool = ..., depth: Queryable[int] = ..., extractPointPosition: bool = ..., format: Queryable[int] = ..., inSubdCVId: Queryable[Multiuse[Tuple[int, int]]] = ..., inSubdCVIdLeft: Queryable[int] = ..., inSubdCVIdRight: Queryable[int] = ..., maxPolys: Queryable[int] = ..., nodeState: Queryable[int] = ..., outSubdCVId: Queryable[Multiuse[Tuple[int, int]]] = ..., outSubdCVIdLeft: Queryable[int] = ..., outSubdCVIdRight: Queryable[int] = ..., outv: Queryable[Multiuse[int]] = ..., preserveVertexOrdering: bool = ..., sampleCount: Queryable[int] = ..., shareUVs: bool = ..., subdNormals: bool = ..., addUnderTransform: bool = ..., connectShaders: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ...) -> Union[List[str], bool, int, Multiuse[Tuple[int, int]], Multiuse[int]]:
    """This command tessellates a subdivision surface and produces polygon.
    The name of the new polygon is returned.
    If construction history is ON, then the name of the new dependency
    node is returned as well.
    Args:
        applyMatrixToResult (bool?): If true, the matrix on the input geometry is applied to the object  
                and the resulting geometry will have identity matrix on it.  If false  
                the conversion is done on the local space object and the resulting  
                geometry has the input object's matrix on it.  
                Default: true  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        copyUVTopology (bool?): Copy over uv topology (shared/unshared) from the original subdivision  
                surface to the converted polygonal mesh.  
                Default: false  
                Properties: create, query, edit
        depth (Queryable[int]?): The depth at which constant-depth tessellates the surface  
                Default: 0  
                Properties: create, query, edit
        extractPointPosition (bool?): Determines how the position of a mesh point is calculated  
                If on the position of the mesh point is returned. If off the  
                position of the point of the surface is returned.  
                Default: false  
                Properties: create, query, edit
        format (Queryable[int]?): Format:  
              
                0. Uniform  
                1. Adaptive  
                2. Polygon Count  
                3. Vertices  
              
                Default: 0  
                Properties: create, query, edit
        inSubdCVId (Queryable[Multiuse[Tuple[int, int]]]?): Input CV Id  
                Properties: create, query, edit, multiuse
        inSubdCVIdLeft (Queryable[int]?): Higher 32 bit integer of the input CV Id  
                Properties: create, query, edit
        inSubdCVIdRight (Queryable[int]?): Lower 32 bit integer of the input CV Id  
                Properties: create, query, edit
        maxPolys (Queryable[int]?): The maximum number of polygons at which by polygons tessellates.  
                If this attribute is greater than zero, it will override the  
                sample count and depth attributes.  
                Default: 0  
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
        outSubdCVId (Queryable[Multiuse[Tuple[int, int]]]?): Output CV Id  
                Properties: create, query, edit, multiuse
        outSubdCVIdLeft (Queryable[int]?): Higher 32 bit integer of the output CV Id  
                Properties: create, query, edit
        outSubdCVIdRight (Queryable[int]?): Lower 32 bit integer of the output CV Id  
                Properties: create, query, edit
        outv (Queryable[Multiuse[int]]?): Out Vertices corresponding to the inSubDCVs.  
                Properties: create, query, edit, multiuse
        preserveVertexOrdering (bool?): Preserve vertex ordering in conversion  
                Default: true  
                Properties: create, query, edit
        sampleCount (Queryable[int]?): The number of samples per face  
                Default: 1  
                Properties: create, query, edit
        shareUVs (bool?): Force sharing of uvs on all common vertices - the value of this  
                attribute gets overridden by the value of the copyUVTopology attribute.  
                Default: false  
                Properties: create, query, edit
        subdNormals (bool?): Keep subdiv surface normals  
                Default: false  
                Properties: create, query, edit
        addUnderTransform (bool?): If true then add the result underneath a transform node  
                Properties: create, query
        connectShaders (bool?): If true, all shader assignment will be copied from the  
                original subdiv surface to the converted polygonal surface.  
                Default: true  
                Properties: create
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create

    Returns:
        List[str]: The polygon and optionally the dependency node name

    Example:
    """

