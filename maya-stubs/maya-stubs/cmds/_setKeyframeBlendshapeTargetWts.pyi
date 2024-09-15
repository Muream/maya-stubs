from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setKeyframeBlendshapeTargetWts(*args: str) -> int:
    """This command can be used to keyframe per-point blendshape target weights. It operates
    on the currently selected objects as follows.
    When the base object is selected, then the target weights are keyed for all
    targets. When only target
    shapes are selected, then the weights for thoses targets are keyframed.setKeyframe, blendShape
    Returns:
        int: number of vertices for which the targets weights are keyed

    Example:
    """

