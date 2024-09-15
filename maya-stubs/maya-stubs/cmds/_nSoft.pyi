from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nSoft(*args: str, query: bool = ..., convert: bool = ..., duplicate: bool = ..., duplicateHistory: bool = ..., goal: float = ..., hideOriginal: bool = ...) -> str:
    """Makes a nSoft body from the object(s) passed on the command
    line or in the selection list.  The geometry can be a NURBS, polygonal,
    lattice object.  The resulting nSoft body is made up of a hierarchy
    with a particle shape and a geometry shape, thus:Dynamics are applied to the particle shape and the resulting particle
    positions then drive the locations of the geometry's CVs, vertices, or
    lattice points.With the convert option, the particle shape and its transform are simply
    inserted below the original shape's hierarchy.
    With the duplicate option, the original geometry's transform and shape are
    duplicated underneath its parent, and the particle shape is placed under
    the duplicate.  Note that any animation on
    the hierarchy will affect the particle shape as well.  If you do not want
    them, then reparent the structure outside the hierarchy.When duplicating, the nSoft portion (the duplicate) is given the name
    "copyOf" + "original object name".  The particle portion is always
    given the name "original object name" + "Particles."None of the flags of the nSoft command can be queried.  The nSoft -q
    command is used only to identify when an object is a nSoft body,
    or when two objects are part of the same nSoft body.
    See the examples.
    Args:
        convert (bool?): This tells the command that you want the original object  
                to be the actual deformed object.  The particle shape portion of the  
                nSoft body will be inserted in the same hierarchy as the original,  
                under the same parent (with one additional intervening transform  
                which is initially the identity).  If no flags are passed, then this  
                is assumed.  The combination -c -h 1 is not valid; if you have  
                this in your scripts, remove the -h 1.  
                Properties: create
        duplicate (bool?): This tells the command that you want to make a copy of  
                the original object and use the copy as the deforming geometry.  
                Input connections to the original object are duplicated.  You would  
                do this if you wanted to keep the original object in your scene and  
                also have a copy of it that was a nSoft body.  
                This flag and -dh are mutually exclusive.  
                Properties: create
        duplicateHistory (bool?): This is the same as -d, except that upstream history,  
                is duplicated as well, instead of just input connections.  
                This flag and -d are mutually exclusive.  
                Properties: create
        goal (float?): This is the same as -d, but in addition it tells the command that  
                you want the resulting nSoft body to try to  
                follow the original geometry, using the set goal weight as the value  
                that controls how strongly it is to follow it.  A value of 1.0 will  
                try to follow exactly, and a value of 0.0 will not follow at all.  
                The default value is 0.5.  This value must be from 0.0 to 1.0.  
                You could use -d with -g, but it is redundant.  If you want history to  
                be duplicated, you can use -dh and -g together.  
                Properties: create
        hideOriginal (bool?): This flag is used only when duplicating (-d, -g, or -dh).  If set to true,  
                whichever of the two objects is NOT the nSoft object will be hidden.  
                In other words, with -d -h true, the original object will be hidden;  
                with -d -c -h 1 the duplicate object will be hidden.  
                You would typically do this if you want to use the non-dynamic object as  
                a goal for the nSoft one (see -g) but you do not want it visible in the scene.  
                The flags -h 1 and -c are mutually exclusive.  
                Properties: create

    Returns:
        str: array

    Example:
    """

