from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setKeyframe(*args: str, edit: bool = ..., query: bool = ..., adjustTangent: bool = ..., animLayer: str = ..., animated: bool = ..., attribute: Multiuse[str] = ..., breakdown: bool = ..., clip: str = ..., controlPoints: bool = ..., dirtyDG: bool = ..., float: Multiuse[float] = ..., hierarchy: str = ..., identity: bool = ..., inTangentType: str = ..., insert: bool = ..., insertBlend: bool = ..., minimizeRotation: bool = ..., noResolve: bool = ..., outTangentType: str = ..., preserveCurveShape: bool = ..., respectKeyable: bool = ..., shape: bool = ..., time: Multiuse[int] = ..., useCurrentLockedWeights: bool = ..., value: float = ...) -> Union[int, bool]:
    """This command creates keyframes for the specified objects,
    or the active objects if none are specified on the command line.The default time for the new keyframes is the current time.
    Override this behavior with the "-t" flag on the command line.The default value for the keyframe is the current value
    of the attribute for which a keyframe is set.  Override
    this behavior with the "-v" flag on the command line.When setting keyframes on animation curves that do not have
    "time" as an input attribute (ie, they are unitless animation curves),
    use "-f/-float" to specify the unitless value at which to set a
    keyframe.The -time and -float flags may be combined in one command.This command sets up Dependency Graph relationships for
    proper evaluation of a given attribute at a given time.
    Args:
        adjustTangent (bool?): Adjsut tangent if insert keys  
                Properties: create
        animLayer (str?): Specifies that the new key should be placed in the specified animation layer.  
                Note that if the objects being keyframed are not already part of the  
                layer, this flag will be ignored.  
                Properties: create
        animated (bool?): Add the keyframe only to the attribute(s) that have already a keyframe on. Default: false  
                Properties: create
        attribute (Multiuse[str]?): Attribute name to set keyframes on.  
                Properties: create, multiuse
        breakdown (bool?): Sets the breakdown state for the key.  Default is false  
                Properties: create, query, edit
        clip (str?): Specifies that the new key should be placed in the specified clip.  
                Note that if the objects being keyframed are not already part of the  
                clip, this flag will be ignored.  
                Properties: create
        controlPoints (bool?): Explicitly specify whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  
                Properties: create
        dirtyDG (bool?): Allow dirty messages to be sent out when a keyframe is set.  
                Properties: create
        float (Multiuse[float]?): Float time at which to set a keyframe on float-based  
                animation curves.  
                Properties: create, multiuse
        hierarchy (str?): Controls the objects this command acts on, relative to the specified  
                (or active) target objects.  
                Valid values are "above," "below," "both," and "none."  
                Default is "hierarchy -query"  
                Properties: create
        identity (bool?): Sets an identity key on an animation layer.  An identity key is one that  
                nullifies the effect of the anim layer.  This flag has effect only when the  
                attribute being keyed is being driven by animation layers.  
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
        minimizeRotation (bool?): For rotations, ensures that the key that is set is a minimum distance  
                away from the previous key.  Default is false  
                Properties: create
        noResolve (bool?): When used with the -value flag, causes the specified value to be set  
                directly onto the animation curve, without attempting to resolve the value  
                across animation layers.  
                Properties: create
        outTangentType (str?): The out tangent type for keyframes set by this command.  
                Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext".  
                Default is "keyTangent -q -g -outTangentType"  
                Properties: create
        preserveCurveShape (bool?): Sets the preserve curve shape when inserting keys.  
                Default value depend on your keySetPreserveCurveShape option.  
                Properties: create
        respectKeyable (bool?): When used with the -attribute flag, prevents the keying of the non keyable attributes.  
                Properties: create
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true  
                Properties: create
        time (Multiuse[int]?): Time at which to set a keyframe on time-based  
                animation curves.  
                Properties: create, multiuse
        useCurrentLockedWeights (bool?): If we are setting a key over an existing key, use that key tangent's locked weight value for the new  
                locked weight value.  Default is false  
                Properties: create
        value (float?): Value at which to set the keyframe. Using the value flag will not  
                cause the keyed attribute to change to the specified value until the  
                scene re-evaluates. Therefore, if you want the attribute to update  
                to the new value immediately, use the setAttr command  
                in addition to setting the key.  
                Properties: create

    Returns:
        int: Number of keyframes set by this command.

    Example:
    """

