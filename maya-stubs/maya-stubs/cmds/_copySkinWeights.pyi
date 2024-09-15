from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def copySkinWeights(*args: str, edit: bool = ..., query: bool = ..., destinationSkin: Queryable[str] = ..., influenceAssociation: Queryable[Multiuse[str]] = ..., mirrorInverse: bool = ..., mirrorMode: Queryable[str] = ..., noBlendWeight: bool = ..., noMirror: bool = ..., normalize: bool = ..., sampleSpace: Queryable[int] = ..., selectedComponents: bool = ..., smooth: bool = ..., sourceSkin: Queryable[str] = ..., surfaceAssociation: Queryable[str] = ..., uvSpace: Queryable[Tuple[str, str]] = ...) -> Union[bool, str, Multiuse[str], int, Tuple[str, str]]:
    """Command to copy or mirror the skinCluster weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.skinCluster, duplicate, mirror
    Args:
        destinationSkin (Queryable[str]?): Specify the destination skin shape  
                Properties: create, query, edit
        influenceAssociation (Queryable[Multiuse[str]]?): The influenceAssociation flag controls how the influences on the source and target skins  
                are matched up. The flag can be included multiple times to specify multiple association  
                schemes that will be invoked one after the other until all influences have been matched  
                up. Supported values are "closestJoint", "closestBone", "label", "name", "oneToOne". The  
                default is closestJoint.  
                Properties: create, query, edit, multiuse
        mirrorInverse (bool?): Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.  
                Properties: create, query, edit
        mirrorMode (Queryable[str]?): The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.  
                Properties: create, query, edit
        noBlendWeight (bool?): When the no blend flag is used, the blend weights on the skin cluster will not be copied across to  
                the destination.  
                Properties: create, query, edit
        noMirror (bool?): When the no mirror flag is used, the weights are copied instead of mirrored.  
                Properties: create, query, edit
        normalize (bool?): Normalize the skin weights.  
                Properties: create, query, edit
        sampleSpace (Queryable[int]?): Selects which space the attribute transfer is performed in.  
                0 is world space, 1 is model space. The default is world space.  
                Properties: create, query, edit
        selectedComponents (bool?): The selectedComponents flag can be used in combination with the sourceSkin and destinationSkin  
                flags to specify that only the skin weights on the selected components should be copied.  
                Properties: create, query, edit
        smooth (bool?): When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.  
                Properties: create, query, edit
        sourceSkin (Queryable[str]?): Specify the source skin shape  
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

