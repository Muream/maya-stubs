from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mayaDpiSetting(*, query: bool = ..., mode: Queryable[int] = ..., realScaleValue: bool = ..., scaleValue: Queryable[float] = ..., systemDpi: bool = ...) -> Union[int, float, bool]:
    """Provide Maya interface scaling based on system DPI or custom scale setting or no scaling. Please note that the change will only take effect after relaunching Maya.The mayaDpiSetting command is not available on macOS. System scaling should be used to change Maya UI scaling.mayaDpiSetting, dpi
    Args:
        mode (Queryable[int]?): Specifies the interface scaling mode:  
              
                0. System Dpi Based Scaling  
                1. Custom Scaling (Must provide the custom scale value with flag "-scaleValue")  
                2. No Scaling  
                Properties: create, query
        realScaleValue (bool?): This is a query mode only flag which returns the real scale value depending on current scaling mode and defined scale value:  
              
                mode 0. Return the current real scale value which is the ratio of current system dpi to default system dpi  
                mode 1. Return the current real scale value which is the product of the defined scale value and the ratio of current system dpi to default system dpi  
                mode 2. Always return 1.0 which indicates real scale is 100% when the scaling mode is no scaling.  
                Properties: query
        scaleValue (Queryable[float]?): Specifies the custom scale of the interface if scaling mode is 1. The allowed values are [1.0, 1.25, 1.5, 2.0].  
                In query mode, return the scale value depend on current scaling mode:  
              
                mode 0. Always return 1.0 which indicates 100% scaling  
                mode 1. Return the custom scale value used  
                mode 2. Always return 1.0 which indicates no custom scaling  
                Properties: create, query
        systemDpi (bool?): This is a query mode only flag which returns the current system dpi value.  
                Properties: query

    Returns:
        int: Scale mode or system DPI value, as queried
        float: Defined scale or real scale, as queried

    Example:
    """

