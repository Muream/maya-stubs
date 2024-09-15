from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsUVSet(*args: str, edit: bool = ..., query: bool = ..., create: bool = ..., useExplicit: bool = ...) -> bool:
    """Allows user to toggle between implicit and explicit UVs on a NURBS object. Also
    provides a facility to create, delete, rename and set the current explicit UVSet.
    An implicit UVSet is non-editable. It uses the parametric make-up of the NURBS object
    to determine the location of UVs (isoparm intersections). NURBS objects also support
    explicit UVSets which are similar to the UVs of a polygonal object. UVs are created
    at the knots (isoparm intersections) of the object and are fully editable. In order
    to access UV editing capabilities on a NURBS object an explicit UVSet must be created
    and set as the current UVSet.nurbs, uvSet, currentUVSet, renameUVSet, deleteUVSet, copyUVSet, createUVSet
    Args:
        create (bool?): Creates an explicit UV set on the specified surface. If the surface already has an  
                explicit UV set this flag will do nothing. Use the -ue/useExplicit flag to set/unset  
                the explicit UV set as the current UV set.  
                Properties: create, query, edit
        useExplicit (bool?): Toggles the usage of explicit/implicit UVs. When true, explicit UVs will be used,  
                otherwise the object will use implicit UVs.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

