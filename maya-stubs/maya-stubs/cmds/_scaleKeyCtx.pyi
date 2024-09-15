from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scaleKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., scaleSpecifiedKeys: bool = ..., type: Queryable[str] = ...) -> Union[str, bool]:
    """This command creates a context which may be used to scale keyframes
    within the graph editor
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
        scaleSpecifiedKeys (bool?): Determines if only the specified keys should be scaled. If false,  
                the non-selected keys will be adjusted during the scale. The default  
                is true.  
                Properties: query, edit
        type (Queryable[str]?): rect | manip  
                Specifies the type of scale manipulator to use  
                (Note: "rect" is a manipulator style context, and "manip"  
                is a gestural style context)  
                Properties: query, edit

    Returns:
        str: Scale type, if the type flag was queried
        bool: Whether specified keys should be scaled, if the scaleSpecifiedKeys flag was queried

    Example:
    """

