from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def addPP(*args: str, attribute: str = ...) -> List[str]:
    """Adds per-point (per-cv, per-vertex, or per-particle) attribute
    capability for an attribute of an emitter or field.  The -atr flag
    identifies the attribute.  If no attribute is named, addPP returns a
    warning and does nothing.The command adds any other necessary attributes wherever they are
    needed, and makes all necessary connections.  If any of the attributes
    already exist, the command simply connects to them.  The command also
    toggles any relevant attributes in the emitter or field to indicate
    that per-point capability is being used.The command adds a separate per-point attribute to the owning object
    for each emitter/field.  For example, for emission rate, there is a
    separate ratePP for each emitter.  These attributes are named
    according to the convention <emitter/field name><attr
    name>PP.  For example, if a particle shape owned an emitter
    "smoke", that shape would get attribute "smokeRatePP."The name of the object must be the emitter or field for which
    per-point capability is to be added (or the name of its parent
    transform).  The addPP command adds the per-point capability for that
    emitter or field but not for any others owned by the same object.  If
    per-point capability is not supported for a named object, the command
    will trigger a warning, but will continue executing for any other
    objects which were valid.If no objects are named, addPP uses any objects in the current
    selection list for which the specified attribute is applicable.  (For
    example, it would add per-point rate for all selected emitters.)If addPP detects that the owner object has left-over attributes from a
    deleted emitter, it will remove those attributes before adding the new
    ones.  Thus, you can delete the emitter, make a new one, and run addPP
    again, and addPP will clean up after the deleted emitter.  This is
    most commonly used if you have a geometry emitter and then decide to
    change the geometry.  Likewise, if addPP detects that some cvs or
    vertices have been added to the geometry, then it will expand the
    corresponding multi-attributes as necessary.  However, if it detects
    that some cvs/vertices have been removed, it will not remove any
    entries from the multi.  See the user manual for more discussion.
    Args:
        attribute (str?): Name of attribute to which you wish to add PP capability.  
                Currently the only attribute supported is rate (for emitters).  
                Properties: create

    Returns:
        List[str]: Returns names of emitters/fields for which the per-point
            capability was added for the specified attribute.

    Example:
    """

