from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def copyDeformerWeights(*args: str, edit: bool = ..., query: bool = ..., destinationDeformer: Queryable[str] = ..., destinationShape: Queryable[str] = ..., mirrorInverse: bool = ..., mirrorMode: Queryable[str] = ..., noMirror: bool = ..., smooth: bool = ..., sourceDeformer: Queryable[str] = ..., sourceShape: Queryable[str] = ..., surfaceAssociation: Queryable[str] = ..., uvSpace: Queryable[Tuple[str, str]] = ...) -> Union[bool, str, Tuple[str, str]]:
    """Command to copy or mirror the deformer weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.deformer, duplicate, mirror
    Args:
        destinationDeformer (Queryable[str]?): Specify the deformer used by the destination shape  
                Properties: create, query, edit
        destinationShape (Queryable[str]?): Specify the destination deformed shape  
                Properties: create, query, edit
        mirrorInverse (bool?): Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.  
                Properties: create, query, edit
        mirrorMode (Queryable[str]?): The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.  
                Properties: create, query, edit
        noMirror (bool?): When the no mirror flag is used, the weights are copied instead of mirrored.  
                Properties: create, query, edit
        smooth (bool?): When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.  
                Properties: create, query, edit
        sourceDeformer (Queryable[str]?): Specify the deformer whose weights should be mirrored.  When queried, returns the deformers used by the source shapes.  
                Properties: create, query, edit
        sourceShape (Queryable[str]?): Specify the source deformed shape  
                Properties: create, query, edit
        surfaceAssociation (Queryable[str]?): The surfaceAssociation flag controls how the weights are transferred between the  
                surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.  
                Properties: create, query, edit
        uvSpace (Queryable[Tuple[str, str]]?): The uvSpace flag indicates that the weight transfer should occur in UV space, based on the  
                source and destination UV sets specified.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

