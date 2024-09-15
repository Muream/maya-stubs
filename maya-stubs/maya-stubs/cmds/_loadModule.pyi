from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def loadModule(*, allModules: bool = ..., load: str = ..., scan: bool = ...) -> List[str]:
    """Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged up with other resources in a "module". Each module resides in its own directory and provides a module definition file to make Maya aware of the plug-ins it provides.When Maya starts up it loads all of the module files it finds, making the module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at this time, Maya is simply made aware of them so that they can be loaded if needed.The loadModule command provides the ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to restart Maya before being able to use them.module
    Args:
        allModules (bool?): Load all new modules not yet loaded in Maya. New modules are the one returned by the -scan option.  
                Properties: create
        load (str?): Load the module specified by the module definition file.  
                Properties: create
        scan (bool?): Rescan module presence. Returns the list of module definition files found and not yet loaded into Maya. Does not load any of these newly found modules, nor change the Maya state.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

