from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def radial(*args: str, edit: bool = ..., query: bool = ..., attenuation: Queryable[float] = ..., magnitude: Queryable[float] = ..., maxDistance: Queryable[float] = ..., name: Queryable[str] = ..., perVertex: bool = ..., position: Queryable[Multiuse[Tuple[float, float, float]]] = ..., torusSectionRadius: Queryable[float] = ..., type: Queryable[float] = ..., volumeExclusion: bool = ..., volumeOffset: Queryable[Tuple[float, float, float]] = ..., volumeShape: Queryable[str] = ..., volumeSweep: Queryable[float] = ...) -> Union[str, float, bool, Multiuse[Tuple[float, float, float]], Tuple[float, float, float]]:
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
    A radial field pushes objects directly towards or directly away from it,
    like a magnet.The transform is the associated dependency node.
    Use connectDynamic to cause the field to affect a dynamic object.If fields are created, this command returns the names of each
    of the fields. If a field was queried,
    the results of the query are returned. If a field was edited, the field
    name is returned.If object names are provided or the active selection list is non-empty,
    the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the
    list is empty, the command defaults to -pos 0 0 0.Setting the -pos flag with objects named on the command line is an error.
    Args:
        attenuation (Queryable[float]?): Attentuation rate of field  
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
        type (Queryable[float]?): Type of radial field (0. 1).  This controls the algorithm by  
                which the field is attenuated. Type 1, provided for backward  
                compatibility, specifies the same algorithm as Alias |  
                Wavefront Dynamation. A value between 0 and 1 yields a linear blend.  
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

