from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyInfo(*args: str, edgeToFace: bool = ..., edgeToVertex: bool = ..., faceNormals: bool = ..., faceToEdge: bool = ..., faceToVertex: bool = ..., invalidEdges: bool = ..., invalidVertices: bool = ..., laminaFaces: bool = ..., nonManifoldEdges: bool = ..., nonManifoldUVEdges: bool = ..., nonManifoldUVs: bool = ..., nonManifoldVertices: bool = ..., vertexToEdge: bool = ..., vertexToFace: bool = ...) -> str:
    """Command queries topological information on polygonal objects and components.
    So, the command will require the following to be specified:
            - selection list to queryquery, polygons, information, topology
    Args:
        edgeToFace (bool?): Returns the faces that share the specified edge. Requires edges to be selected.  
                Properties: create
        edgeToVertex (bool?): Returns the vertices defining an edge. Requires edges to be selected.  
                Properties: create
        faceNormals (bool?): Returns face normals of the specified object. If faces are selected the command  
                returns the face normals of selected faces. Else it returns the face normals  
                of all the faces of the object.  
                Properties: create
        faceToEdge (bool?): Returns the edges defining a face. Requires faces to be selected.  
                Properties: create
        faceToVertex (bool?): Returns the vertices defining a face. Requires faces to be selected.  
                Properties: create
        invalidEdges (bool?): Find all edges that are not associated with any face in the mesh.  
                Properties: create
        invalidVertices (bool?): Find all vertices that are not associated with any face in the mesh.  
                Properties: create
        laminaFaces (bool?): Find all lamina faces in the specified objects.  
                Properties: create
        nonManifoldEdges (bool?): Find all non-manifold edges in the specified objects.  
                Properties: create
        nonManifoldUVEdges (bool?): Find all non-manifold UV edges in the specified objects.  
                Properties: create
        nonManifoldUVs (bool?): Find all non-manifold UVs in the specified objects.  
                Properties: create
        nonManifoldVertices (bool?): Find all non-manifold vertices in the specified objects.  
                Properties: create
        vertexToEdge (bool?): Returns the Edges connected to a vertex. Requires vertices to be selected.  
                Properties: create
        vertexToFace (bool?): Returns the faces that share the specified vertex. Requires vertices to  
                be selected.  
                Properties: create

    Returns:
        str: Components

    Example:
    """

