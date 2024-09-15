from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewFit(*args: str, allObjects: bool = ..., animate: bool = ..., center: bool = ..., fitClipPlanes: bool = ..., fitFactor: float = ..., namespace: str = ..., noChildren: bool = ...) -> bool:
    """The viewFit command positions the specified camera so its
    point-of-view contains all selected objects other than itself. If
    no objects are selected, everything is fit to the view (excepting
    cameras, lights, and sketching plannes). The fit-factor, if
    specified, determines how much of the view should be filled. If a
    camera is not specified, the camera in the active view will be
    used. After the camera is moved, its center of interest is set to
    the center of the bounding box of the objects.Additionally, a list of objects can be passed as arguments.
    If a camera is specified it must be the first argument. Objects
    passed as arguments to the command will be used instead of the
    selected objects.
    Args:
        allObjects (bool?): Specifies that all objects are to be fit regardless of the  
                active list.  
                Properties: create
        animate (bool?): Specifies that the transition between camera positions  
                should be animated.  
                Properties: create
        center (bool?): Specifies that the camera moves to the center of the  
                selected object, but does not move the camera closer.  
                Properties: create
        fitClipPlanes (bool?): Fit orthographic clipping planes in order to contain selection bounding box in the view frustum  
                Properties: create
        fitFactor (float?): Specifies how much of the view should be filled with the  
                "fitted" items.  
                Properties: create
        namespace (str?): Specifies a namespace that should be excluded. All objects  
                in the specified namespace will be excluded from the fit  
                process.  
                Properties: create
        noChildren (bool?): Specifies that the children of fitted objects should be ignored when determining  
                the fit.  
                Properties: create

    Returns:
        bool:

    Example:
    """

