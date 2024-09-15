from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def move(arg0: float = ..., arg1: float = ..., arg2: float = ..., /, *args: str, absolute: bool = ..., componentOffset: bool = ..., componentSpace: bool = ..., constrainAlongNormal: bool = ..., deletePriorHistory: bool = ..., localSpace: bool = ..., moveX: bool = ..., moveXY: bool = ..., moveXYZ: bool = ..., moveXZ: bool = ..., moveY: bool = ..., moveYZ: bool = ..., moveZ: bool = ..., objectSpace: bool = ..., orientJoint: str = ..., parameter: bool = ..., preserveChildPosition: bool = ..., preserveGeometryPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotatePivotRelative: bool = ..., scalePivotRelative: bool = ..., secondaryAxisOrient: str = ..., symNegative: bool = ..., worldSpace: bool = ..., worldSpaceDistance: bool = ..., xformConstraint: str = ...) -> bool:
    """The move command is used to change the positions of geometric
    objects.The default behaviour, when no objects or flags are passed, is
    to do a absolute move on each currently selected object in the
    world space. The value of the coordinates are interpreted as
    being defined in the current linear unit unless the unit is
    explicitly mentioned.When using -objectSpace there are two ways to use this command.
    If numbers are typed without units then the internal values of
    the object are set to these values. If, on the other hand a
    unit is specified then the internal value is set to the equivalent
    internal value that represents that world-space distance.The -localSpace flag moves the object in its parent space. In this
    space the x,y,z values correspond directly to the tx, ty, tz
    channels on the object.The -rotatePivotRelative/-scalePivotRelative flags can be used
    with the -absolute flag to translate an object so that its
    pivot point ends up at the given absolute position. These
    flags will be ignored if components are specified.The -worldSpaceDistance flag is a modifier flag that may be used
    in conjunction with the -objectSpace/-localSpace flags. When this
    flag is specified the command treats the x,y,z values as world
    space units so the object will move the specified world space
    distance but it will move along the axis specified by the
    -objectSpace/-localSpace flag. The default behaviour, without
    this flag, is to treat the x,y,z values as units in object
    space or local space. In other words, the worldspace distance
    moved will depend on the transformations applied to the object
    unless this flag is specified.
    Args:
        absolute (bool?): Perform an absolute operation.  
                Properties: create
        componentOffset (bool?): Move components individually in local space  
                Properties: create
        componentSpace (bool?): Move in local component space  
                Properties: create
        constrainAlongNormal (bool?): When true, transform constraints are applied along the vertex normal first  
                and only use the closest point when no intersection is found along the normal.  
                Properties: create
        deletePriorHistory (bool?): If true then delete the history prior to the current operation.  
                Properties: create
        localSpace (bool?): Move in local space  
                Properties: create
        moveX (bool?): Move in X direction  
                Properties: create
        moveXY (bool?): Move in XY direction  
                Properties: create
        moveXYZ (bool?): Move in all directions (default)  
                Properties: create
        moveXZ (bool?): Move in XZ direction  
                Properties: create
        moveY (bool?): Move in Y direction  
                Properties: create
        moveYZ (bool?): Move in YZ direction  
                Properties: create
        moveZ (bool?): Move in Z direction  
                Properties: create
        objectSpace (bool?): Move in object space  
                Properties: create
        orientJoint (str?): Default is xyz.  
                Properties: create
        parameter (bool?): Move in parametric space  
                Properties: create
        preserveChildPosition (bool?): When true, transforming an object will apply an opposite transform to its  
                child transform to keep them at the same world-space position.  
                Default is false.  
                Properties: create
        preserveGeometryPosition (bool?): When true, transforming an object will apply an opposite transform to its  
                geometry points to keep them at the same world-space position.  
                Default is false.  
                Properties: create
        preserveUV (bool?): When true, UV values on translated components are projected along the translation  
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
        rotatePivotRelative (bool?): Move relative to the object's rotate pivot point.  
                Properties: create
        scalePivotRelative (bool?): Move relative to the object's scale pivot point.  
                Properties: create
        secondaryAxisOrient (str?): Default is xyz.  
                Properties: create
        symNegative (bool?): When set the component transformation is flipped so it is relative to the  
                negative side of the symmetry plane. The default (no flag) is to transform  
                components relative to the positive side of the symmetry plane.  
                Properties: create
        worldSpace (bool?): Move in world space  
                Properties: create
        worldSpaceDistance (bool?): Move is specified in world space units  
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

