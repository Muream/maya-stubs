from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cacheFileCombine(*args: str, edit: bool = ..., query: bool = ..., cacheIndex: bool = ..., channelName: Multiuse[str] = ..., connectCache: Queryable[str] = ..., keepWeights: bool = ..., layerNode: bool = ..., nextAvailable: bool = ..., object: str = ..., objectIndex: Queryable[int] = ...) -> Union[str, bool, int]:
    """Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.cache, file, disk, blend
    Args:
        cacheIndex (bool?): A query only flag that returns the index related to the  
                cache specified with the connectCache flag.  
                Properties: query
        channelName (Multiuse[str]?): Used in conjunction with the connectCache flag to indicate the channel(s) that  
                should be connected.  If not specified, the first channel in the file is used.  
                Properties: edit, multiuse
        connectCache (Queryable[str]?): An edit flag that specifies a cacheFile node that should be connected to the next available index on the specified cacheBlend node. As a query flag, it returns a string array containing the cacheFiles that feed into the specified cacheBlend node.  
                			In query mode, this flag can accept a value.  
                Properties: query, edit
        keepWeights (bool?): This is a flag for use in combination with the connectCache flag only. By default, the connectCache flag will set all weights other than the newly added cacheWeight to 0 so that the new cache gets complete control. This flag disables that behavior so that all existing blend weights are retained.  
                Properties: edit
        layerNode (bool?): A query flag that returns a string array of the existing cacheBlends on the selected object(s). Returns an empty string array if no cacheBlends are found.  
                Properties: query
        nextAvailable (bool?): A query flag that returns the next available index on the selected cacheBlend node.  
                Properties: query
        object (str?): This flag is used in combination with the objectIndex flag. It is  
                used to specify the object whose index you wish to query.  
                			In query mode, this flag needs a value.  
                Properties: query
        objectIndex (Queryable[int]?): In edit mode, used in conjunction with the connectCache flag to indicate  
                the objectIndex to be connected.  
                In query mode, returns the index related to the object specified with  
                the object flag.  
                Properties: query, edit

    Returns:
        str: Name of created cache layer node(s)

    Example:
    """

