from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def memory(*, adjustedVirtualMemory: bool = ..., asFloat: bool = ..., debug: bool = ..., freeMemory: bool = ..., gigaByte: bool = ..., heapMemory: bool = ..., kiloByte: bool = ..., megaByte: bool = ..., pageFaults: bool = ..., pageReclaims: bool = ..., physicalMemory: bool = ..., processVirtualMemory: bool = ..., summary: bool = ..., swapFree: bool = ..., swapLogical: bool = ..., swapMax: bool = ..., swapPhysical: bool = ..., swapReserved: bool = ..., swapVirtual: bool = ..., swaps: bool = ...) -> bool:
    """Used to query essential statistics on memory availability and usage.By default memory sizes are returned in bytes. Since Maya's command engine
    only supports 32-bit signed integers, any returned value which cannot fit
    into 31 bits will be truncated to 2,147,483,647 and a warning message displayed.
    To avoid having memory sizes truncated use one of the memory size flags to
    return the value in larger units (e.g. megabytes) or use the asFloat flag to
    return the value as a float.
    Args:
        adjustedVirtualMemory (bool?): Returns size of adjusted virtual memory allocated by the process.  
                The adjustment is done by computing an offset when the application is launched  
                that will be subtracted from the process virtual memory in order to give the  
                adjusted value.  The returned size is an approximation of the memory used by the  
                process that can be more reliable in some cases, for instance on platforms where  
                display drivers can reserve large ranges of memory addresses, therefore increasing  
                the size of the process virtual memory, even though those addresses are actually  
                not used.  
                Properties: create
        asFloat (bool?): Causes numeric values to be returned as floats rather than ints. This can  
                be useful if you wish to retain some of the significant digits lost when  
                using the unit size flags.  
                Properties: create
        debug (bool?): Print debugging statistics on arena memory (if it exists)  
                Properties: create
        freeMemory (bool?): Returns size of free memory  
                Properties: create
        gigaByte (bool?): Return memory sizes in gigabytes (1024*1024*1024 bytes)  
                Properties: create
        heapMemory (bool?): Returns size of memory heap  
                Properties: create
        kiloByte (bool?): Return memory sizes in kilobytes (1024 bytes)  
                Properties: create
        megaByte (bool?): Return memory sizes in megabytes (1024*1024 bytes)  
                Properties: create
        pageFaults (bool?): Returns number of page faults  
                Properties: create
        pageReclaims (bool?): Returns number of page reclaims  
                Properties: create
        physicalMemory (bool?): Returns size of physical memory  
                Properties: create
        processVirtualMemory (bool?): Returns size of virtual memory allocated by the process  
                Properties: create
        summary (bool?): Returns a summary of memory usage. The size flags are ignored and all  
                memory sizes are given in megabytes.  
                Properties: create
        swapFree (bool?): Returns size of free swap  
                Properties: create
        swapLogical (bool?): Returns size of logical swap  
                Properties: create
        swapMax (bool?): Returns maximum swap size  
                Properties: create
        swapPhysical (bool?): Returns size of physical swap  
                Properties: create
        swapReserved (bool?): Returns size of reserved swap  
                Properties: create
        swapVirtual (bool?): Returns size of virtual swap  
                Properties: create
        swaps (bool?): Returns number of swaps  
                Properties: create

    Returns:
        bool:

    Example:
    """

