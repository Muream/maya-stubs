from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def snapshot(*args: str, edit: bool = ..., query: bool = ..., constructionHistory: bool = ..., endTime: Queryable[int] = ..., increment: Queryable[int] = ..., motionTrail: bool = ..., name: Queryable[str] = ..., startTime: Queryable[int] = ..., update: Queryable[str] = ...) -> Union[List[str], bool, int, str]:
    """This command can be used to create either a series of surfaces evaluated at
    the times specified by the command flags, or a motion trail displaying the
    trajectory of the object's pivot point at the times specified.If the constructionHistory flag is true, the output shapes or motion trail
    will re-update when modifications are made to the animation or construction
    history of the original shape. When construction history is used, the forceUpdate
    flag can be set to false to control when the snapshot recomputes, which will
    typically improve performance.
    Args:
        constructionHistory (bool?): update with changes to original geometry  
                Properties: create, query
        endTime (Queryable[int]?): time to stop copying target geometry  
                Default: 10.0  
                Properties: create, query, edit
        increment (Queryable[int]?): time increment between copies  
                Default: 1.0  
                Properties: create, query, edit
        motionTrail (bool?): Rather than create a series of surfaces, create a motion trail  
                displaying the location of the object's pivot point at the  
                specified time steps. Default is false.  
                Properties: create
        name (Queryable[str]?): the name of the snapshot node. Query returns string.  
                Properties: create, query, edit
        startTime (Queryable[int]?): time to begin copying target geometry  
                Default: 1.0  
                Properties: create, query, edit
        update (Queryable[str]?): This flag can only be used if the snapshot has  
                constructionHistory. It sets the snapshot node's update  
                value. The update value controls whether the snapshot updates  
                on demand (most efficient), when keyframes change (efficient),  
                or whenever any history changes (least efficient). Valid values  
                are "demand", "animCurve", "always".  
                Default: "always"  
                Properties: create, query, edit

    Returns:
        List[str]: names of nodes created or edited: transform-name [snapshot-node-name]

    Example:
    """

