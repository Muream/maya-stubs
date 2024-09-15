from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def moveVertexAlongDirection(*args: str, direction: Multiuse[Tuple[float, float, float]] = ..., magnitude: Multiuse[float] = ..., normalDirection: Multiuse[float] = ..., uDirection: Multiuse[float] = ..., uvNormalDirection: Multiuse[Tuple[float, float, float]] = ..., vDirection: Multiuse[float] = ...) -> bool:
    """The command moves the selected vertex ( control vertex ) in
    the specified unit direction by the given magnitude. The vertex(ices)
    may also be moved in the direction of unit normal ( -n flag ).
    For NURBS surface vertices the direction of movement could also
    be either in tangent along U or tangent along V.  The flags -n,
    -u, -v and -d are mutually exclusive, ie. the selected vertices
    can be all moved in only -n or -u or -v or -d.
    Args:
        direction (Multiuse[Tuple[float, float, float]]?): move the vertex along the direction as specified. The direction is  
                normalized.  
                Properties: create, multiuse
        magnitude (Multiuse[float]?): move by the specified magnitude in the direction vector.  
                Properties: create, multiuse
        normalDirection (Multiuse[float]?): move components in the direction of normal by the given magnitude at  
                the respective components. The normal is 'normalized'.  
                Properties: create, multiuse
        uDirection (Multiuse[float]?): move components in the direction of tangent along U at the  
                respective components where appropriate. The flag is ignored  
                for polygons, NURBS curves. The u direction is normalized.  
                Properties: create, multiuse
        uvNormalDirection (Multiuse[Tuple[float, float, float]]?): move in the triad space [u,v,n] at the respective components by the  
                specified displacements. The flag is ignored for polygons, NURBS curves.  
                Properties: create, multiuse
        vDirection (Multiuse[float]?): move components in the direction of tangent along V at the  
                respective components where appropriate. The flag is ignored  
                for polygons, NURBS curves.  
                Properties: create, multiuse

    Returns:
        bool:

    Example:
    """

