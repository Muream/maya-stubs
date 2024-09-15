from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorComposition(*args: Any, edit: bool = ..., query: bool = ..., active: bool = ..., allCompositions: bool = ..., createTrack: bool = ..., delete: bool = ..., duplicateFrom: str = ..., rename: Tuple[str, str] = ..., tracksNode: bool = ...) -> Union[str, bool]:
    """Commands related to composition management inside Time Editor.timeEditor, nle
    Args:
        active (bool?): Query or edit the active composition.  
                Properties: query, edit
        allCompositions (bool?): Return all compositions inside Time Editor.  
                Properties: query
        createTrack (bool?): Create a default track when creating a new composition.  
                Properties: create
        delete (bool?): Delete the composition.  
                Properties: query, edit
        duplicateFrom (str?): Duplicate the composition.  
                Properties: create
        rename (Tuple[str, str]?): Rename the composition of the first name to the second name.  
                Properties: edit
        tracksNode (bool?): Query the tracks node of a composition.  
                Properties: query

    Returns:
        str: Return values currently not documented.

    Example:
    """

