from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filterGaussianCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., apply: bool = ..., endTime: Queryable[int] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., sampleCount: Queryable[int] = ..., selectedKeys: bool = ..., startTime: Queryable[int] = ..., useQuaternion: bool = ..., width: Queryable[int] = ...) -> Union[str, int, bool]:
    """Creates a smooth (gaussian) filter context. This context can ben used
    to interactively preview/edit the smooth (gaussian) filter on a set of
    animation curves.
    Args:
        apply (bool?): When specified, finalizes the current context state  
                and records the command for the operation. This is equivalent  
                to completing the tool action without exiting the current  
                tool context.  
                Properties: edit
        endTime (Queryable[int]?): Specifies the end time portion of the time range for this filter.  
                This time range is used when selectedKeys is false.  
                Properties: query, edit
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
        sampleCount (Queryable[int]?): This parameter specifies the number of neighbor will be sampled.  
                Properties: query, edit
        selectedKeys (bool?): If true, sets the filter to apply to the selected keys. Otherwise,  
                the filter applies to the specified time range. Default is on.  
                Properties: query, edit
        startTime (Queryable[int]?): Specifies the start time portion of the time range for this filter.  
                This time range is used when selectedKeys is false.  
                Properties: query, edit
        useQuaternion (bool?): When this is enabled, the filter will first convert the curves  
                (rotation channel curves, 3 sibling requires at the same time)  
                from Euler space to quaternions. Then apply the gaussian filter  
                on it. Convert it back from Quaternions back to Euler space eventually.  
                Properties: query, edit
        width (Queryable[int]?): This parameter specifies the width of the gaussian kernel shape.  
                Wider width will  
                Properties: query, edit

    Returns:
        str: Context name

    Example:
    """

