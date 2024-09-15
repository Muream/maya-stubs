from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def aliasAttr(*args: str, edit: bool = ..., query: bool = ..., remove: bool = ...) -> List[str]:
    """Allows aliases (alternate names) to be defined for any attribute of
    a specified node. When an attribute is aliased, the alias will be
    used by the system to display information about the attribute.
    The user may, however, freely use either the alias or the original
    name of the attribute. Only a single alias can be specified for an
    attribute so setting an alias on an already-aliased attribute destroys
    the old alias.dg, dependency, graph, alias, attribute, name
    Args:
        remove (bool?): Specifies that aliases listed should be removed (otherwise new aliases  
                are added).  
                Properties: create

    Returns:
        List[str]: in query mode.

    Example:
    """

