from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bakeClip(*args: str, blend: Tuple[int, int] = ..., clipIndex: Multiuse[int] = ..., keepOriginals: bool = ..., name: str = ...) -> str:
    """This command is used to bake clips and blends into a single clip.character, clip, blend, animation, bake
    Args:
        blend (Tuple[int, int]?): Specify the indices of the clips being blended.  
                Properties: create
        clipIndex (Multiuse[int]?): Specify the index of the clip to bake.  
                Properties: create, multiuse
        keepOriginals (bool?): Keep original clips in the trax editor and place the merged clip into the visor. The default is to schedule the merged clip, and to keep the original clips in the visor.  
                Properties: create
        name (str?): Specify the name of the new clip to create.  
                Properties: create

    Returns:
        str: clip name

    Example:
    """

