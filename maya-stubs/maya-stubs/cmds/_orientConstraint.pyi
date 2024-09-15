from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def orientConstraint(*args: str, edit: bool = ..., query: bool = ..., createCache: Tuple[float, float] = ..., deleteCache: bool = ..., layer: str = ..., maintainOffset: bool = ..., name: Queryable[str] = ..., offset: Queryable[Tuple[float, float, float]] = ..., remove: bool = ..., skip: Multiuse[str] = ..., targetList: bool = ..., weight: Queryable[float] = ..., weightAliasList: bool = ...) -> Union[str, Tuple[float, float, float], bool, float]:
    """Constrain an object's orientation to match the orientation of the
    target or the average of a number of targets.An orientConstraint takes as input one or more "target" DAG transform
    nodes to control the orientation of the single "constraint object"
    DAG transform  The orientConstraint orients the constrained object
    to match the weighted average of the target world space orientations.
    Args:
        createCache (Tuple[float, float]?): This flag is used to generate an animation curve that serves as a cache for  
                the constraint. The two arguments define the start and end frames.  
              
                The cache is useful if the constraint has multiple targets and  
                the constraint's interpolation type is set to "no flip". The "no flip"  
                mode prevents flipping during playback, but the result is dependent on  
                the previous frame.  Therefore in order to consistently get the same  
                result on a specific frame, a cache must be generated. This flag  
                creates the cache and sets the constraint's interpolation type to  
                "cache". If a cache exists already, it will be deleted and replaced  
                with a new cache.  
                Properties: edit
        deleteCache (bool?): Delete an existing interpolation cache.  
                Properties: edit
        layer (str?): Specify the name of the animation layer where the constraint should be added.  
                Properties: create, edit
        maintainOffset (bool?): The offset necessary to preserve the constrained  
                object's initial orientation will be calculated and used as the  
                offset.  
                Properties: create
        name (Queryable[str]?): Sets the name of the constraint node to the specified  
                name.  Default name is constrainedObjectName_constraintType  
                Properties: create, query, edit
        offset (Queryable[Tuple[float, float, float]]?): Sets or queries the value of the offset. Default is 0,0,0.  
                Properties: create, query, edit
        remove (bool?): removes the listed target(s) from the constraint.  
                Properties: edit
        skip (Multiuse[str]?): Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.  
                Properties: create, edit, multiuse
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
        str: [] ( name of the created constraint node)

    Example:
    """

