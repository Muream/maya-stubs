from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def marker(*args: str, edit: bool = ..., query: bool = ..., attach: bool = ..., detach: bool = ..., frontTwist: Queryable[float] = ..., orientationMarker: bool = ..., positionMarker: bool = ..., sideTwist: Queryable[float] = ..., time: Queryable[int] = ..., upTwist: Queryable[float] = ..., valueU: Queryable[float] = ...) -> Union[List[str], float, bool, int]:
    """The marker command creates one or two markers, on a motion path curve,
    at the specified time and location.
    The optionnal string argument is the parent object name.One can specify "-pm -om" option to create both, a position marker
    and an orientation marker.Since there is only one keyframe for each marker of the same type,
    no more than one marker of the same type with the same time value
    can exist.The default marker type is the position marker. The default time is
    the current time.
    Args:
        attach (bool?): This flag specifies to attach the selected 3D position markers  
                to their parent geometry.  
                Properties: create
        detach (bool?): This flag specifies to detach the selected position markers from  
                their parent geometry to the 3D space.  
                Properties: create
        frontTwist (Queryable[float]?): This flag specifies the amount of twist angle about  
                the front vector for the marker.  
                Default is 0.  
                When queried, this flag returns a angle.  
                Properties: query
        orientationMarker (bool?): This flag specifies creation of an orientation marker.  
                Default is not set..  
                When queried, this flag returns a boolean.  
                Properties: query
        positionMarker (bool?): This flag specifies creation of a position marker.  
                Default is set.  
                When queried, this flag returns a boolean.  
                Properties: query
        sideTwist (Queryable[float]?): This flag specifies  the amount of twist angle about  
                the side vector for the marker.  
                Default is 0.  
                When queried, this flag returns a angle.  
                Properties: query
        time (Queryable[int]?): This flag specifies the time for the marker.  
                Default is the current time.  
                When queried, this flag returns a time.  
                Properties: query
        upTwist (Queryable[float]?): This flag specifies the amount of twist angle about  
                the up vector for the marker.  
                Default is 0.  
                When queried, this flag returns a angle.  
                Properties: query
        valueU (Queryable[float]?): This flag specifies the location of the position marker  
                w.r.t. the parent geometry u parameterization.  
                Default is the value at current time.  
                When queried, this flag returns a linear.  
                Properties: query

    Returns:
        List[str]: (name of the created markers)

    Example:
    """

