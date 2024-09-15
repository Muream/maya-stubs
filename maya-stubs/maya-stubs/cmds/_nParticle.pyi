from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nParticle(*args: str, edit: bool = ..., query: bool = ..., attribute: str = ..., cache: bool = ..., conserve: Queryable[float] = ..., count: bool = ..., deleteCache: bool = ..., dynamicAttrList: bool = ..., floatValue: float = ..., gridSpacing: Queryable[Multiuse[float]] = ..., inherit: Queryable[float] = ..., jitterBasePoint: Queryable[Multiuse[Tuple[float, float, float]]] = ..., jitterRadius: Queryable[Multiuse[float]] = ..., lowerLeft: Queryable[Multiuse[Tuple[float, float, float]]] = ..., name: Queryable[str] = ..., numJitters: Queryable[Multiuse[int]] = ..., order: int = ..., particleId: int = ..., perParticleDouble: bool = ..., perParticleVector: bool = ..., position: Multiuse[Tuple[float, float, float]] = ..., shapeName: Queryable[str] = ..., upperRight: Queryable[Multiuse[Tuple[float, float, float]]] = ..., vectorValue: Tuple[float, float, float] = ...) -> Union[str, bool, float, Multiuse[float], Multiuse[Tuple[float, float, float]], Multiuse[int]]:
    """The nParticle command creates a new nParticle object from a list of
    world space points. If an nParticle object is created, the command
    returns the names of the new particle shape and its associated particle
    object dependency node. If an object was queried, the results of the
    query are returned. Per particle attributes can be queried using the
    particleId or the order of the particle in the particle array.
    If an object was edited, nothing is returned.
    Args:
        attribute (str?): Used in per particle attribute query and edit. Specifies the  
                name of the attribute being queried or edited.  
                      In query mode, this flag needs a value.  
                Properties: query, edit
        cache (bool?): Turns caching on/off for the particle shape.  
                Properties: create, query, edit
        conserve (Queryable[float]?): Conservation of momentum control (between 0 and 1).  Specifies  
                the fraction of the particle shape's existing momentum which is  
                conserved from frame to frame.  
                A value of 1 (the default) corresponds to true Newtonian physics,  
                in which momentum is conserved.  
                Properties: query, edit
        count (bool?): Returns the number of particles in the object.  
                Properties: query
        deleteCache (bool?): Deletes the particle shapes cache. This command is not undoable.  
                Properties: create
        dynamicAttrList (bool?): Returns a list of the dynamic attributes in the object.  
                Properties: query
        floatValue (float?): Used only in per particle attribute edit.  Specifies that the edit is  
                of a float attribute and must be followed by the new float value.  
                Properties: edit
        gridSpacing (Queryable[Multiuse[float]]?): Spacing between particles in the grid.  
                Properties: create, query, multiuse
        inherit (Queryable[float]?): Inherit this fraction (0. 1) of emitting object's velocity.  
                Properties: query, edit
        jitterBasePoint (Queryable[Multiuse[Tuple[float, float, float]]]?): Base point (center point) for jitters.  The command will create  
                one swatch of jitters for each base point.  It will pair up  
                other flags with base points in the order they are given in the  
                command line.  If not enough instances of the other flags are  
                availble, the last one on the line with be used for all other  
                instances of -jpb.  
                Properties: create, query, multiuse
        jitterRadius (Queryable[Multiuse[float]]?): Max radius from the center to place the particle instances.  
                Properties: create, query, multiuse
        lowerLeft (Queryable[Multiuse[Tuple[float, float, float]]]?): Lower left point of grid.  
                Properties: create, query, multiuse
        name (Queryable[str]?): name of particle object  
                Properties: query, edit
        numJitters (Queryable[Multiuse[int]]?): Number of jitters (instances) per particle.  
                Properties: create, query, multiuse
        order (int?): Used in per particle attribute query and edit. Specifies the  
                zero-based order (index) of the particle whose attribute is being  
                queried  or edited in the  
                particle array. Querying the value of a per particle attribute  
                requires the -attribute and -id or -order flags and their arguments  
                to precede the -q flag.  
                      In query mode, this flag needs a value.  
                Properties: query, edit
        particleId (int?): Used in per particle attribute query and edit. Specifies the  
                id of the particle whose attribute is being queried or edited.  
                Querying the value of a per particle attribute  
                requires the -attribute and -id or -order flags and their arguments  
                to precede the -q flag.  
                      In query mode, this flag needs a value.  
                Properties: query, edit
        perParticleDouble (bool?): Returns a list of the per-particle double attributes,  
                excluding initial-state, cache, and information-only attributes.  
                Properties: query
        perParticleVector (bool?): Returns a list of the per-particle vector attributes,  
                excluding initial-state, cache, and information-only attributes.  
                Properties: query
        position (Multiuse[Tuple[float, float, float]]?): World-space position of each particle.  
                Properties: multiuse
        shapeName (Queryable[str]?): Specify the shape name used for geometry instancing.  
                DO not confuse this with the -n flag which names the particle object.  
                Properties: query, edit
        upperRight (Queryable[Multiuse[Tuple[float, float, float]]]?): Upper right point of grid.  
                Properties: create, query, multiuse
        vectorValue (Tuple[float, float, float]?): Used only in per particle attribute edit.  Specifies that the edit is  
                of a vector attribute and must be followed by all three float values  
                for the vector.  
                Properties: edit

    Returns:
        str: The name of the nParticle object created

    Example:
    """

