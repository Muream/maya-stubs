from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pose(*args: str, edit: bool = ..., query: bool = ..., allPoses: bool = ..., apply: bool = ..., name: Queryable[str] = ...) -> Union[str, bool]:
    """This command is used to create character poses.character, clip, animation, pose
    Args:
        allPoses (bool?): This flag is used to query all the poses in the scene.  
                Properties: query
        apply (bool?): This flag is used in conjunction with the name flag to specify a pose should be applied to the character.  
                Properties: create
        name (Queryable[str]?): In create mode, specify the pose name. In query mode, return a list of all the poses for the character. In apply mode, specify the pose to be applied.  
                Properties: create, query

    Returns:
        str: Pose name

    Example:
    """

