from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyUVSet(*args: str, edit: bool = ..., query: bool = ..., allUVSets: bool = ..., allUVSetsIndices: bool = ..., allUVSetsWithCount: bool = ..., copy: bool = ..., create: bool = ..., currentLastUVSet: bool = ..., currentPerInstanceUVSet: bool = ..., currentUVSet: bool = ..., delete: bool = ..., genNewUVSet: bool = ..., newUVSet: Queryable[str] = ..., perInstance: bool = ..., projections: bool = ..., rename: bool = ..., reorder: bool = ..., shareInstances: bool = ..., unshared: bool = ..., uvSet: str = ...) -> Union[bool, str]:
    """Command to do the following to uv sets:
            - delete an existing uv set.
            - rename an existing uv set.
        - create a new empty uv set.
        - copy the values from one uv set to a another
          pre-existing uv set.
            - reorder two uv sets
            - set the current uv set to a pre-existing uv set.
        - modify sharing between instances of per-instance uv sets
            - query the current uv set.
            - set the current uv set to the last uv set added to an object.
        - query the names of all uv sets.poly, uvSet, currentUVSet, renameUVSet, deleteUVSet, copyUVSet, createUVSet
    Args:
        allUVSets (bool?): This flag when used in in a query will return a list of all  
                of the uv set names  
                Properties: query, edit
        allUVSetsIndices (bool?): This flag when queried will return a list of the logical plug  
                indices of all the uv sets in the sparse uv set array.  
                Properties: query, edit
        allUVSetsWithCount (bool?): This flag when used in a query will return a list of all  
                of the uv set family names, with a count appended to the perInstance  
                sets indicating the number of instances in the uv set shared by  
                the specified or selected shape.  
                Properties: query, edit
        copy (bool?): This flag when used will result in the copying of the uv set corresponding  
                to name specified with the uvSet flag to the uvset corresponding  
                to the name specified with the newUVSet flag  
                Properties: create, query, edit
        create (bool?): This flag when used will result in the creation of an empty uv set  
                corresponding to the name specified with the uvSet flag. If  
                a uvSet with that name already exists, then no new uv set will  
                be created.  
                Properties: create, query, edit
        currentLastUVSet (bool?): This flag when used will set the current uv set that the object needs to  
                work on, to be the last uv set added to the object.  
                If no uv set exists for the object, then no uv set name will be returned.  
                Properties: create, query, edit
        currentPerInstanceUVSet (bool?): This is a query-only flag for use when the current uv set is a per-instance  
                uv set family. This returns the member of the set family that corresponds  
                to the currently select instance.  
                Properties: query, edit
        currentUVSet (bool?): This flag when used will set the current uv set that the object needs to  
                work on, to be the uv set corresponding to the name specified with the  
                uvSet flag. This does require that a uvSet with the specified name exist.  
                When queried, this returns the current uv set.  
                Properties: create, query, edit
        delete (bool?): This flag when used will result in the deletion of the uv set corresponding  
                to the name specified with the uvSet flag.  
                Properties: create, query, edit
        genNewUVSet (bool?): This is a query-only flag to generate a new unique name.  
                Properties: query, edit
        newUVSet (Queryable[str]?): Specifies the name that the uv set corresponding to the name specified with  
                the uvSet flag, needs to be renamed to.  
                Properties: create, query, edit
        perInstance (bool?): This flag can be used in conjunction with the create flag to indicate  
                whether or not the uv set is per-instance. When you create a per-instance  
                uv set, the set will be applied as shared between all selected instances  
                of the shape unless the unshared flag is used. The perInstance flag can  
                be used in query mode with the currentUVSet or allUVSets  flag to indicate  
                that the set family names (i.e. not containing instance identifiers) will  
                be returned by the query.  
                			In query mode, this flag can accept a value.  
                Properties: create, query, edit
        projections (bool?): This flag when used in a query will return a list of polygon  
                uv projection node names. The order of the list is from  
                most-recently-applied to least-recently-applied.  
                Properties: query, edit
        rename (bool?): This flag when used will result in the renaming of the uv set corresponding  
                to the name specified with the uvSet flag to the name specified using the  
                newUVSet flag.  
                Properties: create, query, edit
        reorder (bool?): This flag when used will result in the reordering of two uv sets corresponding  
                to name specified with the uvSet flag, and the uvset corresponding  
                to the name specified with the newUVSet flag  
                Properties: create, query, edit
        shareInstances (bool?): This flag is used to modify the sharing of per-instance uv sets within  
                a given uv set family so that all selected instances share the specified  
                set. In query mode, it returns a list of the instances that share the  
                set specified by the uvSet flag.  
                Properties: create, query, edit
        unshared (bool?): This flag can be used in conjunction with the create and perInstance flags  
                to indicate that the newly created per-instance set should be created with  
                a separate set per instance.  
                Properties: create, query, edit
        uvSet (str?): Specifies the name of the uv set that this command needs to work on.  
                This flag has to be specified for this command to do anything meaningful  
                other than query the current uv set.  
                			In query mode, this flag needs a value.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

