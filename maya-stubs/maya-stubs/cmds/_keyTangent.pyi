from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def keyTangent(*args: str, edit: bool = ..., query: bool = ..., absolute: bool = ..., animation: str = ..., attribute: Multiuse[str] = ..., controlPoints: bool = ..., float: Multiuse[Range[float]] = ..., g: bool = ..., hierarchy: str = ..., inAngle: Queryable[float] = ..., inTangentType: Queryable[str] = ..., inWeight: Queryable[float] = ..., includeUpperBound: bool = ..., index: Multiuse[int] = ..., ix: Queryable[float] = ..., iy: Queryable[float] = ..., lock: bool = ..., outAngle: Queryable[float] = ..., outTangentType: Queryable[str] = ..., outWeight: Queryable[float] = ..., ox: Queryable[float] = ..., oy: Queryable[float] = ..., pluginTangentTypes: Queryable[str] = ..., relative: bool = ..., shape: bool = ..., stepAttributes: bool = ..., time: Multiuse[NullableRange[float]] = ..., unify: bool = ..., weightLock: bool = ..., weightedTangents: bool = ...) -> Union[int, float, str, bool]:
    """This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.The animation curves comprising a keyset depend on the value
    of the "-animation" flag:Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).This command edits or queries tangent properties of keyframes
    in a keyset.  It is also used to edit or query the default
    tangent type of newly created keyframes (see the setKeyframe
    command for more information on how to override this default).Tangents help manage the shape of the animation curve and affect
    the interpolation between keys.  The tangent angle specifies the
    direction the curve will take as it leaves (or enters) a key.
    The tangent weight specifies how much influence the tangent angle
    has on the curve before the curve starts towards the next key.Maya internally represents tangents as x and y values.  Refer to the API
    documentation for MFnAnimCurve for a description of the relationship
    between tangent angle and weight and the internal x and y values.
    Args:
        absolute (bool?): Changes to tangent positions are NOT relative to the  
                current position.  
                Properties: create, edit
        animation (str?): Where this command should get the animation to act  
                on.  Valid values are "objects," "keys," and  
                "keysOrObjects" Default: "keysOrObjects."  (See  
                Description for details.)  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
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
        g (bool?): Required for all operations on the global tangent type.  
                The global tangent type is used by the setKeyframe command  
                when tangent types have not been specifically applied, except  
                in combination with flags such as 'i/insert' which preserve the shape  
                of the curve.  It is also used when keys are set from the menu.  
                The only flags that can appear on a keyTangent command  
                with the 'g/global' flag are 'itt/inTangentType',  
                'ott/outTangentType' and 'wt/weightedTangents'.  
                Properties: create
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        inAngle (Queryable[float]?): New value for the angle of the in-tangent.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        inTangentType (Queryable[str]?): Specify the in-tangent type.  Valid values are  
                "spline," "linear," "fast," "slow," "flat," "step," "stepnext,"  
                "fixed," "clamped," "plateau", "auto", "autoease", "automix", and "autocustom".  
                Returns a string[] when queried.  
                Properties: create, query, edit
        inWeight (Queryable[float]?): New value for the weight of the in-tangent.  
                Returns a float[] when queried.  
                Properties: create, query, edit
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
        ix (Queryable[float]?): New value for the x-component of the in-tangent.  
                This is a unit independent representation of the tangent  
                component.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        iy (Queryable[float]?): New value for the y-component of the in-tangent.  
                This is a unit independent representation of the tangent  
                component.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        lock (bool?): Lock a tangent so in and out tangents move together.  
                Returns an int[] when queried.  
                Properties: create, query, edit
        outAngle (Queryable[float]?): New value for the angle of the out-tangent.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        outTangentType (Queryable[str]?): Specify the out-tangent type.  Valid values are  
                "spline," "linear," "fast," "slow," "flat," "step," "stepnext,"  
                "fixed," "clamped," "plateau" and "auto", "autoease", "automix", and  
                "autocustom".  
                Returns a string[] when queried.  
                Properties: create, query, edit
        outWeight (Queryable[float]?): New value for the weight of the out-tangent.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        ox (Queryable[float]?): New value for the x-component of the out-tangent.  
                This is a unit independent representation of the tangent  
                component.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        oy (Queryable[float]?): New value for the y-component of the out-tangent.  
                This is a unit independent representation of the tangent  
                component.  
                Returns a float[] when queried.  
                Properties: create, query, edit
        pluginTangentTypes (Queryable[str]?): Returns a list of the plug-in tangent types that have been loaded.  
                Return type is a string array.  
                Properties: query
        relative (bool?): Changes to tangent positions are relative to the  
                current position.  
                Properties: create, edit
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        stepAttributes (bool?): The setKeyframe command will automatically set  
                tangents for boolean and enumerated attributes to step.  This  
                flag mirrors this behavior for the keyTangent command.  When  
                set to false, tangents for these attributes will not be  
                edited.  When set to true (the default) tangents for these  
                attributes will be edited.  
                Properties: create, edit
        time (Multiuse[NullableRange[float]]?): time uniquely representing a key (or key  
                range) on a time-based animCurve. See the code  
                examples below on how to format for a single  
                frame or frame ranges.  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        unify (bool?): Unify a tangent so in and out tangents are equal and move together.  
                Properties: create, edit
        weightLock (bool?): Lock the weight of a tangent so it is fixed.  
                Returns an int[] when queried.  
                Note: weightLock is only obeyed within the graph editor.  It  
                is not obeyed when -inWeight/-outWeight are issued from a command.  
                Properties: create, query, edit
        weightedTangents (bool?): Specify whether or not the tangents on  
                the animCurve are weighted  
                Note: switching a curve from weightedTangents  
                true to false and back to true again will not  
                preserve fixed tangents properly. Use undo instead.  
                Properties: create, query, edit

    Returns:
        int: Number of curves on which tangents were modified.

    Example:
    """

