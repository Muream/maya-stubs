from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def transformLimits(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., enableRotationX: Queryable[Tuple[bool, bool]] = ..., enableRotationY: Queryable[Tuple[bool, bool]] = ..., enableRotationZ: Queryable[Tuple[bool, bool]] = ..., enableScaleX: Queryable[Tuple[bool, bool]] = ..., enableScaleY: Queryable[Tuple[bool, bool]] = ..., enableScaleZ: Queryable[Tuple[bool, bool]] = ..., enableTranslationX: Queryable[Tuple[bool, bool]] = ..., enableTranslationY: Queryable[Tuple[bool, bool]] = ..., enableTranslationZ: Queryable[Tuple[bool, bool]] = ..., remove: bool = ..., rotationX: Queryable[Tuple[float, float]] = ..., rotationY: Queryable[Tuple[float, float]] = ..., rotationZ: Queryable[Tuple[float, float]] = ..., scaleX: Queryable[Tuple[float, float]] = ..., scaleY: Queryable[Tuple[float, float]] = ..., scaleZ: Queryable[Tuple[float, float]] = ..., translationX: Queryable[Tuple[float, float]] = ..., translationY: Queryable[Tuple[float, float]] = ..., translationZ: Queryable[Tuple[float, float]] = ...) -> Union[bool, Tuple[bool, bool], Tuple[float, float]]:
    """The transformLimits command allows us to set, edit, or query
    the limits of the transformation that can be applied to objects.We can also turn any limits off which may have been previously set.
    When an object is first created, all the transformation limits are off
    by default.Transformation limits allow us to control how much an object can
    be transformed. This is most useful for joints, although it can be
    used any place we would like to limit the movement of an object.Default values are:( -1, 1) for translation,
    ( -1, 1) for scaling, and
    (-45,45) for rotation.
    Args:
        enableRotationX (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper x-rotation limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableRotationY (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper y-rotation limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableRotationZ (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper z-rotation limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableScaleX (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper x-scale limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableScaleY (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper y-scale limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableScaleZ (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper z-scale limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableTranslationX (Queryable[Tuple[bool, bool]]?): enable/disable the  ower and upper x-translation limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableTranslationY (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper y-translation limits  
                When queried, it returns boolean boolean  
                Properties: query
        enableTranslationZ (Queryable[Tuple[bool, bool]]?): enable/disable the lower and upper z-translation limits  
                When queried, it returns boolean boolean  
                Properties: query
        remove (bool?): turn all the limits off and reset them to their default values  
                Properties: create
        rotationX (Queryable[Tuple[float, float]]?): set the lower and upper x-rotation limits  
                When queried, it returns angle angle  
                Properties: query
        rotationY (Queryable[Tuple[float, float]]?): set the lower and upper y-rotation limits  
                When queried, it returns angle angle  
                Properties: query
        rotationZ (Queryable[Tuple[float, float]]?): set the lower and upper z-rotation limits  
                When queried, it returns angle angle  
                Properties: query
        scaleX (Queryable[Tuple[float, float]]?): set the lower and upper x-scale limits  
                When queried, it returns float float  
                Properties: query
        scaleY (Queryable[Tuple[float, float]]?): set the lower and upper y-scale limits  
                When queried, it returns float float  
                Properties: query
        scaleZ (Queryable[Tuple[float, float]]?): set the lower and upper z-scale limits  
                When queried, it returns float float  
                Properties: query
        translationX (Queryable[Tuple[float, float]]?): set the lower and upper x-translation limits  
                When queried, it returns linear linear  
                Properties: query
        translationY (Queryable[Tuple[float, float]]?): set the lower and upper y-translation limits  
                When queried, it returns linear linear  
                Properties: query
        translationZ (Queryable[Tuple[float, float]]?): set the lower and upper z-translation limits  
                When queried, it returns linear linear  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

