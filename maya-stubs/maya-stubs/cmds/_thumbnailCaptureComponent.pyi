from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def thumbnailCaptureComponent(*, query: bool = ..., capture: bool = ..., capturedFrameCount: bool = ..., closeCurrentSession: bool = ..., delete: bool = ..., endFrame: Queryable[int] = ..., fileDialogCallback: str = ..., isSessionOpened: bool = ..., launchedFromOptionsBox: bool = ..., previewPath: bool = ..., removeProjectThumbnail: str = ..., save: str = ..., startFrame: Queryable[int] = ...) -> Union[bool, int]:
    """This command is used to generate a thumbnail/playblast sequence from the scene.
    Args:
        capture (bool?): Create a new component to capture a sequence of image for the current scene.  
                Properties: create
        capturedFrameCount (bool?): Query only. Return the number of frames that have been captured.  
                Properties: query
        closeCurrentSession (bool?): Delete the current thumbnail component (preview image will be destroyed).  
                Properties: create
        delete (bool?): Delete the generated image sequence and preview for the current capture session.  
                Properties: create
        endFrame (Queryable[int]?): Set the end captured frame. Only valid when the -c/capture flag is set.  
                If -sf/startFrame is set and not -ef/endFrame, or if endFrame is smaller than startFrame, endFrame will be automatically set to startFrame.  
                Properties: create, query
        fileDialogCallback (str?): MEL only. Set the callback file dialog which is called after the capture component window has been closed. Only valid when the -c/capture flag is set.  
                Properties: create
        isSessionOpened (bool?): Returns true if a thumbnail/playblast capture session is currently running (already opened and still not cancelled/saved).  
                Properties: query
        launchedFromOptionsBox (bool?): Returns true if the thumbnail capture component was launched through the options dialog box, else false.  
                Properties: query
        previewPath (bool?): Returns the generated preview path (the first frame of generated sequence resized to 100x100 px).  
                Properties: query
        removeProjectThumbnail (str?): Remove all captured thumbnail/playblast from the given project file path.  
                Properties: create
        save (str?): Save the generated image sequence for the given file to disk. The file path must be an absolute path.  
                Properties: create
        startFrame (Queryable[int]?): Set the start captured frame. Only valid when -c/capture flag is set.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

