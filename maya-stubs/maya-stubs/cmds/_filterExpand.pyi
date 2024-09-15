from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filterExpand(*args: str, expand: bool = ..., fullPath: bool = ..., selectionMask: Multiuse[int] = ..., symActive: bool = ..., symNegative: bool = ..., symPositive: bool = ..., symSeam: bool = ...) -> List[str]:
    """Based on selected components (or components specified on the command line),
    the command filters and/or expands the list given
    the options.
    Returns a string array containing all matching selection items.
    Selection masks are as follows:
    Args:
        expand (bool?): Each item is a single entity if this is true.  Default is true.  
                Properties: create
        fullPath (bool?): If this is true and the selection item is a DAG object, return its  
                full selection path, instead of the name of the object only when  
                this value is false.  Default is false.  
                Properties: create
        selectionMask (Multiuse[int]?): Specify the selection mask  
                Properties: create, multiuse
        symActive (bool?): If symmetry is enabled only return the components on the active symmetry  
                side of the object. This flag has no effect if symmetry is not active.  
                Properties: create
        symNegative (bool?): If symmetry is enabled only return the components on the negative  
                side of the object relative to the current symmetry plane. This flag has  
                no effect if symmetry is not active.  
                Properties: create
        symPositive (bool?): If symmetry is enabled only return the components on the positive  
                side of the object relative to the current symmetry plane. This flag has  
                no effect if symmetry is not active.  
                Properties: create
        symSeam (bool?): If symmetry is enabled only return the components that lie equally on both sides  
                of the object relative to the current symmetry plane. This flag has  
                no effect if symmetry is not active.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

