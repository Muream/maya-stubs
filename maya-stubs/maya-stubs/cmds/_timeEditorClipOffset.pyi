from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorClipOffset(*args: Any, edit: bool = ..., query: bool = ..., applyToAllRoots: bool = ..., clipId: Multiuse[int] = ..., matchClipId: int = ..., matchDstTime: int = ..., matchObj: str = ..., matchOffsetRot: bool = ..., matchOffsetTrans: bool = ..., matchPath: str = ..., matchRotOp: int = ..., matchSrcTime: int = ..., matchTransOp: int = ..., offsetTransform: bool = ..., path: Multiuse[str] = ..., resetMatch: int = ..., resetMatchPath: str = ..., rootObj: Queryable[Multiuse[str]] = ..., upVectorX: float = ..., upVectorY: float = ..., upVectorZ: float = ...) -> Union[bool, Multiuse[str]]:
    """This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.timeEditor, nle
    Args:
        applyToAllRoots (bool?): Apply root offsets to all roots in the population. However, if the root objects are specified by rootObj flag, this flag will be ignored.  
                Properties: create
        clipId (Multiuse[int]?): ID of the clip to be edited.  
                Properties: create, edit, multiuse
        matchClipId (int?): Specify the ID of a clip to match.  
                Properties: create
        matchDstTime (int?): Specify the time on target clip.  
                Properties: create
        matchObj (str?): Specify the object to match.  
                Properties: create
        matchOffsetRot (bool?): Get the rotation of the match offset matrix.  
                Properties: query
        matchOffsetTrans (bool?): Get the translation of the match offset matrix.  
                Properties: query
        matchPath (str?): Full path of the clip to match. For example: composition1|track1|Group|track2|clip1  
                Properties: create
        matchRotOp (int?): Specify the option for matching rotation.  
              
                0. full - All rotation components are matched  
                1. Y    - Y component is matched  
                2. none - No rotation matching  
                Properties: create
        matchSrcTime (int?): Specify the time on source clip.  
                Properties: create
        matchTransOp (int?): Specify the option for matching translation.  
              
                0. full - All translation components are matched  
                1. XZ   - X and Z components are matched  
                2. none - No translation matching  
                Properties: create
        offsetTransform (bool?): Create/get an offset for the specified clip.  
                Properties: create, query
        path (Multiuse[str]?): Full path of a clip to be edited. For example: composition1|track1|group; composition1|track1|group|track2|clip1.  
                			In query mode, this flag can accept a value.  
                Properties: create, edit, multiuse
        resetMatch (int?): Specify clip ID to remove offset.  
                Properties: create
        resetMatchPath (str?): Specify clip's full path to remove offset. For example: composition1|track1|Group|track2|clip1  
                Properties: create
        rootObj (Queryable[Multiuse[str]]?): Specify the root objects. If specified, this flag will take precedence over applyToAllRoots flag.  
                When used in query mode, returns list of roots defined for the relocator.  
                Properties: create, query, edit, multiuse
        upVectorX (float?): Specify the X coordinate of the up vector.  
                Properties: create
        upVectorY (float?): Specify the Y coordinate of the up vector.  
                Properties: create
        upVectorZ (float?): Specify the Z coordinate of the up vector.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

