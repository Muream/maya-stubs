from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySplitRing(*args: str, edit: bool = ..., query: bool = ..., adjustEdgeFlow: Queryable[float] = ..., caching: bool = ..., constructionHistory: bool = ..., direction: bool = ..., divisions: Queryable[int] = ..., enableProfileCurve: bool = ..., fixQuads: bool = ..., insertWithEdgeFlow: bool = ..., name: str = ..., nodeState: Queryable[int] = ..., profileCurveInputOffset: Queryable[float] = ..., profileCurveInputScale: Queryable[float] = ..., profileCurve_FloatValue: Queryable[float] = ..., profileCurve_Interp: Queryable[int] = ..., profileCurve_Position: Queryable[float] = ..., rootEdge: Queryable[int] = ..., smoothingAngle: Queryable[float] = ..., splitType: Queryable[int] = ..., useEqualMultiplier: bool = ..., useFaceNormalsAtEnds: bool = ..., weight: Queryable[float] = ..., worldSpace: bool = ...) -> Union[str, float, bool, int]:
    """Splits a series of ring edges of connected quads and
    inserts connecting edges between them.
    Args:
        adjustEdgeFlow (Queryable[float]?): The weight value of the edge vertices to be positioned.  
                Default: 1.0f  
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
        direction (bool?): This attribute is used when doing an absolute split.  If true then the  
                distance is taken from the start vertex of the root edge.  If false the  
                distance is taken from the end vertext of the root edge.  
                Default: true  
                Properties: create, query, edit
        divisions (Queryable[int]?): Number of divisions.  
                Default: 2  
                Properties: create, query, edit
        enableProfileCurve (bool?): Enables the use of the profile curve.  
                Default: true  
                Properties: create, query, edit
        fixQuads (bool?): Fixes splits which go across a quad face leaving a 5 and 3  
                sided faces by splitting from the middle of the new edge to  
                the vertex accross from the edge on the 5 sided face.  
                Default: false  
                Properties: create, query, edit
        insertWithEdgeFlow (bool?): True to enable edge flow. Otherwise, the edge flow is disabled.  
                Default: false  
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
        profileCurveInputOffset (Queryable[float]?): Changes the offset to the multisplit profile curve.  
                eg. if the profile curve values go between 0 and 1 and this  
                value is set to -1 then the profile curves values will be  
                adjusted to go between -1 and 0.  
                Default: 0.0f  
                Properties: create, query, edit
        profileCurveInputScale (Queryable[float]?): Changes the range of values that the profile curve represents.  
                eg. if the profile curve values go between 0 and 1 and this  
                value is set to 2 then the profile curves values will be  
                adjusted to go between 0 and 2.  
                Default: 1.0f  
                Properties: create, query, edit
        profileCurve_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        profileCurve_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        profileCurve_Position (Queryable[float]?): ?????  
                Properties: create, query, edit
        rootEdge (Queryable[int]?): The weight attribute uses the start vertex of this  
                edge to determine where the new split occurs.  
                Default: -1  
                Properties: create, query, edit
        smoothingAngle (Queryable[float]?): Angle below which new edges will be smoothed  
                Default: kPi  
                Properties: create, query, edit
        splitType (Queryable[int]?): Format: 0. Absolute, 1. Relative, 2. Multi  
                Default: TdnpolySplitRing::Relative  
                Properties: create, query, edit
        useEqualMultiplier (bool?): Changes how the profile curve effects the offset when doing  
                a multisplit.  If true then the verts will be offset the same distance  
                based on the shortest edge being split.  If false then each inserted  
                edge loop will be offset a distance relative to the length of the edge  
                that is being split.  
                Default: true  
                Properties: create, query, edit
        useFaceNormalsAtEnds (bool?): When doing a multisplit on a set of non-closed edge ring  
                this will toggle the normals at the ends of the split to  
                be calculated as the edge normal or the face normal.  
                Default: true  
                Properties: create, query, edit
        weight (Queryable[float]?): Weight value controlling the relative positioning of the  
                new points on existing edges. Range is [0.0, 1.0].  
                Value of 0.1 indicates the new edges will be placed closer to  
                the start vertex of the first edge of the sequence of edges.  
                Default: 0.5  
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

