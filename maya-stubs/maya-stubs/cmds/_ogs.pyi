from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ogs(*, query: bool = ..., deviceInformation: bool = ..., disposeReleasableTextures: bool = ..., dumpTexture: str = ..., enableHardwareInstancing: bool = ..., fragmentEditor: str = ..., fragmentXML: str = ..., gpuMemoryTotal: Queryable[int] = ..., gpuMemoryUsed: bool = ..., isLegacyViewportEnabled: bool = ..., isRemoteGLSessionEnabled: bool = ..., isWinRemoteSession: bool = ..., pause: bool = ..., rebakeTextures: bool = ..., regenerateUVTilePreview: str = ..., reloadTextures: bool = ..., reset: bool = ..., shaderSource: Queryable[str] = ..., toggleTexturePaging: bool = ..., traceRenderPipeline: bool = ...) -> Union[str, int, bool]:
    """OGS is one of the viewport renderers. As there is a lot of effort involved
    in migrating functionality it will evolve over several releases. As it
    evolves it is prudent to provide safeguards to get the database back to a
    known state. That is the function of this command, similar to how
    'dgdirty' is used to restore state to the dependency graph.ogs, debug
    Args:
        deviceInformation (bool?): If used then output the current device information.  
                Properties: create
        disposeReleasableTextures (bool?): Clear up all the releasable file textures in GPU memory that are not required for rendering.  
                Properties: create
        dumpTexture (str?): If used then dump GPU texture memory usage info (in MB), must be used with FLAG gpuMemoryUsed.  
                The final info detail is specified by the string parameter. Current available values are: "full" , "total".  
                Properties: create
        enableHardwareInstancing (bool?): Enables/disables new gpu instancing of instanceable render items in OGS.  
                Properties: create
        fragmentEditor (str?): If used then launch the fragment editor UI.  
                Properties: create
        fragmentXML (str?): Get the fragment XML associated with a shading node.  
                Properties: create
        gpuMemoryTotal (Queryable[int]?): Get or set the total amount of GPU memory which Maya is allowed to use (in MB).  
                Properties: create, query
        gpuMemoryUsed (bool?): If used then output the estimated amount of GPU memory in use (in MB).  
                Properties: create
        isLegacyViewportEnabled (bool?): To query if the legacy viewport is enabled.  
                Properties: query
        isRemoteGLSessionEnabled (bool?): Query if remote gl is allowed  
                Properties: query
        isWinRemoteSession (bool?): Query if this is a remote session.  
                Properties: query
        pause (bool?): Toggle pausing VP2 display update  
                Properties: create, query
        rebakeTextures (bool?): If used then re-bake all baked textures for OGS.  
                Properties: create
        regenerateUVTilePreview (str?): If used then regenerate all UV tiles preview textures for OGS.  
                Properties: create
        reloadTextures (bool?): If used then reload all textures for OGS.  
                Properties: create
        reset (bool?): If used then reset the entire OGS database for all viewports using it.  
                In query mode the number of viewports that would be affected is returned  
                but the reset is not actually done.  If no viewport is using OGS then  
                OGS will stop listening to DG changes.  
                Properties: create, query
        shaderSource (Queryable[str]?): Get the shader source for the specified material.  
                Properties: query
        toggleTexturePaging (bool?): If used then toggle the default OGS Texture paging mechanism.  
                Properties: create
        traceRenderPipeline (bool?): Enable debug tracing of the renderer pipeline.  
                Properties: create

    Returns:
        str: Result of the operation

    Example:
    """

