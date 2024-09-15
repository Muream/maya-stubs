from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def retimeKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., moveByFrame: int = ..., name: str = ..., snapOnFrame: bool = ...) -> Union[bool, str]:
    """This command creates a context which may be used to scale keyframes
    within the graph editor using the retime tool.
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
        moveByFrame (int?): Move the selected retime bar by the specified number of frames  
                Properties: edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        snapOnFrame (bool?): When set, the retime markers will snap on frames as they are moved.  
                Properties: query, edit

    Returns:
        bool: Query value from the snapOnFame setting.

    Example:
    """

