from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setParticleAttr(*args: str, attribute: str = ..., floatValue: float = ..., object: str = ..., randomFloat: float = ..., randomVector: Tuple[float, float, float] = ..., relative: bool = ..., vectorValue: Tuple[float, float, float] = ...) -> bool:
    """This action will set the value of the chosen attribute for every
    particle or selected component in the selected or passed particle object.
    Components should not be passed to the command line.
    For setting the values of components, the components must be
    selected and only the particle object's names should be passed to
    this action.
    If the attribute is a vector attribute and the -vv flag is passed,
    then the three floats passed will be used to set the values.  If
    the attribute is a vector and the -fv flag is pass and the -vv flag
    is not passed, then the float will be repeated for each of the
    X, Y, and Z values of the attribute.  Similarly, if the attribute is
    a float attribute and a vector value is passed, then the length of
    the vector passed will be used for the value.
    Note:  The attribute passed must be a Per-Particle attribute.
    Args:
        attribute (str?): Tells the action which attribute you want to set  
                Properties: create
        floatValue (float?): Tells what you want the value to be set to of a float attribute  
                Properties: create
        object (str?): If this flag is passed and the STRING is the name of a particle object's transform or shape,  
                then ONLY that object will be edited, ignoring the selection list or command line, and  
                ALL of its particles' values will be changed for the specified attribute.  
                Properties: create
        randomFloat (float?): Tells the command to add a random value from -FLOAT to +FLOAT to  
                the results of each particle.  The default is 0.0.  
                Properties: create
        randomVector (Tuple[float, float, float]?): Tells the command to add a random value from <<-x,-y,-z>> to <<x,y,z>> to  
                the results of each particle. The default 0 0 0.  
                Properties: create
        relative (bool?): If this is set to TRUE (the default is FALSE), then the float or vector value will be added to the current value  
                for each particle.  
                Properties: create
        vectorValue (Tuple[float, float, float]?): Tells what you want the value to be set to of a vector  
                attribute  
                Properties: create

    Returns:
        bool:

    Example:
    """

