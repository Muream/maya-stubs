from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def psdEditTextureFile(*args: Any, addChannel: Multiuse[str] = ..., addChannelColor: Multiuse[Tuple[str, float, float, float]] = ..., addChannelImage: Multiuse[Tuple[str, str]] = ..., deleteChannel: Multiuse[str] = ..., psdFileName: str = ..., snapShotImage: str = ..., uvSnapPostionTop: bool = ...) -> bool:
    """Edits the existing PSD file. Addition and deletion of the channels (layer sets) are
    supported.
    Args:
        addChannel (Multiuse[str]?): Adds an empty layer set with the given name to a already existing PSD file.  
                Properties: create, multiuse
        addChannelColor (Multiuse[Tuple[str, float, float, float]]?): (M) Specifies the filled color of  the layer which is created in a layer set given  
                by the layer name.  
                Properties: create, multiuse
        addChannelImage (Multiuse[Tuple[str, str]]?): (M) Specifies the image file name whose image needs to be added  
                as a layer to a given layer set which is the first string.  
                Properties: create, multiuse
        deleteChannel (Multiuse[str]?): (M) Deletes the channels (layer sets) from a PSD file. This is a multiuse  
                flag.  
                Properties: create, multiuse
        psdFileName (str?): PSD file name.  
                Properties: create
        snapShotImage (str?): Image file name on the disk containing UV snapshot / reference image.  
                Properties: create
        uvSnapPostionTop (bool?): Specifies the position of UV snapshot image layer  in the PSD file. "True"  
                positions this layer at the top and "False" positions the layer at the bottom  
                next to the background layer in the PSD file  
                Properties: create

    Returns:
        bool:

    Example:
    """

