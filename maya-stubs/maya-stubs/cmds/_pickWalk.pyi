from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pickWalk(*args: str, direction: str = ..., recurse: bool = ..., type: str = ...) -> List[str]:
    """The pickWalk command allows you to quickly change the selection list
    relative to the nodes that are currently selected. It is called
    pickWalk, because it walks from one selection list to another
    by unselecting what's currently selected, and selecting nodes that
    are in the specified direction from the currently selected list.
    If you specify objects on the command line, the pickWalk command
    will walk from those objects instead of the selected list.If the -type flag is instances, then the left and right direction will
    walk to the previous or next instance of the same selected dag node.
    Args:
        direction (str?): The direction to walk from the node. The choices are  
                up | down | left | right | in | out. up walks to the parent node,  
                down to the child node, and left and right to the sibling nodes.  
                If a CV on a surface is selected, the left and right directions walk  
                in the U parameter direction of the surface, and the up and down directions  
                walk in the V parameter direction.  
                In and out are only used if the type flag is 'latticepoints'.  
                Default is right.  
                Properties: create
        recurse (bool?): If specified then recurse down when walking  
                Properties: create
        type (str?): The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints.  
                If type is nodes, then the left and right direction walk to the next dag siblings.  
                If type is instances, the left and right direction walk to the previous or next  
                instance of the same dag node.  
                If type is edgeloop, then the edge loop starting at the first selected edge will  
                be selected.  
                If type is edgering, then the edge ring starting at the first selected edge will  
                be selected.  
                If type is faceloop, and there are two connected quad faces selected which define  
                a face loop, then that face loop will be selected.  
              
                edgeloop, edgering and faceloop all remember which was the first edge or faces  
                selected for as long as consecutive selections are made by this command.  They  
                use this information to determine what the "next" loop or ring selection should  
                be.  Users can make selections forwards and backwards by using the direction  
                flag with "left" or "right".  
              
                If type is motiontrailpoints, then the left and right direction walk to the previous  
                or next motion trail points respectively.  
              
                Default is nodes.  
                Properties: create

    Returns:
        List[str]: A list of the newly selected items

    Example:
    """

