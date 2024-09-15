from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewSet(arg0: str = ..., /, *, query: bool = ..., animate: bool = ..., back: bool = ..., bottom: bool = ..., fit: bool = ..., fitFactor: float = ..., front: bool = ..., home: bool = ..., keepRenderSettings: bool = ..., leftSide: bool = ..., namespace: str = ..., nextView: bool = ..., persp: bool = ..., previousView: bool = ..., rightSide: bool = ..., side: bool = ..., top: bool = ..., viewNegativeX: bool = ..., viewNegativeY: bool = ..., viewNegativeZ: bool = ..., viewX: bool = ..., viewY: bool = ..., viewZ: bool = ...) -> bool:
    """This command positions the camera to one of the pre-defined
    positions. If the fit flag is set in conjunction with persp, top,
    side, or front, the view is "fit" based on the list of selected
    objects (if there are any) or on all the objects if nothing is
    selected. Notice that the fit flag cannot be set in conjunction with
    view along axis commands like viewX. If a camera is not specified,
    the camera in the active view will be used. If no flag is specified,
    the camera is set to the home position.
    Args:
        animate (bool?): Specifies that the transition between camera positions  
                should be animated.  
                Properties: create
        back (bool?): Moves the camera to the back position.  
                Properties: create
        bottom (bool?): Moves the camera to the bottom position.  
                Properties: create
        fit (bool?): Apply a viewFit after positioning camera to persp, top, side,  
                or front.  
                Properties: create, query
        fitFactor (float?): Specifies how much of the view should be filled with the "fitted" items  
                Properties: create
        front (bool?): Moves the camera to the front position.  
                Properties: create
        home (bool?): Executes the camera's home attribute command. Before the  
                string is executed, all occurances of "%camera" will be  
                replaced by the camera's name. Use the camera command to set a  
                camera's home command.  
                Properties: create
        keepRenderSettings (bool?): Retain the 'renderable' flag vaue on the view. Especially important if it switches from  
                perspective to orthographic and then back again.  
                Properties: create, query
        leftSide (bool?): Moves the camera to the left side position.  
                Properties: create
        namespace (str?): Specifies a namespace that should be excluded. All objects  
                in the specified namespace will be excluded from the fit  
                process.  
                Properties: create
        nextView (bool?): Moves the camera to the next position.  
                Properties: create, query
        persp (bool?): Moves the camera to the persp position.  
                Properties: create
        previousView (bool?): Moves the camera to the previous position.  
                Properties: create, query
        rightSide (bool?): Moves the camera to the right side position.  
                Properties: create
        side (bool?): Moves the camera to the (right) side position (deprecated).  
                Properties: create
        top (bool?): Moves the camera to the top position.  
                Properties: create
        viewNegativeX (bool?): Moves the camera to view along negative X axis.  
                Properties: create
        viewNegativeY (bool?): Moves the camera to view along negative Y axis.  
                Properties: create
        viewNegativeZ (bool?): Moves the camera to view along negative Z axis.  
                Properties: create
        viewX (bool?): Moves the camera to view along X axis.  
                Properties: create
        viewY (bool?): Moves the camera to view along Y axis.  
                Properties: create
        viewZ (bool?): Moves the camera to view along Z axis.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

