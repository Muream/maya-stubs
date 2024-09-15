from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewPlace(arg0: str = ..., /, *, animate: bool = ..., eyePoint: Tuple[float, float, float] = ..., fieldOfView: float = ..., lookAt: Tuple[float, float, float] = ..., ortho: bool = ..., perspective: bool = ..., upDirection: Tuple[float, float, float] = ..., viewDirection: Tuple[float, float, float] = ...) -> bool:
    """This command positions the camera as specified. The lookAt and
    viewDirection flags are mutually exclusive, as are the ortho and
    perspective flags. If this command switches a camera from ortho to
    perspective or the other way around without specifying a new field
    of view, then one is calculated based on a heuristic involving the
    selected objects.If the camera is not specified on the command line, the command
    will check to see if there is a camera on the active list.The user should be aware that some positions will be
    unattainable. For example, using a new camera located at the
    origin and specifying a lookAt of [0 0 -5] and an up of [1 1
    1]. In these cases, the camera will always aim at the lookAt, and
    the new up direction will be determined by transforming the
    specified up into camera space and then projecting this vector
    onto a plane defined by the camera's up and right vectors. Using
    the example above, the new up vector will be [1 1 0].
    Args:
        animate (bool?): If set to true then animate the camera transition from current  
                position to the final one.  
                Properties: create
        eyePoint (Tuple[float, float, float]?): The new eye point in world coordinates.  
                Properties: create
        fieldOfView (float?): The new field of view (in degrees, for perspective cameras,  
                and in world distance for ortho cameras)  
                Properties: create
        lookAt (Tuple[float, float, float]?): The new look-at point in world coordinates.  
                Properties: create
        ortho (bool?): Sets the camera to be orthgraphic.  
                Properties: create
        perspective (bool?): Sets the camera to be perspective.  
                Properties: create
        upDirection (Tuple[float, float, float]?): The new up direction vector.  
                Properties: create
        viewDirection (Tuple[float, float, float]?): The new view direction vector.  
                Properties: create

    Returns:
        bool:

    Example:
    """

