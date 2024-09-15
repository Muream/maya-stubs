from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pluginDisplayFilter(arg0: str = ..., /, *, query: bool = ..., classification: Queryable[str] = ..., deregister: bool = ..., exists: bool = ..., label: Queryable[str] = ..., listFilters: bool = ..., register: bool = ...) -> Union[str, bool]:
    """Register, deregister or query a plugin display filter.
    Plug-ins can use this command to register their own display filters which
    will appear in the 'Show' menus on Maya's model panels.displayfilter, modeleditor, modelpanel
    Args:
        classification (Queryable[str]?): The classification used to filter objects in Viewport 2.0.  
                This classification is the same as MFnPlugin::registerNode().  
                If the node was registered with multiple classifications, use the one beginning with "drawdb".  
                The default value of this flag is an empty string (""). It will not  
                filter any objects in Viewport 2.0.  
                Properties: create, query
        deregister (bool?): Deregister a plugin display filter.  
                Properties: create
        exists (bool?): Returns true if the specified filter exists, false otherwise.  
                Other flags are ignored.  
                Properties: create
        label (Queryable[str]?): The string to be displayed for this filter in the UI. E.g. in the 'Show' menu of a model panel.  
                The default value of this flag is the same as the plugin display filter name.  
                Properties: create, query
        listFilters (bool?): Returns an array of all plugin display filters.  
                Properties: query
        register (bool?): Register a plugin display filter.  
                The -register is implied if both -register and -deregister flags are missing in create mode.  
                You are responsible for deregistering any filters which you register.  
                Filters are reference counted, meaning that if you register the same filter twice  
                then you will have to deregister it twice as well.  
                Properties: create

    Returns:
        str: string[]

    Example:
    """

