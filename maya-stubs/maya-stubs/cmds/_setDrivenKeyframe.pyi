from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setDrivenKeyframe(*args: str, edit: bool = ..., query: bool = ..., attribute: Multiuse[str] = ..., controlPoints: bool = ..., count: bool = ..., currentDriver: Queryable[str] = ..., driven: bool = ..., driver: bool = ..., driverValue: Multiuse[float] = ..., hierarchy: str = ..., inTangentType: str = ..., insert: bool = ..., insertBlend: bool = ..., outTangentType: str = ..., shape: bool = ..., value: float = ...) -> Union[int, bool, str]:
    """This command sets a driven keyframe.  A driven keyframe is similar
    to a regular keyframe. However, while a standard keyframe always has
    an x-axis of time in the graph editor, for a drivenkeyframe the
    user may choose any attribute as the x-axis of the graph editor.For example, you can keyframe the emission of a faucet so that
    so that it emits whenever the faucet handle is rotated around y.
    The faucet emission in this example is called the driven attribute.
    The handle rotation is called the driver. Once you have used
    setDrivenKeyframe to set up the relationship between the emission
    and the rotation, you can go to the graph editor and modify the
    relationship between the attributes just as you would modify the
    animation curve on any keyframed object.In the case of an attribute driven by a single driver, the
    dependency graph is connected like this:driver attribute ---> animCurve ---> driven attributeYou can set driven keyframes with more than a single driver.
    The effects of the multiple drivers are combined together by
    a blend node.
    Args:
        attribute (Multiuse[str]?): Attribute name to set keyframes on.  
                Properties: create, multiuse
        controlPoints (bool?): Explicitly specify whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  
                Properties: create
        count (bool?): Returns the count of driven/drivers attributes for the selected item  
                instead of the names  
                Properties: query
        currentDriver (Queryable[str]?): Set the driver to be used for the current driven keyframe to the  
                attribute passed as an argument.  
                Properties: create, query
        driven (bool?): Returns list of driven attributes for the selected item.  
                Properties: query
        driver (bool?): Returns list of available drivers for the attribute.  
                Properties: query
        driverValue (Multiuse[float]?): Value of the driver to use for this keyframe.  
                Default value is the current value.  
                Properties: create, multiuse
        hierarchy (str?): Controls the objects this command acts on, relative to the specified  
                (or active) target objects.  
                Valid values are "above," "below," "both," and "none."  
                Default is "hierarchy -query"  
                Properties: create
        inTangentType (str?): The in tangent type for keyframes set by this command.  
                Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext"  
                Default is "keyTangent -q -g -inTangentType"  
                Properties: create
        insert (bool?): Insert keys at the given time(s) and preserve  
                the shape of the animation curve(s). Note: the tangent  
                type on inserted keys will be fixed so that the  
                curve shape can be preserved.  
                Properties: create
        insertBlend (bool?): If true, a pairBlend node will be inserted for channels that have  
                nodes other than animCurves driving them, so that such channels can  
                have blended animation. If false, these channels will not have keys  
                inserted. If the flag is not specified, the blend will be inserted based  
                on the global preference for blending animation.  
                Properties: create
        outTangentType (str?): The out tangent type for keyframes set by this command.  
                Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext".  
                Default is "keyTangent -q -g -outTangentType"  
                Properties: create
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true  
                Properties: create
        value (float?): Value to set the keyframe at. Default is the current value.  
                Properties: create

    Returns:
        int: Number of keyframes set.

    Example:
    """

