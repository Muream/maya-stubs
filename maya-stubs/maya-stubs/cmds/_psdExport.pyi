from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def psdExport(*args: Any, query: bool = ..., alphaChannelIdx: Queryable[int] = ..., bytesPerChannel: Queryable[int] = ..., emptyLayerSet: bool = ..., format: Queryable[str] = ..., layerName: Queryable[str] = ..., layerSetName: str = ..., outFileName: Queryable[str] = ..., preMultiplyAlpha: bool = ..., psdFileName: str = ...) -> Union[bool, int, str]:
    """Writes the Photoshop file layer set into different formats.  The output
            file depth (bit per channel ) can be different from that of the input.
            If the input is 16 bpc and output is 8 bpc, there will be data loss.photoshop, psd, texture, convert, export
    Args:
        alphaChannelIdx (Queryable[int]?): Index of the alpha channel to output, if not supplied, writes out the  
                default alpha channel.  The index is zero based.  
                This is useful to write out specific alpha channels available as  
                "Additional Alpha Channels" of Photoshop.  
                Properties: create, query
        bytesPerChannel (Queryable[int]?): Output file depth. Any of these keyword:  
              
                0 for choosing depth based on input  
                1 for 8 bits per channel  
                2 for 16 bits per channel  
              
                Default is 0.  
                Properties: create, query
        emptyLayerSet (bool?): Option to check if the given layer set is empty or not.  This should be  
                used in query mode and input file name and layer set names should be specified.  
                Properties: create, query
        format (Queryable[str]?): Output file format. Any of these keyword: "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg"  
                Default is iff.  
                Properties: create, query
        layerName (Queryable[str]?): Name of the layer to output.  
                Properties: create, query
        layerSetName (str?): Name of the layer set to output, if not supplied, writes out the Composite image.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        outFileName (Queryable[str]?): Name(with path) of the output file.  
                Properties: create, query
        preMultiplyAlpha (bool?): Option to multiply RGB colors with alpha values.  If (r,g,b,a) is the  
                value of pixel, it will be changed to (r*a, g*a, b*a, a) when this flag  
                is used.  
                Properties: create, query
        psdFileName (str?): Name(with path) of the input Photoshop file.  
                			In query mode, this flag needs a value.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

