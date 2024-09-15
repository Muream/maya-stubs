from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def poseInterpolator(arg0: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., addPose: str = ..., drivers: bool = ..., deletePose: str = ..., exportPoses: str = ..., goToPose: str = ..., index: bool = ..., importPoses: str = ..., kernelWidth: str = ..., mirror: Multiuse[str] = ..., name: str = ..., pose: Multiuse[Tuple[str, str]] = ..., poseNames: bool = ..., rename: Tuple[str, str] = ..., searchAndReplace: Tuple[str, str] = ..., updatePose: str = ...) -> None: ...
