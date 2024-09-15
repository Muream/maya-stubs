from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attrControlGrp(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., attribute: Queryable[str] = ..., changeCommand: Queryable[Callable[..., Any]] = ..., enable: bool = ..., exists: bool = ..., handlesAttribute: str = ..., hideMapButton: bool = ..., label: Queryable[str] = ..., preventOverride: bool = ...) -> Union[str, Callable[..., Any], bool]:
    """This command creates a control of the type most appropriate for the specified
    attribute, and associates the control with the attribute. Any change to the
    control will cause a change in the attribute value, and any change to the
    attribute value will be reflected in the control. Not all attribute types are
    supported.attribute, control
    Args:
        annotation (Queryable[str]?): Sets or queries the annotation value of the control group.  
                Properties: create, query, edit
        attribute (Queryable[str]?): Sets or queries the attribute the control represents. The name of the attribute  
                must be fully specified, including the name of the node. Some types of  
                attributes are not supported, but most commonly used attribute types are.  
                Properties: create, query, edit
        changeCommand (Queryable[Callable[..., Any]]?): Sets or queries the change command of the control group. The change  
                command will be executed when the control is used to change the value  
                of the attribute.  
                Properties: create, query, edit
        enable (bool?): Sets or queries the enable state of the control group. The control is dimmed if  
                the enable state is set to false.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create, query, edit
        handlesAttribute (str?): Returns true or false as to whether this command can create a control for the  
                specified attribute.  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        hideMapButton (bool?): Force the map button to remain hidden for this control.  
                Properties: create, query, edit
        label (Queryable[str]?): Sets or queries the label of the control group.  
                Properties: create, query, edit
        preventOverride (bool?): Sets or queries the prevent adjustment state of the control group. If true,  
                the RMB menu for the control will not allow adjustments to be made.  
                Properties: create, query, edit

    Returns:
        str: The control name.

    Example:
    """

