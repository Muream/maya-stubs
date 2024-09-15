from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def performanceOptions(*, query: bool = ..., clusterResolution: Queryable[float] = ..., disableStitch: Queryable[str] = ..., disableTrimBoundaryDisplay: Queryable[str] = ..., disableTrimDisplay: Queryable[str] = ..., latticeResolution: Queryable[float] = ..., passThroughBindSkinAndFlexors: Queryable[str] = ..., passThroughBlendShape: Queryable[str] = ..., passThroughCluster: Queryable[str] = ..., passThroughDeltaMush: Queryable[str] = ..., passThroughFlexors: Queryable[str] = ..., passThroughLattice: Queryable[str] = ..., passThroughMeshBoolean: Queryable[str] = ..., passThroughPaintEffects: Queryable[str] = ..., passThroughSculpt: Queryable[str] = ..., passThroughWire: Queryable[str] = ..., regionOfEffect: Queryable[str] = ..., skipHierarchyTraversal: bool = ..., useClusterResolution: Queryable[str] = ..., useLatticeResolution: Queryable[str] = ...) -> Union[str, float, bool]:
    """Sets the global performance options for the application.  The options allow
    the disabling of features such as stitch surfaces or deformers to
    cut down on computation time in the scene.Performance options that are in effect may be on all the time, or they can be
    turned on only for interaction.  In the latter case, the options will only
    take effect during UI interaction or playback.Note that none of these performance options will affect rendering.
    Args:
        clusterResolution (Queryable[float]?): Sets the global cluster resolution.  This value may range between  
                0.0 (exact calculation) and 10.0 (rough approximation)  
                Properties: query
        disableStitch (Queryable[str]?): Sets the state of stitch surface disablement.  Setting this  
                to "on" suppresses the generation of stitch surfaces.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        disableTrimBoundaryDisplay (Queryable[str]?): Sets the state of trim boundary drawing disablement.  Setting this  
                to "on" suppresses the drawing of surface trim boundaries.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        disableTrimDisplay (Queryable[str]?): Sets the state of trim drawing disablement.  Setting this  
                to "on" suppresses the drawing of surface trims.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        latticeResolution (Queryable[float]?): Sets the global lattice resolution.  This value may range between  
                0.0 (exact calculation) and 1.0 (rough approximation)  
                Properties: query
        passThroughBindSkinAndFlexors (Queryable[str]?): Sets the state of bind skin and all flexors pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughBlendShape (Queryable[str]?): Sets the state of blend shape deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughCluster (Queryable[str]?): Sets the state of cluster deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughDeltaMush (Queryable[str]?): Sets the state of delta mush deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughFlexors (Queryable[str]?): Sets the state of flexor pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughLattice (Queryable[str]?): Sets the state of lattice deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughMeshBoolean (Queryable[str]?): Sets the state of mesh booleans pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughPaintEffects (Queryable[str]?): Sets the state of paint effects pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughSculpt (Queryable[str]?): Sets the state of sculpt deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        passThroughWire (Queryable[str]?): Sets the state of wire deformer pass through.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        regionOfEffect (Queryable[str]?): When enabled, an interactive update of translation commands will attempt to  
                determine which components are being changed and only update effected components  
                as a performance optimization while dragging a manip.  
                Properties: query
        skipHierarchyTraversal (bool?): When enabled, hierarchy traversal of invisible objects in the scene will be  
                disabled in order to increase performance however this has a side effect of  
                performing redundant viewport refreshes on certain actions such as manipulations,  
                start/end of playback, idle refresh calls, etc.  
                Properties: query
        useClusterResolution (Queryable[str]?): Sets the state of cluster deformer global resolution.  This  
                allows clusters to be calculated at a lower resolution.  
                Valid values are "on", "off", "interactive".  
                Properties: query
        useLatticeResolution (Queryable[str]?): Sets the state of lattice deformer global resolution.  This  
                allows lattices to be calculated at a lower resolution.  
                Valid values are "on", "off", "interactive".  
                Properties: query

    Returns:
        str: One of "on", "off", or "interactive" giving the state of the option
        float: Global resolution value

    Example:
    """

