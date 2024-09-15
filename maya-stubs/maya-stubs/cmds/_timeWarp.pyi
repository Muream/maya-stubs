from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeWarp(*args: str, edit: bool = ..., query: bool = ..., deleteFrame: int = ..., frame: Queryable[Multiuse[float]] = ..., g: bool = ..., interpType: Queryable[Tuple[int, str]] = ..., moveFrame: Queryable[Tuple[int, float]] = ...) -> Union[str, Multiuse[float], bool, Tuple[int, str], Tuple[int, float]]:
    """This command is used to create a time warp input to a set of animation curves.fcurve, animCurve, animation, timing
    Args:
        deleteFrame (int?): The flag value indicates the 0. based index of the warp frame to delete. This flag can only be used in edit mode.  
                Properties: edit
        frame (Queryable[Multiuse[float]]?): In create and edit mode, this flag can be used to specify warp frames added to the warp operation.  
                In query mode, this flag returns a list of the frame values where warping occurs. The moveFrame flag command can be used to query the associated warped values.  
                Properties: create, query, edit, multiuse
        g (bool?): In create mode, creates a global time warp node which impacts every animated object in the scene. In query mode, returns the global time warp node. Note: only one global time warp can exist in the scene.  
                Properties: create, query, edit
        interpType (Queryable[Tuple[int, str]]?): This flag can be used to set the interpolation type for a given span. Valid interpolation types are linear, easeIn and easeOut. When queried, it returns a string array of the interpolation types for the specified time warp.  
                Properties: create, query, edit
        moveFrame (Queryable[Tuple[int, float]]?): This flag can be used to move a singular warp frame. The first value specified indicates the 0. based index of the warp frame to move. The second value indicates the new warp frame value. This flag can only be used in edit and query mode. When queried, it returns an array of the warped frame values.  
                Properties: query, edit

    Returns:
        str: timeWarp name

    Example:
    """

