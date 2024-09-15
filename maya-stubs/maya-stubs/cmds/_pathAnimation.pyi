from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pathAnimation(*args: str, edit: bool = ..., query: bool = ..., bank: bool = ..., bankScale: Queryable[float] = ..., bankThreshold: Queryable[float] = ..., curve: Queryable[str] = ..., endTimeU: Queryable[Multiuse[int]] = ..., endU: Queryable[float] = ..., follow: bool = ..., followAxis: Queryable[str] = ..., fractionMode: bool = ..., inverseFront: bool = ..., inverseUp: bool = ..., name: Queryable[str] = ..., startTimeU: Queryable[Multiuse[int]] = ..., startU: Queryable[float] = ..., upAxis: Queryable[str] = ..., useNormal: bool = ..., worldUpObject: Queryable[str] = ..., worldUpType: Queryable[str] = ..., worldUpVector: Queryable[Tuple[float, float, float]] = ...) -> Union[str, bool, float, Multiuse[int], Tuple[float, float, float]]:
    """The pathAnimation command constructs the necessary graph nodes
    and their interconnections for a motion path animation. Motion path
    animation requires a curve and one or more other objects.
    During the animation, the objects will be moved along the 3D curve
    or the curveOnSurface.There are two ways to specify the moving objects:Likewise, there are two ways to specify a motion curve:When the end time is not specified: only one keyframe
    will be created either at the current time, or at the specified
    start time.
    Args:
        bank (bool?): If on, enable alignment of the up axis of the moving  
                object(s) to the curvature of the path geometry.  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        bankScale (Queryable[float]?): This flag specifies a factor to scale the amount of  
                bank angle.  
                Default is 1.0  
                When queried, this flag returns a float.  
                Properties: query
        bankThreshold (Queryable[float]?): This flag specifies the limit of the bank angle.  
                Default is 90 degrees  
                When queried, this flag returns an angle.  
                Properties: query
        curve (Queryable[str]?): This flag specifies the name of the curve for the path.  
                Default is NONE  
                When queried, this flag returns a string.  
                Properties: query
        endTimeU (Queryable[Multiuse[int]]?): This flag specifies the ending time of the animation  
                for the u parameter.  
                Default is NONE.  
                When queried, this flag returns a time.  
                Properties: query, multiuse
        endU (Queryable[float]?): This flag specifies the ending value of the u  
                parameterization for the animation.  
                Default is the end parameterization value of the curve.  
                When queried, this flag returns a linear.  
                Properties: query
        follow (bool?): If on, enable alignment of the front axis of the moving object(s).  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        followAxis (Queryable[str]?): This flag specifies which object local axis to be  
                aligned to the tangent of the path curve.  
                Default is y  
                When queried, this flag returns a string.  
                Properties: query
        fractionMode (bool?): If on, evaluation on the path is based on the fraction  
                of length of the path curve.  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        inverseFront (bool?): This flag specifies whether or not to align  
                the front axis of the moving object(s) to the opposite direction  
                of the tangent vector of the path geometry.  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        inverseUp (bool?): This flag specifies whether or not to align  
                the up axis of the moving object(s) to the opposite direction  
                of the normal vector of the path geometry.  
                Default is false.  
                When queried, this flag returns a boolean.  
                Properties: query
        name (Queryable[str]?): This flag specifies the name for the new motion path node.  
                (instead of the default name)  
                When queried, this flag returns a string.  
                Properties: query
        startTimeU (Queryable[Multiuse[int]]?): This flag specifies the starting time of the animation  
                for the u parameter.  
                Default is the the current time.  
                When queried, this flag returns a time.  
                Properties: query, multiuse
        startU (Queryable[float]?): This flag specifies the starting value of the u  
                parameterization for the animation.  
                Default is the start parameterization value of the curve.  
                When queried, this flag returns a linear.  
                Properties: query
        upAxis (Queryable[str]?): This flag specifies which object local axis to be  
                aligned a computed up direction.  
                Default is z  
                When queried, this flag returns a string.  
                Properties: query
        useNormal (bool?): This flag is now obsolete. Use -wut/worldUpType instead.  
                Properties: create, query, edit
        worldUpObject (Queryable[str]?): Set the DAG object to use for worldUpType "object" and  
                "objectrotation". See -wut/worldUpType for greater detail.  
                The default value is no up object, which is interpreted  
                as world space.  
                Properties: create, query, edit
        worldUpType (Queryable[str]?): Set the type of the world up vector computation.  
                The worldUpType can have one of 5 values: "scene",  
                "object", "objectrotation", "vector", or "normal".  
                If the value is "scene", the upVector is  
                aligned with the up axis of the scene and  
                worldUpVector and worldUpObject are ignored.  
                If the value is "object", the upVector is  
                aimed as closely as possible to the  
                origin of the space of the worldUpObject and  
                the worldUpVector is ignored.  
                If the value is "objectrotation" then the  
                worldUpVector is interpreted as being in  
                the coordinate space of the worldUpObject, transformed into  
                world space and the upVector is aligned as  
                closely as possible to the result.  
                If the value is "vector", the upVector  
                is aligned with worldUpVector as closely as  
                possible and worldUpObject is ignored.  
                Finally, if the value is "normal" the upVector is aligned to  
                the path geometry.  
                The default worldUpType is "vector".  
                Properties: create, query, edit
        worldUpVector (Queryable[Tuple[float, float, float]]?): Set world up vector.  This is the vector in world  
                coordinates that up vector should align with.  
                See -wut/worldUpType for greater detail.  
                If not given at creation time, the default  
                value of (0.0, 1.0, 0.0) is used.  
                Properties: create, query, edit

    Returns:
        str: (name of the created motionPath node)

    Example:
    """

