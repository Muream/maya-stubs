from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def proximityWrap(*args: str, edit: bool = ..., query: bool = ..., addDrivers: Multiuse[str] = ..., applyUserDefaults: bool = ..., canBeAdded: Queryable[Multiuse[str]] = ..., driverIndices: bool = ..., dumpInfo: bool = ..., freeDriverIndex: bool = ..., removeDrivers: Multiuse[str] = ...) -> Union[List[str], Multiuse[str], bool]:
    """This command creates a proximityWrap deformer, which deforms geometry based on the
    distance from its drivers.
    Args:
        addDrivers (Multiuse[str]?): Add connect new drivers to the proximityWrap node  
                Properties: edit, multiuse
        applyUserDefaults (bool?): Flag used in with the addDriver flag. When set, new drivers will set the  
                user default attributes from the option var settings. When the flag is not set,  
                the user default attributes will not be set.  
                Default is on.  
                Properties: edit
        canBeAdded (Queryable[Multiuse[str]]?): Returns true if all listed shapes can be added as drivers. The reason for an item  
                returning false would be that it is already connected as a driver, it is connected  
                as the deformed geometry or it represents in invalid object.  
                Properties: query, multiuse
        driverIndices (bool?): List connected driver indices  
                Properties: query
        dumpInfo (bool?): Return a python dictionary containing information relating to the proximityWrap  
                node. Some information is returned in string form in mel but the flag is meant to be used  
                in python.  
                Properties: query
        freeDriverIndex (bool?): Returns the first index which has no driver connected  
                Properties: query
        removeDrivers (Multiuse[str]?): Remove connected drivers  
                Properties: edit, multiuse

    Returns:
        List[str]: (the proximityWrap node name)

    Example:
    """

