from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def unloadPlugin(*args: str, addCallback: Callable[..., Any] = ..., force: bool = ..., removeCallback: Callable[..., Any] = ...) -> List[str]:
    """Unload plug-ins from Maya. After the successful execution of
    this command, plug-in services will no longer be available.
    Args:
        addCallback (Callable[..., Any]?): Add a procedure to be called just before a plugin is  
                unloaded. The procedure should have one string argument, which  
                will be the plugin's name.  
                Properties: create
        force (bool?): Unload the plugin even if it is providing services.  This  
                is not recommended.  If you unload a plug-in that implements  
                a node or data type in the scene, those instances will be  
                converted to unknown nodes or data and the scene will no  
                longer behave properly. Maya may become unstable or even  
                crash. If you use this flag you are advised to save your scene  
                in MayaAscii format and restart Maya as soon as possible.  
                Properties: create
        removeCallback (Callable[..., Any]?): Remove a procedure which was previously added  
                with -addCallback.  
                Properties: create

    Returns:
        List[str]: the internal names of the successfully unloaded plug-ins

    Example:
    """

