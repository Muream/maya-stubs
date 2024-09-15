from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def untangleUV(*args: str, mapBorder: str = ..., maxRelaxIterations: int = ..., pinBorder: bool = ..., pinSelected: bool = ..., pinUnselected: bool = ..., relax: str = ..., relaxTolerance: float = ..., shapeDetail: float = ...) -> int:
    """This command will aid in the creation of non-overlapping regions (i.e. polygons)
    in texture space by untangling texture UVs. This is done in two stages:1) Use this command to map the UV border determined by the current selection
    or passed component into a shape that is more suitable for subsequent relaxation.2) Relax all the internal texture UVs by performing a length minimization
    algorithm on all edges in texture space.poly, uv, map, border, relax, untangle
    Args:
        mapBorder (str?): Map the border containing the selected UV into a variety of shapes that may  
                be more amenable to UV relaxation operations. There are various types of  
                mapping available. All the resulting mappings are fit inside the unit square.  
              
                Valid values for the STRING are:  
                circular - a circular mapping with picked UV closest to (0,0)  
                square - map to unit square with picked UV at (0,0)  
                shape - a mapping which attempts to reflect the actual shape of the object  
                        where the picked UV is placed on the line from (0,0) -> (0.5,0.5)  
                shape_circular - shape mapping which will interpolate to a circular mapping  
                                 just enough to prevent self-intersections of the mapped border   
                shape_square - shape mapping which will interpolate to a square mapping just  
                               enough to prevent self-intersections of the mapped border  
                Properties: create
        maxRelaxIterations (int?): The relaxation process is an iterative algorithm. Using this flag  
                will put an upper limit on the number of iterations that will be  
                performed.  
                Properties: create
        pinBorder (bool?): If this is true, then the relevant texture borders are pinned in  
                place during any relaxation  
                Properties: create
        pinSelected (bool?): If this is true, then then any selected UVs are pinned in  
                place during any relaxation  
                Properties: create
        pinUnselected (bool?): If this is true, then all unselected UVs in each mesh are pinned in  
                place during any relaxation  
                Properties: create
        relax (str?): Relax all UVs in the shell of the selected UV's. The relaxation is done by  
                simulating a spring system where each UV edge is treated as a spring.  
                There are a number of different methods characterized by the way the UV  
                edges are weighted in the spring system. These weightings are determined by  
                STRING. Valid values for STRING are:  
                uniform - every edge is weighted the same. This is the fastest method.  
                inverse_length - every edge weight is inversely proportional to it's world space length.  
                inverse_sqrt_length - every edge weight is inversely proportional the the square root of it's world space length.  
                harmonic - this weighting can yield near optimal results in matching the UV's with  
                the geometry, but can also take a long time.  
                Properties: create
        relaxTolerance (float?): This sets the tolerance which is used to determine when the  
                relaxation process can stop. Smaller tolerances yield better  
                results but can take much longer.  
                Properties: create
        shapeDetail (float?): If the mapBorder flag is set to circular or square, then this flag  
                will control how much of the border's corresponding surface shape  
                should be retained in the final mapped border.  
                Properties: create

    Returns:
        int: the number of relaxation iterations carried out

    Example:
    """

