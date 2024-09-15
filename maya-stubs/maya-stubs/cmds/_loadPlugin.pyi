from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def loadPlugin(*args: str, addCallback: Callable[..., Any] = ..., allPlugins: bool = ..., name: str = ..., quiet: bool = ..., removeCallback: Callable[..., Any] = ...) -> List[str]:
    """Load plug-ins into Maya. The parameter(s) to this command
    are either the names or pathnames of plug-in files.  The
    convention for naming plug-ins is to use a .so extension
    on Linux, a .mll extension on Windows and .bundle
    extension on Mac OS X. If no extension is provided then the default
    extension for the platform will be used. To load a Python plugin
    you must explicitly supply the '.py' extension.If the plugin was specified with a pathname then that is
    where the plugin will be searched for. If no pathname was
    provided then the current working directory (i.e. the one
    returned by Maya's 'pwd' command) will be searched, followed
    by the directories in the MAYA_PLUG_IN_PATH environment variable.When the plug-in is loaded, the name used in Maya's
    internal plug-in registry for the plug-in information will
    be the file name with the extension removed.  For example,
    if you load the plug-in "newNode.mll" the name used in
    the Maya's registry will be "newNode".  This value as
    well as that value with either a ".so", ".mll" or ".bundle"
    extension can be used as valid arguments to either the
    unloadPlugin or pluginInfo commands.
    Args:
        addCallback (Callable[..., Any]?): Add a MEL or Python callback script to be called after a plug-in is loaded.  
              
                For MEL, the procedure should have the following signature:  
                global proc procedureName(string $pluginName).  
              
                For Python, you may specify either a script as a string, or a Python callable  
                object such as a function.  If you specify a string, then put the formatting  
                specifier "%s" where you want the name of the plug-in to be inserted.  If you  
                specify a callable such as a function, then the name of the plug-in will be  
                passed as an argument.  
                Properties: create
        allPlugins (bool?): Cause all plug-ins in the search path specified  
                in MAYA_PLUG_IN_PATH to be loaded.  
                Properties: create
        name (str?): Set a user defined name for the plug-ins  
                that are loaded.  If the name is already taken, then a number  
                will be added to the end of the name to make it unique.  
                Properties: create
        quiet (bool?): Don't print a warning if you attempt to load a plug-in that  
                is already loaded.  
                Properties: create
        removeCallback (Callable[..., Any]?): Removes a procedure which was previously added  
                with -addCallback.  
                Properties: create

    Returns:
        List[str]: the internal names of the successfully loaded plug-ins

    Example:
    """

