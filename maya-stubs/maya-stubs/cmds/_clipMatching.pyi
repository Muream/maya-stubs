from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def clipMatching(*args: str, clipDst: Tuple[str, float] = ..., clipSrc: Tuple[str, float] = ..., matchRotation: int = ..., matchTranslation: int = ...) -> bool:
    """This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.character, clip, animation
    Args:
        clipDst (Tuple[str, float]?): The clip to match so that the source clip can be offsetted correctly.  This flag  
                takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order  
                to have the source clip match at a certain time in the destination clip.  
                Properties: create
        clipSrc (Tuple[str, float]?): The clip to offset so that it aligns with the destination clip.  This flag takes  
                in a clip name and the percentage value ranging from 0.0 to 1.0 in order to  
                have it match at a certain time in the clip.  
                Properties: create
        matchRotation (int?): This flag sets the rotation match type. By default, it is set to not match the  
                rotation.  
                0. None  
                1. Match full rotation  
                2. Match projected rotation on ground plane  
                Properties: create
        matchTranslation (int?): This flag sets the translation match type. By default, it is set to not match  
                the translation.  
                0. None  
                1. Match full translation  
                2. Match projected translation on ground plane  
                Properties: create

    Returns:
        bool:

    Example:
    """

