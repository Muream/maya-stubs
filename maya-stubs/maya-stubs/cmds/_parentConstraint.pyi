from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def parentConstraint(*args: str, edit: bool = ..., query: bool = ..., createCache: Tuple[float, float] = ..., decompRotationToChild: bool = ..., deleteCache: bool = ..., layer: str = ..., maintainOffset: bool = ..., name: Queryable[str] = ..., remove: bool = ..., skipRotate: Multiuse[str] = ..., skipTranslate: Multiuse[str] = ..., targetList: bool = ..., weight: Queryable[float] = ..., weightAliasList: bool = ...) -> Union[List[str], str, bool, float]:
    """Constrain an object's position and rotation so that it behaves as if it
    were a child of the target object(s). In the case of multiple targets,
    the overall position and rotation of the constrained object is the
    weighted average of each target's contribution to the position and
    rotation of the object.A parentConstraint takes as input one or more "target" DAG transform
    nodes at which to position and rotate the single "constraint
    object" DAG transform node.  The parentConstraint positions and rotates
    the constrained object at the weighted average of the world
    space position, rotation and scale target objects.
    Args:
        createCache (Tuple[float, float]?): This flag is used to generate an animation curve that serves as a  
                cache for the constraint. The two arguments define the start and end  
                frames.  
              
                The cache is useful if the constraint has multiple targets and  
                the constraint's interpolation type is set to "no flip". The "no flip"  
                mode prevents flipping during playback, but the result is dependent on  
                the previous frame. Therefore in order to consistently get the same  
                result on a specific frame, a cache must be generated. This flag  
                creates the cache and sets the constraint's interpolation type to  
                "cache". If a cache exists already, it will be deleted and replaced  
                with a new cache.  
                Properties: edit
        decompRotationToChild (bool?): During constraint creation, if the rotation offset between the constrained  
                object and the target object is maintained, this flag indicates close to  
                which object the offset rotation is decomposed. Setting this flag will make  
                the rotation decomposition close to the constrained object instead of the  
                target object, which is the default setting.  
                Properties: create
        deleteCache (bool?): Delete an existing interpolation cache.  
                Properties: edit
        layer (str?): Specify the name of the animation layer where the constraint should be added.  
                Properties: create, edit
        maintainOffset (bool?): If this flag is specified the position and rotation of the  
                constrained object will be maintained.  
                Properties: create
        name (Queryable[str]?): Sets the name of the constraint node to the specified  
                name.  Default name is constrainedObjectName_constraintType  
                Properties: create, query, edit
        remove (bool?): removes the listed target(s) from the constraint.  
                Properties: edit
        skipRotate (Multiuse[str]?): Causes the axis specified not to be considered when  
                constraining rotation.  Valid arguments are "x", "y", "z" and "none".  
                Properties: create, multiuse
        skipTranslate (Multiuse[str]?): Causes the axis specified not to be considered when  
                constraining translation.  Valid arguments are "x", "y", "z" and "none".  
                Properties: create, multiuse
        targetList (bool?): Return the list of target objects.  
                Properties: query
        weight (Queryable[float]?): Sets the weight value for the specified target(s).  
                If not given at creation time, the default value of 1.0 is used.  
                Properties: create, query, edit
        weightAliasList (bool?): Returns the names of the attributes that control the weight  
                of the target objects. Aliases are returned in the same order  
                as the targets are returned by the targetList flag  
                Properties: query

    Returns:
        List[str]: Name of the created constraint node

    Example:
    """

