from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def blindDataType(*, dataType: Multiuse[str] = ..., longDataName: Multiuse[str] = ..., longNames: bool = ..., query: bool = ..., shortDataName: Multiuse[str] = ..., shortNames: bool = ..., typeId: int = ..., typeNames: bool = ...) -> str:
    """This command creates a blind data type, which is represented by a
    blindDataTemplate node in the DG. A blind data type can have one
    or more attributes. On the command line, the attributes should be
    ordered by type for best memory utilization, largest first:
    string, binary, double, float, int, and finally boolean.
    Once a blind data type is created, blind data of that type may
    be assigned using the polyBlindData command. Note that as well
    as polygon components, blind data may be assigned to objects
    and to NURBS patches. A blind data type may not be modified
    after it is created: in order to do so it must be deleted and
    recreated. Any existing blind data of that type would also need
    to be deleted and recreated.
    When used with the query flag, this command will return information
    about the attributes of the specified blind data type.create, blinddata, type
    Args:
        dataType (Multiuse[str]?): Specifies the dataTypes that are part of BlindData node being created.  
                Allowable strings are "int", "float", "double", "string", "boolean" and "binary".  
                Must be used togeter with the -ldn and -sdn flags to specify each attribute.  
                Properties: create, multiuse
        longDataName (Multiuse[str]?): Specifies the long names of the datas that are part of BlindData node being  
                created. Must be used togeter with the -dt and -sdn flags to specify each attribute.  
                Properties: create, multiuse
        longNames (bool?): Specifies that for a query command the long attributes names be listed.  
                Properties: create
        query (bool?): Specifies that this is a special query type command.  
                Properties: create
        shortDataName (Multiuse[str]?): Specifies the short names of the data that are part of BlindData node being  
                created. Must be used togeter with the -dt and -ldn flags to specify each attribute.  
                Properties: create, multiuse
        shortNames (bool?): Specifies that for a query command the short attribute names be listed.  
                Properties: create
        typeId (int?): Specifies the typeId of the BlindData type being created.  
                Properties: create
        typeNames (bool?): Specifies that for a query command the data types be listed.  
                Properties: create

    Returns:
        str: Name of nodes created

    Example:
    """

