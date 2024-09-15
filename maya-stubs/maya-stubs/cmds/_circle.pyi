from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def circle(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., center: Queryable[Tuple[float, float, float]] = ..., centerX: Queryable[float] = ..., centerY: Queryable[float] = ..., centerZ: Queryable[float] = ..., degree: Queryable[int] = ..., first: Queryable[Tuple[float, float, float]] = ..., firstPointX: Queryable[float] = ..., firstPointY: Queryable[float] = ..., firstPointZ: Queryable[float] = ..., fixCenter: bool = ..., nodeState: Queryable[int] = ..., normal: Queryable[Tuple[float, float, float]] = ..., normalX: Queryable[float] = ..., normalY: Queryable[float] = ..., normalZ: Queryable[float] = ..., radius: Queryable[float] = ..., sections: Queryable[int] = ..., sweep: Queryable[float] = ..., tolerance: Queryable[float] = ..., useTolerance: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ...) -> Union[List[str], bool, Tuple[float, float, float], float, int]:
    """The circle command creates a circle or partial circle (arc)
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        center (Queryable[Tuple[float, float, float]]?): The center point of the circle.  
                Properties: create, query, edit
        centerX (Queryable[float]?): X of the center point.  
                Default: 0  
                Properties: create, query, edit
        centerY (Queryable[float]?): Y of the center point.  
                Default: 0  
                Properties: create, query, edit
        centerZ (Queryable[float]?): Z of the center point.  
                Default: 0  
                Properties: create, query, edit
        degree (Queryable[int]?): The degree of the resulting circle:  
                1. linear,  
                3. cubic  
                Default: 3  
                Properties: create, query, edit
        first (Queryable[Tuple[float, float, float]]?): The start point of the circle if fixCenter is false.  
                Determines the orientation of the circle if fixCenter is true.  
                Properties: create, query, edit
        firstPointX (Queryable[float]?): X of the first point.  
                Default: 1  
                Properties: create, query, edit
        firstPointY (Queryable[float]?): Y of the first point.  
                Default: 0  
                Properties: create, query, edit
        firstPointZ (Queryable[float]?): Z of the first point.  
                Default: 0  
                Properties: create, query, edit
        fixCenter (bool?): Fix the center of the circle to the specified center point.  
                Otherwise the circle will start at the specified first point.  
                Default: true  
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
        normal (Queryable[Tuple[float, float, float]]?): The normal of the plane in which the circle will lie.  
                Properties: create, query, edit
        normalX (Queryable[float]?): X of the normal direction.  
                Default: 0  
                Properties: create, query, edit
        normalY (Queryable[float]?): Y of the normal direction.  
                Default: 0  
                Properties: create, query, edit
        normalZ (Queryable[float]?): Z of the normal direction.  
                Default: 1  
                Properties: create, query, edit
        radius (Queryable[float]?): The radius of the circle.  
                Default: 1.0  
                Properties: create, query, edit
        sections (Queryable[int]?): The number of sections determines the resolution of the circle.  
                Used only if useTolerance is false.  
                Default: 8  
                Properties: create, query, edit
        sweep (Queryable[float]?): The sweep angle determines the completeness of the circle.  
                A full circle is 2Pi radians, or 360 degrees.  
                Default: 6.2831853  
                Properties: create, query, edit
        tolerance (Queryable[float]?): The tolerance with which to build a circle.  
                Used only if useTolerance is true  
                Default: 0.01  
                Properties: create, query, edit
        useTolerance (bool?): Use the specified tolerance to determine resolution.  
                Otherwise number of sections will be used.  
                Default: false  
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

    Returns:
        List[str]: Object name and node name

    Example:
    """

