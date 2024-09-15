from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def makeIdentity(*args: str, apply: bool = ..., jointOrient: bool = ..., normal: int = ..., preserveNormals: bool = ..., rotate: bool = ..., scale: bool = ..., translate: bool = ...) -> bool:
    """The makeIdentity command is a quick way to reset the selected
    transform and all of its children down to the shape level by the
    identity transformation.  You can also specify which of transform,
    rotate or scale is applied down from the selected transform.
    The identity transformation means:If a transform is a joint, then the "translate" attribute may not be 0,
    but will be used to position the joints so that they preserve their
    world space positions.  The translate flag doesn't apply to joints,
    since joints must preserve their world space positions.  Only the rotate
    and scale flags are meaningful when applied to joints.If the -a/apply flag is true, then the transforms that are reset
    are accumulated and applied to the all shapes below the modified
    transforms, so that the shapes will not move. The pivot positions are
    recalculated so that they also will not move in world space.
    If this flag is false, then the transformations are reset to identity,
    without any changes to preserve position.
    Args:
        apply (bool?): If this flag is true, the accumulated transforms are applied to  
                the shape after the transforms are made identity, such that the  
                world space positions of the transforms pivots are preserved,  
                and the shapes do not move. The default is false.  
                Properties: create
        jointOrient (bool?): If this flag is set, the joint orient on joints will be reset  
                to align with worldspace.  
                Properties: create
        normal (int?): If this flag is set to 1, the normals on polygonal objects  
                will be frozen.  This flag is valid only when the -apply flag is on.  
                If this flag is set to 2, the normals on polygonal objects will  
                be frozen only if its a non-rigid transformation matrix.  
                ie, a transformation that does not contain shear, skew or  
                non-proportional scaling.  
                The default behaviour is not to freeze normals.  
                Properties: create
        preserveNormals (bool?): If this flag is true, the normals on polygonal objects will be  
                reversed if the objects are negatively scaled (reflection).  
                This flag is valid only when the -apply flag is on.  
                Properties: create
        rotate (bool?): If this flag is true, only the rotation is applied to the shape.  
                The rotation will be changed to 0, 0, 0.  
                If neither translate nor rotate nor scale flags are specified,  
                then all (t, r, s) are applied.  
                Properties: create
        scale (bool?): If this flag is true, only the scale is applied to the shape.  
                The scale factor will be changed to 1, 1, 1.  
                If neither translate nor rotate nor scale flags are specified,  
                then all (t, r, s) are applied.  
                Properties: create
        translate (bool?): If this flag is true, only the translation is applied to the shape.  
                The translation will be changed to 0, 0, 0.  
                If neither translate nor rotate nor scale flags are specified,  
                then all (t, r, s)  are applied.  (Note: the translate flag is not  
                meaningful when applied to joints, since joints are made to preserve  
                their world space position.  This flag will have no effect on joints.)  
                Properties: create

    Returns:
        bool:

    Example:
    """

