from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def containerBind(*args: str, edit: bool = ..., query: bool = ..., allNames: bool = ..., bindingSet: str = ..., bindingSetConditions: bool = ..., bindingSetList: bool = ..., force: bool = ..., preview: bool = ...) -> bool:
    """This is an accessory command to the container command which is used
    for some automated binding operations on the container. A container's
    published interface can be bound using a bindingSet on the
    associated container template.bind, container
    Args:
        allNames (bool?): Specifies that all published names on the container should be considered  
                during the binding operation.  By default only unbound published names  
                will be operated on.  Additionally specifying the 'force' option with 'all'  
                will cause all previously bound published names to be reset (or unbound)  
                before the binding operation is performed; in the event that there is no  
                appropriate binding found for the published name, it will be left in the  
                unbound state.  
                Properties: create
        bindingSet (str?): Specifies the name of the template binding set to use for the bind or  
                query operation.  
                This flag is not available in query mode.  
                			In query mode, this flag needs a value.  
                Properties: query
        bindingSetConditions (bool?): Used in query mode, returns a list of binding set condition entries from the  
                specified template binding set.  The list returned is composed of  
                of all published name / condition string pairs for each entry in the  
                binding set.  
                This flag returns all entries in the associated binding set and does not take  
                into account the validity of each entry with respect to the container's  
                list of published names, bound or unbound state, etc.  
                Properties: query
        bindingSetList (bool?): Used in query mode, returns a list of available binding sets that  
                are defined on the associated container template.  
                Properties: query, edit
        force (bool?): This flag is used to force certain operations to proceed that would normally  
                not be performed.  
                Properties: create
        preview (bool?): This flag will provide a preview of the results of a binding operation but  
                will not actually perform it.  A list of publishedName/boundName  
                pairs are returned for each published name that would be affected by the  
                binding action.  
                If the binding of a published name will not change as a result of the action it  
                will not be listed.  
                Published names that were bound but will become unbound are also listed,  
                in this case the associated boundName will be indicated by an empty string.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

