from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attributeName(arg0: str = ..., /, *, leaf: bool = ..., long: bool = ..., nice: bool = ..., short: bool = ...) -> str:
    """This command takes one "node.attribute"-style specifier on the command line
    and returns either the attribute's long, short, or nice name.  (The "nice" name,
    or UI name, is the name used to display the attribute in Maya's interface, and
    may be localized when running Maya in a language other than English.)
    If more than one "node.attribute" specifier is given on the command line,
    only the first valid specifier is processed.query, attribute, nice, name
    Args:
        leaf (bool?): When false, shows parent multi attributes (like  
                "controlPoints[2].xValue").  When true, shows only the  
                leaf-level attribute name (like "xValue").  Default is true.  
                Note that for incomplete attribute strings, like a missing  
                multi-parent index ("controlPoints.xValue") or an  
                incorrectly named compound (cntrlPnts[2].xValue), this  
                flag defaults to true and provides a result as long as the  
                named leaf-level attribute is defined for the node.  
                Properties: create
        long (bool?): Returns names in "long name" format like "translateX"  
                Properties: create
        nice (bool?): Returns names in "nice name" format like "Translate X"  
                Properties: create
        short (bool?): Returns names in "short name" format like "tx"  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

