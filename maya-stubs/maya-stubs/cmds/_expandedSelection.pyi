from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def expandedSelection(*args: str, depth: int = ..., expansionType: str = ...) -> Union[str, List[str]]:
    """Examines the current selection list and returns that list, expanded to meet certain
    criteria. See the command flags for the exact criteria that will be used.select
    Args:
        depth (int?): Number of steps away from current selection to expand to.  
                A value of 0 will not expand the selection at all.  
                Properties: create
        expansionType (str?): The type of graph along which to expand the selection. Legal values are:  
                DG : Use the normal DG connections  
                EG : Use the evaluation graph connections  
                SG : Use the scheduling graph connections within the evaluation graph  
              
                If the actual selected node is not included in the graph being expanded on, e.g.  
                there is no evaluation node when using the EG type, then the selected node will not  
                appear in the output.  
                If this flag is not specified then the type defaults to DG.  
                Properties: create

    Returns:
        str: List of objects in the requested selection list expansion
        List[str]: List of nodes visited in the DG expansion
        List[str]: (Python only) List of single nodes and tuples visited in the EG or SG expansion, where tuples represent the DG nodes in a cluster

    Example:
    """

