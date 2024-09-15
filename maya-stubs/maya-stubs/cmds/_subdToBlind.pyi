from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdToBlind(*args: Any, absolutePosition: bool = ..., includeCreases: bool = ..., includeZeroOffsets: bool = ...) -> bool:
    """The subdivision surface hierarchical edits will get copied into blind
    data on the given polygon.  The polygon face count and topology
    must match the subdivision surface base mesh face count and topology.
    If they don't, the blind data will still appear, but is not guaranteed
    to produce the same result when converted back to a subdivision surface.The command takes a single subdivision surface and a single polygonal
    object.  Additional subdivision surfaces or polygonal objects will be
    ignored.subdivision, surface, hierarchy, blind, data
    Args:
        absolutePosition (bool?): If set to true, the hierarchical edits are represented as the point positions,  
                not the point offsets.  Most of the time, this is not desirable, but if you're  
                just going to be merging/deleting a bunch of things and not move any vertices,  
                then you could set it to true.  False is the default and saves the offsets.  
                Properties: create
        includeCreases (bool?): If set, the creases get transfered as well.  With it false, the subdivision  
                surface created from the blind data + polygon will have lost all the craese  
                information.  The default is false.  
                Properties: create
        includeZeroOffsets (bool?): If set, the zero offset will get included in the blind data.  This will  
                greatly increase the size of the blind data, but will also let you keep  
                all created vertices in the conversion back to polys.  This flag does  
                not change the behaviour for the vertices up to and including level 2  
                as they're always created.  If not set, only the edited vertices will  
                be included in the blind data.  This will still maintain the shape of  
                your object faithfully.  The default is false.  
                Properties: create

    Returns:
        bool: Command result

    Example:
    """

