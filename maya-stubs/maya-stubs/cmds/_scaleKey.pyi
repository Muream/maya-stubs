from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scaleKey(*args: str, animation: str = ..., attribute: Multiuse[str] = ..., autoSnap: bool = ..., controlPoints: bool = ..., float: Multiuse[Range[float]] = ..., floatPivot: float = ..., floatScale: float = ..., hierarchy: str = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., newEndFloat: float = ..., newEndTime: int = ..., newStartFloat: float = ..., newStartTime: int = ..., scaleSpecifiedKeys: bool = ..., shape: bool = ..., time: Multiuse[NullableRange[float]] = ..., timePivot: int = ..., timeScale: float = ..., valuePivot: float = ..., valueScale: float = ...) -> int:
    """This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).This command takes keyframes at (or within) the specified times (or time ranges)
    and scales them.  If no times are specified, the scale is applied to active keyframes
    or (if no keys are active) all keys of active objects.This command has two sets of flags for scaling in time/x-axis. One set of flags is
    for time-based animation curves, and the other set of flags is for float-based (unitless) animation curves.
    Most animation curves in Maya are time-based. Unitless animation curves are less common.
    Use the set of flags that corresponds to the type of animation curves being scaled.To scale all selected animation curves regardless of their type, use both sets of flags.
    Args:
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        autoSnap (bool?): Auto snap scaled keys if True.  
                Default value depend on scaleKeyAutoSnap option  
                Properties: create
        controlPoints (bool?): This flag explicitly specifies whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        float (Multiuse[Range[float]]?): value uniquely representing a non-time-based  
                key (or key range) on a time-based animCurve.  Valid  
                floatRange include single values (-f 10) or a  
                string with a lower and upper bound, separated by a  
                colon (-f "10. 20")  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        floatPivot (float?): Scale pivot along the x-axis for float-based (unitless) animCurves  
                Properties: create
        floatScale (float?): Amount to scale along the x-axis for float-based (unitless) animation curves  
                animCurves  
                Properties: create
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        includeUpperBound (bool?): When the -t/time or -f/float flags represent a range  
                of keys, this flag determines whether the keys at the  
                upper bound of the range are included in the keyset.  
                Default value: true.  This flag is only valid when  
                the argument to the -t/time flag is a time range with  
                a lower and upper bound.  (When used with the "pasteKey"  
                command, this flag refers only to the time range of the  
                target curve that is replaced, when using options such  
                as "replace," "fitReplace," or "scaleReplace."  This  
                flag has no effect on the curve pasted from the clipboard.)  
                Properties: create
        index (Multiuse[int]?): index of a key on an animCurve  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        newEndFloat (float?): The end of the float range to which the float-based (unitless) animation curves should be scaled.  
                Properties: create
        newEndTime (int?): The end of the time range to which the time-based animation curves should be scaled.  
                Properties: create
        newStartFloat (float?): The start of the float range to which the float-based (unitless) animation curves should be scaled.  
                Properties: create
        newStartTime (int?): The start of the time range to which the time-based animation curves should be scaled.  
                Properties: create
        scaleSpecifiedKeys (bool?): Determines if only the specified keys are affected by the scale.  
                If false, other keys may be adjusted with the scale. The  
                default is true.  
                Properties: create
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        time (Multiuse[NullableRange[float]]?): time uniquely representing a key (or key  
                range) on a time-based animCurve. See the code  
                examples below on how to format for a single  
                frame or frame ranges.  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        timePivot (int?): Scale pivot along the time-axis for time-based animation curves  
                Properties: create
        timeScale (float?): Amount to scale along the time-axis for time-based animation curves  
                Properties: create
        valuePivot (float?): Scale pivot along the value-axis  
                Properties: create
        valueScale (float?): Amount of scale along the value-axis  
                Properties: create

    Returns:
        int: Number of curves on which scale was performed

    Example:
    """

