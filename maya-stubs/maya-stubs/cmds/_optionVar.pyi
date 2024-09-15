from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def optionVar(*, query: str = ..., arraySize: str = ..., category: str = ..., clearArray: Multiuse[str] = ..., clearStash: Multiuse[str] = ..., default: bool = ..., exists: str = ..., floatArray: Multiuse[str] = ..., floatValue: Multiuse[Tuple[str, float]] = ..., floatValue2: Multiuse[Tuple[str, float, float]] = ..., floatValue3: Multiuse[Tuple[str, float, float, float]] = ..., floatValue4: Multiuse[Tuple[str, float, float, float, float]] = ..., floatValueAppend: Multiuse[Tuple[str, float]] = ..., init: bool = ..., intArray: Multiuse[str] = ..., intValue: Multiuse[Tuple[str, int]] = ..., intValue2: Multiuse[Tuple[str, int, int]] = ..., intValue3: Multiuse[Tuple[str, int, int, int]] = ..., intValue4: Multiuse[Tuple[str, int, int, int, int]] = ..., intValueAppend: Multiuse[Tuple[str, int]] = ..., list: bool = ..., listCategories: bool = ..., listModified: bool = ..., prefFile: Queryable[str] = ..., remove: Multiuse[str] = ..., removeFromArray: Multiuse[Tuple[str, int]] = ..., stash: Multiuse[str] = ..., stringArray: Multiuse[str] = ..., stringValue: Multiuse[Tuple[str, str]] = ..., stringValueAppend: Multiuse[Tuple[str, str]] = ..., transient: bool = ..., unstash: Multiuse[str] = ..., version: int = ...) -> Union[int, List[str], None, str]:
    """This command allows you to set and query variables which are
    persistent between different invocations of Maya.  These variables
    are stored as part of the preferences.
    Args:
        arraySize (str?): returns the size of the array named "string".  If no such  
                variable exists, it returns 0.  If the variable is not an  
                array, it returns 1.  
                Properties: create
        category (str?): Set category for the specified variables.  
              
                This flag can also be combined with list/listModified flags to get all the  
                variables in the specified category.  
                Properties: create
        clearArray (Multiuse[str]?): If there is an array named "string", it is set to be empty.  
                Empty arrays are not saved.  
                Properties: create, multiuse
        clearStash (Multiuse[str]?): Clear backup copy of a variable.  
                Properties: create, multiuse
        default (bool?): The variable's current and default values will be set to the specified  
                values.  
              
                This flag can also be combined with the query flag to get the default  
                value or with the exists flag to determine if a default value has been  
                specified.  
              
                It can also be used with list/listModifed flags to  
                list variables with a default value.  
                Properties: create
        exists (str?): Returns 1 if a variable named "string" exists, 0 otherwise.  
                The default/transient flags can be used to list variables  
                that have a default value or are transient.  
                All other flags will be ignored if this is used. (Query has  
                higher precedence)  
                Properties: create
        floatArray (Multiuse[str]?): Creates a new empty float array variable named "string".  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        floatValue (Multiuse[Tuple[str, float]]?): creates a new variable named "string" with float value "float".  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different)  
                Properties: create, multiuse
        floatValue2 (Multiuse[Tuple[str, float, float]]?): Creates a new variable named "string" with a 2 element float array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        floatValue3 (Multiuse[Tuple[str, float, float, float]]?): Creates a new variable named "string" with a 3 element float array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        floatValue4 (Multiuse[Tuple[str, float, float, float, float]]?): Creates a new variable named "string" with a 4 element float array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        floatValueAppend (Multiuse[Tuple[str, float]]?): adds this value to the end of the array of floats named "string".  
                If no such array exists, one is created.  If there was a float  
                value with this name before, it becomes the first element of the  
                array.  If any other kind of value existed, it is overridden.  
                Properties: create, multiuse
        init (bool?): Used to initialize or reset variables. If the flag is set to true or the  
                variable does not exist then the variable's current and default values  
                will be set to the specified values. If the flag if set to false then  
                only the default value will be set and the current value will not be  
                modified.  
                Properties: create
        intArray (Multiuse[str]?): Creates a new empty int array variable named "string".  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        intValue (Multiuse[Tuple[str, int]]?): creates a new variable named "string" with integer value "int".  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        intValue2 (Multiuse[Tuple[str, int, int]]?): Creates a new variable named "string" with a 2 element int array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        intValue3 (Multiuse[Tuple[str, int, int, int]]?): Creates a new variable named "string" with a 3 element int array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        intValue4 (Multiuse[Tuple[str, int, int, int, int]]?): Creates a new variable named "string" with a 4 element int array.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        intValueAppend (Multiuse[Tuple[str, int]]?): adds this value to the end of the array of ints named "string".  
                If no such array exists, one is created.  If there was an int  
                value with this name before, it becomes the first element of the  
                array.  If any other kind of value existed, it is overridden.  
                Properties: create, multiuse
        list (bool?): This returns a list of all the defined variable names.  
              
                The category flag can be used to list variables in the specified  
                category and the default/transient flags can be used to list  
                variables that have a default value or are transient.  
              
                All other flags will be ignored if this one is used. (Query and exists  
                flags have a higher precedence).  
                Properties: create
        listCategories (bool?): This returns a list of all the defined variable categories. All other  
                flags will be ignored if this one is used. (Query and exists flags  
                have a higher precedence).  
                Properties: create
        listModified (bool?): This returns a list of all the variables that have been changed from  
                their default value.  
              
                Variables that don't have a default value will also be returned unless  
                the default flag is used to filter the list to variables that have a  
                default value. The category flag can also be used to filter the list by  
                category.  
              
                All other flags will be ignored if this one is used. (Query and exists  
                flags have a higher precedence).  
                Properties: create
        prefFile (Queryable[str]?): Flag need to be used in conjunction with category  
                Specify where the optionVars from specified category need to be saved when saving preferences.  
                Properties: create, query
        remove (Multiuse[str]?): removes the variable named "string", if one exists.  
                Note: all removals are done before any value  
                setting, if both the -r and other (-sv, -iv, -fv) flags are  
                used in the same command.  
                Properties: create, multiuse
        removeFromArray (Multiuse[Tuple[str, int]]?): removes the element numbered "int" in the array named "string".  
                Everything beyond it then gets shuffled down.  
                Properties: create, multiuse
        stash (Multiuse[str]?): Make a backup copy of a variable.  
                Properties: create, multiuse
        stringArray (Multiuse[str]?): Creates a new empty string array variable named "string".  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different).  
                Properties: create, multiuse
        stringValue (Multiuse[Tuple[str, str]]?): creates a new variable named using the first string with value given  
                by the second string.  
                If a variable already exists with this name, it is overridden  
                in favour of the new value (even if the type is different)  
                Properties: create, multiuse
        stringValueAppend (Multiuse[Tuple[str, str]]?): adds the value given by the second string to the end of the array of  
                strings named by the first string.  
                If no such array exists, one is created. If there was a string  
                value with this name before, it becomes the first element of the  
                array. If any other kind of value existed, it is overridden.  
                Properties: create, multiuse
        transient (bool?): Indicates that specified variables will not be persisted across sessions.  
                This flag can also be combined with -exists to determine if a variable is  
                transient.  
                Properties: create
        unstash (Multiuse[str]?): Restore a variable from a backup copy.  
                Properties: create, multiuse
        version (int?): Preferences version number to warn about incompatbile preference  
                files  
                Properties: create

    Returns:
        int: 0 or 1 for the exists option
        List[str]: When the list option is used
        None: otherwise

    Example:
    """

