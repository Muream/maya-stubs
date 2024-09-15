from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyInstallAction(*args: Any, query: bool = ..., commandName: bool = ..., convertSelection: bool = ..., installConstraint: bool = ..., installDisplay: bool = ..., keepInstances: bool = ..., uninstallConstraint: bool = ..., uninstallDisplay: bool = ...) -> Union[List[str], bool]:
    """Installs/uninstalls several things to help the user to perform the
    specified action :
    Args:
        commandName (bool?): return as a string the name of the command previously installed  
                Properties: query
        convertSelection (bool?): convert all polys selected in object mode  
                into their full matching component selection. For example : if a polyMesh is selected,  
                polyInstallAction -cs polyCloseBorder  
                will select all border edges.  
                Properties: create
        installConstraint (bool?): C: install selection pickmask and internal constraints for actionname  
                Q: returns 1 if any internal constraint is set for current action  
                Properties: create, query
        installDisplay (bool?): C: install display attributes for actionname  
                Q: returns 1 if any display is set for current action  
                Properties: create, query
        keepInstances (bool?): Convert components for all selected instances rather than only the first selected instance.  
                Properties: create
        uninstallConstraint (bool?): uninstall internal constraints previously installed  
                Properties: create
        uninstallDisplay (bool?): uninstall display attributes previously installed  
                Properties: create

    Returns:
        List[str]: When installing constraint, returns as an array of strings the
            items on which the installed command will act on. otherwise, returns nothing

    Example:
    """

