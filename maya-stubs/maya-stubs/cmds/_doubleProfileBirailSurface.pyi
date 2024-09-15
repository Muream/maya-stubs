from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def doubleProfileBirailSurface(arg0: str = ..., arg1: str = ..., arg2: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., blendFactor: Queryable[float] = ..., caching: bool = ..., nodeState: Queryable[int] = ..., tangentContinuityProfile1: bool = ..., tangentContinuityProfile2: bool = ..., transformMode: Queryable[int] = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., polygon: int = ...) -> Union[List[str], float, bool, int]:
    """The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".This command builds a railed surface by sweeping profile "profile1"
    along the two given rail curves "rail1", "rail2" until "profile2" is
    reached. By using the -blend control, the railed surface creation
    could be biased more towards one of the two profile curves. The curves
    ( both profiles and rails ) could also be surface curves ( isoparams,
    curve on surfaces ). If the profile curves are surface curves the
    surface constructed could be made tangent continuous to the surfaces
    underlying the profiles using the flags -tp1, -tp2 respectively.
    Current Limitation: Its necessary that the two profile curves
    intersect the rail curves for successful surface creation.
    Args:
        blendFactor (Queryable[float]?): A blend factor applied in between the two profiles.  
                The amount of influence 'inputProfile1' has in the surface creation.  
                Default: 0.5  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
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
        tangentContinuityProfile1 (bool?): Need tangent continuity across the input profile at inputProfile1.  
                Default: false  
                Properties: create, query, edit
        tangentContinuityProfile2 (bool?): Need tangent continuity across the input curve at inputProfile2.  
                Default: false  
                Properties: create, query, edit
        transformMode (Queryable[int]?): transform mode ( Non proportional, proportional ). Non proportional is default value.  
                Default: 0  
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
        polygon (int?): The value of this argument controls the type of the object  
                created by this operation  
              
                 0. nurbs surface  
                 1. polygon (use nurbsToPolygonsPref to set the parameters for the conversion)  
                 2. subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)  
                 3. Bezier surface  
                 4. subdivision surface solid (use nurbsToSubdivPref to set the  
                parameters for the conversion)  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

