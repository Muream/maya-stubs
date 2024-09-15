from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyBlindData(*args: str, edit: bool = ..., associationType: str = ..., binaryData: Multiuse[str] = ..., booleanData: Multiuse[bool] = ..., delete: bool = ..., doubleData: Multiuse[float] = ..., int64Data: Multiuse[int] = ..., intData: Multiuse[int] = ..., longDataName: Multiuse[str] = ..., rescan: bool = ..., reset: bool = ..., shape: bool = ..., shortDataName: Multiuse[str] = ..., stringData: Multiuse[str] = ..., typeId: int = ...) -> str:
    """Command creates blindData types (basically creates an instance of
    TdnPolyBlindData). When used with the query flag, it returns the data
    types that define this blindData type.
    This command is to be used create a blindData node *and* to edit the same..
    The associationType flag *has* to be specified at all times.. This is
    because if an instance of the specified BD typeId exists in the history
    chain but if the associationType is not the same, then a new polyBlindData
    node is created..
    For object level blind data, only the object itself must be specified.
    A new compound attribute BlindDataNNNN will be created on the object.
    Blind data attribute names must be unique across types for object level
    blind data.
    So, the command will require the following to be specified:
        - typeId,
        - associationType
        - longDataName or shortDataName of data being edited.
        - The actual data being specified.
        - The components that this data is to be attached to.Polygon, blinddata, assign, command
    Args:
        associationType (str?): Specifies the dataTypes that are part of BlindData node being created.  
                Allowable associations are "object" for any object, and "vertex" "edge" and  
                "face" for mesh objects. Other associations for other geometry types may  
                be added.  
                Properties: create, edit
        binaryData (Multiuse[str]?): Specifies the data type is a binary data value  
                Properties: create, edit, multiuse
        booleanData (Multiuse[bool]?): Specifies the data type is a boolean logic value  
                Properties: create, edit, multiuse
        delete (bool?): Specifies that this will remove the blind data if found  
                Properties: create, edit
        doubleData (Multiuse[float]?): Specifies the data type is a floating point double value  
                Properties: create, edit, multiuse
        int64Data (Multiuse[int]?): Specifies the data type is an 64. bit integer value  
                Properties: create, edit, multiuse
        intData (Multiuse[int]?): Specifies the data type is an integer value  
                Properties: create, edit, multiuse
        longDataName (Multiuse[str]?): Specifies the long name of the data that is being modified by this command.  
                Properties: create, edit, multiuse
        rescan (bool?): Enables a rescan of blind data nodes for cached information  
                Properties: create, edit
        reset (bool?): Specifies that this command will reset the given attribute to default value  
                Properties: create, edit
        shape (bool?): For object association only, apply blind data to the shape(s) below  
                this node instead of the node itself  
                Properties: create, edit
        shortDataName (Multiuse[str]?): Specifies the short name of the data that is being modified by this command.  
                Properties: create, edit, multiuse
        stringData (Multiuse[str]?): Specifies the data type is a string value  
                Properties: create, edit, multiuse
        typeId (int?): Specifies the typeId of the BlindData type being created  
                Properties: create, edit

    Returns:
        str: Name of nodes created

    Example:
    """

