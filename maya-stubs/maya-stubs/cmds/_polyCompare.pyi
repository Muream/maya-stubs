from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCompare(*args: str, colorSetIndices: bool = ..., colorSets: bool = ..., edges: bool = ..., faceDesc: bool = ..., userNormals: bool = ..., uvSetIndices: bool = ..., uvSets: bool = ..., vertices: bool = ...) -> int:
    """Compares two Polygonal Geometry objects with a fine control on what to compare.If no objects are specified in the command line, then the
    objects from the active list are used.Default behaviour is to compare all flags.Use MEL script polyCompareTwoObjects.mel to get formatted output from this command.
    Args:
        colorSetIndices (bool?): Compare poly1, poly2 for matching Color Indices.  
                Properties: create
        colorSets (bool?): Compare poly1, poly2 for matching Color Sets.  
                Properties: create
        edges (bool?): Compare poly1, poly2 for matching Edges.  
                Properties: create
        faceDesc (bool?): Compare poly1, poly2 for matching Face Descriptions. Face descriptions describe the topology of a face, for example number and orientation of edges, number of topology of any holes in the face etc.  
                Properties: create
        userNormals (bool?): Compare poly1, poly2 for matching User Normals.  
                Properties: create
        uvSetIndices (bool?): Compare poly1, poly2 for matching UV Indices.  
                Properties: create
        uvSets (bool?): Compare poly1, poly2 for matching UV Sets.  
                Properties: create
        vertices (bool?): Compare poly1, poly2 for matching Vertices.  
                Properties: create

    Returns:
        int: 0 if successful, non-zero if poly1 and poly2 are not determined to be equal based on requested flags.
            The non-zero value depends on which attributes are different:
            
            Vertices = 1          
            Edges = 2             
            Face Descriptions = 4 
            UV Sets = 8           
            UV Indices = 16       
            Color Sets = 32       
            Color Indices = 64    
            User Normals = 128    
            
            So a return value of 3, for example, indicates both vertices and edges are different.

    Example:
    """

