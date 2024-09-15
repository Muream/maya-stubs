from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def latticeDeformKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., envelope: Queryable[float] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., latticeColumns: Queryable[int] = ..., latticeRows: Queryable[int] = ..., name: str = ..., scaleLatticePts: bool = ...) -> Union[str, float, int, bool]:
    """This command creates a context which may be used to
    deform key frames with lattice manipulator.  This context
    only works in the graph editor.
    Args:
        envelope (Queryable[float]?): Specifies the influence of the lattice.  
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
        latticeColumns (Queryable[int]?): Specifies the number column points the lattice contains.  
                Properties: query, edit
        latticeRows (Queryable[int]?): Specifies the number of rows the lattice contains.  
                Properties: query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        scaleLatticePts (bool?): Specifies if the selected lattice points should scale  
                around the pick point. If this value is false the  
                the default operation is 'move'  
                Properties: query, edit

    Returns:
        str: Context name

    Example:
    """

