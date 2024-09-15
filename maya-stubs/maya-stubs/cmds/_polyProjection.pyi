from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyProjection(*args: str, constructionHistory: bool = ..., createNewMap: bool = ..., imageCenterX: float = ..., imageCenterY: float = ..., imageScaleU: float = ..., imageScaleV: float = ..., insertBeforeDeformers: bool = ..., keepImageRatio: bool = ..., mapDirection: str = ..., projectionCenterX: float = ..., projectionCenterY: float = ..., projectionCenterZ: float = ..., projectionScaleU: float = ..., projectionScaleV: float = ..., rotateX: float = ..., rotateY: float = ..., rotateZ: float = ..., rotationAngle: float = ..., seamCorrect: bool = ..., smartFit: bool = ..., type: str = ..., uvSetName: str = ...) -> str:
    """Creates a mapping on the selected polygonal faces.  When construction
            history is created, the name of the new node is returned.  In other cases,
            the command returns nothing.poly, mapping, projection, planar, cylindrical, spherical
    Args:
        constructionHistory (bool?): Turn the construction history on or off (where applicable).  
                Properties: create
        createNewMap (bool?): Create new map if it does not exist.  
                Properties: create
        imageCenterX (float?): Specifies the X (U) translation of the projected UVs.  
                        Default is 0.5.  
                Properties: create
        imageCenterY (float?): Specifies the Y (V) translation of the projected UVs.  
                        Default is 0.5.  
                Properties: create
        imageScaleU (float?): Specifies the U scale factor of the projected UVs.  
                        Default is 1.  
                Properties: create
        imageScaleV (float?): Specifies the V scale factor of the projected UVs.  
                        Default is 1.  
                Properties: create
        insertBeforeDeformers (bool?): Specifies if the projection node should be inserted  
                        before or after deformer nodes already applied to the shape.  
                        Inserting the projection after the deformer leads to texture  
                        swimming during animation and is most often undesirable.  
                        Default is on.  
                Properties: create
        keepImageRatio (bool?): Specifies if the xy scaling in the planar projection has to be  
                        uniform.  By setting this flag, the texture aspect ratio is  
                        preserved.  This flag is ignored for cylindrical and spherical  
                        projections.  
                Properties: create
        mapDirection (str?): Specifies the direction of the projection.  By specifying this flag, the  
                        projection placement values (pcx, pcy, pcz, rx, ry, rz, psu, psv) are  
                        internally computed.  If both this flag and the projection values are  
                        specified, the projection values are ignored.  
                        Valid Values are :  
                                X                       Projects along the X Axis  
                                Y                       Projects along the Y Axis  
                                Z                       Projects along the Z Axis  
                                bestPlane       Projects on the best plane fitting the object  
                                camera          Projects along the viewing direction  
                                perspective Creates perspective projection if current camera is perspective  
                        Default is bestPlane.  
                Properties: create
        projectionCenterX (float?): Specifies the X coordinate of the center of the projection manipulator.  
                Properties: create
        projectionCenterY (float?): Specifies the Y coordinate of the center of the projection manipulator.  
                Properties: create
        projectionCenterZ (float?): Specifies the Z coordinate of the center of the projection manipulator.  
                Properties: create
        projectionScaleU (float?): Specifies the U scale component of the projection manipulator.  
                Properties: create
        projectionScaleV (float?): Specifies the V scale component of the projection manipulator.  
                Properties: create
        rotateX (float?): Specifies the X-axis rotation of the projection manipulator.  
                Properties: create
        rotateY (float?): Specifies the Y-axis rotation of the projection manipulator.  
                Properties: create
        rotateZ (float?): Specifies the Z-axis rotation of the projection manipulator.  
                Properties: create
        rotationAngle (float?): Specifies the rotation of the projected UVs in the UV space.  
                        Default is 0.  
                Properties: create
        seamCorrect (bool?): Specifies if seam correction has to be done for spherical  
                        and cylindrical projections.  This flag is ignored, if the  
                        planar projection is specified.  
                Properties: create
        smartFit (bool?): Specifies if the projection manipulator has to be placed  
                        fitting the object.  Used for cylindrical and spherical  
                        projections.  For smart fitting the planar projection, the  
                        mapDirection flag has to be used, since there are several  
                        options for smart fitting a planar projection.  
                Properties: create
        type (str?): Specify the type of mapping to be performed.  
                        Valid values for the STRING are  
                         "planar"  
                         "cylindrical"  
                         "spherical"  
                        Default is planar.  
                Properties: create
        uvSetName (str?): Specifies name of the uv set to work on.  
                Properties: create

    Returns:
        str: Name of node created

    Example:
    """

