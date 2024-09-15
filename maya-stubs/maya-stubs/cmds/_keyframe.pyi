from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def keyframe(*args: str, edit: bool = ..., query: bool = ..., absolute: bool = ..., adjustBreakdown: bool = ..., animation: str = ..., attribute: Multiuse[str] = ..., breakdown: bool = ..., clipTime: Tuple[int, int, float] = ..., controlPoints: bool = ..., eval: bool = ..., float: Multiuse[Range[float]] = ..., floatChange: Queryable[float] = ..., hierarchy: str = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., indexValue: bool = ..., keyframeCount: bool = ..., lastSelected: bool = ..., name: bool = ..., option: str = ..., relative: bool = ..., selected: bool = ..., shape: bool = ..., tickDrawSpecial: bool = ..., time: Multiuse[NullableRange[float]] = ..., timeChange: Queryable[int] = ..., valueChange: Queryable[float] = ...) -> Union[int, bool, float]:
    """This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).This command edits the time and/or value of keys of
    specified objects and/or parameter curvesUnless otherwise specified by the -query flag, the command
    defaults to editing keyframes.
    Args:
        absolute (bool?): Move amounts are absolute.  
                Properties: create
        adjustBreakdown (bool?): When false, moving keys will not preserve breakdown  
                timing, when true (the default) breakdowns will be adjusted  
                to preserve their timing relationship.  
                Properties: create
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        breakdown (bool?): Sets the breakdown state for the key.  Returns  
                an integer.  Default is false.  The breakdown state of a key  
                cannot be set in the same command as it is moved (i.e., via  
                the -tc or -fc flags).  
                Properties: create, query, edit
        clipTime (Tuple[int, int, float]?): Modifies the final time where a key is inserted using an  
                offset, pivot, and scale.  
                Properties: create
        controlPoints (bool?): This flag explicitly specifies whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        eval (bool?): Returns the value(s) of the animCurves when evaluated  
                (without regard to input connections)  
                at the times given by the -t/time or -f/float flags.  Cannot  
                be used in combination with other query flags, and  
                cannot be used with time ranges (-t "5. 10").  
                When no -t or -f flags appear on the command line, the  
                evals are queried at the current time.  Query returns a float[].  
                Properties: create, query
        float (Multiuse[Range[float]]?): value uniquely representing a non-time-based  
                key (or key range) on a time-based animCurve.  Valid  
                floatRange include single values (-f 10) or a  
                string with a lower and upper bound, separated by a  
                colon (-f "10. 20")  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        floatChange (Queryable[float]?): How much (with -relative) or where (with -absolute)  
                to move keys (on non-time-input animation curves)  
                along the x (float) axis. Returns float[] when queried.  
                Properties: create, query, edit
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
        indexValue (bool?): Query-only flag that returns an int for the key's index.  
                Properties: create, query
        keyframeCount (bool?): Returns an int for the number of keys found for the  
                targets.  
                Properties: create, query
        lastSelected (bool?): When used in queries, this flag returns requested values  
                for the last selected key.  
                Properties: create, query
        name (bool?): Returns the names of animCurves of specified nodes,  
                attributes or keys.  
                Properties: create, query
        option (str?): Valid values are "move," "insert," "over," and  
                "segmentOver." When you "move" a key, the key will not cross over  
                (in time) any keys before or after it. When you "insert" a key,  
                all keys before or after (depending upon the -timeChange value)  
                will be moved an equivalent amount. When you "over" a key, the key  
                is allowed to move to any time (as long as a key is not there already).  
                When you "segmentOver" a set of keys (this option only has a  
                noticeable effect when more than one key is being moved) the first  
                key (in time) and last key define a segment (unless you specify a  
                time range). That segment is then allowed to move over other keys,  
                and keys will be moved to make room for the segment.  
                Properties: create, edit
        relative (bool?): Move amounts are relative to a key's current position.  
                Properties: create
        selected (bool?): When used in queries, this flag returns requested values  
                for any active keys.  
                Properties: create, query
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        tickDrawSpecial (bool?): Sets the special drawing state for this key when it  
                is drawn as a tick in the timeline.  
                Properties: create, edit
        time (Multiuse[NullableRange[float]]?): time uniquely representing a key (or key  
                range) on a time-based animCurve. See the code  
                examples below on how to format for a single  
                frame or frame ranges.  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        timeChange (Queryable[int]?): How much (with -relative) or where (with -absolute)  
                to move keys (on time-input animation curves)  
                along the x (time) axis.  Returns float[] when queried.  
                Properties: create, query, edit
        valueChange (Queryable[float]?): How much (with -relative) or where (with -absolute)  
                to move keys along the y (value) axis. Returns float[]  
                when queried.  
                Properties: create, query, edit

    Returns:
        int: (except where noted below)
            Number of curves on which keys were modified.
            In -query mode, the command can return a variety of things,
            as described with each queryable flag below.

    Example:
    """

