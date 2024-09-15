from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def arrayMapper(*, destAttr: str = ..., inputU: str = ..., inputV: str = ..., mapTo: str = ..., target: Multiuse[str] = ..., type: str = ...) -> List[str]:
    """Create an arrayMapper node and connect it to a target object.
    If the -type flag is used, then this command also creates an external
    node used for computing the output values. If the input attribute
    does not already exist, it will be created. The output attribute
    must exists. If    a flag is omitted, the selection list will be used
    to supply the needed objects. If none are found, that action is omitted.
    Args:
        destAttr (str?): Specifies the attribute which will be the downstream  
                connection for the output data from the mapper node. The  
                attribute type will be used to determine which output attribute  
                to use: float array gets outValuePP, vector array gets outColorPP.  
                If the flag is omitted, no output connection is made.  
                Properties: create
        inputU (str?): Specifies the upstream attribute to connect to the mapper's  
                uCoordPP attribute. If the flag is omitted, no input connection  
                is made.  
                Properties: create
        inputV (str?): Specifies the upstream attribute to connect to the mapper's  
                vCoordPP attribute. If the flag is omitted, no input connection  
                is made.  
                Properties: create
        mapTo (str?): Specifies an existing node to be used to compute the output values.  
                This node must be of the appropriate type. Currently, only ramp nodes  
                may be used.  
                Properties: create
        target (Multiuse[str]?): Specifies the target object to be connected to.  
                Properties: create, multiuse
        type (str?): Specifies the node type to create which will be used to compute  
                the output values. Currently, only ramp is valid. If the flag is  
                omitted, no connection is made and the external node is not created.  
                Properties: create

    Returns:
        List[str]: Names of created arrayMapper nodes.

    Example:
    """

