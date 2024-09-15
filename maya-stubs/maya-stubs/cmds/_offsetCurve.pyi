from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def offsetCurve(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., connectBreaks: Queryable[int] = ..., cutLoop: bool = ..., cutRadius: Queryable[float] = ..., distance: Queryable[float] = ..., nodeState: Queryable[int] = ..., normal: Queryable[Tuple[float, float, float]] = ..., reparameterize: bool = ..., stitch: bool = ..., subdivisionDensity: Queryable[int] = ..., tolerance: Queryable[float] = ..., useGivenNormal: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., range: bool = ...) -> Union[List[str], bool, int, float, Tuple[float, float, float]]:
    """The offset command creates new offset curves from the selected curves.
    The connecting type for breaks in offsets is off (no connection),
    circular (connect with an arc) or linear (connect linearly resulting
    in a sharp corner). If loop cutting is on then any loops in the
    offset curves are trimmed away. For the default cut radius of 0.0 a
    sharp corner is created at each intersection. For values greater than
    0.0 a small arc of that radius is created at each intersection.
    The cut radius value is only valid when loop cutting is on.
    Offsets (for planar curves) are calculated in the plane of that curve
    and 3d curves are offset in 3d. The subdivisionDensity flag is the maximum
    number of times the offset object can be subdivided (i.e. calculate
    the offset until the offset comes within tolerance or the iteration
    reaches this maximum.)
    The reparameterize option allows the offset curve to have a different
    parameterization to the original curve. This avoids uneven parameter
    distributions in the offset curve that can occur with large offsets
    of curves, but is more expensive to compute.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        connectBreaks (Queryable[int]?): Connect breaks method (between gaps):  
                0. off,  
                1. circular,  
                2. linear  
                Default: 2  
                Properties: create, query, edit
        cutLoop (bool?): Do loop cutting.  
                Default: false  
                Properties: create, query, edit
        cutRadius (Queryable[float]?): Loop cut radius. Only used if cutLoop attribute is set true.  
                Default: 0.0  
                Properties: create, query, edit
        distance (Queryable[float]?): Offset distance  
                Default: 1.0  
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
        normal (Queryable[Tuple[float, float, float]]?): Offset plane normal  
                Properties: create, query, edit
        reparameterize (bool?): Do reparameterization. It is not advisable to change this value.  
                Default: false  
                Properties: create, query, edit
        stitch (bool?): Stitch curve segments together. It is not advisable to change this value.  
                Default: true  
                Properties: create, query, edit
        subdivisionDensity (Queryable[int]?): Maximum subdivision density per span  
                Default: 5  
                Properties: create, query, edit
        tolerance (Queryable[float]?): Tolerance  
                Default: 0.01  
                Properties: create, query, edit
        useGivenNormal (bool?): Use the given normal (or, alternativelly, geometry normal)  
                Default: 1  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        range (bool?): Force a curve range on complete input curve.  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

