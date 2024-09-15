from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def imagePlane(*args: str, edit: bool = ..., query: bool = ..., camera: Queryable[str] = ..., counter: bool = ..., detach: bool = ..., dropFrame: bool = ..., fileName: str = ..., frameDuration: Queryable[int] = ..., height: Queryable[float] = ..., imageSize: Queryable[Tuple[int, int]] = ..., lookThrough: Queryable[str] = ..., maintainRatio: bool = ..., name: Queryable[str] = ..., negTimesOK: bool = ..., numFrames: Queryable[int] = ..., quickTime: bool = ..., showInAllViews: bool = ..., timeCode: Queryable[int] = ..., timeCodeTrack: bool = ..., timeScale: Queryable[int] = ..., twentyFourHourMax: bool = ..., width: Queryable[float] = ...) -> Union[bool, str, int, float, Tuple[int, int]]:
    """The imagePlane command allows querying of various properties of
            an image plane and any movie in use by the image plane. It also supports
            creating and edit.
            The object passed to the command may either be an imagePlane node,
            or a camera, in which case the command uses the image plane attached
            to the camera (if any). If no object is passed in, the current
            selection is used.
            Currently, most movie related queries work only on 64 bit Windows systems.image, plane
    Args:
        camera (Queryable[str]?): When creating, it will try to attach the created image plane to the specified camera.  
                If the given camera is invalid, creating will fail.  
                When querying, it will query which camera current image plane is attaching to.  
                If it has no camera attached to (free image plane), it will return an empty string.  
                When edit, it will make the image plane attach to the new specified camera.  
                If the camera given is invalid, it will do nothing.  
                When the image plane is attached to a camera, the image plane's transform node will be set identity.  
                The detach command will not restore the original position of the image plane.  
                but the undo command will restore the original position of the image plane.  
                Properties: create, query, edit
        counter (bool?): Query the 'counter' flag of the movie's timecode format.  
                If this is true, the timecode returned by the -timeCode flag will be a simple counter.  
                If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).
        detach (bool?): This flag can only be used in the edit mode, when this flag is used in edit, it will  
                detach current image plane from any camera it attaches to and make it a free image plane.  
                Properties: edit
        dropFrame (bool?): Query the 'drop frame' flag of the movie's timecode format.  
                Properties: query
        fileName (str?): Set the image name for image plane to read.  
                Properties: create, edit
        frameDuration (Queryable[int]?): Query the frame duration of the movie's timecode format.  
                Properties: query
        height (Queryable[float]?): Height of the image plane. When creating, if this flag is not specified,  
                it will use 10.0 as default height.  
                Properties: create, query, edit
        imageSize (Queryable[Tuple[int, int]]?): Get size of the loaded image.  
                Properties: query
        lookThrough (Queryable[str]?): The camera currently used for image plane to look through.  
                Properties: create, query, edit
        maintainRatio (bool?): Let the image plane respect the picture aspect ratio. When creating,  
                if this flag is not specified, it will use true as default value.  
                Properties: create, query, edit
        name (Queryable[str]?): Set the image plane node name when creating or return the image plane name when querying.  
                Properties: create, query
        negTimesOK (bool?): Query the 'neg times OK' flag of the movie's timecode format.  
                Properties: query
        numFrames (Queryable[int]?): Query the whole number of frames per second of the movie's timecode format.  
                Properties: query
        quickTime (bool?): Query whether the image plane is using a QuickTime movie.  
                Properties: query
        showInAllViews (bool?): The flag is used to show the current image plane in all views or not.  
                Properties: create, query, edit
        timeCode (Queryable[int]?): Query the whole number of frames per second of the movie's timecode format.  
                Properties: query
        timeCodeTrack (bool?): Query whether the movie on the image plane has a timecode track.  
                Properties: query
        timeScale (Queryable[int]?): Query the timescale of the movie's timecode format.  
                Properties: query
        twentyFourHourMax (bool?): Query the '24 hour max' flag of the movie's timecode format.  
                Properties: query
        width (Queryable[float]?): Width of the image plane. When creating, if this flag is not specified,  
                it will use 10.0 as default width.  
                Properties: create, query, edit

    Returns:
        bool: Command result

    Example:
    """

