from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def binMembership(*args: str, query: bool = ..., addToBin: str = ..., exists: str = ..., inheritBinsFromNodes: str = ..., isValidBinName: str = ..., listBins: bool = ..., makeExclusive: str = ..., notifyChanged: bool = ..., removeFromBin: str = ...) -> bool:
    """Command to assign nodes to bins.binMembership
    Args:
        addToBin (str?): Add the nodes in a node list to a bin.  
                Properties: create
        exists (str?): Query if a node exists in a bin.  The exists flag can take only one node.  
                Properties: create
        inheritBinsFromNodes (str?): Let the node in the flag's argument inherit bins from nodes  
                in the specified node list.  The node list is specified as the  
                object of the command.  
                Properties: create
        isValidBinName (str?): Query if the specified bin name is valid.  If so, return true.  
                Otherwise, return false.  
                Properties: create
        listBins (bool?): Query and return a list of bins a list of nodes belong to.  
                If a bin contains any of the nodes in the selection list,  
                then it should be included  
                in the returned bin list.  
                Properties: create, query
        makeExclusive (str?): Make the specified nodes belong exclusively in the specified bin.  
                Properties: create
        notifyChanged (bool?): This flag is used to notify that binMembership has been changed.  
                Properties: create
        removeFromBin (str?): Remove the nodes in a node list from a bin.  
                Properties: create

    Returns:
        bool: Command result

    Example:
    """

