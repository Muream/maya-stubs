from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def substituteGeometry(*args: str, disableNonSkinDeformers: bool = ..., newGeometryToLayer: bool = ..., oldGeometryToLayer: bool = ..., reWeightDistTolerance: float = ..., retainOldGeometry: bool = ...) -> str:
    """This command can be used to replace the geometry which is already connected
    to deformers with a new geometry. The weights on the old geometry will be
    retargeted to the new geometry.deformers, replace, geometry, skin
    Args:
        disableNonSkinDeformers (bool?): This flag controls the state of deformers other than skin deformers after  
                the substitution has taken place. If the flag is true then non-skin deformer  
                nodes are left in a disabled state at the completion of the command.  
                Default value is false.  
                Properties: create
        newGeometryToLayer (bool?): Create a new layer for the new geometry.  
                Properties: create
        oldGeometryToLayer (bool?): Create a new layer and move the old geometry to this layer  
                Properties: create
        reWeightDistTolerance (float?): Specify the distance tolerance value to be used for retargeting weights.  
                While transferring weights the command tries to find the corresponding  
                vertices by overlapping the geometries with all deformers disabled. Sometimes  
                this results in selection of unrelated vertices. (Example when a hole in  
                the old geometry has been filled with new vertices in the new geometry.)  
                This distance tolerance value is used to detect this kind of faults and  
                either ignore these cases or to vary algorithm to find more corresponding  
                vertices.  
                Properties: create
        retainOldGeometry (bool?): A copy of the old geometry should be retained  
                Properties: create

    Returns:
        str: Name of shapes that were replaced

    Example:
    """

