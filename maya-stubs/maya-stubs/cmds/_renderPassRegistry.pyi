from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderPassRegistry(*, channels: int = ..., isPassSupported: bool = ..., passID: str = ..., passName: bool = ..., renderer: str = ..., supportedChannelCounts: bool = ..., supportedDataTypes: bool = ..., supportedPassSemantics: bool = ..., supportedRenderPassNames: bool = ..., supportedRenderPasses: bool = ...) -> List[str]:
    """query information related with render passes.render, pass
    Args:
        channels (int?): Specify the number of channels for query.  
                Properties: create
        isPassSupported (bool?): Return whether the pass is supported by the renderer  
                This flag must be specified by the flag -passID firstly. The renderer whose default  
                value is the current renderer is specified by the flag renderer.  
                Properties: create
        passID (str?): Specify the render pass ID for query.  
                Properties: create
        passName (bool?): Get the pass name for the passID.  
                This flag must be specified by the flag -passID firstly.  
                Properties: create
        renderer (str?): Specify a renderer when using this command.  
                By default the current renderer is specified.  
                Properties: create
        supportedChannelCounts (bool?): List channel counts supported by the renderer(specified by the flag -renderer) and  
                the specified pass ID.  
                This flag must be specified by the flag -passID firstly.  
                Properties: create
        supportedDataTypes (bool?): List frame buffer types supported by the renderer(specified by the flag -renderer),  
                the specified passID and channels.  
                This flag must be specified by the flag -passID and -channels firstly.  
                Properties: create
        supportedPassSemantics (bool?): List pass semantics supported by the specified passID.  
                This flag must be specified by the flag -passId firstly.  
                Properties: create
        supportedRenderPassNames (bool?): List render pass names supported by the renderer(specified by the flag -renderer).  
                Properties: create
        supportedRenderPasses (bool?): List render passes supported by the renderer(specified by the flag -renderer).  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

