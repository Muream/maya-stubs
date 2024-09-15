from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def revolve(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., autoCorrectNormal: bool = ..., axis: Queryable[Tuple[float, float, float]] = ..., axisChoice: Queryable[int] = ..., axisX: Queryable[float] = ..., axisY: Queryable[float] = ..., axisZ: Queryable[float] = ..., bridge: bool = ..., caching: bool = ..., computePivotAndAxis: Queryable[int] = ..., degree: Queryable[int] = ..., endSweep: Queryable[float] = ..., nodeState: Queryable[int] = ..., pivot: Queryable[Tuple[float, float, float]] = ..., pivotX: Queryable[float] = ..., pivotY: Queryable[float] = ..., pivotZ: Queryable[float] = ..., radius: Queryable[float] = ..., radiusAnchor: Queryable[float] = ..., sections: Queryable[int] = ..., startSweep: Queryable[float] = ..., tolerance: Queryable[float] = ..., useTolerance: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., polygon: int = ..., range: bool = ..., rebuild: bool = ..., useLocalPivot: bool = ...) -> Union[List[str], bool, Tuple[float, float, float], int, float]:
    """This command creates a revolved surface by revolving the given profile
    curve about an axis.  The profile curve can be a curve, curve-on-surface,
    surface isoparm, or trim edge.
    Args:
        autoCorrectNormal (bool?): If this is set to true we will attempt to reverse the direction of the axis in case it is necessary to do so for the surface normals to end up pointing to the outside of the object.  
                Default: false  
                Properties: create, query, edit
        axis (Queryable[Tuple[float, float, float]]?): Revolve axis  
                Properties: create, query, edit
        axisChoice (Queryable[int]?): Only used for computed axis/pivot case.  As we are computing the axis for a planar curve, we have two choices for the major axis based axis.  We will choose the axis corresponding to the longer dimension of the object (0), or explicitly choose one or the other (choices 1 and 2).  
                Default: 0  
                Properties: create, query, edit
        axisX (Queryable[float]?): X of the axis  
                Default: 1  
                Properties: create, query, edit
        axisY (Queryable[float]?): Y of the axis  
                Default: 0  
                Properties: create, query, edit
        axisZ (Queryable[float]?): Z of the axis  
                Default: 0  
                Properties: create, query, edit
        bridge (bool?): If true, we will close a partial revolve to get a pie shaped surface.  The surface will be closed, but not periodic the way it is in the full revolve case.  
                Default: false  
                Properties: create, query, edit
        caching (bool?): Toggle caching for all attributes so that no recomputation is needed  
                Properties: create, query, edit
        computePivotAndAxis (Queryable[int]?): If this is set to 2, we will compute the axis, use the curve position and radius to compute the pivot for the revolve internally.  The value of the pivot and axis attributes are ignored.  If this is set to 1, we will take the supplied axis, but compute the pivot.  If this is set to 0, we will take both the supplied axis and pivot.  
                Default: 0  
                Properties: create, query, edit
        degree (Queryable[int]?): The degree of the resulting surface.  
                Default: 3  
                Properties: create, query, edit
        endSweep (Queryable[float]?): The value for the end sweep angle, in the current units.  This must be no more than the maximum, 360 degrees, or 2 Pi radians.  
                Default: 6.2831853  
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
        pivot (Queryable[Tuple[float, float, float]]?): Revolve pivot point  
                Properties: create, query, edit
        pivotX (Queryable[float]?): X of the pivot  
                Default: 0  
                Properties: create, query, edit
        pivotY (Queryable[float]?): Y of the pivot  
                Default: 0  
                Properties: create, query, edit
        pivotZ (Queryable[float]?): Z of the pivot  
                Default: 0  
                Properties: create, query, edit
        radius (Queryable[float]?): The pivot point will be this distance away from the bounding box of the curve, if computedPivot is set to true.  The value of the pivot attribute is ignored.  
                Default: 1  
                Properties: create, query, edit
        radiusAnchor (Queryable[float]?): The position on the curve for the anchor point so that we can compute the pivot using the radius value.  If in 0. 1 range, its on the curve, normalized parameter range.  If < 0 or > 1, its computed based on the bounding box.  
                Default: -1  
                Properties: create, query, edit
        sections (Queryable[int]?): Number of sections of the resulting surface (if tolerance is not used).  
                Default: 8  
                Properties: create, query, edit
        startSweep (Queryable[float]?): The value for the start sweep angle, in the current units.  This must be no more than the maximum, 360 degrees, or 2 Pi radians.  
                Default: 0  
                Properties: create, query, edit
        tolerance (Queryable[float]?): Tolerance to build to (if useTolerance attribute is set)  
                Default: 0.01  
                Properties: create, query, edit
        useTolerance (bool?): Use the tolerance, or the number of sections to control the sections.  
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
        useLocalPivot (bool?): If true, then the pivot of the profile curve is used  
                as the start point of the axis of revolution.  
                Properties: create, query, edit

    Returns:
        List[str]: Object name and node name

    Example:
    """

