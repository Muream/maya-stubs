from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def copyKey(*args: str, animLayer: str = ..., animation: str = ..., attribute: Multiuse[str] = ..., clipboard: str = ..., controlPoints: bool = ..., float: Multiuse[Range[float]] = ..., forceIndependentEulerAngles: bool = ..., hierarchy: str = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., option: str = ..., shape: bool = ..., time: Multiuse[NullableRange[float]] = ...) -> int:
    """This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).This command copies curve segments's hierarchies from
    specified targets and puts them in the clipboard.  Source
    curves are unchanged.  The pasteKey command applies these
    curves to other objects.The shape of the copied curve placed in the clipboard
    depends on the copyKey "-option" specified.  Each of these options
    below will be explained using an example.  For all the explanations,
    let us assume that the source animation curve (from which keys will
    be copied) has 5 keyframes at times 10, 15, 20, 25, and 30.TbaseKeySetCmd.h
    Args:
        animLayer (str?): Specifies that the keys getting copied should come from this  
                specified animation layer. If no keys on the object exist  
                on this layer, then no keys are copied.  
                Properties: create
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        clipboard (str?): Specifies the clipboard to which animation is copied.  
                Valid clipboards are "api" and "anim".  The default clipboard  
                is: anim  
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
        forceIndependentEulerAngles (bool?): Specifies that the rotation curves should always be placed on the  
                clipboard as independent Euler Angles. The default value is false.  
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
        option (str?): The option to use when performing the copyKey operation.  
                Valid options are "keys," and "curve."  The default copy option  
                is: keys  
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

    Returns:
        int: Number of animation curves copied.

    Example:
    """

