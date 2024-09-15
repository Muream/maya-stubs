from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def moduleInfo(*, definition: bool = ..., listModules: bool = ..., moduleName: str = ..., path: bool = ..., version: bool = ...) -> List[str]:
    """Returns information on modules found by Maya.module
    Args:
        definition (bool?): Returns module definition file name for the module specified by the -moduleName parameter.  
                Properties: create
        listModules (bool?): Returns an array containing the names of all currently loaded modules.  
                Properties: create
        moduleName (str?): The name of the module whose information you want to retrieve. Has to be used with either -definition / -path / -version flags.  
                Properties: create
        path (bool?): Returns the module path for the module specified by the -moduleName parameter.  
                Properties: create
        version (bool?): Returns the module version for the module specified by the -moduleName parameter.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

