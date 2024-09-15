from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def xform(*args: str, query: bool = ..., absolute: bool = ..., boundingBox: bool = ..., boundingBoxInvisible: bool = ..., centerPivots: bool = ..., centerPivotsOnComponents: bool = ..., deletePriorHistory: bool = ..., euler: bool = ..., matrix: Queryable[Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]] = ..., objectSpace: bool = ..., pivots: Queryable[Tuple[float, float, float]] = ..., preserve: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotateAxis: Queryable[Tuple[float, float, float]] = ..., rotateOrder: Queryable[str] = ..., rotatePivot: Queryable[Tuple[float, float, float]] = ..., rotateTranslation: Queryable[Tuple[float, float, float]] = ..., rotation: Queryable[Tuple[float, float, float]] = ..., scale: Queryable[Tuple[float, float, float]] = ..., scalePivot: Queryable[Tuple[float, float, float]] = ..., scaleTranslation: Queryable[Tuple[float, float, float]] = ..., shear: Queryable[Tuple[float, float, float]] = ..., translation: Queryable[Tuple[float, float, float]] = ..., worldSpace: bool = ..., worldSpaceDistance: bool = ..., zeroTransformPivots: bool = ...) -> Union[bool, Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], Tuple[float, float, float], str]:
    """This command can be used query/set any element in a
    transformation node. It can also be used to query some values
    that cannot be set directly such as the transformation matrix
    or the bounding box. It can also set both pivot points to
    convenient values.All values are specified in transformation coordinates.
    (attribute-space)In addition, the attributes are applied/returned in the order in
    which they appear in the flags section. (which corresponds to the
    order they appear in the transformation matrix as given below)move, rotate, scaleThe transformation matrix for a node is built by post-multiplying
    the following matrices in the given order (Note: rotations are
    applied according to the rotation order parameter and the 6
    different rotation possibilities are not shown below)
    Args:
        absolute (bool?): perform absolute transformation (default)  
                Properties: create
        boundingBox (bool?): Returns the bounding box of an object. The values  
                returned are in the following order:  
                xmin ymin zmin xmax ymax zmax.  
                Properties: query
        boundingBoxInvisible (bool?): Returns the bounding box of an object.  
                This includes the bounding boxes of all invisible  
                children which are not included using the  
                boundingBox flag. The values returned are in  
                following order: xmin ymin zmin xmax ymax zmax.  
                Properties: query
        centerPivots (bool?): Set pivot points to the center of the object's  
                bounding box. (see -p flag)  
                Properties: create
        centerPivotsOnComponents (bool?): Set pivot points to the center of the component's  
                bounding box. (see -p flag)  
                Properties: create
        deletePriorHistory (bool?): If true then delete the construction history before the operation is performed.  
                Properties: create
        euler (bool?): modifer for -relative flag that specifies rotation  
                values should be added to current XYZ rotation values.  
                Properties: create
        matrix (Queryable[Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]]?): Sets/returns the composite transformation matrix.  
                *Note* the matrix is represented by 16 double  
                arguments that are specified in row order.  
                Properties: create, query
        objectSpace (bool?): treat values as object-space transformation values  
                (only works for pivots, translations, rotation, rotation  
                axis, matrix, and bounding box flags)  
                Properties: create, query
        pivots (Queryable[Tuple[float, float, float]]?): convenience method that changes both the rotate and  
                scale pivots simultaneously. (see -rp -sp flags for  
                more info)  
                Properties: create, query
        preserve (bool?): preserve overall transformation. used to prevent object  
                from "jumping" when changing pivots or rotation order. the  
                default value is true. (used with -sp, -rp, -roo, -cp, -ra)  
                Properties: create
        preserveUV (bool?): When true, UV values on rotated components are projected across the rotation  
                in 3d space. For small edits, this will freeze the world space texture mapping  
                on the object.  
                When false, the UV values will not change for a selected vertices.  
                Default is false.  
                Properties: create
        reflection (bool?): To move the corresponding symmetric components also.  
                Properties: create
        reflectionAboutBBox (bool?): Sets the position of the reflection axis  at the geometry bounding box  
                Properties: create
        reflectionAboutOrigin (bool?): Sets the position of the reflection axis  at the origin  
                Properties: create
        reflectionAboutX (bool?): Specifies the X=0 as reflection plane  
                Properties: create
        reflectionAboutY (bool?): Specifies the Y=0 as reflection plane  
                Properties: create
        reflectionAboutZ (bool?): Specifies the Z=0 as reflection plane  
                Properties: create
        reflectionTolerance (float?): Specifies the tolerance to findout the corresponding reflected components  
                Properties: create
        relative (bool?): perform relative transformation  
                Properties: create
        rotateAxis (Queryable[Tuple[float, float, float]]?): rotation axis orientation (when used with  
                the -p flag the overall rotation is preserved  
                by modifying the rotation to compensate for  
                the axis rotation)  
                Properties: create, query
        rotateOrder (Queryable[str]?): rotation order (when used with the -p flag the  
                overall rotation is preserved by modifying the  
                local rotation to be quivalent to the old one)  
                Valid values for this flag are  
                <xyz | yzx | zxy | xzy | yxz | zyx>  
                Properties: create, query
        rotatePivot (Queryable[Tuple[float, float, float]]?): rotate pivot point transformation (when used with  
                the -p flag the overall transformation is preserved  
                by modifying the rotation translation)  
                Properties: create, query
        rotateTranslation (Queryable[Tuple[float, float, float]]?): rotation translation  
                Properties: create, query
        rotation (Queryable[Tuple[float, float, float]]?): rotation transformation  
                Properties: create, query
        scale (Queryable[Tuple[float, float, float]]?): scale transformation  
                Properties: create, query
        scalePivot (Queryable[Tuple[float, float, float]]?): scale pivot point transformation (when used with  
                the -p flag the overall transformation is preserved  
                by modifying the scale translation)  
                Properties: create, query
        scaleTranslation (Queryable[Tuple[float, float, float]]?): scale translation  
                Properties: create, query
        shear (Queryable[Tuple[float, float, float]]?): shear transformation.  
                The values represent the shear <xy,xz,yz>  
                Properties: create, query
        translation (Queryable[Tuple[float, float, float]]?): translation  
                Properties: create, query
        worldSpace (bool?): (works for pivots, translations, rotation, rotation  
                axis, matrix, and bounding box flags). Note that, when  
                querying the scale, that this calculation is cumulative  
                and is only valid if there are all uniform scales and  
                no rotation. In a hierarchy with non-uniform scale  
                and rotation, this value may not correspond entirely with  
                the perceived global scale.  
                Properties: create, query
        worldSpaceDistance (bool?): Values for -sp, -rp, -st, -rt, -t, -piv flags  
                are treated as world space distances to move along the  
                local axis. (where the local axis depends on whether  
                the command is operating in local-space or object-space.  
                This flag has no effect for world space.  
                Properties: create, query
        zeroTransformPivots (bool?): reset pivot points and pivot translations without  
                changing the overall matrix by applying these values  
                into the translation channel.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

