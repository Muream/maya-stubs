from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def extrude(arg0: str = ..., arg1: str = ..., /, *, edit: bool = ..., query: bool = ..., caching: bool = ..., degreeAlongLength: Queryable[int] = ..., direction: Queryable[Tuple[float, float, float]] = ..., directionX: Queryable[float] = ..., directionY: Queryable[float] = ..., directionZ: Queryable[float] = ..., extrudeType: Queryable[int] = ..., fixedPath: bool = ..., length: Queryable[float] = ..., nodeState: Queryable[int] = ..., pivot: Queryable[Tuple[float, float, float]] = ..., reverseSurfaceIfPathReversed: bool = ..., rotation: Queryable[float] = ..., scale: Queryable[float] = ..., subCurveSubSurface: bool = ..., useComponentPivot: Queryable[int] = ..., useProfileNormal: bool = ..., constructionHistory: bool = ..., mergeItems: bool = ..., name: str = ..., object: bool = ..., polygon: int = ..., range: bool = ..., rebuild: bool = ...) -> Union[List[str], bool, int, Tuple[float, float, float], float]:
    """This command computes a surface given a profile curve and possibly
    a path curve. There are three ways to extrude a profile curve. The
    most basic method is called a "distance" extrude where direction and
    length are specified. No path curve is necessary in this case. The
    second method is called "flat" extrude. This method sweeps the profile
    curve down the path curve without changing the orientation of the
    profile curve. Finally, the third method is called "tube" extrude.
    This method sweeps a profile curve down a path curve while the
    profile curve rotates so that it maintains a relationship with the
    path curve.
    Args:
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        degreeAlongLength (Queryable[int]?): Surface degree along the distance when a distance extrude is performed  
                Default: 1  
                Properties: create, query, edit
        direction (Queryable[Tuple[float, float, float]]?): The direction in which to extrude.  
                Use only for distance extrudeType and useProfileNormal off  
                Properties: create, query, edit
        directionX (Queryable[float]?): X of the direction  
                Default: 0  
                Properties: create, query, edit
        directionY (Queryable[float]?): Y of the direction  
                Default: 1  
                Properties: create, query, edit
        directionZ (Queryable[float]?): Z of the direction  
                Default: 0  
                Properties: create, query, edit
        extrudeType (Queryable[int]?): The extrude type (distance-0, flat-1, or tube-2)  
                Default: 2  
                Properties: create, query, edit
        fixedPath (bool?): If true, the resulting surface will be placed at the path curve.  
                Otherwise, the resulting surface will be placed at the profile curve.  
                Default: false  
                Properties: create, query, edit
        length (Queryable[float]?): The distance to extrude.  
                Use only for distance extrudeType  
                Default: 1  
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
        pivot (Queryable[Tuple[float, float, float]]?): The pivot point used for tube extrudeType  
                Properties: create, query, edit
        reverseSurfaceIfPathReversed (bool?): If true, extrude type is tube (2) and path has been internally reversed then computed surface is reversed in the direction corresponding to the path.  
                Default: false  
                Properties: create, query, edit
        rotation (Queryable[float]?): Amount to rotate the profile curve as it sweeps along the path curve.  
                Default: 0.0  
                Properties: create, query, edit
        scale (Queryable[float]?): Amount to scale the profile curve as it sweeps along the path curve.  
                Default: 1.0  
                Properties: create, query, edit
        subCurveSubSurface (bool?): If true, curve range on the path will get applied to the resulting surface instead of cut before the extrude.  
                Default: false  
                Properties: create, query, edit
        useComponentPivot (Queryable[int]?): Use closest endpoint of the path - 0, component pivot - 1 or the center of the bounding box of the profile - 2  
                Default: 0  
                Properties: create, query, edit
        useProfileNormal (bool?): If true, use the profile curve normal for the direction in which to extrude.  
                Use only for distance or tube extrudeType.  
                Default: false  
                Properties: create, query, edit
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        mergeItems (bool?): Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1. 2].  
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
        range (bool?): Force a curve range on complete input curve.  
                Properties: create
        rebuild (bool?): Rebuild the input curve(s) before using them in the operation.  Use nurbsCurveRebuildPref to set the parameters for the conversion.  
                Properties: create

    Returns:
        List[str]: Object name and node name

    Example:
    """

