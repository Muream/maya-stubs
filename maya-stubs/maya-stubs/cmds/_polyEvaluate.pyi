from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyEvaluate(*args: str, accurateEvaluation: bool = ..., activeShells: bool = ..., activeUVShells: bool = ..., area: bool = ..., boundingBox: bool = ..., boundingBox2d: bool = ..., boundingBoxComponent: bool = ..., boundingBoxComponent2d: bool = ..., displayStats: bool = ..., edge: bool = ..., edgeComponent: bool = ..., face: bool = ..., faceArea: bool = ..., faceComponent: bool = ..., format: bool = ..., shell: bool = ..., triangle: bool = ..., triangleComponent: bool = ..., uvArea: bool = ..., uvComponent: bool = ..., uvEdgePairs: bool = ..., uvFaceArea: bool = ..., uvSetName: str = ..., uvShell: bool = ..., uvShellIds: bool = ..., uvcoord: bool = ..., uvsInShell: int = ..., vertex: bool = ..., vertexComponent: bool = ..., worldArea: bool = ..., worldFaceArea: bool = ...) -> Any:
    """Returns the required counts on the specified objects.If no objects are specified in the command line, then the
    objects from the active list are used.In MEL, the values are returned in the same order as the flags are set.
    Under Python, there is no concept of argument ordering, so the items are
    returned in a dictionary keyed by the name of the flag.  In Python, if only
    one item is requested, then it will not be returned in a dictionary.For user convenience, if no flag is set, then all values are echoed.All flags (except -fmt/format) are in fact query-flags. For
    user convenience, the -q flag may be ommitted.Some comments for non-formatted output :
    Args:
        accurateEvaluation (bool?): used to get accurate results for the bounding box computation  
                For objects with large vertex counts, accurate evaluation takes more time  
                Properties: create
        activeShells (bool?): returns the indices of active shells as an array of int  
                Properties: create
        activeUVShells (bool?): returns the indices of active UV shells (for the current map if one  
                is not specified) as an array of int  
                Properties: create
        area (bool?): returns the surface area of the object's faces in local space as a float  
                Properties: create
        boundingBox (bool?): returns the object's bounding box in 3d space  
                as 6 floats in MEL: xmin xmax ymin ymax zmin zmax, or as  
                a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))  
                Properties: create
        boundingBox2d (bool?): returns the object's uv bounding box (for the current map if one is not specified) in 2d space  
                as 4 floats in MEL : xmin xmax ymin ymax, or as  
                a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))  
                Properties: create
        boundingBoxComponent (bool?): returns the bounding box of selected components in 3d space  
                as 6 floats in MEL : xmin xmax ymin ymax zmin zmax, or as  
                a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))  
                Properties: create
        boundingBoxComponent2d (bool?): returns the bounding box of selected/specified components uv coordinates in 2d space  
                as 4 floats in MEL : xmin xmax ymin ymax, or as  
                a tuple of two pairs in Python: ((xmin,xmax), (ymin,ymax))  
                Properties: create
        displayStats (bool?): toggles the display of poly statistics for the active View.  
                All other flags are ignored if this flag is specified (Obsolete  
                - refer to the headsUpDisplay command)  
                Properties: create
        edge (bool?): returns the number of edges as an int  
                Properties: create
        edgeComponent (bool?): returns the object's number of selected edges as an int  
                Properties: create
        face (bool?): returns the number of faces as an int  
                Properties: create
        faceArea (bool?): returns the surface area of selected/specified faces in local space as an array of float  
                Properties: create
        faceComponent (bool?): returns the object's number of selected faces as an int  
                Properties: create
        format (bool?): used to display the results as an explicit sentence  
                Properties: create
        shell (bool?): returns the number of shells (disconnected pieces) as an int  
                Properties: create
        triangle (bool?): returns the number of triangles as an int  
                Properties: create
        triangleComponent (bool?): returns the number of triangles of selected components as an int  
                Properties: create
        uvArea (bool?): returns the UV area of the object's faces in 2d space as a float  
                Properties: create
        uvComponent (bool?): returns the object's number of selected uv coordinates as an int  
                Properties: create
        uvEdgePairs (bool?): returns the pairs of UVs that are on the selected/specified edges  
                Properties: create
        uvFaceArea (bool?): returns the UV area of selected/specified faces in 2d space as an array of float  
                Properties: create
        uvSetName (str?): used when querying texture vertices to specify the uv set.  If a uv set  
                is not specified then the current map for the object will be used  
                Properties: create
        uvShell (bool?): returns the number of UV shells (for the current map if one is not  
                specified) as an int  
                Properties: create
        uvShellIds (bool?): returns the UV shell indices for selected/specified faces or UVs as an array of int  
                (for the current map if one is not specified), one shell index per each face/UV.  
                Properties: create
        uvcoord (bool?): returns the number of uv coordinates (for the current map if one is  
                not specified) as an int  
                Properties: create
        uvsInShell (int?): returns all UVs inside specified shell(for the current map if one is not specified), use activeUVShells  
                to get shell indices for current selection, use uvShellIds to get shell indices for specified faces or UVs  
                Properties: create
        vertex (bool?): returns the number of vertices as an int  
                Properties: create
        vertexComponent (bool?): returns the object's number of selected vertices as an int  
                Properties: create
        worldArea (bool?): returns the surface area of the object's faces in world space as a float  
                Properties: create
        worldFaceArea (bool?): returns the surface area of selected/specified faces in world space as an array of float  
                Properties: create

    Returns:
        Any: a MEL array of values, a Python dictionary, or a string, depending on
            the format requested and the language called from.

    Example:
    """

