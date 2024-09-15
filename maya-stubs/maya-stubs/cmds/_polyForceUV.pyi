from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyForceUV(*args: str, cameraProjection: bool = ..., createNewMap: bool = ..., flipHorizontal: bool = ..., flipVertical: bool = ..., g: bool = ..., local: bool = ..., normalize: str = ..., numItems: int = ..., preserveAspectRatio: bool = ..., unitize: bool = ..., unshare: bool = ..., uvSetName: str = ...) -> bool:
    """A set of functionalities can be called through this command.  The input for
    this command is a set of faces.  Based on the arguments passed, the UVs for
    these selected faces can be created.Based on the current view direction/orientation, the UVs are generated and
    assigned to the faces.  Any previously assigned UV information will be lost.The UVs are computed based on the plane defined by the user, and is applied
    to the selected faces.  This tool has 2 phases.  In the first phase,
    the faces to be mapped (faces to which UVs are to be created) are selected.
    In the second phase, the points (vertices, CVs) that define the
    projecting plane are selected.  Any previously assigned UV information will
    be lost.A new set of unitized UVs are generated and assigned to the faces.
            Any previously assigned UV information will be lost.Force the specified UV to be unshared by possibly creating new UVs.  Any previously assigned UV information will be lost.poly, uv, normalize, unitize, flip, bestPlane
    Args:
        cameraProjection (bool?): Project the UVs based on the camera position/orientation  
                Properties: create
        createNewMap (bool?): Create new map if it does not exist.  
                Properties: create
        flipHorizontal (bool?): OBSOLETE flag.  Use polyFlipUV instead.  
                Properties: create
        flipVertical (bool?): OBSOLETE flag.  Use polyFlipUV instead.  
                Properties: create
        g (bool?): OBSOLETE flag.  
                Properties: create
        local (bool?): OBSOLETE flag.  
                Properties: create
        normalize (str?): OBSOLETE flag.  Use polyNormalizeUV instead.  
                Properties: create
        numItems (int?): This flag is only used for the best plane texturing  
                        of polygonal faces.  This flag should be followed by a  
                        selection list. If not specified, the selected objects will  
                        be used (in the order they were selected).   
                        This flag specifies the number of items (leading) in the  
                        selection list that should be used for the mapping.  
                        The trailing items will be used for computing the  
                        plane (See example below).  The best plane texturing  
                        is better suited for using interactively from within its context.  
                        You can type "BestPlaneTexturingTool"  
                        in the command window OR (EditPolygons->Texture->BestPlaneTexturing  
                        from the Menu) to enter its context.  
                Properties: create
        preserveAspectRatio (bool?): OBSOLETE flag.  
                Properties: create
        unitize (bool?): To unitize the UVs of the selected faces  
                Properties: create
        unshare (bool?): To unshare tye specified UV  
                Properties: create
        uvSetName (str?): Specifies name of the uv set to work on  
                Properties: create

    Returns:
        bool: true/false

    Example:
    """

