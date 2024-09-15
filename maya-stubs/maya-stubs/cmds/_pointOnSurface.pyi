from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pointOnSurface(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., nodeState: Queryable[int] = ..., normal: bool = ..., normalizedNormal: bool = ..., normalizedTangentU: bool = ..., normalizedTangentV: bool = ..., parameterU: Queryable[float] = ..., parameterV: Queryable[float] = ..., position: bool = ..., tangentU: bool = ..., tangentV: bool = ..., turnOnPercentage: bool = ...) -> Union[Tuple[float, float, float], str, bool, int, float]:
    """This command returns information for a point on a surface.
    If no flag is specified, this command assumes p/position by default.
    If more than one flag is specifed, then a string array is returned.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
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
        normal (bool?): Returns the (x,y,z) normal of the specified point on the surface  
                Properties: create, query, edit
        normalizedNormal (bool?): Returns the (x,y,z) normalized normal of the specified point  
                on the surface  
                Properties: create, query, edit
        normalizedTangentU (bool?): Returns the (x,y,z) normalized U tangent of the specified point  
                on the surface  
                Properties: create, query, edit
        normalizedTangentV (bool?): Returns the (x,y,z) normalized V tangent of the specified point  
                on the surface  
                Properties: create, query, edit
        parameterU (Queryable[float]?): The U parameter value on surface  
                Default: 0.0  
                Properties: query, edit
        parameterV (Queryable[float]?): The V parameter value on surface  
                Default: 0.0  
                Properties: query, edit
        position (bool?): Returns the (x,y,z) positon of the specified point on the surface  
                Properties: create, query, edit
        tangentU (bool?): Returns the (x,y,z) U tangent of the specified point on the surface  
                Properties: create, query, edit
        tangentV (bool?): Returns the (x,y,z) V tangent of the specified point on the surface  
                Properties: create, query, edit
        turnOnPercentage (bool?): Whether the parameter is normalized (0,1) or not  
                Default: false  
                Properties: query, edit

    Returns:
        Tuple[float, float, float]: Vector query result
        str: String query result

    Example:
    """

