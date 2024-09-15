from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgfilter(*args: Any, attribute: str = ..., list: bool = ..., logicalAnd: Tuple[str, str] = ..., logicalNot: str = ..., logicalOr: Tuple[str, str] = ..., name: str = ..., node: str = ..., nodeType: str = ..., plug: str = ...) -> Union[str, List[str], bool]:
    """Thecommand is used to define Dependency Graph filters
    that select DG objects based on certain criteria.  The command itself
    can be used to filter objects or it can be attached to aobject to selectively filter what output is traced.
    If objects are specified then apply the filter to those objects and
    return a boolean indicating whether they passed or not, otherwise
    return the name of the filter.  An invalid filter will pass all
    objects.  For multiple objects the return value is the logical
    "AND" of all object's return values.dg, dependency, graph, alias, attribute, name
    Args:
        attribute (str?): Select objects whose attribute names match the pattern.  
                Properties: create
        list (bool?): List the available filters.  If used in conjunction with the -name  
                flag it will show a description of what the filter is.  
                Properties: create
        logicalAnd (Tuple[str, str]?): Logical AND of two filters.  
                Properties: create
        logicalNot (str?): Logical inverse of filter.  
                Properties: create
        logicalOr (Tuple[str, str]?): Logical OR of two filters.  
                Properties: create
        name (str?): Use filter named FILTER (or create new filter with that name).  
                If no objects are specified then the name given to the filter  
                will be returned.  
                Properties: create
        node (str?): Select objects whose node names match the pattern.  
                Properties: create
        nodeType (str?): Select objects whose node type names match the pattern.  
                Properties: create
        plug (str?): Select objects whose plug names match the pattern.  
                Properties: create

    Returns:
        str: if creating filter or getting filter info
        List[str]: if listing filters
        bool: if applying filter

    Example:
    """

