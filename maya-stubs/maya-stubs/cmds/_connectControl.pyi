from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def connectControl(arg0: str = ..., /, *args: str, fileName: bool = ..., index: int = ..., preventContextualMenu: bool = ..., preventOverride: bool = ...) -> bool:
    """This command attaches a UI widget, specified as the first argument, to
    one or more dependency node attributes. The attributes/nodes don't
    have to exist yet, they will get looked up as needed. With no flag
    specified, this command works on these kinds of controls: floatField,
    floatScrollBar, floatSlider, intField, intScrollBar, intSlider,
    floatFieldGrp, intFieldGrp, checkBox, radioCollection, and
    optionMenu. With theflag, It will also work on the
    individual components of all other groups.This command sets up abetween the control
    and the (first-specified) attribute. If this first attribute is
    changed in any way, the control will be appropriately updated to match
    its value.Summary: if you change the control, ALL the connected attributes
    change. If you change the FIRST attribute attached to the control,
    then the control will change.NOTE: the two-way connection will not be established if the attributes
    do not exist when thecommand is run. If the
    user later uses the control, the connection will be established at
    that time.To effectively usewith radioCollections and
    optionMenus, you must attach a piece of data to each radioButton and
    menuItem. This piece of data (an integer) can be attached using theflag in theandcommands. When the button/item is selected, the attribute will be set
    to the value of its data. When the attribute is changed, the
    collection (or optionMenu) will switch to the item that matches the
    new attribute value. If no item matches, it will be left unchanged.There are some specialized controls that have connection capability
    (and more) built right into them. See attrFieldSliderGrp,
    attrFieldGrp, and attrColorSliderGrp. Using these classes can be
    easier than using connectControl.
    Args:
        fileName (bool?): This flag causes the connection to be treated as a  
                filename, and the conversion from internal to external  
                filename representation is made as the data is  
                copied. This only applies to connections to Tfield  
                controls.  
                Properties: create
        index (int?): This flag enables you to pick out a sub-control from a  
                group that contains a number of different controls.  
                For example, you can connect one field of a  
                floatFieldGrp.  You must count each member of the  
                group, including any text labels that may exist.  For  
                example, if you have a check box group with a label,  
                the label will count as index 1, and the first check  
                box as index 2.  (Indices are 1. based)  
                Properties: create
        preventContextualMenu (bool?): If true, this flag will block the right mouse button menu  
                of the associated control attribute.  
                Properties: create
        preventOverride (bool?): If true, this flag disallows overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create

    Returns:
        bool:

    Example:
    """

