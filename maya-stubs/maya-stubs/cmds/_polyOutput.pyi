from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyOutput(*args: str, allValues: bool = ..., color: bool = ..., colorDesc: bool = ..., edge: bool = ..., edgeFace: bool = ..., face: bool = ..., faceNorm: bool = ..., force: bool = ..., group: bool = ..., noOutput: bool = ..., normDesc: bool = ..., outputFile: str = ..., triangle: bool = ..., uvDesc: bool = ..., uvValue: bool = ..., vert: bool = ..., vertEdge: bool = ..., vertNorm: bool = ...) -> bool:
    """Dumps a description of internal memory representation of poly objects.
    If no objects are specified in the command line, then the
    objects from the active list are used.
    If information on the geometry in the history of a poly shape is desired,
    then the plug of interest needs to be specified in the command line.
    Default behaviour is to print only a summary. Use the flags
    above to get more details on a specific part of the object.
    Args:
        allValues (bool?): Shortcut for setting all the flags above  
                Properties: create
        color (bool?): Prints the color per vertex. In case of multiple sets,  
                all sets are printed.  
                Properties: create
        colorDesc (bool?): Print the color per vertex description. Each integer  
                is an entry in the color array.  
                Properties: create
        edge (bool?): Print the edge description.  
                Properties: create
        edgeFace (bool?): Prints the edge to face adjascency list. Only  
                available if the information is already computed on  
                the object.  
                Properties: create
        face (bool?): Print the faces description  
                Properties: create
        faceNorm (bool?): Prints the normals per face. Only available if the  
                information is already computed on the object.  
                Properties: create
        force (bool?): Force evaluation of missing pieces before printing.  
                Properties: create
        group (bool?): Print the groups of the object.  
                Properties: create
        noOutput (bool?): Dont output any data.  Would be useful if you want to  
                just evaluate the data, for testing purposes.  
                Properties: create
        normDesc (bool?): Prints the normals per vertex description. Each  
                integer is an entry in the vertNorm array. Only  
                available if the information is already computed on  
                the object.  
                Properties: create
        outputFile (str?): Location of the output file.  
                Properties: create
        triangle (bool?): Prints the triangles per face. Only available if the  
                information is already computed on the object.  
                Properties: create
        uvDesc (bool?): Print the UV description. Each integer is an entry in  
                the uvValue array.  
                Properties: create
        uvValue (bool?): Prints the UV positions. In case of multiple UV sets,  
                all sets are printed.  
                Properties: create
        vert (bool?): Prints the vertex positions.  
                Properties: create
        vertEdge (bool?): Prints the vertex to edge adjascency list. Only  
                available if the information is already computed on  
                the object.  
                Properties: create
        vertNorm (bool?): Prints the normals per vertex. Only available if the  
                information is already computed on the object.  
                Properties: create

    Returns:
        bool:

    Example:
    """

