from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def matchTransform(*args: str, pivots: bool = ..., position: bool = ..., positionX: bool = ..., positionY: bool = ..., positionZ: bool = ..., rotatePivot: bool = ..., rotation: bool = ..., rotationX: bool = ..., rotationY: bool = ..., rotationZ: bool = ..., scale: bool = ..., scaleBox: bool = ..., scalePivot: bool = ..., scaleX: bool = ..., scaleY: bool = ..., scaleZ: bool = ...) -> bool:
    """This command modifies the source object's transform to match the
    target object's transform.If no flags are specified then the command will match position,
    rotation and scaling.
    Args:
        pivots (bool?): Match the source object(s) scale/rotate pivot positions to the target transform's pivot.  
                Properties: create
        position (bool?): Match the source object(s) position to the target object.  
                Properties: create
        positionX (bool?): Match the source object(s) X position to the target object.  
                Properties: create
        positionY (bool?): Match the source object(s) Y position to the target object.  
                Properties: create
        positionZ (bool?): Match the source object(s) Z position to the target object.  
                Properties: create
        rotatePivot (bool?): Match the source object(s) rotate pivot position to the target transform's pivot.  
                Properties: create
        rotation (bool?): Match the source object(s) rotation to the target object.  
                Properties: create
        rotationX (bool?): Match the source object(s) X rotation to the target object.  
                Properties: create
        rotationY (bool?): Match the source object(s) Y rotation to the target object.  
                Properties: create
        rotationZ (bool?): Match the source object(s) Z rotation to the target object.  
                Properties: create
        scale (bool?): Match the source object(s) scale to the target transform.  
                Properties: create
        scaleBox (bool?): Use the source/target object's child bounding box size when matching scaling.  
                Properties: create
        scalePivot (bool?): Match the source object(s) scale pivot position to the target transform's pivot.  
                Properties: create
        scaleX (bool?): Match the source object(s) X scale to the target object.  
                Properties: create
        scaleY (bool?): Match the source object(s) Y scale to the target object.  
                Properties: create
        scaleZ (bool?): Match the source object(s) Z scale to the target object.  
                Properties: create

    Returns:
        bool:

    Example:
    """

