from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getParticleAttr(*args: str, array: bool = ..., attribute: str = ..., object: str = ...) -> List[float]:
    """This action will return either an array of values, or the average
    value and maximum offset, for a specied per-particle attribute of a
    particle object or component.  If a particle component is specified on
    the command line, values are returned for that component only.  If an
    object name is given instead, values are returned for all particles in
    that object.  If no object name is passed, but a particle object or
    component is selected, values are returned for the selection.If you list components, they must all be from the same particle
    object; the action ignores all objects after the first.  Likewise if
    you list more than one object, the actiion will return values only for
    the first one.
    Args:
        array (bool?): Tells the action whether you want a full array of data. If set true,  
                the action returns an array of floats containing the values for all  
                the specified particles.  If set false (the default), the action  
                returns the average value and the maximum offset from the average over  
                the component.  If the attribute is a vector attribute, the action  
                returns six values: Average X, Average Y, Average Z, Maximum offset in X, Y, and Z of component.  
                Properties: create
        attribute (str?): Tells the action which attribute you want the value of.  
                Must be a per-particle attribute.  
                Properties: create
        object (str?): This flag is obsolete.  Instead of using it, please pass the  
                name of the object and/or components you want on the command line.  
                See the examples.  
                Properties: create

    Returns:
        List[float]: Command result

    Example:
    """

