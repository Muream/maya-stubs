from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyColorMod(*args: str, edit: bool = ..., query: bool = ..., alphaScale_FloatValue: Queryable[float] = ..., alphaScale_Interp: Queryable[int] = ..., alphaScale_Position: Queryable[float] = ..., baseColorName: str = ..., blueScale_FloatValue: Queryable[float] = ..., blueScale_Interp: Queryable[int] = ..., blueScale_Position: Queryable[float] = ..., caching: bool = ..., constructionHistory: bool = ..., greenScale_FloatValue: Queryable[float] = ..., greenScale_Interp: Queryable[int] = ..., greenScale_Position: Queryable[float] = ..., huev: Queryable[float] = ..., intensityScale_FloatValue: Queryable[float] = ..., intensityScale_Interp: Queryable[int] = ..., intensityScale_Position: Queryable[float] = ..., name: str = ..., nodeState: Queryable[int] = ..., redScale_FloatValue: Queryable[float] = ..., redScale_Interp: Queryable[int] = ..., redScale_Position: Queryable[float] = ..., satv: Queryable[float] = ..., value: Queryable[float] = ...) -> Union[str, float, int, bool]:
    """Modifies the attributes of a poly color set.
    Args:
        alphaScale_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        alphaScale_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        alphaScale_Position (Queryable[float]?): ?????  
                Properties: create, query, edit
        baseColorName (str?): The name of the color set to be modified.  
                Properties: create
        blueScale_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        blueScale_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        blueScale_Position (Queryable[float]?): ?????  
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
        greenScale_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        greenScale_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        greenScale_Position (Queryable[float]?): ?????  
                Properties: create, query, edit
        huev (Queryable[float]?): Hue  rotates hue value of the final color.  
                Default: 0.0  
                Properties: create, query, edit
        intensityScale_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        intensityScale_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        intensityScale_Position (Queryable[float]?): ?????  
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
        redScale_FloatValue (Queryable[float]?): ?????  
                Properties: create, query, edit
        redScale_Interp (Queryable[int]?): ?????  
                Default: 0  
                Properties: create, query, edit
        redScale_Position (Queryable[float]?): ?????  
                Properties: create, query, edit
        satv (Queryable[float]?): Sat scales the staturation of the final color.  
                Default: 1.0  
                Properties: create, query, edit
        value (Queryable[float]?): Value scales the final color value.  
                Default: 1.0  
                Properties: create, query, edit

    Returns:
        str: The node name.

    Example:
    """

