from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyColorSet(*args: str, edit: bool = ..., query: bool = ..., allColorSets: bool = ..., clamped: bool = ..., colorSet: Queryable[str] = ..., copy: bool = ..., create: bool = ..., currentColorSet: bool = ..., currentPerInstanceSet: bool = ..., delete: bool = ..., newColorSet: Queryable[str] = ..., perInstance: bool = ..., rename: bool = ..., representation: Queryable[str] = ..., shareInstances: bool = ..., unshared: bool = ...) -> Union[bool, str]:
    """Command to do the following to color sets:poly, colorSet, currentColorSet, renameColorSet, deleteColorSet, copyColorSet, createColorSet
    Args:
        allColorSets (bool?): This flag when used in a query will return a list of all  
                of the color set names  
                Properties: create, query, edit
        clamped (bool?): This flag specifies if the color set will truncate any value that is  
                outside 0 to 1 range.  
                Properties: create, query, edit
        colorSet (Queryable[str]?): Specifies the name of the color set that this command needs to work on.  
                This flag has to be specified for this command to do anything meaningful  
                other than query the current color set.  
                Properties: create, query, edit
        copy (bool?): This flag when used will result in the copying of the color set corresponding  
                to name specified with the colorSet flag to the colorSet corresponding  
                to the name specified with the newcolorSet flag  
                Properties: create, query, edit
        create (bool?): This flag when used will result in the creation of an empty color set  
                corresponding to the name specified with the colorSet flag. If  
                a color set with that name already exists, then no new color set will  
                be created.  
                Properties: create, query, edit
        currentColorSet (bool?): This flag when used will set the current color set that the object needs to  
                work on, to be the color set corresponding to the name specified with the  
                colorSet flag. This does require that a colorSet with the specified name exist.  
                When queried, this returns the current color set.  
                Properties: create, query, edit
        currentPerInstanceSet (bool?): This is a query-only flag for use when the current color set is a per-instance  
                color set family. This returns the member of the set family that corresponds  
                to the currently select instance.  
                Properties: query, edit
        delete (bool?): This flag when used will result in the deletion of the color set corresponding  
                to the name specified with the colorSet flag.  
                Properties: create, query, edit
        newColorSet (Queryable[str]?): Specifies the name that the color set corresponding to the name specified with  
                the colorSet flag, needs to be renamed to.  
                Properties: create, query, edit
        perInstance (bool?): This flag can be used in conjunction with the create flag to indicate  
                whether or not the color set is per-instance. When you create a per-instance  
                color set, the set will be applied as shared between all selected instances  
                of the shape unless the unshared flag is used. The perInstance flag can  
                be used in query mode with the currentColorSet or allColorSets flag to indicate  
                that the set family names (i.e. not containing instance identifiers) will  
                be returned by the query.  
                			In query mode, this flag can accept a value.  
                Properties: create, query, edit
        rename (bool?): This flag when used will result in the renaming of the color set corresponding  
                to the name specified with the colorSet flag to the name specified using the  
                newColorSet flag.  
                Properties: create, query, edit
        representation (Queryable[str]?): This flag corresponds to the color channels to used, for example  
                A(alpha only), RGB, and RGBA.  
                Properties: create, query, edit
        shareInstances (bool?): This flag is used to modify the sharing of per-instance color sets within  
                a given color set family so that all selected instances share the specified  
                set. In query mode, it returns a list of the instances that share the  
                set specified by the colorSet flag.  
                Properties: create, query, edit
        unshared (bool?): This flag can be used in conjunction with the create and perInstance flags  
                to indicate that the newly created per-instance set should be created with  
                a separate set per instance.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

