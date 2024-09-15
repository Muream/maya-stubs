from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texLatticeDeformContext(*args: Any, edit: bool = ..., query: bool = ..., envelope: Queryable[float] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., latticeColumns: Queryable[int] = ..., latticeRows: Queryable[int] = ..., name: str = ..., showMoveManipulator: bool = ..., snapPixelMode: bool = ..., useBoundingRect: bool = ...) -> Union[int, float, bool, str]:
    """This command creates a context which may be used to
    deform UV maps with lattice manipulator.  This context
    only works in the texture UV editor.
    Args:
        envelope (Queryable[float]?): Specifies the influence of the lattice.  
                Properties: create, query, edit
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
        latticeColumns (Queryable[int]?): Specifies the number column points the lattice contains.  The  
                maximum size lattice is restricted to 8 columns.  
                Properties: create, query, edit
        latticeRows (Queryable[int]?): Specifies the number of rows the lattice contains. The  
                maximum size lattice is restricted to 8 rows.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        showMoveManipulator (bool?): Specifies whether show move manipulator in UV Editor  
                Properties: create, query, edit
        snapPixelMode (bool?): Specifies the influenced uv points should be snapped to a pixel  
                center or corner.  
                Properties: create, query, edit
        useBoundingRect (bool?): When constructing the lattice use the bounding box of the  
                selected UVs for the extents of the lattice.  When this is  
                disabled the extents of the marquee selections are used as the  
                extents for the lattice.  
                Properties: create, query, edit

    Returns:
        int: Number of column divisions, when querying the latticeColumns flag.
        int: Number of row divisions, when querying the latticeRows flag.
        float: Value of the deform envelope, when querying the envelope flag.
        bool: Whether snapping to pixels is on, when querying the snapPixelMode flag.
        bool: Whether the bounding rectangle is to be used for deforemation, when querying the useBoundingRect flag.

    Example:
    """

