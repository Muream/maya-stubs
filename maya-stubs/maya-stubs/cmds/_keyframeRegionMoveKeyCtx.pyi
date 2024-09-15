from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def keyframeRegionMoveKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., option: Queryable[str] = ...) -> str:
    """This command creates a context which may be used to move keyframes
    within the keyframe region of the dope sheet editor
    Args:
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        option (Queryable[str]?): Valid values are "move," "insert," "over," and  
                "segmentOver". Specifies the keyframe -option to use.  When you  
                "move" a key, the key will not cross over  
                (in time) any keys before or after it. When you "insert" a key,  
                all keys before or after (depending upon the -timeChange value)  
                will be moved an equivalent amount. When you "over" a key, the key  
                is allowed to move to any time (as long as a key is not there already).  
                When you "segmentOver" a set of keys (this option only has a  
                noticeable effect when more than one key is being moved) the first  
                key (in time) and last key define a segment (unless you specify a  
                time range). That segment is then allowed to move over other keys,  
                and keys will be moved to make room for the segment.  
                Properties: create, query, edit

    Returns:
        str: Context name

    Example:
    """

