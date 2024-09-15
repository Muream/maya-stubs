from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def launch(*, directory: str = ..., movie: str = ..., pdfFile: str = ..., webPage: str = ...) -> bool:
    """Launch the appropriate application to open the document, web page or directory
    specified.
    Args:
        directory (str?): A directory.  
                Properties: create
        movie (str?): A movie file. The only acceptable movie file formats are MPEG,  
                Quicktime, and Windows Media file. The file's name must end  
                with .mpg, .mpeg, .mp4, .wmv, .mov, or .qt.  
                Properties: create
        pdfFile (str?): A PDF (Portable Document Format) document. The file's name must  
                end with .pdf.  
                Properties: create
        webPage (str?): A web page.  
                Properties: create

    Returns:
        bool:

    Example:
    """

