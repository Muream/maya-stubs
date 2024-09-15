from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyColorPerVertex(*args: str, edit: bool = ..., query: bool = ..., alpha: Queryable[float] = ..., clamped: bool = ..., colorB: Queryable[float] = ..., colorDisplayOption: bool = ..., colorG: Queryable[float] = ..., colorR: Queryable[float] = ..., colorRGB: Queryable[Tuple[float, float, float]] = ..., notUndoable: bool = ..., relative: bool = ..., remove: bool = ..., representation: Queryable[int] = ...) -> Union[bool, float, Tuple[float, float, float], int]:
    """Command associates color(rgb and alpha) with vertices on polygonal objects.
    When used with the query flag, it returns the color associated with the
    specified components.poly, color, colorPerVertex, vertexColor
    Args:
        alpha (Queryable[float]?): Specifies the alpha channel of color  
                Properties: create, query, edit
        clamped (bool?): This flag specifies if the color set will truncate any value that is  
                outside 0 to 1 range.  
                Properties: create, query, edit
        colorB (Queryable[float]?): Specifies the B channel of color  
                Properties: create, query, edit
        colorDisplayOption (bool?): Change the display options on the mesh to display the vertex colors.  
                Properties: create, query, edit
        colorG (Queryable[float]?): Specifies the G channel of color  
                Properties: create, query, edit
        colorR (Queryable[float]?): Specifies the R channel of color  
                Properties: create, query, edit
        colorRGB (Queryable[Tuple[float, float, float]]?): Specifies the RGB channels of color  
                Properties: create, query, edit
        notUndoable (bool?): Execute the command, but without having the command  
                be undoable. This option will greatly improve performance  
                for large numbers of object. This will make the command  
                not undoable regardless of whether undo has been  
                enabled or not.  
                Properties: create, query, edit
        relative (bool?): When used, the color values specified are added relative to the current values.  
                Properties: create, query, edit
        remove (bool?): When used, the color values are removed from the selected or specified objects  
                or components. This option only supports meshes with no construction history, or meshes  
                whose construction history includes a recent polyColorPerVertexNode. For meshes whose construction  
                history includes a polgon operation the polyColorPerVertexNode, consider using the polyColorDel command instead  
                Properties: create, query, edit
        representation (Queryable[int]?): This flag corresponds to the color channels to used, for example  
                A(alpha only), RGB, and RGBA.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

