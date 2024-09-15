from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def launchImageEditor(*, editImageFile: str = ..., viewImageFile: str = ...) -> bool:
    """Launch the appropriate application to edit/view the image files specified.
    This command works only on the Macintosh and Windows platforms.
    Args:
        editImageFile (str?): If the file is a PSD, then the specified verison of Photoshop is launched,  
                and the file is opened in it. If file is any other image type,  
                then the preferred image editor is launched, and the file is opened in it.  
                Properties: create
        viewImageFile (str?): Opens up an Image editor to view images.  
                Properties: create

    Returns:
        bool:

    Example:
    """

