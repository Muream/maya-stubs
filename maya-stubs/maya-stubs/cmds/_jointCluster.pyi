from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def jointCluster(*args: str, edit: bool = ..., query: bool = ..., aboveBound: Queryable[float] = ..., aboveCluster: bool = ..., aboveDropoffType: Queryable[str] = ..., aboveValue: Queryable[float] = ..., belowBound: Queryable[float] = ..., belowCluster: bool = ..., belowDropoffType: Queryable[str] = ..., belowValue: Queryable[float] = ..., deformerTools: bool = ..., joint: str = ..., name: str = ...) -> Union[str, float, bool]:
    """The joint cluster command adds high-level controls to
    manage the cluster percentage values on a bound skin
    around a joint. JointClusters are one way
    to create smooth bending behaviour on skin when joints
    rotate.CVs/vertices between Joint1 and aaaaa (aboveBound) receive only
    translation/rotation/scale from Joint1. CVs vertices between aaaa and
    bbbb transition between translation/rotatation/scale from Joint1 and
    Joint2. CV2 beyand bbbbb (below bound) receive only translation/
    rotation scale from Joint3.
    Args:
        aboveBound (Queryable[float]?): Specifies the where the drop-off begins in the  
                direction of the bone above the joint. A value of 100 indicates  
                the entire length of the bone. The default value is 10.  
                Properties: create, query, edit
        aboveCluster (bool?): Returns the name of the cluster associated with the bone  
                above this joint.  
                Properties: query
        aboveDropoffType (Queryable[str]?): Specifies the type of percentage drop-off in the direction  
                of the bone above this joint. Valid values are "linear",  
                "exponential", "sine" and "none". Default is linear.  
                Properties: create, query, edit
        aboveValue (Queryable[float]?): Specifies the drop-off percentage of the joint cluster in the  
                direction of the bone above the cluster. A value of 100 indicates  
                the entire length of the bone. The default value is 50.  
                Properties: create, query, edit
        belowBound (Queryable[float]?): Specifies where the drop-off ends in the  
                direction of the bone below the joint. A value of 100 indicates  
                the entire length of the bone. The default value is 10.  
                Properties: create, query, edit
        belowCluster (bool?): Returns the name of the cluster associated with this joint.  
                Properties: query
        belowDropoffType (Queryable[str]?): Specifies the type of type of percentage drop-off in the direction  
                of the bone below this joint. Valid values are "linear",  
                "exponential", "sine" and "none".  
                Default is linear.  
                Properties: create, query, edit
        belowValue (Queryable[float]?): Specifies the drop-off percentage of the joint cluster in the  
                direction of the joint below the cluster. A value of 100 indicates  
                the entire length of the bone. The default value is 50.  
                Properties: create, query, edit
        deformerTools (bool?): Used to query for the helper nodes associated with the jointCluster.  
                Properties: query
        joint (str?): Specifies the joint that the cluster should act about.  
                Properties: create
        name (str?): This flag is obsolete.  
                Properties: create

    Returns:
        str: Name of the new jointCluster node

    Example:
    """

