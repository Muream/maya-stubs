from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scale(arg0: float = ..., arg1: float = ..., arg2: float = ..., /, *args: str, absolute: bool = ..., centerPivot: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., distanceOnly: bool = ..., localSpace: bool = ..., objectCenterPivot: bool = ..., objectSpace: bool = ..., orientAxes: Tuple[float, float, float] = ..., pivot: Tuple[float, float, float] = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., scaleX: bool = ..., scaleXY: bool = ..., scaleXYZ: bool = ..., scaleXZ: bool = ..., scaleY: bool = ..., scaleYZ: bool = ..., scaleZ: bool = ..., symNegative: bool = ..., worldSpace: bool = ..., xformConstraint: str = ...) -> bool:
    """The scale command is used to change the sizes of geometric
    objects.The default behaviour, when no objects or flags are passed,
    is to do a relative scale on each currently selected object
    object using each object's existing scale pivot point.
    Args:
        absolute (bool?): Perform an absolute operation.  
                Properties: create
        centerPivot (bool?): Let the pivot be the center of the bounding box of all objects  
                Properties: create
        componentSpace (bool?): Move in local component space  
                Properties: create
        constrainAlongNormal (bool?): When true, transform constraints are applied along the vertex normal first  
                and only use the closest point when no intersection is found along the normal.  
                Properties: create
        deletePriorHistory (bool?): If true then delete the history prior to the current operation.  
                Properties: create
        distanceOnly (bool?): Scale only the distance between the objects.  
                Properties: create
        localSpace (bool?): Use local space for scaling  
                Properties: create
        objectCenterPivot (bool?): Let the pivot be the center of the bounding box of each object  
                Properties: create
        objectSpace (bool?): Use object space for scaling  
                Properties: create
        orientAxes (Tuple[float, float, float]?): Use the angles for the orient axes.  
                Properties: create
        pivot (Tuple[float, float, float]?): Define the pivot point for the transformation  
                Properties: create
        preserveChildPosition (bool?): When true, transforming an object will apply an opposite transform to its  
                child transform to keep them at the same world-space position.  
                Default is false.  
                Properties: create
        preserveGeometryPosition (bool?): When true, transforming an object will apply an opposite transform to its  
                geometry points to keep them at the same world-space position.  
                Default is false.  
                Properties: create
        preserveUV (bool?): When true, UV values on scaled components are projected along the axis of  
                scaling in 3d space. For small edits, this will freeze the world space texture  
                mapping on the object.  
                When false, the UV values will not change for a selected vertices.  
                Default is false.  
                Properties: create
        reflection (bool?): To move the corresponding symmetric components also.  
                Properties: create
        reflectionAboutBBox (bool?): Sets the position of the reflection axis  at the geometry bounding box  
                Properties: create
        reflectionAboutOrigin (bool?): Sets the position of the reflection axis  at the origin  
                Properties: create
        reflectionAboutX (bool?): Specifies the X=0 as reflection plane  
                Properties: create
        reflectionAboutY (bool?): Specifies the Y=0 as reflection plane  
                Properties: create
        reflectionAboutZ (bool?): Specifies the Z=0 as reflection plane  
                Properties: create
        reflectionTolerance (float?): Specifies the tolerance to findout the corresponding reflected components  
                Properties: create
        relative (bool?): Perform a operation relative to the object's current position  
                Properties: create
        scaleX (bool?): Scale in X direction  
                Properties: create
        scaleXY (bool?): Scale in X and Y direction  
                Properties: create
        scaleXYZ (bool?): Scale in all directions (default)  
                Properties: create
        scaleXZ (bool?): Scale in X and Z direction  
                Properties: create
        scaleY (bool?): Scale in Y direction  
                Properties: create
        scaleYZ (bool?): Scale in Y and Z direction  
                Properties: create
        scaleZ (bool?): Scale in Z direction  
                Properties: create
        symNegative (bool?): When set the component transformation is flipped so it is relative to the  
                negative side of the symmetry plane. The default (no flag) is to transform  
                components relative to the positive side of the symmetry plane.  
                Properties: create
        worldSpace (bool?): Use world space for scaling  
                Properties: create
        xformConstraint (str?): Apply a transform constraint to moving components.  
              
                none - no constraint  
                surface - constrain components to the surface  
                edge - constrain components to surface edges  
                live - constraint components to the live surface  
                Properties: create

    Returns:
        bool:

    Example:
    """

