from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ogsRender(*args: str, edit: bool = ..., query: bool = ..., activeMultisampleType: Queryable[str] = ..., activeRenderOverride: Queryable[str] = ..., activeRenderTargetFormat: Queryable[str] = ..., availableFloatingPointTargetFormat: bool = ..., availableMultisampleType: bool = ..., availableRenderOverrides: bool = ..., camera: Queryable[str] = ..., currentFrame: bool = ..., currentView: bool = ..., enableFloatingPointRenderTarget: bool = ..., enableMultisample: bool = ..., frame: float = ..., height: Queryable[int] = ..., layer: Queryable[str] = ..., noRenderView: bool = ..., width: Queryable[int] = ...) -> Union[bool, str, int]:
    """Renders an image or a sequence using the OGS rendering engineogs, offline, rendering
    Args:
        activeMultisampleType (Queryable[str]?): Query the current active multisample type.  
                Properties: query, edit
        activeRenderOverride (Queryable[str]?): Set or query the current active render override.  
                Properties: query, edit
        activeRenderTargetFormat (Queryable[str]?): Query the current active floating point target format.  
                Properties: query, edit
        availableFloatingPointTargetFormat (bool?): Returns the names of available floating point render target format.  
                Properties: query
        availableMultisampleType (bool?): Returns the names of available multisample type.  
                Properties: query
        availableRenderOverrides (bool?): Returns the names of available render overrides.  
                Properties: query
        camera (Queryable[str]?): Specify the camera to use.  Use the first available camera if the camera  
                given is not found.  
                Properties: create, query, edit
        currentFrame (bool?): Render the current frame.  
                Properties: create, query, edit
        currentView (bool?): When turned on, only the current view will be rendered.  
                Properties: create, query, edit
        enableFloatingPointRenderTarget (bool?): Enable/disable floating point render target.  
                Properties: query, edit
        enableMultisample (bool?): Enable/disable multisample.  
                Properties: query, edit
        frame (float?): Specify the frame to render.  
                Properties: create, edit
        height (Queryable[int]?): The height flag pass the height to the ogsRender command. If not used,  
                the height is taken from the render globals settings.  
                Properties: create, query, edit
        layer (Queryable[str]?): Render the specified legacy render layer.  
                Only this render layer will be rendered,  
                regardless of the renderable attribute value of the render layer.  
                The layer name will be appended to the output image file name.  
                The specified render layer becomes the current render layer before rendering,  
                and remains as current render layer after the rendering.  
                This argument uses legacy render layers as this command does not recognize the newer  
                renderSetup render layer system introduced in Maya 2016.  
                Properties: create, query, edit
        noRenderView (bool?): When turned on, the render view is not updated after image computation  
                Properties: create, query, edit
        width (Queryable[int]?): The width flag pass the width to the ogsRender command. If not used,  
                the width is taken from the render globals settings.  
                Properties: create, query, edit

    Returns:
        bool: Query result

    Example:
    """

