from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def autoKeyframe(*, edit: bool = ..., query: bool = ..., addAttr: str = ..., characterOption: Queryable[str] = ..., listAttr: bool = ..., noReset: bool = ..., state: bool = ...) -> Union[int, str, bool]:
    """With no flags, this command will set keyframes on all
    attributes that have been modified since an "autoKeyframe -state on"
    command was issued.  To stop keeping track of modified attributes,
    use "autoKeyframe -state off"autoKeyframe does not create new animation curves.  An attribute
    must have already been keyframed (with the setKeyframe command)
    for autoKeyframe to  add new keyframes for modified attributes.You can also query the current state of autoKeyframing
    with "autoKeyframe -query -state".
    Args:
        addAttr (str?): Add to the list of plugs (node.attribute) that autoKeyframe is currently  
                considering for auto keying.  This list is transient and short-lived, and  
                is reset as soon as autoKeyframe sets the keyframe or decides that no  
                keyframe is to be set, on completion of the next set attribute.  
                Properties: edit
        characterOption (Queryable[str]?): Valid options are: "standard", "all". Dictates whether  
                when auto-keying characters the auto-key works as usual or whether  
                it keys all of the character attributes. Default is "standard".  
                Properties: create, query, edit
        listAttr (bool?): Returns the list of plugs (node.attribute) that autoKeyframe is currently  
                considering for auto keying.  This list is transient and short-lived, and  
                is reset as soon as autoKeyframe sets the keyframe or decides that no  
                keyframe is to be set, on completion of the next set attribute.  
                Properties: query
        noReset (bool?): Must be used in conjunction with the state/st flag.  
                When noReset/nr is specified, the list of plugs to be autokeyed  
                is not cleared when the state changes  
                Properties: create, edit
        state (bool?): turns on/off remembering of modified attributes  
                Properties: create, query, edit

    Returns:
        int: Number of keyframes set.

    Example:
    """

