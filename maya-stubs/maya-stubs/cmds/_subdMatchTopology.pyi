from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdMatchTopology(*args: str, frontOfChain: bool = ...) -> bool:
    """Command matches topology across multiple subdiv surfaces - at all levels.subdivision, surface, deformers, refine, level, coarse, fine
    Args:
        frontOfChain (bool?): This command is used to specify that the new addTopology node should be  
                placed ahead (upstream) of existing deformer and skin nodes in the shape's  
                history (but not ahead of existing tweak nodes). The input to the addTopology  
                node will be the upstream shape rather than the visible downstream shape, so  
                the behavior of this flag is the most intuitive if the downstream deformers  
                are in their reset (hasNoEffect) position when the new deformer is added.  
                Properties: create

    Returns:
        bool: Success or Failure.

    Example:
    """

