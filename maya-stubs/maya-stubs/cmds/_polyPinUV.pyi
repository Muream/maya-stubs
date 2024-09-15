from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyPinUV(*args: str, edit: bool = ..., query: bool = ..., createHistory: bool = ..., operation: Queryable[int] = ..., unpinned: bool = ..., uvSetName: Queryable[str] = ..., value: Queryable[Multiuse[float]] = ...) -> Union[bool, int, str, Multiuse[float]]:
    """This command is used to pin and unpin UVs. A "pinned" UV is one which should not be modified.Each UV has an associated pin weight, that defaults to 0.0 meaning that the UV is not pinned. If pin weight is set to 1.0 then it becomes fully pinned and UV tools should not modify that UV.
    If the pin weight is set to a value between 0.0 and 1.0 then UV tools should weight their changes to that UV accordingly.UV pinning is not enforced by the shape node: it is up to each tool to decide whether it will obey the pin weights.uv, pin
    Args:
        createHistory (bool?): For objects that have no construction history, this flag can be used  
                to force the creation of construction history for pinning.  By default,  
                history is not created if the object has no history.  Regardless of this  
                flag, history is always created if the object already has history.  
                Properties: create, query, edit
        operation (Queryable[int]?): Operation to perform.  Valid values are:  
                0. Set pin weights on the selected UVs.  
                1. Set pin weights to zero for the selected UVs.  
                2. Remove pin weights from the entire mesh.  
                3. Invert pin weights of the entire mesh.  
                Default is 0.  
                Properties: create, query, edit
        unpinned (bool?): List all selected UVs which are not pinned.  
                Properties: query, edit
        uvSetName (Queryable[str]?): Specifies the name of the UV set to edit UVs on. If not  
                specified the current UV set will be used if it exists.  
                Properties: create, query, edit
        value (Queryable[Multiuse[float]]?): Specifies the pin value for the selected UV components.  
                When specified multiple times, the values are assigned respectively to  
                the specified UVs.  
                Properties: create, query, edit, multiuse

    Returns:
        bool: Success or Failure.

    Example:
    """

