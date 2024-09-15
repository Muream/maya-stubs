from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyOptions(*args: Any, query: bool = ..., activeObjects: bool = ..., allEdges: bool = ..., backCullVertex: bool = ..., backCulling: bool = ..., colorMaterialChannel: Queryable[str] = ..., colorShadedDisplay: bool = ..., displayAlphaAsGreyScale: bool = ..., displayBlueChannel: bool = ..., displayBorder: bool = ..., displayCenter: bool = ..., displayColorAsGreyScale: bool = ..., displayCreaseEdge: bool = ..., displayCreaseVertex: bool = ..., displayGeometry: bool = ..., displayGreenChannel: bool = ..., displayInvisibleFaces: bool = ..., displayItemNumbers: Queryable[Tuple[bool, bool, bool, bool]] = ..., displayMapBorder: bool = ..., displayMetadata: Queryable[Tuple[bool, bool, bool]] = ..., displayNormal: bool = ..., displayRedChannel: bool = ..., displaySubdComps: bool = ..., displayTangent: bool = ..., displayTriangle: bool = ..., displayUVTopology: bool = ..., displayUVs: bool = ..., displayVertex: bool = ..., displayWarp: bool = ..., facet: bool = ..., fullBack: bool = ..., gl: bool = ..., hardBack: bool = ..., hardEdge: bool = ..., hardEdgeColor: bool = ..., materialBlend: Queryable[str] = ..., newPolymesh: bool = ..., point: bool = ..., pointFacet: bool = ..., relative: bool = ..., reuseTriangles: bool = ..., sizeBorder: Queryable[float] = ..., sizeNormal: Queryable[float] = ..., sizeUV: Queryable[float] = ..., sizeVertex: Queryable[float] = ..., smoothDrawType: Queryable[int] = ..., softEdge: bool = ..., vertexNormalMethod: Queryable[int] = ..., wireBackCulling: bool = ...) -> Union[bool, str, Tuple[bool, bool, bool, bool], Tuple[bool, bool, bool], float, int]:
    """Changes the global display polygonal attributes.
    Args:
        activeObjects (bool?): Apply user choices for all active objects.  
                Properties: create, query
        allEdges (bool?): Display all edges in solid line.  
                Properties: create, query
        backCullVertex (bool?): BackCull vertices.  
                Properties: create, query
        backCulling (bool?): Display with no back culling.  
                Properties: create, query
        colorMaterialChannel (Queryable[str]?): If colorShadedDisplay is true, then determines which  
                material channel to display color per vertex in.  
                The options are:  
              
                "none" : disable material shading  
                "ambient" : ambient material channel  
                "ambientDiffuse" :  ambient and diffuse material channel  
                "diffuse" :  diffuse material channel  
                "specular" :  specular material channel  
                "emission" :  emission material channel  
                Properties: create, query
        colorShadedDisplay (bool?): Use color per vertex display in shaded mode.  
                Properties: create, query
        displayAlphaAsGreyScale (bool?): Display alpha as greyscale.  
                Properties: create, query
        displayBlueChannel (bool?): Display Blue channel.  
                Properties: create, query
        displayBorder (bool?): Highlight border edge.  
                Properties: create, query
        displayCenter (bool?): Display facet centers.  
                Properties: create, query
        displayColorAsGreyScale (bool?): Display color channels as greyscale.  
                Properties: create, query
        displayCreaseEdge (bool?): Highlight creased edges  
                Properties: create, query
        displayCreaseVertex (bool?): Highlight creased vertices  
                Properties: create, query
        displayGeometry (bool?): Display geometry.  
                Properties: create, query
        displayGreenChannel (bool?): Display Green channel.  
                Properties: create, query
        displayInvisibleFaces (bool?): Highlight invisible faces  
                Properties: create, query
        displayItemNumbers (Queryable[Tuple[bool, bool, bool, bool]]?): Displays item numbers (vertices edges facets uvs)  
                Properties: create, query
        displayMapBorder (bool?): Highlight map border edge.  
                Properties: create, query
        displayMetadata (Queryable[Tuple[bool, bool, bool]]?): Displays component metadata (vertices edges facets vertexFaces)  
                Properties: create, query
        displayNormal (bool?): Display normals.  
                Properties: create, query
        displayRedChannel (bool?): Display Red channel.  
                Properties: create, query
        displaySubdComps (bool?): Display subdivided components when in Smooth Mesh Preview mode.  
                Properties: create, query
        displayTangent (bool?): Display tangent.  
                Properties: create, query
        displayTriangle (bool?): Display triangulation.  
                Properties: create, query
        displayUVTopology (bool?): Option on UV display to display UVs topologically.  
                Properties: create, query
        displayUVs (bool?): Display UVs.  
                Properties: create, query
        displayVertex (bool?): Display vertices.  
                Properties: create, query
        displayWarp (bool?): Highlight warped facets.  
                Properties: create, query
        facet (bool?): For use with -dn flag. Set the normal display style to facet display.  
                Properties: create, query
        fullBack (bool?): Display with full back culling.  
                Properties: create, query
        gl (bool?): Apply user choices for all objects.  
                Properties: create, query
        hardBack (bool?): Backculled hard edges only for backculled faces.  
                Properties: create, query
        hardEdge (bool?): Display only hard edges.  
                Properties: create, query
        hardEdgeColor (bool?): Display hard edges as separate color.  
                Properties: create, query
        materialBlend (Queryable[str]?): The options are:  
                "overwrite"  
                "add"  
                "subtract"  
                "multiply"  
                "divide"  
                "average"  
                "modulate2x"  
                Properties: create, query
        newPolymesh (bool?): Set component display state of new polymesh objects.  
                Properties: create, query
        point (bool?): For use with -dn flag. Set the normal display style to vertex display.  
                Properties: create, query
        pointFacet (bool?): For use with -dn flag. Set the normal display style to vertex and face display.  
                Properties: create, query
        relative (bool?): When this flag is used with flags dealing with size,  
                the value (size) is a multiplication factor :  
                i.e for flags : -sizeNormal, -sizeBorder.  
                When this flag is used with flags dealing with a boolean value,  
                the boolean value is toggled :  
                i.e for flags : displayVertex, displayCenter, displayTriangle,  
                displayBorder, backCullVertex, displayWarp, displayItemNumbers.  
                Properties: create, query
        reuseTriangles (bool?): Avoid regenerating triangles, by reusing the old triangles upstream  
                in the construction history.  The construction history is searched  
                upstream and downstream for other mesh nodes, and the given boolean  
                value is set on those mesh nodes.  Note, that this command does not  
                set the value on the given mesh node.  That has to be done using  
                the setAttr command.  
                This option would affect only the interactive 3d viewport.  
                The batch-rendering would use the properly computed triangles.  
                This is useful only for interactive performance such as skinning  
                playback, when the display mode is shaded (or wireframe with  
                triangles displayed)  Using this option for wireframe display mode  
                is not recomended.  
                Properties: create, query
        sizeBorder (Queryable[float]?): Set the size of the polygonal border edges.  
                Properties: create, query
        sizeNormal (Queryable[float]?): Set the size of the polygonal normals.  
                Properties: create, query
        sizeUV (Queryable[float]?): Set the size of the polygonal UV.  
                Properties: create, query
        sizeVertex (Queryable[float]?): Set the size of the polygonal vertex.  
                Properties: create, query
        smoothDrawType (Queryable[int]?): This setting only works with the newPolymesh flag.  
                Sets a new default attribute value for the smoothDrawType attribute on a polymesh object.  
                Options are:  
                0. Catmull-Clark  
                1. Linear  
                2. OpenSubdiv Catmull-Clark Uniform  
                3. OpenSubdiv Catmull-Clark Adaptive  
                Properties: create, query
        softEdge (bool?): Display soft edges in dotted lines.  
                Properties: create, query
        vertexNormalMethod (Queryable[int]?): This setting only works with the newPolymesh flag.  
                Sets a new default attribute value for the vertexNormalMethod attribute on a polymesh object.  
                Options are:  
                0. Unweighted  
                1. Angle Weighted  
                2. Area Weighted  
                3. Angle And Area Weighted  
                Properties: create, query
        wireBackCulling (bool?): Backculled faces are in wireframe.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

