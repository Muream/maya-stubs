from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def instancer(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addObject: bool = ..., cycle: Queryable[str] = ..., cycleStep: Queryable[float] = ..., cycleStepUnits: Queryable[str] = ..., index: Queryable[int] = ..., levelOfDetail: Queryable[str] = ..., name: Queryable[str] = ..., object: Queryable[Multiuse[str]] = ..., objectPosition: Queryable[str] = ..., objectRotation: Queryable[str] = ..., objectScale: Queryable[str] = ..., pointDataSource: bool = ..., removeObject: bool = ..., rotationOrder: Queryable[str] = ..., rotationUnits: Queryable[str] = ..., valueName: Queryable[str] = ...) -> Union[str, float, int, Multiuse[str], bool]:
    """This command is used to create a instancer node and set the proper
    attributes in the node.instancer
    Args:
        addObject (bool?): This flag indicates that objects specified by the -object flag will be added to  
                the instancer node as instanced objects.  
                Properties: create, edit
        cycle (Queryable[str]?): This flag sets or queries the cycle attribute for the instancer node.  
                The options are "none" or "sequential".  The default is "none".  
                Properties: create, query, edit
        cycleStep (Queryable[float]?): This flag sets or queries the cycle step attribute for the instancer node.  This attribute  
                indicates the size of the step in frames or seconds (see cycleStepUnit).  
                Properties: create, query, edit
        cycleStepUnits (Queryable[str]?): This flag sets or queries the cycle step unit attribute for the instancer  
                node.  The options are "frames" or "seconds".  The default is "frames".  
                Properties: create, query, edit
        index (Queryable[int]?): This flag is used to query the name of the ith instanced object.  
                Properties: query
        levelOfDetail (Queryable[str]?): This flag sets or queries the level of detail of the instanced objects.  The  
                options are "geometry", "boundingBox", "boundingBoxes".  The default is  
                "geometry".  
                Properties: create, query, edit
        name (Queryable[str]?): This flag sets or queries the name of the instancer node.  
                Properties: create, query
        object (Queryable[Multiuse[str]]?): This flag indicates which objects will be add/removed from the list of instanced  
                objects.  The flag is used in conjuction with the -add and -remove flags.  If  
                neither of these flags is specified on the command line then -add is assumed.  
                Properties: create, query, edit, multiuse
        objectPosition (Queryable[str]?): This flag queries the given objects position.  This object can be any instanced object or  
                sub-object.  
                Properties: query
        objectRotation (Queryable[str]?): This flag queries the given objects rotation.  This object can be any instanced object or  
                sub-object.  
                Properties: query
        objectScale (Queryable[str]?): This flag queries the given objects scale.  This object can be any instanced object or  
                sub-object.  
                Properties: query
        pointDataSource (bool?): This flag is used to query the source node supply the data for the input points.  
                Properties: query
        removeObject (bool?): This flag indicates that objects specified by the -object flag will be  
                removed from the instancer node as instanced objects.  
                Properties: edit
        rotationOrder (Queryable[str]?): This flag specifies the rotation order associated with the rotation flag.  The  
                options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.  
                Properties: create, query, edit
        rotationUnits (Queryable[str]?): This flag specifies the rotation units associated with the rotation flag.  The  
                options are degrees or radians.  By default the attribute is degrees.  
                Properties: create, query, edit
        valueName (Queryable[str]?): This flag is used to query the value(s) of the array associated with the given  
                name.  If the -index flag is used in conjuction with this flag then the ith  
                value will be returned.  Otherwise, the entire array will be returned.  
                Properties: query

    Returns:
        str: Command result

    Example:
    """

