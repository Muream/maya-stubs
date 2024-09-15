from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mimicManipulation(*, manipulations: str = ..., prevalidation: bool = ..., refresh: bool = ...) -> List[bool]:
    """This command mimics what various manipulators do to support
    Evaluation-Manager-accelerated manipulation.  This command should be
    use for testing, debugging and benchmarking purposes.
    Manipulations are described using a string representing a JSON object.
    This object must have a member named "session" containing an array,
    where each member of that array represents a manipulation transaction,
    i.e. plugs set by a single manipulation action.  Each of these transactions
    is also an array of plugs to set.  A plug to set is an object with a
    "plug" member, which is a string describing the plug to be manipulated,
    and a "value" member, which is the value to set to this plug.  Note that
    only plugs with attributes of type "double" or "double3" can currently be
    set and the value must be a number or an array of 3 numbers.
    A session can be thought of as the global action of a manipulation, from
    the time the manipulator is grabbed to the moment it is released, including
    the movements in between.  A transaction can be thought of as one delta
    inside the manipulation after which evaluation must happen to show the
    results, like a single mouse movement while the manipulator is held after
    which evaluation and viewport refresh must occur.manipulation
    Args:
        manipulations (str?): JSON string representing the manipulations to be performed.  
                Properties: create
        prevalidation (bool?): Flag to control if prevalidation of the manipulated plugs will be  
                performed.  If it is and the plugs are already properly supported by  
                the Evaluation Manager, Evaluation Manager manipulation will be used  
                on the very first frame instead of requiring an initial frame with  
                dirty propagation and DG evaluation to validate Evaluation Manager  
                manipulation can be safely performed.  
                Properties: create
        refresh (bool?): Flag to control if a refresh is triggered after each manipulation.  
                Note that refresh is necessary for evaluation to kick in.  
                Properties: create

    Returns:
        List[bool]: True if the transaction could be evaluated by the Evaluation Manager, false otherwise, for each provided transaction

    Example:
    """

