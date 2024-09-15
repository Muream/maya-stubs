from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def threadCount(*, query: bool = ..., numberOfThreads: Queryable[int] = ...) -> Union[bool, int]:
    """This command sets the number of threads to be used by Maya in
    regions of code that are multithreaded. By default the number
    of threads is equal to the number of logical CPUs, not the
    number of physical CPUs. Logical CPUs are different from
    physical CPUs in the following ways:A physical CPU with hyperthreading counts as two logical CPUsA dual-core CPU counts as two logical CPUsWith some workloads, using one thread per logical CPU may
    not perform well. This is sometimes the case with
    hyperthreading. It is worth experimenting with different
    numbers of threads to see which gives the best performance.
    Note that having more threads can mean Maya uses more memory.Setting a value of zero means the number of threads used will
    equal the number of logical processors in the system.
    Args:
        numberOfThreads (Queryable[int]?): Sets the number of threads to use  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

