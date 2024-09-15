from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def convertTessellation(*args: str, allCameras: bool = ..., camera: str = ...) -> bool:
    """Command to translate the basic tessellation attributes to advanced.
    If a camera flag is specified the translation will be based on the distance
    the surface is from the camera. The closer the surface is to the camera the
    more triangles there will be in the tessellation. If the "-allCameras" flags
    is specified, the renderable camera closest to the surface will be used to
    set the tessellation. The camera tessellation estimate is also dependent on
    the current render resolution; a higher resolution the result in a more
    finely tessellated surface.
    Multiple NURB surfaces may be specified on the command line, or if no
    command arguments are specified the surfaces on the active list will be
    used.
    This command operates by calculating the chord height such that smooth
    tessellation is achieved when the surface is rendered.  The advanced
    tessellation setting will be enabled on each surface specified, the
    primary tessellation parameters will be set, and chord height will be
    used as the secondary criteria.tessellation
    Args:
        allCameras (bool?): Specifies that all renderable cameras should be used in calculating  
                    the screen based tessellation.  
                Properties: create
        camera (str?): Specifies the camera which should be used in calculating the screen  
                    based tessellation.  
                Properties: create

    Returns:
        bool: Success or Failure.

    Example:
    """

