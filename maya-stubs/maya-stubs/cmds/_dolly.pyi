from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dolly(arg0: str = ..., /, *, absolute: bool = ..., distance: float = ..., dollyTowardsCenter: bool = ..., orthoScale: float = ..., relative: bool = ...) -> bool:
    """The dolly command moves a camera along the viewing direction in
    the world space. The viewing-direction and up-direction of the
    camera are not altered. There are two modes of operation:Relative mode: for a perspective camera, the camera is moved along
    its viewing direction, and the distance of travel is computed with
    respect to the current position of the camera in the world
    space. In relative mode, when the camera is moved, its COI is
    moved along with it, and is kept at the same distance, in front of
    the camera, as before applying the dolly operation. For
    orthographic camera, the viewing width of the camera is changed by
    scaling its ortho width by the new value specified on the command
    line.Absolute mode: for a perspective camera, the camera is moved along
    its viewing direction, to the distance that is computed with
    respect to the current position of the world center of interest
    (COI) of the camera. In the absolute mode, when the camera is
    moved, the COI of the camera is not moved with the camera, but it
    is fixed at its current location in space. For orthographic
    camera, the viewing width of the camera is changed by replacing
    its ortho width with the new value specified on the command
    line. This command may be applied to more than one cameras;
    objects that are not cameras are ignored. When no camera name
    supplied on the command line, this command is applied to all
    currently active cameras.The dolly command can be applied to either a perspective or an
    orthographic camera.
    Args:
        absolute (bool?): This flag modifies the behavior of the distance and orthoScale  
                flags. When used in conjunction with the distance flag, the distance  
                argument specifies how far the camera's eye point should be set from  
                the camera's center of interest. When used with the orthoScale flag,  
                the orthoScale argument specifies the camera's new ortho width.  
                Properties: create
        distance (float?): Unit distance to dolly a perspective camera.  
                Properties: create
        dollyTowardsCenter (bool?): This flag controls whether the dolly is performed towards the  
                center of the view (if true), or towards the point where the user  
                clicks (if false). By default, dollyTowardsCenter is on.  
                Properties: create
        orthoScale (float?): Scale to change the ortho width of an orthographic camera.  
                Properties: create
        relative (bool?): This flag modifies the behavior of the distance and orthoScale  
                flags. When used in conjunction with the distance flag, the camera  
                eye and center of interest are both moved by the amount specified  
                by the distance flag's argument. When used with the orthoScale flag,  
                the orthoScale argument is used multiply the camera's ortho width.By  
                default the relative flag is always on.  
                Properties: create

    Returns:
        bool:

    Example:
    """

