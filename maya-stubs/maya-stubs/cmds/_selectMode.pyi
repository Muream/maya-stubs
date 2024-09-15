from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectMode(*, query: bool = ..., component: bool = ..., hierarchical: bool = ..., leaf: bool = ..., object: bool = ..., preset: bool = ..., root: bool = ..., template: bool = ...) -> bool:
    """Thecommand is used to change the selection
    mode.  Object, component, root, leaf and template modes are
    mutually exclusive.
    Args:
        component (bool?): Set component selection on. Component selection mode allows  
                filtered selection based on the component selection mask.  
                The component selection mask is the set of selection masks  
                related to objects that indicate which components are  
                selectable.  
                Properties: create, query
        hierarchical (bool?): Set hierarchical selection on. There are  
                three types of hierarchical selection: root, leaf and  
                template.  Hierarchical mode is set if root, leaf or  
                template mode is set. Setting to hierarchical mode  
                will set the mode to whichever of root, leaf, or  
                template was last on.  
                Properties: create, query
        leaf (bool?): Set leaf selection mode on.  This mode allows the leaf  
                level objects to be selected.  It is similar to object  
                selection mode but ignores the object selection mask.  
                Properties: create, query
        object (bool?): Set object selection on. Object selection mode allows  
                filtered selection based on the object selection mask.  
                The object selection mask is the set of selection masks  
                related to objects that indicate which objects are  
                selectable.  The masks are controlled by the "selectType"  
                command.  Object selection mode selects the leaf level  
                objects.  
                Properties: create, query
        preset (bool?): Allow selection of anything with the mask set,  
                independent of it being an object or a component.  
                Properties: create, query
        root (bool?): Set root selection mode on.  This mode allows  
                the root of a hierarchy to be selected by selecting  
                any of its descendents.  It ignores the object selection  
                mask.  
                Properties: create, query
        template (bool?): Set template selection mode on.  This mode allows  
                selection of templated objects.  It selects the templated  
                object closest to the root of the hierarchy.  
                Properties: create, query

    Returns:
        bool: if a query operation

    Example:
    """

