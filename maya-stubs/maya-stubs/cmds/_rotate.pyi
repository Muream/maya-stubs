from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rotate(arg0: float = ..., arg1: float = ..., arg2: float = ..., /, *args: str, absolute: bool = ..., centerPivot: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., euler: bool = ..., forceOrderXYZ: bool = ..., objectCenterPivot: bool = ..., objectSpace: bool = ..., orientAxes: Tuple[float, float, float] = ..., pivot: Tuple[float, float, float] = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotateX: bool = ..., rotateXY: bool = ..., rotateXYZ: bool = ..., rotateXZ: bool = ..., rotateY: bool = ..., rotateYZ: bool = ..., rotateZ: bool = ..., symNegative: bool = ..., translate: bool = ..., worldSpace: bool = ..., xformConstraint: str = ...) -> bool:
    """The rotate command is used to change the rotation of
    geometric objects. The rotation values are specified as
    Euler angles (rx, ry, rz). The values are interpreted based
    on the current working unit for Angular measurements. Most
    often this is degrees.The default behaviour, when no objects or flags are passed,
    is to do a absolute rotate on each currently selected object
    in the world space.
    Args:
        absolute (bool?): Perform an absolute operation.  
                Properties: create
        centerPivot (bool?): Let the pivot be the center of the bounding box of all objects  
                Properties: create
        componentSpace (bool?): Rotate in local component space  
                Properties: create
        constrainAlongNormal (bool?): When true, transform constraints are applied along the vertex normal first  
                and only use the closest point when no intersection is found along the normal.  
                Properties: create
        deletePriorHistory (bool?): If true then delete the history prior to the current operation.  
                Properties: create
        euler (bool?): Modifer for -relative flag that specifies rotation  
                values should be added to current XYZ rotation values.  
                Properties: create
        forceOrderXYZ (bool?): When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.  
                Properties: create
        objectCenterPivot (bool?): Let the pivot be the center of the bounding box of each object  
                Properties: create
        objectSpace (bool?): Perform rotation about object-space axis.  
                Properties: create
        orientAxes (Tuple[float, float, float]?): Euler axis for orientation.  
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
        preserveUV (bool?): When true, UV values on rotated components are projected across the rotation  
                in 3d space. For small edits, this will freeze the world space texture mapping  
                on the object.  
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
        rotateX (bool?): Rotate in X direction  
                Properties: create
        rotateXY (bool?): Rotate in X and Y direction  
                Properties: create
        rotateXYZ (bool?): Rotate in all directions (default)  
                Properties: create
        rotateXZ (bool?): Rotate in X and Z direction  
                Properties: create
        rotateY (bool?): Rotate in Y direction  
                Properties: create
        rotateYZ (bool?): Rotate in Y and Z direction  
                Properties: create
        rotateZ (bool?): Rotate in Z direction  
                Properties: create
        symNegative (bool?): When set the component transformation is flipped so it is relative to the  
                negative side of the symmetry plane. The default (no flag) is to transform  
                components relative to the positive side of the symmetry plane.  
                Properties: create
        translate (bool?): When true, the command will modify the node's translate attribute instead of its  
                rotateTranslate attribute, when rotating around a pivot other than the object's  
                own rotate pivot.  
                Properties: create
        worldSpace (bool?): Perform rotation about global world-space axis.  
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

