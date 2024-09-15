from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pasteKey(*args: str, edit: bool = ..., query: bool = ..., animLayer: str = ..., animation: str = ..., attribute: Multiuse[str] = ..., clipboard: str = ..., connect: bool = ..., copies: int = ..., float: Range[float] = ..., floatOffset: float = ..., includeUpperBound: bool = ..., index: int = ..., matchByName: bool = ..., option: str = ..., time: NullableRange[float] = ..., timeOffset: int = ..., valueOffset: float = ...) -> int:
    """The pasteKey command pastes curve segment hierarchies from the
    clipboard onto other objects or curves. If the object hierarchy
    from which the curve segments were copied or cut does not match
    the object hierarchy being pasted to, pasteKey will paste as much
    as it can match in the hierarchy.  If animation from only one object
    is on the clipboard, it will be pasted to each of the target objects.
    If animation from more than one object is on the clipboard, selection
    list order determines what animation is pasted to which object.Valid operations include:TbaseKeySetCmd.hThe way the keyset clipboard will be pasted to the specified object's
    attributes depends on the paste "-option" specified. Each of these
    options below will be explained using an example. For all the
    explanations, let us assume that there is a curve segment
    with 20 frames of animation on the keyset clipboard (you can put
    curve segments onto the clipboard using theorcommands). We will call the animation curve that
    we are pasting to the
    Args:
        animLayer (str?): Specifies that the keys getting pasted should be pasted onto  
                curves on the specified animation layer.If that layer doesn't  
                exist for the specified objects or attributes then the keys  
                won't get pasted.  
                Properties: create
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        clipboard (str?): Specifies the clipboard from which animation is pasted.  
                Valid clipboards are "api" and "anim".  The default clipboard  
                is: anim  
                Properties: create
        connect (bool?): When true, connect the source curve with the  
                destination curve's value at the paste time.  
                (This has the effect of shifting the clipboard curve  
                in value to connect with the destination curve.)  
                False preserves the source curve's original keyframe  
                values. Default is false.  
                Properties: create
        copies (int?): The number of times to paste the source curve.  
                Properties: create
        float (Range[float]?): value uniquely representing a non-time-based  
                key (or key range) on a time-based animCurve.  Valid  
                floatRange include single values (-f 10) or a  
                string with a lower and upper bound, separated by a  
                colon (-f "10. 20")  
                      In query mode, this flag needs a value.  
                Properties: create
        floatOffset (float?): How much to offset the pasted keys in time (for non-time-input  
                animation curves).  
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
        index (int?): index of a key on an animCurve  
                      In query mode, this flag needs a value.  
                Properties: create
        matchByName (bool?): When true, we will only paste onto items in the scene whose  
                node and attribute names match up exactly with a corresponding  
                item in the clipboard. No hierarchy information is used.  
                Default is false, and in this case the usual matching by  
                hierarchy occurs.  
                Properties: create
        option (str?): Valid values are "insert", "replace",  
                "replaceCompletely", "merge", "scaleInsert,"  
                "scaleReplace", "scaleMerge", "fitInsert",  
                "fitReplace", and "fitMerge". The default paste  
                option is: "insert".  
                Properties: create
        time (NullableRange[float]?): time uniquely representing a key (or key  
                range) on a time-based animCurve.  See the code  
                examples below on how to format for a single  
                frame or frame ranges.  
                      In query mode, this flag needs a value.  
                Properties: create
        timeOffset (int?): How much to offset the pasted keys in time (for time-input  
                animation curves).  
                Properties: create
        valueOffset (float?): How much to offset the pasted keys in value.  
                Properties: create

    Returns:
        int: The number of curves pasted

    Example:
    """

