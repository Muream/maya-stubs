from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def emit(*, attribute: Multiuse[str] = ..., floatValue: Multiuse[float] = ..., object: str = ..., position: Multiuse[Tuple[float, float, float]] = ..., vectorValue: Multiuse[Tuple[float, float, float]] = ...) -> List[int]:
    """Theaction allows users to add particles to an existing particle
    object without the use of an emitter.  At the same time, it allows them to
    set any per-particle attribute for the particles that are created with the
    action.The particles created do not become a part of the initial state
    for the particle object, and will disappear when the scene is rewound unless
    they are saved into the initial state by the user explicitly.  In addition,
    a particle object will accept particles from an emit action ONLY at frames
    greater than or equal to its start frame.  For example, if you want to use the
    emit action to create particles at frame -5, you must set startFrame for that
    particle shape to -5 or less.Unlike many commands or actions, the emit action uses the order of its flags
    as important information as to how it works.  Theandflags can appear anywhere in the argument list.  Theand the
    value flags are interpreted based on their order.  Any value flags after an
    -attribute flag and before the next -attribute flag will set the values for
    the attribute specified by the closest -attribute flag before them in the
    argument list.  See thesection below for more detail on
    how these flags work.Currently, no creation expression is executed for the new particles
    unless they are created from within a particle expression defined with
    thecommand or the Expression Editor.  If you
    want any particular values put into the particles at the time they are
    created, then those values should be set using the, andflags.
    Args:
        attribute (Multiuse[str]?): Specifies the attribute on the particle object that any  
                value flags following it and before the next -attribute flag  
                will be associated with.  The same attribute can be specified  
                later in the command to pick up where the first one left off.  
                The attributes used must be per-particle attributes.  This  
                will accept both long and short names for the attributes.  
                Note the per-particle attribute must already exist on the  
                particle object prior to being specified via this command flag.  
                Properties: create, multiuse
        floatValue (Multiuse[float]?): Sets the float value to be used for the "current" attribute of  
                the "current" particle.  By current attribute, it is meant the  
                attribute specified by the most recent -attribute flag.  By  
                current particle, it is meant the particle in the list of -position  
                flags that corresponds to the number of values that  have  
                been set for the "current" attribute.  If the current attribute  
                is a vector-per-particle attribute, then the float value  
                specified will be used for all three components of the vector.  
                Properties: create, multiuse
        object (str?): This flag takes the name of a particleShape or the transform  
                directly above it in the DAG as its parent.  It specifies  
                which object to add the particles to.  This flag must  
                be passed, as the selection list is ignored for this action.  
                Properties: create
        position (Multiuse[Tuple[float, float, float]]?): Specifies the positions in the particle object's space  
                (usually world space) where the particles are to be created.  
                One particle is created for each occurence of this flag.  
                Properties: create, multiuse
        vectorValue (Multiuse[Tuple[float, float, float]]?): Sets the vector value to be used for the "current" attribute of  
                the "current" particle.  By current attribute, it is meant the  
                attribute specified by the most recent -attribute flag.  By  
                current particle, it is meant the particle in the list of -position  
                flags that corresponds to the number of values that have  
                been set for the "current" attribute.  If the current attribute  
                is a float-per-particle attribute, then the length of the  
                vector described by this flag will be used.  The length is  
                described as SQR( xVal2 + yVal2 + zVal2 ).  
                Properties: create, multiuse

    Returns:
        List[int]: Integer array containing the list of the particleId attribute values
            for the created particles in the same order that the position flags
            were passed.

    Example:
    """

