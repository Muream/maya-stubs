from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyQueryBlindData(*args: str, associationType: str = ..., binaryData: str = ..., booleanData: bool = ..., doubleData: float = ..., intData: int = ..., longDataName: Multiuse[str] = ..., maxValue: float = ..., minValue: float = ..., shortDataName: Multiuse[str] = ..., showComp: bool = ..., stringData: str = ..., subString: str = ..., typeId: int = ...) -> str:
    """Command query's blindData associated with particular polygonal components.
    So, the command will require the following to be specified:
            - selection list to query
    Optional are the:
            - typeId
            - associationType
            - longDataName or shortDataName of data being queried.
            - The actual data being specified.
            - showComponent flag
    Note that for object level blind data, the showComponent flag will be ignored.
    If no components are selected, the assocation flag will be ignored and
    object level data will be queried.query, blind, data
    Args:
        associationType (str?): Specifies the dataTypes that are part of BlindData node being queried.  
                Allowable associations are "object" for any object, and "vertex" "edge" and  
                "face" for mesh objects.  
                Properties: create
        binaryData (str?): Specifies the binary string value to search for  
                Properties: create
        booleanData (bool?): Specifies the string value to search for  
                Properties: create
        doubleData (float?): Specifies the double/float value to search for  
                Properties: create
        intData (int?): Specifies the integer value to search for  
                Properties: create
        longDataName (Multiuse[str]?): Specifies the long name of the data that is being queried by this command.  
                Properties: create, multiuse
        maxValue (float?): Specifies the maximum value to search for.  This option will query float,  
                double, and integer types of blind data.  
                Properties: create
        minValue (float?): Specifies the minimum value to search for.  This option will query float,  
                double and integer types of blind data.  
                Properties: create
        shortDataName (Multiuse[str]?): Specifies the short name of the data that is being queried by this command.  
                Properties: create, multiuse
        showComp (bool?): The showComponent option controls whether the object.[component].attribute  
                name is output preceeding the actual value.  If the showComponent option  
                is used then the restriction of only returning 1 type of blind data (i.e.  
                one of integer, float, double... is removed, as the return for all are  
                strings.  
                If the association is object and not component, then this option will  
                still cause all the attribute names to be printed  
                Properties: create
        stringData (str?): Specifies the string value to search for  
                Properties: create
        subString (str?): Specifies the substring that should be checked against a STRING type blind  
                data.  If the sub string is found query is successful.  Will not look at non  
                String type blind data elements.  
                Properties: create
        typeId (int?): Specifies the typeId of the BlindData type being queried.  If the typeId  
                is not specified, then all of the components that match the query will be  
                output.  The typeId of the elements found will be output if the ShowComponents  
                option is used.  Will be in the format "object.component.attribute::typeId".  
                If the typeId is specifed then the "::typeId" portion will not be output with  
                the ShowComponents option.  
                Properties: create

    Returns:
        str: Blind data

    Example:
    """

