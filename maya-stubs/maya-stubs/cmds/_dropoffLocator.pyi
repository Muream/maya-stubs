from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dropoffLocator(arg0: float = ..., arg1: float = ..., arg2: str = ..., /, *args: str) -> List[str]:
    """This command adds one or more dropoff locators to a wire curve, one for
    each selected curve point. The dropoff locators can be used to provide
    localized tuning of the wire deformation about the curve point.The arguments are two floats, the envelope and percentage, followed by
    the wire node name and then by the curve point(s).
    Returns:
        List[str]: Locator name(s)

    Example:
    """

