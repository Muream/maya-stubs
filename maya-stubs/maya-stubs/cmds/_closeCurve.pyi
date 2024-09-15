from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def closeCurve(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., blendBias: Queryable[float] = ..., blendKnotInsertion: bool = ..., caching: bool = ..., nodeState: Queryable[int] = ..., parameter: Queryable[float] = ..., preserveShape: Queryable[int] = ..., constructionHistory: bool = ..., curveOnSurface: bool = ..., name: str = ..., object: bool = ..., replaceOriginal: bool = ...) -> Union[List[str], float, bool, int]:
    """The closeCurve command closes a curve, making it periodic.
    The pathname to the newly closed curve and the name
    of the resulting dependency node are returned.  If a curve
    is not specified in the command, then the first active curve
    will be used.
    Args:
        blendBias (Queryable[float]?): Skew the result toward the first or the second curve depending  
                on the blend value being smaller or larger than 0.5.  
                Default: 0.5  
                Properties: create, query, edit
        blendKnotInsertion (bool?): If set to true, insert a knot in one of the original curves  
                (relative position given by the parameter attribute below)  
                in order to produce a slightly different effect.  
                Default: false  
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
        parameter (Queryable[float]?): The parameter value for the positioning of the newly inserted knot.  
                Default: 0.1  
                Properties: create, query, edit
        preserveShape (Queryable[int]?): 0. without preserving the shape  
                1. preserve shape  
                2. blend  
                Default: 1  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        curveOnSurface (bool?): If possible, create 2D curve as a result.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        replaceOriginal (bool?): Create "in place" (i.e., replace).  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

