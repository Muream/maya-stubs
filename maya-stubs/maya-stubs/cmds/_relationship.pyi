from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def relationship(arg0: str = ..., arg1: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., b: bool = ..., relationshipData: Queryable[Multiuse[str]] = ...) -> Union[bool, Multiuse[str]]:
    """This is primarily for use with file IO. Rather than write out the specific attributes/connections required to maintain a relationship, a description of the related nodes/plugs is written instead. The relationship must have an owner node, and have a specific type. During file read, maya will make the connections and/or set the data necessary to represent the realtionship in the dependency graph.relationship, lightLinker
    Args:
        b (bool?): Break the specified relationship instead of creating it  
                Properties: create, query, edit
        relationshipData (Queryable[Multiuse[str]]?): Provide relationship data to be used when creating the relationship.  
                Properties: create, query, edit, multiuse

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

