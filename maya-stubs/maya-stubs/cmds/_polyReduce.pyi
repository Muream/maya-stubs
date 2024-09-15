from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyReduce(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., cachingReduce: bool = ..., colorWeights: Queryable[float] = ..., compactness: Queryable[float] = ..., constructionHistory: bool = ..., geomWeights: Queryable[float] = ..., invertVertexWeights: bool = ..., keepBorder: bool = ..., keepBorderWeight: Queryable[float] = ..., keepColorBorder: bool = ..., keepColorBorderWeight: Queryable[float] = ..., keepCreaseEdge: bool = ..., keepCreaseEdgeWeight: Queryable[float] = ..., keepFaceGroupBorder: bool = ..., keepFaceGroupBorderWeight: Queryable[float] = ..., keepHardEdge: bool = ..., keepHardEdgeWeight: Queryable[float] = ..., keepMapBorder: bool = ..., keepMapBorderWeight: Queryable[float] = ..., keepOriginalVertices: bool = ..., keepQuadsWeight: Queryable[float] = ..., name: str = ..., nodeState: Queryable[int] = ..., percentage: Queryable[float] = ..., preserveLocation: bool = ..., preserveTopology: bool = ..., replaceOriginal: bool = ..., sharpness: Queryable[float] = ..., symmetryPlaneW: Queryable[float] = ..., symmetryPlaneX: Queryable[float] = ..., symmetryPlaneY: Queryable[float] = ..., symmetryPlaneZ: Queryable[float] = ..., symmetryTolerance: Queryable[float] = ..., termination: Queryable[int] = ..., triangleCount: Queryable[int] = ..., triangulate: bool = ..., useVirtualSymmetry: Queryable[int] = ..., uvWeights: Queryable[float] = ..., version: Queryable[int] = ..., vertexCount: Queryable[int] = ..., vertexMapName: Queryable[str] = ..., vertexWeightCoefficient: Queryable[float] = ..., weightCoefficient: Queryable[float] = ...) -> Union[str, bool, float, int]:
    """Simplify a polygonal object by reducing geometry while preserving the
    overall shape of the mesh.The algorithm for polyReduce was changed in 2014 to use a new algorithm derived
    from Softimage. However, the command still defaults to using the old algorithm
    for backwards compatibility.  Therefore, we recommend setting the version flag
    to 1 for best results as the new algorithm is better at preserving geometry
    features.  Additionally, some flags only apply to a specific algorithm and
    this is documented for each flag.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        cachingReduce (bool?): Cache intermediate reductions for speed at the expense of memory.  
                It is recommended that caching be enabled when using the new  
                algorithm. (-version 1)  However, caching is not recommended  
                when using then old algorithm because it can cause stability  
                issues.  
                C: Default is false.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        colorWeights (Queryable[float]?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                How much consideration vertex color is given in the reduction  
                algorithm. A higher weight means the reduction will try  
                harder to preserve vertex coloring.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        compactness (Queryable[float]?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                Tolerance for compactness for the generated triangles  
                A value of 0 will accept all triangles during decimation  
                A value close to 0 will attempt to eliminate triangles  
                that have collinear edges (zero area triangles)  
                A value closer to 1 will attempt to eliminate triangles  
                that are not strictly equilateral (of equal lengths)  
                The closer to 1.0, the more expensive the computation  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off (where applicable). If  
                construction history is on then the corresponding node will be  
                inserted into the history chain for the mesh. If construction history  
                is off then the operation will be performed directly on the object.  
              
                Note: If the object already has construction history then  
                this flag is ignored and the node will always be inserted into  
                the history chain.  
                Properties: create, query
        geomWeights (Queryable[float]?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                How much consideration vertex positions are given in the  
                reduction algorithm.  A higher weight means the reduction  
                will try harder to preserve geometry.  
                C: Default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        invertVertexWeights (bool?): This flag controls how weight map values are interpreted.  
                If true, a vertex weight of 1.0 means a vertex is unlikely to be reduced.  
                If false, a vertex weight of 0.0 means a vertex is unlikely to be reduced.  
                This flag only applies when using the new algorithm. (-version 1)  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepBorder (bool?): If true, reduction will try to retain geometric borders and  
                the border of the selection.  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepBorderWeight (Queryable[float]?): If keepBorder is on, this flag specifies the weight to assign  
                to borders.  Setting this value to 0 will disable border preservation  
                and a value of 1 will exactly preserve all border vertices which is  
                useful for matching adjacent meshes.  This flag only applies  
                when using the new algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepColorBorder (bool?): If true, reduction will try to retain color borders.  These are  
                determined according to color Ids.  This flag only applies  
                when using the new algorithm. (-version 1)  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepColorBorderWeight (Queryable[float]?): If keepColorBorder is on, this flag specifies the weight to  
                assign to color borders.  Setting this value to 0 will disable  
                color border preservation and a value of 1 will exactly preserve  
                all color borders.  This flag only applies when using the new  
                algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepCreaseEdge (bool?): If true, reduction will try to retain crease edges.  
                C: Default is true.  This flag only applies  
                when using the new algorithm. (-version 1)  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepCreaseEdgeWeight (Queryable[float]?): If keepCreaseEdge is on, this flag specifies the weight to assign  
                to crease edges.  Setting this value to 0 will disable crease  
                edge preservation and a value of 1 will exactly preserve all crease edges.  
                This flag only applies when using the new algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepFaceGroupBorder (bool?): If true, reduction will try to retain borders of face groups,  
                which are mostly used to define material assignments.  This  
                flag only applies when using the new algorithm. (-version 1)  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepFaceGroupBorderWeight (Queryable[float]?): If keepFaceGroupBorder is on, this flag specifies the weight to  
                assign to material borders.  Setting this value to 0 will disable  
                group border preservation and a value of 1 will exactly preserve all  
                group borders.  This flag only applies when using the new  
                algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepHardEdge (bool?): If true, reduction will try to retain hard edges.  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepHardEdgeWeight (Queryable[float]?): If keepHardEdge is on, this flag specifies the weight to assign  
                to hard edges.  Setting this value to 0 will disable hard  
                edge preservation and a value of 1 will exactly preserve all hard edges.  
                This flag only applies when using the new algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepMapBorder (bool?): If true, reduction will try to retain UV borders.  A UV border  
                is present if the faces on either side of the edge do not share  
                UV Ids.  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepMapBorderWeight (Queryable[float]?): If keepMapBorder is on, this flag specifies the weight to assign  
                to UV map borders.  Setting this value to 0 will disable UV map  
                border preservation and a value of 1 will exactly preserve all UV borders.  
                This flag only applies when using the new algorithm. (-version 1)  
                C: Default is 0.5.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        keepOriginalVertices (bool?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                If true, vertices will try to retain their original positions  
                and will not be repositioned for optimal shape.  
                NOTE: In the newer algorithm vertices always retain  
                their exact original positions. (though the Ids will change)  
                C: Default is false.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        keepQuadsWeight (Queryable[float]?): This flag controls how much consideration is given to  
                oreserving quad faces during reduction.  A higher  
                weight means the reduction will try harder to keep quad  
                faces and avoid creation of triangles. If the version  
                flag is set to 1 (-version 1) and the keepQuadsWeight  
                flag is set to 1.0 then a special quad reduction algorithm  
                is used that does a better job of preserving quads.  
                Howver, this special quad reduction algorithm does  
                not support symmetry so those flags will be ignored  
                when the keepQuadsWeight flag is set to 1.0.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
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
        percentage (Queryable[float]?): This flag specifies how many vertices to remove during reduction as a  
                percentage of the original mesh.  This flag only applies if the termination  
                flag is set to 0 or when using the old algorithm.  
                C: Default is 0. 100 will remove every possible vertex, 0 will remove none.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        preserveLocation (bool?): This flag guarantees that if the original geometry is preserved, the new  
                geometry will have the same location.  
                C: Default is false.  
                Properties: create
        preserveTopology (bool?): this flag guarantees that the topological type will be preserved during  
                reduction.  In particular, if the input is manifold then the output will be  
                manifold.  This option also prevents holes in the mesh from being closed off.  
                This flag only applies when using the new algorithm. (-version 1)  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        replaceOriginal (bool?): Create "in place" (i.e., replace) (not available in all commands). NOTE:  
                This flag is intended for use by the "Reduce" menu item. If  
                'polyReduce -rpo 0' is executed from the command line, Shader information will  
                not be copied from the original mesh to the result.  
                Properties: create
        sharpness (Queryable[float]?): Sharpness controls the balance between preserving small, sharp  
                details versus larger shapes.  At low values, details that are  
                small relative to the general shape of the object are more  
                likely to be collapsed.  At high values, they are more likely  
                to be kept.  This flag only applies when using the new  
                algorithm. (-version 1)  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetryPlaneW (Queryable[float]?): W value of the symmetry plane.  This flag only applies  
                when using the new algorithm (-version 1) and the  
                useVirtualSymmetry flag is set to 2.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetryPlaneX (Queryable[float]?): X value of the symmetry plane.  This flag only applies  
                when using the new algorithm (-version 1) and the  
                useVirtualSymmetry flag is set to 2.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetryPlaneY (Queryable[float]?): Y value of the symmetry plane.  This flag only applies  
                when using the new algorithm (-version 1) and the  
                useVirtualSymmetry flag is set to 2.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetryPlaneZ (Queryable[float]?): Z value of the symmetry plane.  This flag only applies  
                when using the new algorithm (-version 1) and the  
                useVirtualSymmetry flag is set to 2.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetryTolerance (Queryable[float]?): Tolerance to use when applying symmetry.  
                For each vertex of the mesh, we find its exact symmetric point,  
                then we look for the closest vertex to the exact symmetry up to  
                the tolerance distance.  Higher values risk finding more  
                spurious symmetries, lower values might miss symmetries.  
                The value is distance in object space.  This flag only applies  
                when using the new algorithm (-version 1) and the  
                useVirtualSymmetry flag is not set to 0.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        termination (Queryable[int]?): This flag specifies the termination condition to use  
                when reducing the mesh.  This flag only applies to the  
                new algorithm. (-version 1)  
                0 Percentage  
                1 Vertex count  
                2 Triangle count  
                C: Default is 0.  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        triangleCount (Queryable[int]?): This flag specifies a target number of triangles to retain after reduction.  
                Note that other factors such as quad and feature preservation  
                may take precendence and cause the actual number of triangles to be different.  
                This flag only applies when using the new algorithm (-version 1)  
                and the termination flag is set to 2.  
                C: Default is 0.  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        triangulate (bool?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                This attribute specifies if the geometry  
                or the selected faces has to be triangulated,  
                before performing reduction.  
                C: Default is true.  
                Q: When queried, this flag returns a boolean.  
                Properties: create, query, edit
        useVirtualSymmetry (Queryable[int]?): This flag controls whether symmetry is preserved during the  
                reduction. This flag only applies when using the new  
                algorithm (-version 1) and the keepQuadsWeight flag is less  
                than 1.0.  
                0 No symmetry preservation  
                1 Automatic. Try to find suitable symmetry during reduction.  
                2 Plane.  Specify a symmetry plane to use during reduction.  
                C: Default is 0.  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        uvWeights (Queryable[float]?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                How much consideration uv positions are given in the  
                reduction algorithm. A higher weight means the  
                reduction will try harder to preserve uv positions.  
                C: Default is 0.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        version (Queryable[int]?): Version of the poly reduce algorithm to use.  
                0 Old algorithm used in Maya 2013 and prior for backwards compatibility  
                1 New algorithm derived from Softimage and used in Maya 2014 and later  
                The default is 0 for backwards compatibility but for best results  
                it is recommended that the new algorithm is used as it is better at  
                preserving mesh details. Some flags only apply to a specific algorithm  
                and this is documented for each flag.  
                C: Default is 0 for backwards compatibility.  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        vertexCount (Queryable[int]?): This flag specifies a target number of vertices to retain after reduction.  
                Note that other factors such as quad and feature preservation  
                may take precendence and cause the actual number of vertices to be different.  
                This flag only applies when using the new algorithm (-version 1)  
                and the termination flag is set to 1.  
                C: Default is 0.  
                Q: When queried, this flag returns an integer.  
                Properties: create, query, edit
        vertexMapName (Queryable[str]?): Name of a color set to be added to the output mesh that stores  
                a mapping from vertices in the output mesh to vertices in the  
                input mesh.  The color set is RGB.  The original vertex Id that  
                maps to an output vertex is of a vertex is 65536*r + g where r  
                and g are the red and green channel at a vertex. The blue  
                channel is always zero.  Each vertex in the output mesh has a  
                shared color. This flag only applies when using the new  
                algorithm. (-version 1)  
                Q: When queried, this flag returns a string.  
                Properties: create, query
        vertexWeightCoefficient (Queryable[float]?): This flag specifies a constant value to multiply to each weight map value.  
                A value of zero turns off the weight map.  This flag only applies  
                when using the new algorithm. (-version 1)  
                C: Default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        weightCoefficient (Queryable[float]?): This flag only applies when using the old algorithm and  
                is provided for backwards compatibility.  
                The weight of each vertex is multiplied with this coefficient  
                when the reduction is performed.  This value does not have  
                to be edited, normally.  It gives finer control over the  
                weighted reduction. This attribute is replaced by  
                vertexWeightCoefficient in the new algorithm when the version  
                flag is set to 1.  
                C: Default is 10000.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

