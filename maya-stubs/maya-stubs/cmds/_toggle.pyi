from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toggle(*args: str, query: bool = ..., above: bool = ..., below: bool = ..., boundary: bool = ..., boundingBox: bool = ..., controlVertex: bool = ..., doNotWrite: bool = ..., editPoint: bool = ..., extent: bool = ..., facet: bool = ..., geometry: bool = ..., gl: bool = ..., highPrecisionNurbs: bool = ..., hull: bool = ..., latticePoint: bool = ..., latticeShape: bool = ..., localAxis: bool = ..., newCurve: bool = ..., newPolymesh: bool = ..., newSurface: bool = ..., normal: bool = ..., origin: bool = ..., point: bool = ..., pointDisplay: bool = ..., pointFacet: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., selectHandle: bool = ..., state: bool = ..., surfaceFace: bool = ..., template: bool = ..., uvCoords: bool = ..., vertex: bool = ...) -> bool:
    """The toggle command is used to toggle the display of various
    object features for objects which have these components. For
    example, CV and edit point display may be toggled for those
    listed     NURB curves or surfaces.Note: This command is not undoable.
    Args:
        above (bool?): Toggle state for all objects above listed objects.  
                Properties: create
        below (bool?): Toggle state for all objects below listed objects.  
                Properties: create
        boundary (bool?): Toggle boundary display of listed mesh objects.  
                Properties: create, query
        boundingBox (bool?): Toggle or query the bounding box display of listed objects.  
                Properties: create, query
        controlVertex (bool?): Toggle CV display of listed curves and surfaces.  
                Properties: create, query
        doNotWrite (bool?): Toggle the "this should be written to the file" state.  
                Properties: create, query
        editPoint (bool?): Toggle edit point display of listed curves and surfaces.  
                Properties: create, query
        extent (bool?): Toggle display of extents of listed mesh objects.  
                Properties: create, query
        facet (bool?): For use with normal flag. Set the normal display style to facet display.  
                Properties: create, query
        geometry (bool?): Toggle geometry display of listed objects.  
                Properties: create, query
        gl (bool?): Toggle state for all objects  
                Properties: create
        highPrecisionNurbs (bool?): Toggle high precision display for Nurbs  
                Properties: create, query
        hull (bool?): Toggle hull display of listed curves and surfaces.  
                Properties: create, query
        latticePoint (bool?): Toggle point display of listed lattices  
                Properties: create, query
        latticeShape (bool?): Toggle display of listed lattices  
                Properties: create, query
        localAxis (bool?): Toggle local axis display of listed objects.  
                Properties: create, query
        newCurve (bool?): Set component display state of new curve objects  
                Properties: create, query
        newPolymesh (bool?): Set component display state of new polymesh objects  
                Properties: create, query
        newSurface (bool?): Set component display state of new surface objects  
                Properties: create, query
        normal (bool?): Toggle display of normals of listed surface and mesh objects.  
                Properties: create, query
        origin (bool?): Toggle origin display of listed surfaces.  
                Properties: create, query
        point (bool?): For use with normal flag. Set the normal display style to vertex display.  
                Properties: create, query
        pointDisplay (bool?): Toggle point display of listed surfaces.  
                Properties: create, query
        pointFacet (bool?): For use with normal flag. Set the normal display style to vertex and face display.  
                Properties: create, query
        rotatePivot (bool?): Toggle rotate pivot display of listed objects.  
                Properties: create, query
        scalePivot (bool?): Toggle scale pivot display of listed objects.  
                Properties: create, query
        selectHandle (bool?): Toggle select handle display of listed objects.  
                Properties: create, query
        state (bool?): Explicitly set the state to true or false instead of toggling the state.  
                Can not be queried.  
                Properties: create
        surfaceFace (bool?): Toggle surface face handle display of listed surfaces.  
                Properties: create, query
        template (bool?): Toggle template state of listed objects  
                Properties: create, query
        uvCoords (bool?): Toggle display uv coords of listed mesh objects.  
                Properties: create, query
        vertex (bool?): Toggle vertex display of listed mesh objects.  
                Properties: create, query

    Returns:
        bool: when in the query mode. none otherwise.

    Example:
    """

