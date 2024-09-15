from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filterKeyReducerCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., apply: bool = ..., endTime: Queryable[int] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., keySync: bool = ..., name: str = ..., precision: Queryable[float] = ..., precisionMode: Queryable[int] = ..., preserveKeyTangent: Queryable[Multiuse[str]] = ..., selectedKeys: bool = ..., startTime: Queryable[int] = ...) -> Union[str, int, bool, float, Multiuse[str]]:
    """Creates/edits a KeyReducer filter context. This context can be used
    to interactively preview/edit the KeyReducer filter on a set of
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
        keySync (bool?): When true, a secondary filter pass is applied that adds a key to sibling  
                curves (X,Y,Z) for each key that is encountered.  
                Properties: query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        precision (Queryable[float]?): Defines the precision parameter.  
              
                For the Key Reducer filter, this parameter specifies the error limit between the  
                source and output curves. Greater values reduce precision. Lower values increase  
                precision.  
                Properties: query, edit
        precisionMode (Queryable[int]?): Specifies the precision mode for the Key Reducer filter. Avaiable  
                modes are:  
              
                0. Absolute value.  
                1. Percentage  
              
                Default is 1 (percentage mode).  
                Properties: query, edit
        preserveKeyTangent (Queryable[Multiuse[str]]?): When specified, keys whose in or out tangent type match the  
                specified type are preserved.  
              
                Supported tangent types:  
              
                fixed  
                linear  
                flat  
                smooth  
                step  
                clamped  
                plateau  
                stepnext  
                auto  
                Properties: query, edit, multiuse
        selectedKeys (bool?): If true, sets the filter to apply to the selected keys. Otherwise,  
                the filter applies to the specified time range. Default is on.  
                Properties: query, edit
        startTime (Queryable[int]?): Specifies the start time portion of the time range for this filter.  
                This time range is used when selectedKeys is false.  
                Properties: query, edit

    Returns:
        str: Context name

    Example:
    """

