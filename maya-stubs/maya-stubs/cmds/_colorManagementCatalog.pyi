from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorManagementCatalog(*, addTransform: str = ..., editUserTransformPath: str = ..., listSupportedExtensions: bool = ..., listTransformConnections: bool = ..., path: str = ..., queryUserTransformPath: bool = ..., removeTransform: str = ..., transformConnection: str = ..., type: str = ...) -> bool:
    """This non-undoable action performs additions and removals of custom color
    transforms from the Autodesk native color transform catalog.  Once a custom
    color transform has been added to the catalog, it can be used in the same way
    as the builtin Autodesk native color transforms.color, management
    Args:
        addTransform (str?): Add transform to collection.  
                Properties: create
        editUserTransformPath (str?): Edit the user transform directory. By changing the directory, all custom  
                transforms currently added could be changed, and new ones could appear.  
                Properties: create
        listSupportedExtensions (bool?): List the file extensions that are supported by add transform.  This list is  
                valid for all transform types, and therefore this flag does not require  
                use of the type flag.  
                Properties: create
        listTransformConnections (bool?): List the transforms that can be used as source (for "view" and "output" types)  
                or destination (for "input" and "rendering space" types) to connect a custom  
                transform to the rest of the transform collection.  
                Properties: create
        path (str?): In addTransform mode, the path to the transform data file.  
                Properties: create
        queryUserTransformPath (bool?): Query the user transform directory.  
                Properties: create
        removeTransform (str?): Remove transform from collection.  
                Properties: create
        transformConnection (str?): In addTransform mode, an existing transform to which the added transform  
                will be connected. For an input transform or rendering space transform, this  
                will be a destination. For a view or output transform, this will be a source.  
                Properties: create
        type (str?): The type of transform added, removed, or whose transform connections are to  
                be listed. Must be one of "view", "rendering space", "input", or "output".  
                Properties: create

    Returns:
        bool:

    Example:
    """

