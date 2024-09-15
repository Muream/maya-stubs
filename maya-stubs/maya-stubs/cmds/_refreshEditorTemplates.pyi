from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def refreshEditorTemplates() -> bool:
    """This command refreshes all cached attribute editor templates,
    including those copied from the standard AE. These are the templates
    constructed internally on a per node type basis. This is useful
    if attribute elements have changed and the templates need to
    be re-evaluated accordingly.
    Returns:
        bool:

    Example:
    """

