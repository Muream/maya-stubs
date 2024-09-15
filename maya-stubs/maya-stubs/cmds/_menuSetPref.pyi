from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def menuSetPref(*, edit: bool = ..., query: bool = ..., exists: bool = ..., force: bool = ..., loadAll: bool = ..., removeAll: bool = ..., saveAll: bool = ..., saveBackup: bool = ..., version: bool = ...) -> bool:
    """Provides the functionality to save and load menuSets between sessions of Maya.
    For Internal Use Only!
    Args:
        exists (bool?): Returns whether the menuSet preferences file exists or not.  
                Properties: query
        force (bool?): Forces a specified operation to continue even if errors are encountered (such as invalid  
                preferences).  
                Properties: create, edit
        loadAll (bool?): Loads all the menuSets from the preferences file only if the preferences version matches,  
                or the -force flag is enabled.  On successful load, of a prefs file, an empty string is returned,  
                otherwise, a description of the problem encountered is returned.  
                Properties: create
        removeAll (bool?): Removes all the menuSets from the preferences file (removes the whole file).  
                Properties: create
        saveAll (bool?): Saves all the current menuSets into the preferences file.  
                Properties: create
        saveBackup (bool?): Saves a backup of the current menu set preferences file if one exists.  This backup will  
                be saved in the same location as the current preferences file.  
                Properties: create
        version (bool?): The base version string which is saved out to file. It is also checked upon loading  
                in order to indicate changes in the default prefs since the prefs were last saved out.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

