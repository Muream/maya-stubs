from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def matrixUtil(arg0: float = ..., arg1: float = ..., arg2: float = ..., arg3: float = ..., arg4: float = ..., arg5: float = ..., arg6: float = ..., arg7: float = ..., arg8: float = ..., arg9: float = ..., arg10: float = ..., arg11: float = ..., arg12: float = ..., arg13: float = ..., arg14: float = ..., arg15: float = ..., /, *, edit: bool = ..., query: bool = ..., inverse: bool = ..., quaternion: Queryable[Tuple[float, float, float, float]] = ..., relative: bool = ..., rotation: Queryable[Tuple[float, float, float]] = ..., scale: Queryable[Tuple[float, float, float]] = ..., shear: Queryable[Tuple[float, float, float]] = ..., translation: Queryable[Tuple[float, float, float]] = ..., transpose: bool = ...) -> Union[str, bool, Tuple[float, float, float, float], Tuple[float, float, float]]:
    """Command to deal with matrix, composition and decompositionmatrix, decomposeMatrix, decomposeMatrix
    Args:
        inverse (bool?): Compose or query will return the inversed matrix.  
                Properties: create, query, edit
        quaternion (Queryable[Tuple[float, float, float, float]]?): Compose, edit or query a matrix using specified quaternion values as rotation components.  
                Properties: create, query, edit
        relative (bool?): Add translation, rotation, scale or shear, instead of seting it as absolute.  
                Properties: create, query, edit
        rotation (Queryable[Tuple[float, float, float]]?): Compose, edit or query a matrix using specified values as rotation components.  
                Properties: create, query, edit
        scale (Queryable[Tuple[float, float, float]]?): Compose, edit or query a matrix using specified values as scale components.  
                Properties: create, query, edit
        shear (Queryable[Tuple[float, float, float]]?): Compose, edit or query a matrix using specified values as shear components.  
                Properties: create, query, edit
        translation (Queryable[Tuple[float, float, float]]?): Compose a matrix using specified values as translation components.  
                Properties: create, query, edit
        transpose (bool?): Compose or query will return the transposed matrix.  
                Properties: create, query, edit

    Returns:
        str: Command result

    Example:
    """

