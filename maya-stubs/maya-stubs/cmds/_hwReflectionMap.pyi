from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hwReflectionMap(*args: str, edit: bool = ..., query: bool = ..., backTextureName: Queryable[str] = ..., bottomTextureName: Queryable[str] = ..., cubeMap: bool = ..., decalMode: bool = ..., enable: bool = ..., frontTextureName: Queryable[str] = ..., leftTextureName: Queryable[str] = ..., rightTextureName: Queryable[str] = ..., sphereMapTextureName: Queryable[str] = ..., topTextureName: Queryable[str] = ...) -> Union[str, bool]:
    """This command creates a hwReflectionMap node for having reflection on
    textured surfaces that currently have their boolean attribute
    displayHWEnvironment set to true.
    Args:
        backTextureName (Queryable[str]?): This flag specifies the file texture name for the back side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        bottomTextureName (Queryable[str]?): This flag specifies the file texture name for the bottom side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        cubeMap (bool?): If on, the reflection of the textures is done using the cube mapping.  
                Default is false. The reflection is done using sphere mapping.  
                When queried, this flag returns a boolean.  
                Properties: query
        decalMode (bool?): If on, the reflection color replaces the surface shading.  
                Default is false. The reflection is multiplied to the surface shading.  
                When queried, this flag returns a boolean.  
                Properties: query
        enable (bool?): If on, enable the corresponding hwReflectionMap node.  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        frontTextureName (Queryable[str]?): This flag specifies the file texture name for the front side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        leftTextureName (Queryable[str]?): This flag specifies the file texture name for the left side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        rightTextureName (Queryable[str]?): This flag specifies the file texture name for the right side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        sphereMapTextureName (Queryable[str]?): This flag specifies the file texture name for the sphere mapping option.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query
        topTextureName (Queryable[str]?): This flag specifies the file texture name for the top side of the cube.  
                Default is none  
                When queried, this flag returns a string.  
                Properties: query

    Returns:
        str: (name of the created hwReflectionMap node)

    Example:
    """

