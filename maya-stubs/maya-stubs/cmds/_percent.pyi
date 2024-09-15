from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def percent(arg0: str = ..., /, *args: str, query: bool = ..., addPercent: bool = ..., dropoffAxis: Tuple[float, float, float] = ..., dropoffCurve: str = ..., dropoffDistance: float = ..., dropoffPosition: Tuple[float, float, float] = ..., dropoffType: str = ..., multiplyPercent: bool = ..., value: Queryable[float] = ...) -> Union[bool, float]:
    """This command sets percent values on members of a weighted node such as
    a cluster or a jointCluster. With no flags specified the command sets
    the percent value for selected components of the specified node to the
    specified percent value. A dropoff from the specified percent value to
    0 can be specified from a point, plane or curve using a dropoff
    distance around that shape. The percent value can also be added or
    multiplied with existing percent values of the node components.
    Args:
        addPercent (bool?): Add the percent value specified with the -v flag to the existing percent values  
                Properties: create
        dropoffAxis (Tuple[float, float, float]?): Specifies the axis along which to dropoff the percent value,  
                starting from the dropoffPosition.  
                Properties: create
        dropoffCurve (str?): Specifies the curve around which to dropoff the percent value.  
                Properties: create
        dropoffDistance (float?): Specifies the dropoff distance from the point, plane or curve  
                that was specified using the -dp -dax or -dc flags.  
                Properties: create
        dropoffPosition (Tuple[float, float, float]?): Specifies the point around which to dropoff the percent value.  
                Properties: create
        dropoffType (str?): Specifies the type of dropoff. Used in conjunction with  
                the -dp, -dax or -dc flags. Default is linear.  
                Valid values are: linear, sine, exponential, linearSquared, none.  
                Properties: create
        multiplyPercent (bool?): Multiply the percent value specified with the -v flag with existing percent values  
                Properties: create
        value (Queryable[float]?): The percent value to be applied. The default is 1. In query mode,  
                returns an array of doubles corresponding to the weights of the  
                selected object components.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

