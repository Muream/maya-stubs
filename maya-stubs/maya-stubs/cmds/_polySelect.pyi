from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySelect(*args: str, query: bool = ..., add: bool = ..., addFirst: bool = ..., asSelectString: bool = ..., deselect: bool = ..., edgeBorder: Multiuse[int] = ..., edgeBorderPath: Multiuse[Tuple[int, int]] = ..., edgeBorderPattern: Multiuse[Tuple[int, int]] = ..., edgeLoop: Multiuse[int] = ..., edgeLoopOrBorder: Multiuse[int] = ..., edgeLoopOrBorderPattern: Multiuse[Tuple[int, int]] = ..., edgeLoopPath: Multiuse[Tuple[int, int]] = ..., edgeLoopPattern: Multiuse[Tuple[int, int]] = ..., edgeRing: Multiuse[int] = ..., edgeRingPath: Multiuse[Tuple[int, int]] = ..., edgeRingPattern: Multiuse[Tuple[int, int]] = ..., edgeUVLoopOrBorder: Multiuse[int] = ..., everyN: int = ..., extendToShell: Multiuse[int] = ..., noSelection: bool = ..., replace: bool = ..., shortestEdgePath: Multiuse[Tuple[int, int]] = ..., shortestEdgePathUV: Multiuse[Tuple[int, int]] = ..., shortestFacePath: Multiuse[Tuple[int, int]] = ..., toggle: bool = ...) -> Union[List[int], bool]:
    """This command makes different types of poly component selections.  The return value
    is an integer array containing the id's of the components in the selection in order.
    If a given type of selection loops back on itself then this is indicated by the start id
    appearing twice, once at the start and once at the end.
    Args:
        add (bool?): Indicates that the specified items should be  
                added to the active list without removing existing  
                items from the active list.  
                Properties: create, query
        addFirst (bool?): Indicates that the specified items should be  
                added to the front of the active list without  
                removing existing items from the active list.  
                Properties: create, query
        asSelectString (bool?): Changes the return type from an integer array to  
                a string array which can be used as a selection string.  
                Properties: create, query
        deselect (bool?): Indicates that the specified items should  
                be removed from the active list if they are on the  
                active list.  
                Properties: create, query
        edgeBorder (Multiuse[int]?): Select all conected border edges starting at the given edge.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeBorderPath (Multiuse[Tuple[int, int]]?): Given two edges on the same border, this will select  
                the edges on the border in the path between them.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeBorderPattern (Multiuse[Tuple[int, int]]?): Given two edges on the same border, this will check how  
                many edges there are between the given edges and then  
                continue that pattern of selection around the border.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeLoop (Multiuse[int]?): Select an edge loop starting at the given edge.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeLoopOrBorder (Multiuse[int]?): Select an edge loop or all conected border edges,  
                depending on whether the edge is on a border or not,  
                starting at the given edge.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeLoopOrBorderPattern (Multiuse[Tuple[int, int]]?): Given two edges either on the same edge loop or on the  
                same edge border, this will check how many edges there  
                are between the given edges and then continue that pattern  
                of selection around the edge loop or edge border.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeLoopPath (Multiuse[Tuple[int, int]]?): Given two edges that are on the same edge loop, this  
                will select the shortest path between them on the loop.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeLoopPattern (Multiuse[Tuple[int, int]]?): Given two edges on the same edge loop, this will check how  
                many edges there are between the given edges and then  
                continue that pattern of selection around the edge loop.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeRing (Multiuse[int]?): Select an edge ring starting at the given edge.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeRingPath (Multiuse[Tuple[int, int]]?): Given two edges that are on the same edge ring, this  
                will select the shortest path between them on the ring.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeRingPattern (Multiuse[Tuple[int, int]]?): Given two edges on the same edge ring, this will check how  
                many edges there are between the given edges and then  
                continue that pattern of selection around the edge ring.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        edgeUVLoopOrBorder (Multiuse[int]?): Select an edge loop or border, terminating at UV borders.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        everyN (int?): Number of elements to stride over. If less than 1 then  
                use 1, meaning every element. 2 means every second one, etc.  
                Properties: create
        extendToShell (Multiuse[int]?): Select the poly shell given a face id.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        noSelection (bool?): If this flag is used then the selection is not  
                changed at all.  
                Properties: create, query
        replace (bool?): Indicates that the specified items should  
                replace the existing items on the active list.  
                Properties: create, query
        shortestEdgePath (Multiuse[Tuple[int, int]]?): Given two vertices, this will select the shortest path  
                between them in the 3d object space.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        shortestEdgePathUV (Multiuse[Tuple[int, int]]?): Given two UVs, this will select the shortest path  
                between them in the 2d texture space.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        shortestFacePath (Multiuse[Tuple[int, int]]?): Given two faces, this will select the shortest path  
                between them in the 3d object space.  
                      In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        toggle (bool?): Indicates that those items on the given list which  
                are on the active list should be removed from the active  
                list and those items on the given list which are not on  
                the active list should be added to the active list.  
                Properties: create, query

    Returns:
        List[int]: List of selected components.

    Example:
    """

