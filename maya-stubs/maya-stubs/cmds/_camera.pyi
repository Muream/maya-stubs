from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def camera(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., aspectRatio: Queryable[float] = ..., cameraScale: Queryable[float] = ..., centerOfInterest: Queryable[float] = ..., clippingPlanes: bool = ..., depthOfField: bool = ..., displayFieldChart: bool = ..., displayFilmGate: bool = ..., displayFilmOrigin: bool = ..., displayFilmPivot: bool = ..., displayGateMask: bool = ..., displayResolution: bool = ..., displaySafeAction: bool = ..., displaySafeTitle: bool = ..., fStop: Queryable[float] = ..., farClipPlane: Queryable[float] = ..., farFocusDistance: Queryable[float] = ..., filmFit: Queryable[str] = ..., filmFitOffset: Queryable[float] = ..., filmRollOrder: Queryable[str] = ..., filmRollValue: Queryable[float] = ..., filmTranslateH: Queryable[float] = ..., filmTranslateV: Queryable[float] = ..., focalLength: Queryable[float] = ..., focusDistance: Queryable[float] = ..., homeCommand: Queryable[str] = ..., horizontalFieldOfView: Queryable[float] = ..., horizontalFilmAperture: Queryable[float] = ..., horizontalFilmOffset: Queryable[float] = ..., horizontalPan: Queryable[float] = ..., horizontalRollPivot: Queryable[float] = ..., horizontalShake: Queryable[float] = ..., journalCommand: bool = ..., lensSqueezeRatio: Queryable[float] = ..., lockTransform: bool = ..., motionBlur: bool = ..., name: Queryable[str] = ..., nearClipPlane: Queryable[float] = ..., nearFocusDistance: Queryable[float] = ..., orthographic: bool = ..., orthographicWidth: Queryable[float] = ..., overscan: Queryable[float] = ..., panZoomEnabled: bool = ..., position: Queryable[Tuple[float, float, float]] = ..., postScale: Queryable[float] = ..., preScale: Queryable[float] = ..., renderPanZoom: bool = ..., rotation: Queryable[Tuple[float, float, float]] = ..., shakeEnabled: bool = ..., shakeOverscan: Queryable[float] = ..., shakeOverscanEnabled: bool = ..., shutterAngle: Queryable[float] = ..., startupCamera: bool = ..., stereoHorizontalImageTranslate: Queryable[float] = ..., stereoHorizontalImageTranslateEnabled: bool = ..., verticalFieldOfView: Queryable[float] = ..., verticalFilmAperture: Queryable[float] = ..., verticalFilmOffset: Queryable[float] = ..., verticalLock: bool = ..., verticalPan: Queryable[float] = ..., verticalRollPivot: Queryable[float] = ..., verticalShake: Queryable[float] = ..., worldCenterOfInterest: Queryable[Tuple[float, float, float]] = ..., worldUp: Queryable[Tuple[float, float, float]] = ..., zoom: Queryable[float] = ...) -> Union[List[str], float, bool, str, Tuple[float, float, float]]:
    """Create, edit, or query a camera with the specified properties.The resulting camera can be repositioned using the viewPlace
    command. Many of the camera settings only affect the resulting
    rendered image. E.g. the F/Stop, shutter speed, the film related
    options, etc. Scaling the camera icon does not change any camera
    properties.
    Args:
        aspectRatio (Queryable[float]?): The ratio of the film back width to the film back height.  
                Properties: create, query, edit
        cameraScale (Queryable[float]?): Scale the camera.  
                Properties: create, query, edit
        centerOfInterest (Queryable[float]?): Set the linear distance from the camera's eye point to the  
                center of interest.  
                Properties: create, query, edit
        clippingPlanes (bool?): Activate manual clipping planes.  
                Properties: create, query, edit
        depthOfField (bool?): Determines whether a depth of field calculation is performed  
                to give varying focus depending on the distance of the  
                objects.  
                Properties: create, query, edit
        displayFieldChart (bool?): Activate display of the video field chart when looking through  
                the camera.  
                Properties: create, query, edit
        displayFilmGate (bool?): Activate display of the film gate icons when looking through  
                the camera.  
                Properties: create, query, edit
        displayFilmOrigin (bool?): Activate the display of the film origin guide when  
                looking through the camera.  
                Properties: create, query, edit
        displayFilmPivot (bool?): Activate display of the film pivot guide when looking  
                through the camera.  
                Properties: create, query, edit
        displayGateMask (bool?): Display the gate mask, file or resolution, as a shaded area  
                to the edge of the viewport.  
                Properties: create, query, edit
        displayResolution (bool?): Activate display of the current rendering resolution (as  
                defined in the render globals) when looking through the  
                camera.  
                Properties: create, query, edit
        displaySafeAction (bool?): Activate display of the video Safe Action guide  
                when looking through the camera.  
                Properties: create, query, edit
        displaySafeTitle (bool?): Activate display of the video Safe Title guide  
                when looking through the camera.  
                Properties: create, query, edit
        fStop (Queryable[float]?): A real lens normally contains a diaphragm or other stop which  
                blocks some of the light that would otherwise pass through  
                it. This stop is usually approximately round, and its diameter  
                as seen from the front of the lens is called the lens  
                diameter. The lens diameter is often described by its relation  
                to the focal length of the lens. A lens whose diameter is  
                one-eighth its local length is said to have an F-stop of  
                8. This is an optical property of the lens.  
                Properties: create, query, edit
        farClipPlane (Queryable[float]?): Specify the distance to the far clipping plane.  
                Properties: create, query, edit
        farFocusDistance (Queryable[float]?): Linear distance to the far focus plane.  
                Properties: create, query, edit
        filmFit (Queryable[str]?): This describes how the digital image (in pixels) relates to  
                the film back. Since the film back is defined in terms of real  
                numbers with some arbitrary film aspect, and the digital image  
                is defined in integer pixels with an equally arbitrary (and  
                different) resolution, relating the two can get  
                complicated. There are 4 choices:   
              
                horizontal   
                In this case the digital image is made to fit the film  
                back exactly in the horizontal direction. This then gives each  
                pixel a horizontal size = (film back width) / (horizontal  
                resolution). The pixel height is then = (pixel width) / (pixel  
                aspect ratio). Now that the pixel has a size, resolution gives  
                us a complete image. That image will match the film back  
                exactly in width. It will almost never match in height, either  
                being too tall or too short. By playing with the numbers you  
                can get it pretty close though.  
                vertical  
                This is the same idea as horizontal fit, only applied  
                vertically. Thus the digital image will match the film back  
                exactly in height, but miss in width.  
                fill  
                This is a convenience item. The system calculates both  
                horizontal and vertical fits and then applies the one that  
                makes the digital image larger than the film back.  
                overscan  
                Overscanning the film gate in the camera view allows us  
                to choreograph action outside of the frustum from within the  
                camera view without having to resort to a dolly or zoom. This  
                feature is also essential for animating image planes.  
                Properties: create, query, edit
        filmFitOffset (Queryable[float]?): Since we know from the above that the digital image may not  
                match the film back exactly, we now have the question of how  
                to position one relative to the other. Thus fit  
                offset. Normally the centers are aligned. Fit offset lets you  
                move the smaller image within the larger one. Specify the  
                distance for film offset (inches).  
                Properties: create, query, edit
        filmRollOrder (Queryable[str]?): Specifies how the roll is applied with respect to the  
                pivot value.  
              
                Rotate-Translate  
                The film back is first rotated then translated by the  
                pivot point value.  
                Translate-Rotate  
                The film back is first translated then rotated by the  
                film roll value.  
                Properties: create, query, edit
        filmRollValue (Queryable[float]?): This specifies that amount of rotation around the film back.  
                The roll value is specified in degrees. The rotation occurs around  
                the specified pivot point. This value is used to compute a film  
                roll matrix, which is a component of the post-projection matrix.  
                Properties: create, query, edit
        filmTranslateH (Queryable[float]?): The horizontal film translation. Values are normalized to  
                the viewing area.  
                Properties: create, query, edit
        filmTranslateV (Queryable[float]?): The vertical film translation. Values are normalized to the  
                viewing area.  
                Properties: create, query, edit
        focalLength (Queryable[float]?): This is the distance along the lens axis between the lens and  
                the film plane when "focal distance" is infinitely large. This  
                is an optical property of the lens. This double precision  
                parameter is always specified in millimeters.  
                Properties: create, query, edit
        focusDistance (Queryable[float]?): Set the focus at a certain distance in front of the camera.  
                Properties: create, query, edit
        homeCommand (Queryable[str]?): Specify the command to execute when "viewSet -home" is applied  
                to this camera. All occurances of "%camera" will be replaced  
                with the cameras name before viewSet runs the command.  
                Properties: create, query, edit
        horizontalFieldOfView (Queryable[float]?): This is the film back width as seen by the lens when focused  
                at infinity (ie., focal length away) measured as an  
                angle. Note that it has nothing to do with pixels or the  
                digital image or any aspects. Angle of view is a derived  
                field, that is, it is not used internally by Alias and can be  
                completely determined from other information. It is included  
                as a convenience for the user. Its derivation is aov = 2 *  
                atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw"  
                is the film back width and "f" is the focal length.  
                Properties: create, query, edit
        horizontalFilmAperture (Queryable[float]?): The horizontal width of the camera's film plane. The camera's  
                film is located on the film plane. The extent of the film  
                which will be exposed to an image of the scene in front of the  
                lens is limited to a rectangular area described by the film  
                back. This double precision parameter is always specified in  
                inches.  
                Properties: create, query, edit
        horizontalFilmOffset (Queryable[float]?): Horizontal offset from the center of the film back. Normally  
                the film back will be centered on the lens axis. However, this  
                need not be so. Film offset is the displacement of the center  
                of the film back from the lens axis, also measured in  
                inches. Note that offsetting the film back will distort the  
                image, but will not alter the focus. This double precision  
                parameter is always specified in inches.  
                Properties: create, query, edit
        horizontalPan (Queryable[float]?): Horizontal 2D camera pan (inches)  
                Properties: create, query, edit
        horizontalRollPivot (Queryable[float]?): The horizontal pivot point from the center of the film back.  
                The pivot point is used during rotation of the film back.  The pivot  
                is the point where the rotation occurs around. This double precision  
                parameter corresponds to the normalized viewport. This value is a  
                part of the post projection matrix.  
                Properties: create, query, edit
        horizontalShake (Queryable[float]?): Another horizontal offset from the center of the film back,  
                which can be used and stored on the camera in addition to the  
                horizonal film offset attribute.  This allows for film-based  
                camera shake internal to the camera.  This works in exactly the same  
                units and coordinates that the film offset attribute does.  
                The effect of this attribute is toggled by the shake enabled attribute.  
                Properties: create, query, edit
        journalCommand (bool?): Journal interactive camera commands. Commands can be undone  
                when a camera is journaled.  
                Properties: create, query, edit
        lensSqueezeRatio (Queryable[float]?): This is presently just an information field in the camera  
                editor is meant to convey the horizontal distortion of the  
                anamorphic lens normally used with some film formats. If it  
                were used, it would do something like pixel aspect. Remember  
                however that lens distortion (intentional or not) is slightly  
                different than the output hardware's quantization. The fact  
                that a "net" distortion parameter could be used for both may  
                or may not confuse the issue.  
                Properties: create, query, edit
        lockTransform (bool?): Lock the camera. When a camera is locked, its transformation information,  
                that is, its Translate and Rotate properties cannot be adjusted, and the  
                center of interest point cannot be moved.  
                For orthographic cameras, Orthographic Width is also locked.  
                For camera groups, Aim and Up locator's translate is also locked.  
                For stereo cameras, the root camera is locked.  
                Properties: create, query, edit
        motionBlur (bool?): Determines whether the camera's image is motion blured (as  
                opposed to an object's image). For example, if you want to  
                blur the camera movement when you are performing a flyby.  
                Properties: create, query, edit
        name (Queryable[str]?): Name of the camera.  
                Properties: create, query, edit
        nearClipPlane (Queryable[float]?): Specify the distance to the NEAR clipping plane.  
                Properties: create, query, edit
        nearFocusDistance (Queryable[float]?): Linear distance to the near focus plane.  
                Properties: create, query, edit
        orthographic (bool?): Activate the orthographic camera.  
                Properties: create, query, edit
        orthographicWidth (Queryable[float]?): Set the orthographic projection width.  
                Properties: create, query, edit
        overscan (Queryable[float]?): Set the percent of overscan.  
                Properties: create, query, edit
        panZoomEnabled (bool?): Toggle camera 2D pan and zoom  
                Properties: create, query, edit
        position (Queryable[Tuple[float, float, float]]?): Three linear values can be specified to translate the camera.  
                Properties: create, query, edit
        postScale (Queryable[float]?): The post-scale value.  This value multiplied against  
                the computed projection matrix. It is applied after the  
                the film roll.  
                Properties: create, query, edit
        preScale (Queryable[float]?): The pre-scale value. The value is multiplied against  
                the computed projection matrix. It is applied before the film  
                roll.  
                Properties: create, query, edit
        renderPanZoom (bool?): Toggle camera 2D pan and zoom in render  
                Properties: create, query, edit
        rotation (Queryable[Tuple[float, float, float]]?): Three angular values can be specified to rotate the camera.  
                Properties: create, query, edit
        shakeEnabled (bool?): Toggles the effect of the horizontal and vertical shake  
                attributes.  
                Properties: create, query, edit
        shakeOverscan (Queryable[float]?): Controls the amount of overscan in the output rendered image.  
                For use when adding film-based camera shake.  Acts as a multiplier  
                to the film aperture on the camera.  
                Properties: create, query, edit
        shakeOverscanEnabled (bool?): Toggles the effect of the shake overscan attribute.  
                Properties: create, query, edit
        shutterAngle (Queryable[float]?): Specify the shutter angle (degrees).  
                Properties: create, query, edit
        startupCamera (bool?): A startup camera is marked undeletable and implicit. This flag  
                can be used to set or query the startup state of a  
                camera. There must always be at least one startup camera.  
                Properties: create, query, edit
        stereoHorizontalImageTranslate (Queryable[float]?): A film-back offset for use in stereo camera rigs.  
                Properties: create, query, edit
        stereoHorizontalImageTranslateEnabled (bool?): Toggles the effect of the stereo HIT attribute.  
                Properties: create, query, edit
        verticalFieldOfView (Queryable[float]?): Set the vertical field of view.  
                Properties: create, query, edit
        verticalFilmAperture (Queryable[float]?): The vertical height of the camera's film plane. This double  
                precision parameter is always specified in inches.  
                Properties: create, query, edit
        verticalFilmOffset (Queryable[float]?): Vertical offset from the center of the film back. This double  
                precision parameter is always specified in inches.  
                Properties: create, query, edit
        verticalLock (bool?): Lock the size of the vertical film aperture.  
                Properties: create, query, edit
        verticalPan (Queryable[float]?): Vertical 2D camera pan (inches)  
                Properties: create, query, edit
        verticalRollPivot (Queryable[float]?): Vertical pivot point used for rotating the film back. This  
                double precision parameter corresponds to the normalized viewport.  
                This value is used to compute the film roll matrix, which is a  
                component of the post projection matrix.  
                Properties: create, query, edit
        verticalShake (Queryable[float]?): Vertical offset from the center of the film back.  See horizontal  
                shake attribute description.  This is toggled by the shake enabled  
                attribute.  
                Properties: create, query, edit
        worldCenterOfInterest (Queryable[Tuple[float, float, float]]?): Camera world center of interest point.  
                Properties: create, query, edit
        worldUp (Queryable[Tuple[float, float, float]]?): Camera world up vector.  
                Properties: create, query, edit
        zoom (Queryable[float]?): The percent over the film viewable frustum to display  
                Properties: create, query, edit

    Returns:
        List[str]: (transform name and shape name)

    Example:
    """

