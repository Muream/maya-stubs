from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectKey(*args: str, addTo: bool = ..., animation: str = ..., attribute: Multiuse[str] = ..., clear: bool = ..., controlPoints: bool = ..., float: Multiuse[Range[float]] = ..., hierarchy: str = ..., inTangent: bool = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., keyframe: bool = ..., outTangent: bool = ..., remove: bool = ..., replace: bool = ..., shape: bool = ..., time: Multiuse[NullableRange[float]] = ..., toggle: bool = ..., unsnappedKeys: float = ...) -> int:
    """This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).This command places keyframes and/or keyframe tangents
    on the active list.
    Args:
        addTo (bool?): Add to the current selection of keyframes/tangents  
                Properties: create
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        clear (bool?): Remove all keyframes and tangents from the active list.  
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
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        inTangent (bool?): Select in-tangents of keyframes in the specified time range  
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
        keyframe (bool?): select only keyframes (cannot be combined with -in/-out)  
                Properties: create
        outTangent (bool?): Select out-tangents of keyframes in the specified time range  
                Properties: create
        remove (bool?): Remove from the current selection of keyframes/tangents  
                Properties: create
        replace (bool?): Replace the current selection of keyframes/tangents  
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
        toggle (bool?): Toggle the picked state of the specified keyset  
                Properties: create
        unsnappedKeys (float?): Select only keys that have times that are not a multiple of  
                the specified numeric value.  
                Properties: create

    Returns:
        int: The number of curves on which keys were
            selected (or deselcted).

    Example:
    """

