from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getPanel(*, allConfigs: bool = ..., allPanels: bool = ..., allScriptedTypes: bool = ..., allTypes: bool = ..., atPosition: Tuple[int, int] = ..., configWithLabel: str = ..., containing: str = ..., invisiblePanels: bool = ..., scriptType: str = ..., type: str = ..., typeOf: str = ..., underPointer: bool = ..., visiblePanels: bool = ..., withFocus: bool = ..., withLabel: str = ...) -> List[str]:
    """This command returns panel and panel configuration information.
    Args:
        allConfigs (bool?): Return the names of the all panel configuration in a string array.  
                Properties: create
        allPanels (bool?): Return the names of all the panels in a string array.  
                Properties: create
        allScriptedTypes (bool?): Return the names of all types of scripted panels in a string array.  
                Properties: create
        allTypes (bool?): Return the names of all types of panels, except scripted types in  
                a string array.  
                Properties: create
        atPosition (Tuple[int, int]?): Return the name of the panel which contains the specified screen coordinates.  
                An empty string is returned if there is no panel at those coordinates.  
                Properties: create
        configWithLabel (str?): Return the name of the panel configuration with the specified label text.  
                Properties: create
        containing (str?): Return the name of the panel containing the specified control.  
                An empty string is returned if the specified control is not in  
                any panel.  
                Properties: create
        invisiblePanels (bool?): Return the names of all the invisible panels in a string array.  
                Properties: create
        scriptType (str?): Return the names of all scripted panels of the specified type in a  
                string array.  
                Properties: create
        type (str?): Return the names of all panels of the specified type in a string array.  
                Properties: create
        typeOf (str?): Return the type of the specified panel.  
                Properties: create
        underPointer (bool?): Return the name of the panel that the pointer is currently over.  
                An empty string is returned if the pointer is not over any panel.  
                Properties: create
        visiblePanels (bool?): Return the names of all the visible panels in a string array.  
                Properties: create
        withFocus (bool?): Return the name of the panel that currently has focus.  If no  
                panel has focus then the last panel that had focus is returned.  
                Properties: create
        withLabel (str?): Return the name of the panel with the specified label text.  
                Properties: create

    Returns:
        List[str]: An array of panel names

    Example:
    """

