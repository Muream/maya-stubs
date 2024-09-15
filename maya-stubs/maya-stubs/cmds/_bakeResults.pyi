from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bakeResults(*args: str, edit: bool = ..., query: bool = ..., animation: str = ..., attribute: Multiuse[str] = ..., bakeOnOverrideLayer: bool = ..., controlPoints: bool = ..., destinationLayer: str = ..., disableImplicitControl: bool = ..., float: Multiuse[Range[float]] = ..., hierarchy: str = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., minimizeRotation: bool = ..., oversamplingRate: int = ..., preserveOutsideKeys: bool = ..., removeBakedAnimFromLayer: bool = ..., removeBakedAttributeFromLayer: bool = ..., resolveWithoutLayer: Multiuse[str] = ..., sampleBy: int = ..., shape: bool = ..., simulation: bool = ..., smart: Union[Tuple[()], Tuple[bool, float]] = ..., sparseAnimCurveBake: bool = ..., time: Multiuse[NullableRange[float]] = ...) -> int:
    """This command allows the user to replace a chain of dependency nodes
    which define the value for an attribute with a single animation curve.
    Command allows the user to specify the range and frequency of sampling.This command operates on a keyset. A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices. Times and indices should
    be specified as a range, as shown below.
    Args:
        animation (str?): Where this command should get the animation to act  
                on. Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects." See  
                command description for details.  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        bakeOnOverrideLayer (bool?): If true, all layered and baked attribute will be added as a top override layer.  
                Properties: create
        controlPoints (bool?): This flag explicitly specifies whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        destinationLayer (str?): This flag can be used to specify an existing layer where the baked results  
                should be stored. Use this flag with caution. If the destination layer already has animation on it  
                that contributes to the final result, it will be replaced by the output of the bake. As a result,  
                it is possible that the combined animation visible in the scene is different before / after the baking  
                process.  
                Properties: create
        disableImplicitControl (bool?): Whether to disable implicit control after the anim curves  
                are obtained as the result of this command. An implicit control  
                to an attribute is some function that affects the attribute  
                without using an explicit dependency graph connection. The  
                control of IK, via ik handles, is an example.  
                Properties: create
        float (Multiuse[Range[float]]?): value uniquely representing a non-time-based  
                key (or key range) on a time-based animCurve. Valid  
                floatRange include single values (-f 10) or a  
                string with a lower and upper bound, separated by a  
                colon (-f "10. 20")  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        includeUpperBound (bool?): When the -t/time or -f/float flags represent a range  
                of keys, this flag determines whether the keys at the  
                upper bound of the range are included in the keyset.  
                Default value: true. This flag is only valid when  
                the argument to the -t/time flag is a time range with  
                a lower and upper bound. Note: when used with the "pasteKey"  
                command, this flag refers only to the time range of the  
                target curve that is replaced, when using options such  
                as "replace," "fitReplace," or "scaleReplace." This  
                flag has no effect on the curve pasted from the clipboard.  
                Properties: create
        index (Multiuse[int]?): index of a key on an animCurve  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        minimizeRotation (bool?): Specify whether to minimize the local Euler component from key to key during baking of rotation channels.  
                Properties: create
        oversamplingRate (int?): Amount of samples per sampleBy period. Default is 1.  
                Properties: create
        preserveOutsideKeys (bool?): Whether to preserve keys that are outside the bake range  
                when there are directly connected animation curves or a pairBlend node  
                which has an animation curve as its direct input. The default  
                (false) is to remove frames outside the bake range. If the channel  
                that you are baking is not controlled by a single animation curve,  
                then a new animation curve will be created with keys only in the  
                bake range. In the case of pairBlend-driven channels, setting pok to  
                true will retain both the pairBlend and its input animCurve. The  
                blended values will be baked onto the animCurve and the weight of the  
                pairBlend weight will be keyed to the animCurve during the baked  
                range.  
                Properties: create
        removeBakedAnimFromLayer (bool?): If true, all baked animation will be removed from the layer.  
                Otherwise all layer associated with the baked animation will be muted.  
                Properties: create
        removeBakedAttributeFromLayer (bool?): If true, all baked attribute will be removed from the layer.  
                Otherwise all layer associated with the baked attribute will be muted.  
                Properties: create
        resolveWithoutLayer (Multiuse[str]?): This flag can be used to specify a list of layers to be merged together during the bake process. This  
                is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines  
                the proper value to key on the destination layer to achieve the same result as the merged layers.  
                Properties: create, multiuse
        sampleBy (int?): Amount to sample by. Default is 1.0 in current timeUnit.  
                Properties: create
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        simulation (bool?): Using this flag instructs the command to preform a simulation instead  
                of just evaluating each attribute separately over the range of time.  
                The simulation flag is required to bake animation that depends on  
                the whole scene being evaluated at each time step such as dynamics. The  
                default is false.  
                Properties: create
        smart (Union[Tuple[()], Tuple[bool, float]]?): Specify whether to enable smart bake and the optional smart bake tolerance.  
                Properties: create
        sparseAnimCurveBake (bool?): When this is true and anim curves are being baked, do not insert  
                any keys into areas of the curve where animation is defined. And, use  
                as few keys as possible to bake the pre and post infinity behavior.  
                When this is false, one key will be inserted at each time step. The  
                default is false.  
                Properties: create
        time (Multiuse[NullableRange[float]]?): time uniquely representing a key (or key  
                range) on a time-based animCurve. See the code  
                examples below on how to format for a single  
                frame or frame ranges.  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse

    Returns:
        int: - The number of channels baked

    Example:
    """

