from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySelectConstraint(*, query: bool = ..., angle: Queryable[int] = ..., anglePropagation: bool = ..., angleTolerance: Queryable[float] = ..., anglebound: Queryable[Tuple[float, float]] = ..., border: bool = ..., borderPropagation: bool = ..., convexity: Queryable[int] = ..., crease: bool = ..., disable: bool = ..., dist: Queryable[int] = ..., distaxis: Queryable[Tuple[float, float, float]] = ..., distbound: Queryable[Tuple[float, float]] = ..., distpoint: Queryable[Tuple[float, float, float]] = ..., edgeDistance: int = ..., geometricarea: Queryable[int] = ..., geometricareabound: Queryable[Tuple[float, float]] = ..., holes: Queryable[int] = ..., length: Queryable[int] = ..., lengthbound: Queryable[Tuple[float, float]] = ..., loopPropagation: bool = ..., max2dAngle: float = ..., max3dAngle: float = ..., mode: Queryable[int] = ..., nonmanifold: Queryable[int] = ..., oppositeEdges: bool = ..., order: Queryable[int] = ..., orderbound: Queryable[Tuple[int, int]] = ..., orient: Queryable[int] = ..., orientaxis: Queryable[Tuple[float, float, float]] = ..., orientbound: Queryable[Tuple[float, float]] = ..., planarity: Queryable[int] = ..., propagate: Queryable[int] = ..., random: Queryable[int] = ..., randomratio: Queryable[float] = ..., returnSelection: bool = ..., ringPropagation: bool = ..., shell: bool = ..., size: Queryable[int] = ..., smoothness: Queryable[int] = ..., stateString: bool = ..., textured: Queryable[int] = ..., texturedarea: Queryable[int] = ..., texturedareabound: Queryable[Tuple[float, float]] = ..., textureshared: Queryable[int] = ..., topology: Queryable[int] = ..., type: Queryable[int] = ..., uvBorderSelection: bool = ..., uvConstraint: bool = ..., uvEdgeLoopPropagation: bool = ..., uvEdgeRingPropagation: bool = ..., uvFaceOrientation: Queryable[int] = ..., uvShell: bool = ..., visibility: Queryable[int] = ..., visibilityangle: Queryable[float] = ..., visibilitypoint: Queryable[Tuple[float, float, float]] = ..., where: Queryable[int] = ..., wholeSensitive: bool = ...) -> Union[bool, int, float, Tuple[float, float], Tuple[float, float, float], Tuple[int, int]]:
    """Changes the global polygonal selection constraints.
    Args:
        angle (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        anglePropagation (bool?): If true, selection will be extended to all connected components whose normal  
                is close to any of the normals of the original selection (see angleTolerance)  
                Properties: create, query
        angleTolerance (Queryable[float]?): When angle propagation is turned on, this controls what is the maximum  
                difference of the normal vectors where the selection propagates.  
                Properties: create, query
        anglebound (Queryable[Tuple[float, float]]?): min and max angles.  The given value should be in the current units that  
                Maya is using.  See the examples for how to check the current unit.  
                For vertices :    angle between the 2 edges owning the vertex.  
                For edges :        angle between the 2 faces owning the edge.  
                Properties: create, query
        border (bool?): Use "-uvConstraint true" to edit/query UV view constraint.  
                If true, selection will be extended to all connected border components  
                so that the whole "loop" is selected. It also removes all nonborder components  
                from the existing selection (compatibility mode)  
                Properties: create, query
        borderPropagation (bool?): If true, selection will be extended to all connected border components  
                so that the whole "loop" is selected.  
                Properties: create, query
        convexity (Queryable[int]?): 0(off) 1(concave) 2(convex).  
                Properties: create, query
        crease (bool?): If true, selection will be extended to all connected creased components.  
                Properties: create, query
        disable (bool?): Toggles off all constraints for all component types, but  
                leaves the other constraint parameters.   
                This flag may be used together with other ones toggling some  
                constraints on : if so, all constraints are  
                disabled first (no matter the position of the -disable flag in  
                the command line) then the specified ones are activated.  
                Properties: create
        dist (Queryable[int]?): 0(off) 1(to point) 2(to axis) 3(to plane).  
                Properties: create, query
        distaxis (Queryable[Tuple[float, float, float]]?): axis. (Normal to the plane in case of distance to plane).  
                Properties: create, query
        distbound (Queryable[Tuple[float, float]]?): min and max distances.  
                Properties: create, query
        distpoint (Queryable[Tuple[float, float, float]]?): point. (Axis/plane origin in case of distance to axis/plane).  
                Properties: create, query
        edgeDistance (int?): Maximum distance (number of edges) to extend the edge selection for "Contiguous Edges" propagate mode. 0 means to ignore the distance constraint.  
                Properties: create
        geometricarea (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        geometricareabound (Queryable[Tuple[float, float]]?): min and max areas.  
                Properties: create, query
        holes (Queryable[int]?): 0(off) 1(holed) 2(non holed).  
                Properties: create, query
        length (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        lengthbound (Queryable[Tuple[float, float]]?): min and max lengths.  
                Properties: create, query
        loopPropagation (bool?): If true, edge selection will be extended to a loop.  
                Properties: create, query
        max2dAngle (float?): Maximum angle between two consecutive edges in the 2d tangent plane for "Contiguous Edges" propagate mode.  
                Properties: create
        max3dAngle (float?): Maximum angle between two consecutive edges in 3d space for "Contiguous Edges" propagate mode.  
                Properties: create
        mode (Queryable[int]?): 0(Off) 1(Next) 2(Current and Next) 3(All and Next).  
                Off :             no constraints are used at all.  
                Next :             constraints will be used to filter next selections.  
                Current and Next :    constraints will be aplied on current selection  
                and then used to filter next selections.  
                All and Next :        all items satisfying constraints are selected.  
                Properties: create, query
        nonmanifold (Queryable[int]?): 0(off) 1(on)  
                Properties: create, query
        oppositeEdges (bool?): Use the opposite edges  
                Properties: create
        order (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        orderbound (Queryable[Tuple[int, int]]?): min and max orders.  
                number of owning edges.  
                Properties: create, query
        orient (Queryable[int]?): 0(off) 1(orientation) 2(direction).  
                Properties: create, query
        orientaxis (Queryable[Tuple[float, float, float]]?): axis.  
                Properties: create, query
        orientbound (Queryable[Tuple[float, float]]?): min and max angles.  The given value should be in the current units that  
                Maya is using.  See the examples for how to check the current unit.  
                Properties: create, query
        planarity (Queryable[int]?): 0(off) 1(non planar) 2(planar).  
                Properties: create, query
        propagate (Queryable[int]?): 0(Off) 1(More) 2(Less) 3(Border) 4(Contiguous Edges) 5(Grow Along Loop) 6(Shrink Along Loop).  
                More :        will add current selection border to current selection.  
                Less :        will remove current selection border from current selection.  
                Border :    will keep only current selection border.  
                Contiguous Edges :    Add edges aligned with the current  
                edges selected. The direction and number of edges selected is  
                controlled by the -m2a, -m3a, and -ed flags.  
                Grow Along Loop:    Will grow current selection along loop, support face, edge, vertex and UV.  
                Shrink Along Loop:    Will shrink current selection along loop, support face, edge, vertex and UV.  
                Properties: create, query
        random (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        randomratio (Queryable[float]?): ratio [0,1].  
                Properties: create, query
        returnSelection (bool?): If true, current selection will not be modified, instead the new selection will be returned as result.  
                Properties: create
        ringPropagation (bool?): If true, edge selection will be extended to a ring.  
                Properties: create, query
        shell (bool?): If true, selection will be extended to all connected components  
                so that the whole piece of object is selected.  
                Properties: create, query
        size (Queryable[int]?): 0(off) 1(triangles) 2(quads) 3(nsided).  
                Properties: create, query
        smoothness (Queryable[int]?): 0(off) 1(hard) 2(smooth).  
                Properties: create, query
        stateString (bool?): Query only flag. Returns the MEL command that would restore all  
                the current settings.  
                Properties: query
        textured (Queryable[int]?): 0(off) 1(mapped) 2(unmapped).  
                Properties: create, query
        texturedarea (Queryable[int]?): 0(off) 1(Area specified is unsigned) 2(Area specified is signed).  
                Properties: create, query
        texturedareabound (Queryable[Tuple[float, float]]?): min and max areas.  
                Properties: create, query
        textureshared (Queryable[int]?): 0(off) 1(on).  
                This option will select any UVs on the currentMap which are shared  
                by more than one vertex  
                Properties: create, query
        topology (Queryable[int]?): 0(off) 1(non triangulatable) 2(lamina) 3(non triangulatable and lamina)  
                Properties: create, query
        type (Queryable[int]?): 0x0000(none)  
                0x0001(vertex)  
                0x8000(edge)  
                0x0008(face)  
                0x0010(texture coordinates)  
                Properties: create, query
        uvBorderSelection (bool?): This flag only works on UV view  
                If true, selection will be extended to all UV border components  
                It also removes all components not on UV border from the existing selection  
                Properties: create, query
        uvConstraint (bool?): If true, applicable constraint flags will work on UV view.  
                      In query mode, this flag can accept a value.  
                Properties: create
        uvEdgeLoopPropagation (bool?): Use "-uvConstraint true" to edit/query UV view constraint.  
                If true, UV edge selection will be extended to a loop.  
                Properties: create, query
        uvEdgeRingPropagation (bool?): This flag only works on UV view  
                If true, UV edge selection will be extended to a ring.  
                Properties: create, query
        uvFaceOrientation (Queryable[int]?): This flag only works on UV view  
                0(Off) 1(Front Face) 2(Back Face).  
                Properties: create, query
        uvShell (bool?): If true, selection will be extended to all connected components in UV space  
                Properties: create, query
        visibility (Queryable[int]?): 0(off) 1(on).  
                Properties: create, query
        visibilityangle (Queryable[float]?): angle [0,360].  
                Properties: create, query
        visibilitypoint (Queryable[Tuple[float, float, float]]?): point.  
                Properties: create, query
        where (Queryable[int]?): 0(off) 1(on border) 2(inside).  
                Properties: create, query
        wholeSensitive (bool?): Tells how to select faces : either  
                 by picking anywhere inside the face (if true)  
                 or by picking on the face center marker (if false).  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

