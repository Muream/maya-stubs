from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def volumeAxis(*args: str, edit: bool = ..., query: bool = ..., alongAxis: Queryable[float] = ..., aroundAxis: Queryable[float] = ..., attenuation: Queryable[float] = ..., awayFromAxis: Queryable[float] = ..., awayFromCenter: Queryable[float] = ..., detailTurbulence: Queryable[float] = ..., directionX: Queryable[float] = ..., directionY: Queryable[float] = ..., directionZ: Queryable[float] = ..., directionalSpeed: Queryable[float] = ..., invertAttenuation: bool = ..., magnitude: Queryable[float] = ..., maxDistance: Queryable[float] = ..., name: Queryable[str] = ..., perVertex: bool = ..., position: Queryable[Multiuse[Tuple[float, float, float]]] = ..., torusSectionRadius: Queryable[float] = ..., turbulence: Queryable[float] = ..., turbulenceFrequencyX: Queryable[float] = ..., turbulenceFrequencyY: Queryable[float] = ..., turbulenceFrequencyZ: Queryable[float] = ..., turbulenceOffsetX: Queryable[float] = ..., turbulenceOffsetY: Queryable[float] = ..., turbulenceOffsetZ: Queryable[float] = ..., turbulenceSpeed: Queryable[float] = ..., volumeExclusion: bool = ..., volumeOffset: Queryable[Tuple[float, float, float]] = ..., volumeShape: Queryable[str] = ..., volumeSweep: Queryable[float] = ...) -> Union[str, float, bool, Multiuse[Tuple[float, float, float]], Tuple[float, float, float]]:
    """For each listed object, the command creates a new field.
    The field has a shape which lives in the DAG and it has an associated
    dependency node. The field is added to the list of fields owned
    by the object. Use connectDynamic to cause the field to affect a dynamic
    object. Note that if more than one object is listed, a separate field is
    created for each object.If fields are created, this command returns the names of each
    owning shape and of the field shapes themselves. If a field was queried,
    the results of the query are returned. If a field was edited, the field
    name is returned.If no object names are provided but the active selection list is non-empty,
    the command creates a field for every object in the list. If the
    list is empty, the command defaults to -pos 0 0 0.
    A volume axis field can push particles in four directions, defined with
    respect to a volume: along the axis, away from the axis or center,
    around the axis, and in a user-specified direction.  These are analogous
    to the emission speed controls of volume emitters. The volume axis field
    also contains a wind turbulence model (different from the
    turbulence field) that simulates an evolving flow of liquid or
    gas. The turbulence has a build in animation that is driven
    by a connection to a time node.The transform is the associated dependency node.
    Use connectDynamic to cause the field to affect a dynamic object.If fields are created, this command returns the names of each
    of the fields. If a field was queried,
    the results of the query are returned. If a field was edited, the field
    name is returned.If object names are provided or the active selection list is non-empty,
    the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the
    list is empty, the command defaults to -pos 0 0 0.Setting the -pos flag with objects named on the command line is an error.
    Args:
        alongAxis (Queryable[float]?): Initial velocity multiplier in the direction along  
                the central axis of the volume.  See the diagrams in  
                the documentation.  
                Properties: query, edit
        aroundAxis (Queryable[float]?): Initial velocity multiplier in the direction around  
                the central axis of the volume.  See the diagrams  
                in the documentation.  
                Properties: query, edit
        attenuation (Queryable[float]?): Attentuation rate of field  
                Properties: query, edit
        awayFromAxis (Queryable[float]?): Initial velocity multiplier in the direction away  
                from the central axis of the volume.  See the diagrams  
                in the documentation.  Used only with the cylinder, cone,  
                and torus volumes.  
                Properties: query, edit
        awayFromCenter (Queryable[float]?): Initial velocity multiplier in the direction away from  
                the center point of a cube or sphere volume. Used only with  
                the cube and sphere volumes.  
                Properties: query, edit
        detailTurbulence (Queryable[float]?): The relative intensity of a second higher frequency turbulence.  
                This can be used to create fine features in large scale flows.  
                Both the speed and the frequency on this second turbulence are  
                higher than the primary turbulence. When the detailTurbulence  
                is non-zero the simulation may run a bit slower, due to the  
                computation of a second turbulence.  
                Properties: query, edit
        directionX (Queryable[float]?): x-component of force direction.  Used with directional speed.  
                Properties: query, edit
        directionY (Queryable[float]?): y-component of force direction.  Used with directional speed.  
                Properties: query, edit
        directionZ (Queryable[float]?): z-component of force direction.  Used with directional speed.  
                Properties: query, edit
        directionalSpeed (Queryable[float]?): Adds a component of speed in the  
                direction specified by the directionX, Y, and Z attributes.  
                Properties: query, edit
        invertAttenuation (bool?): If this attribute is FALSE, the default, then the  
                attenuation makes the field's effect decrease as the  
                affected point is further from the volume's axis and  
                closer to its edge.  If the is set to TRUE, then the  
                effect of the field increases in this case, making the  
                full effect of the field felt at the volume's edge.  
                Properties: query, edit
        magnitude (Queryable[float]?): Strength of field.  
                Properties: query, edit
        maxDistance (Queryable[float]?): Maximum distance at which field is exerted.  
                -1 indicates that the field has no maximum distance.  
                Properties: query, edit
        name (Queryable[str]?): name of field  
                Properties: query, edit
        perVertex (bool?): Per-vertex application. If this flag is set true, then each  
                individual point (CV, particle, vertex,etc.) of the chosen object  
                exerts an identical copy of the force field. If this flag is set to  
                false, then the froce is exerted only from the geometric center of  
                the set of points.  
                Properties: query, edit
        position (Queryable[Multiuse[Tuple[float, float, float]]]?): Position in space (x,y,z) where you want to place a gravity field.  
                The gravity then emanates from this position in space rather  
                than from an object. Note that you can both use -pos  
                (creating a field at a position) and also provide object names.  
                Properties: query, edit, multiuse
        torusSectionRadius (Queryable[float]?): Section radius for a torus volume.  Applies only to torus.  
                Similar to the section radius in the torus modelling primitive.  
                Properties: query, edit
        turbulence (Queryable[float]?): Adds a force simulating a turbulent  
                wind that evolves over time.  
                Properties: query, edit
        turbulenceFrequencyX (Queryable[float]?): The repeats of the turbulence function in X.  
                Properties: query, edit
        turbulenceFrequencyY (Queryable[float]?): The repeats of the turbulence function in Y.  
                Properties: query, edit
        turbulenceFrequencyZ (Queryable[float]?): The repeats of the turbulence function in Z.  
                Properties: query, edit
        turbulenceOffsetX (Queryable[float]?): The translation of the turbulence function in X.  
                Properties: query, edit
        turbulenceOffsetY (Queryable[float]?): The translation of the turbulence function in Y.  
                Properties: query, edit
        turbulenceOffsetZ (Queryable[float]?): The translation of the turbulence function in Z.  
                Properties: query, edit
        turbulenceSpeed (Queryable[float]?): The rate of change of the turbulence over time.  
                The turbulence loops seamlessly every 1.0/turbulenceSpeed seconds.  
                To animate this rate attach a new time node to the time input  
                on the volumeAxisNode then animate the time value on the time node.  
                Properties: query, edit
        volumeExclusion (bool?): Volume exclusion of the field.  If true, points outside the  
                volume (defined by the volume shape attribute) are affected,  If false,  
                points inside the volume are affected.  Has no effect if volumeShape  
                is set to "none."  
                Properties: query, edit
        volumeOffset (Queryable[Tuple[float, float, float]]?): Volume offset of the field.  Volume offset translates  
                the field's volume by the specified amount from the actual  
                field location. This is in the field's local space.  
                Properties: query, edit
        volumeShape (Queryable[str]?): Volume shape of the field.  Sets/edits/queries the  
                field's volume shape attribute.  If set to any value other  
                than "none", determines a 3. D volume within which the field has effect.  
                Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."  
                Properties: query, edit
        volumeSweep (Queryable[float]?): Volume sweep of the field.  Applies only to sphere, cone,  
                cylinder, and torus.  Similar effect to the sweep attribute  
                in modelling.  
                Properties: query, edit

    Returns:
        str: Command result

    Example:
    """

