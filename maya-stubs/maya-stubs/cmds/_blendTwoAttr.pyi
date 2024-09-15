from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def blendTwoAttr(*args: str, edit: bool = ..., query: bool = ..., attribute: Multiuse[str] = ..., attribute0: Queryable[str] = ..., attribute1: Queryable[str] = ..., blender: Queryable[str] = ..., controlPoints: bool = ..., driver: Queryable[int] = ..., name: Queryable[str] = ..., shape: bool = ..., time: NullableRange[float] = ...) -> Union[List[str], str, int]:
    """A blendTwoAttr nodes takes two inputs, and blends the values of the inputs
    from one to the other, into an output value. The blending of the two
    inputs uses a blending function, and the following formula:The blendTwoAttr command can be used to blend the animation of an
    object to transition smoothly between the animation of two other
    objects.When the blendTwoAttr command is issued, it creates a blendTwoAttr
    node on the specified attributes, and reconnects whatever was previously
    connected to the attributes to the new blend nodes. You may also
    specify which two attributes should be used to blend together.The driver is used when you want to keyframe an object after it is
    being animated by a blend node. The current driver index specifies
    which of the two blended attributes should be keyframed.
    Args:
        attribute (Multiuse[str]?): A list of attributes for the selected nodes for which a  
                blendTwoAttr node will be created.  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        attribute0 (Queryable[str]?): The attribute that should be connected to the first input  
                of the new blendTwoAttr node.  
                When queried, it returns a string.  
                Properties: create, query, edit
        attribute1 (Queryable[str]?): The attribute that should be connected to the second input  
                of the new blendTwoAttr node.  
                When queried, it returns a string.  
                Properties: create, query, edit
        blender (Queryable[str]?): The blender attribute. This is the attribute that will be  
                connected to the newly created blendTwoAttr node(s) blender attribute.  
                This attribute controls how much of each of the two attributes  
                to use in the blend. If this flag is not specified, a new  
                animation curve is created whose value goes from 1 to 0  
                throughout the time range specified by the -t flag. If -t is not  
                specified, an abrupt change from the value of the first to the  
                value of the second attribute will occur at the current time  
                when this command is issued.  
                Properties: create, query, edit
        controlPoints (bool?): Explicitly specify whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  
                Properties: create
        driver (Queryable[int]?): The index of the driver attribute for this blend node (0 or 1)  
                When queried, it returns an integer.  
                Properties: create, query, edit
        name (Queryable[str]?): name for the new blend node(s)  
                Properties: create, query
        shape (bool?): Consider all attributes of shapes below transforms as well,  
                except "controlPoints". Default: true  
                Properties: create
        time (NullableRange[float]?): The time range between which the blending between the 2 attributes  
                should occur. If a single time is specified, then the blend will  
                cause an abrupt change from the first to the second attribute at  
                that time.  If a range is specified, a smooth blending will occur  
                over that time range. The default is to make a sudden transition  
                at the current time.  
                Properties: create

    Returns:
        List[str]: The names of the blendTwoAttr dependency nodes that were created.

    Example:
    """

