from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def particleInstancer(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addObject: bool = ..., aimAxis: Queryable[str] = ..., aimDirection: Queryable[str] = ..., aimPosition: Queryable[str] = ..., aimUpAxis: Queryable[str] = ..., aimWorldUp: Queryable[str] = ..., attributeMapping: bool = ..., cycle: Queryable[str] = ..., cycleStartObject: Queryable[str] = ..., cycleStep: Queryable[float] = ..., cycleStepUnits: Queryable[str] = ..., index: Queryable[int] = ..., instanceId: Queryable[str] = ..., levelOfDetail: Queryable[str] = ..., name: Queryable[str] = ..., object: Queryable[Multiuse[str]] = ..., objectIndex: Queryable[str] = ..., particleAge: Queryable[str] = ..., position: Queryable[str] = ..., removeObject: bool = ..., rotation: Queryable[str] = ..., rotationOrder: Queryable[str] = ..., rotationType: Queryable[str] = ..., rotationUnits: Queryable[str] = ..., scale: Queryable[str] = ..., shear: Queryable[str] = ..., visibility: Queryable[str] = ...) -> Union[str, bool, float, int, Multiuse[str]]:
    """This command is used to create a particle instancer node and set the proper
    attributes in the particle shape and in the instancer node.  It will
    also create the connections needed between the particle shape and the instancer
    node.particle, instancer
    Args:
        addObject (bool?): This flag indicates that objects specified by the -object flag will be added to  
                the instancer node as instanced objects.  
                Properties: create, edit
        aimAxis (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the aim axis  
                of the instanced objects.  
                Properties: create, query, edit
        aimDirection (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the aim direction  
                of the instanced objects.  
                Properties: create, query, edit
        aimPosition (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the aim position  
                of the instanced objects.  
                Properties: create, query, edit
        aimUpAxis (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the aim up axis  
                of the instanced objects.  
                Properties: create, query, edit
        aimWorldUp (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the aim world up  
                of the instanced objects.  
                Properties: create, query, edit
        attributeMapping (bool?): This flag queries the particle attribute mapping list.  
                Properties: query
        cycle (Queryable[str]?): This flag sets or queries the cycle attribute for the instancer node.  The options are  
                "none", "sequential". The default is "none".  
                Properties: create, query, edit
        cycleStartObject (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the cycle start object  
                of the instanced objects.  
                Properties: create, query, edit
        cycleStep (Queryable[float]?): This flag sets or queries the cycle step attribute for the instancer node.  This attribute  
                indicates the size of the step in frames or seconds (see cycleStepUnits).  
                Properties: create, query, edit
        cycleStepUnits (Queryable[str]?): This flag sets or queries the cycle step unit attribute for the instancer node.  
                The options are "frames" or "seconds".  The default is "frames".  
                Properties: create, query, edit
        index (Queryable[int]?): This flag is used to query the name of the ith instanced object.  
                Properties: query
        instanceId (Queryable[str]?): This flag queries the particle attribute name to be used for the id of the instanced objects.  
                Properties: query
        levelOfDetail (Queryable[str]?): This flag sets or queries the level of detail of the instanced objects.  The options are  
                "geometry", "boundingBox" or "boundingBoxes".  The default is "geometry".  
                Properties: create, query, edit
        name (Queryable[str]?): This flag sets or queries the name of the instancer node.  
                Properties: create, query
        object (Queryable[Multiuse[str]]?): This flag indicates which objects will be add/removed from the list of instanced  
                objects.  The flag is used in conjuction with the -addObject and -remove flags.  If  
                neither of these flags is specified on the command line then -addObject is assumed.  
                Properties: create, query, edit, multiuse
        objectIndex (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the object index  
                of the instanced objects.  
                Properties: create, query, edit
        particleAge (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the age  
                of the instanced objects.  
                Properties: create, query, edit
        position (Queryable[str]?): DEFAULT "worldPosition"  
                This flag sets or queries the particle attribute name to be used for the positions  
                of the instanced objects.  By default the attribute is worldPosition.  
                Properties: create, query, edit
        removeObject (bool?): This flag indicates that objects specified by the -object flag will be  
                removed from the instancer node as instanced objects.  
                Properties: edit
        rotation (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the rotation  
                of the instanced objects.  
                Properties: create, query, edit
        rotationOrder (Queryable[str]?): This flag specifies the rotation order associated with the rotation flag.  The options are  
                XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.  
                Properties: create, query, edit
        rotationType (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the rotation type  
                of the instanced objects.  
                Properties: create, query, edit
        rotationUnits (Queryable[str]?): This flag specifies the rotation units associated with the rotation flag.  The options are  
                degrees or radians.  By default the attribute is degrees.  
                Properties: create, query, edit
        scale (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the scale  
                of the instanced objects.  
                Properties: create, query, edit
        shear (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the shear  
                of the instanced objects.  
                Properties: create, query, edit
        visibility (Queryable[str]?): This flag sets or queries the particle attribute name to be used for the visibility  
                of the instanced objects.  
                Properties: create, query, edit

    Returns:
        str: Command result

    Example:
    """

