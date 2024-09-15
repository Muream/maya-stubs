from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cameraView(arg0: str = ..., /, *, edit: bool = ..., addBookmark: bool = ..., animate: bool = ..., bookmarkType: int = ..., camera: str = ..., name: str = ..., removeBookmark: bool = ..., setCamera: bool = ..., setView: bool = ...) -> str:
    """This command creates a preset view for a camera which is then
    independent of the camera. The view stores a camera's eye point,
    center of interest point, up vector, tumble pivot, horizontal
    aperture, vertical aperature, focal length, orthographic width,
    and whether the camera is orthographic or perspective by default.
    Or you can only store 2D pan/zoom attributes by setting the
    bookmarkType to 1. These settings can be applied to any other
    camera through the set camera flag.This command can be used for creation or edit of camera view
    objects.  This command can only be executed with one of the add
    bookmark, or remove bookmark and one of set camera, or the set
    view flags set.
    Args:
        addBookmark (bool?): Associate this view with the camera specified or the camera in  
                the active model panel. This flag can be used for creation or  
                edit.  
                Properties: create, edit
        animate (bool?): Set the animation capability for view switches.  
                Properties: create, edit
        bookmarkType (int?): Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D  
                Pan/Zoom bookmark.  
                Properties: create
        camera (str?): Specify the camera to use. This flag should be used in  
                conjunction with the add bookmark, remove bookmark, set  
                camera, or set view flags. If this flag is not specified the  
                camera in the active model panel will be used.  
                Properties: edit
        name (str?): Set the name of the view. This flag can only be used for  
                creation.  
                Properties: create
        removeBookmark (bool?): Remove the association of this view with the camera specified  
                or the camera in the active model panel. This can only be used  
                with edit.  
                Properties: edit
        setCamera (bool?): Set this view into a camera specified by the camera flag or the  
                camera in the active model panel. This flag can only be used  
                with edit.  
                Properties: edit
        setView (bool?): Set the camera view to match a camera specified or the active  
                model panel. This flag can only be used with edit.  
                Properties: edit

    Returns:
        str: (name of the camera view)

    Example:
    """

