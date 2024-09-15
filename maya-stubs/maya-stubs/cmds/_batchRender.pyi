from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def batchRender(arg0: str = ..., arg1: str = ..., arg2: str = ..., arg3: str = ..., arg4: str = ..., /, *, filename: str = ..., melCommand: str = ..., numProcs: int = ..., preRenderCommand: str = ..., remoteRenderMachine: str = ..., renderCommandOptions: str = ..., showImage: bool = ..., status: str = ..., useRemoteRender: bool = ..., useStandalone: bool = ..., verbosity: int = ...) -> bool:
    """The batchRender command is used to spawn off a separate
    rendering session of the current maya file. If no
    mayaFile is specified, it'll ask you whether you want the
    current job killed.The batchRender will spawn a separate maya process in which
    commands will be communicated to it through a commandPort. If Maya
    is unable to find an available port an error will be
    produced. Maya will attempt to use ports 7835 through 7844.
    Args:
        filename (str?): Filename to be rendered; if empty, a temporary filename will be created.  
                Properties: create
        melCommand (str?): Mel command to execute to run a renderer other than the software renderer.  
                Properties: create
        numProcs (int?): Number of processors to use (0 means use all available processors).  
                Properties: create
        preRenderCommand (str?): Command to be run prior to invoking a batch render.  
                Properties: create
        remoteRenderMachine (str?): Name of remote render machine. Not available on Windows.  
                Properties: create
        renderCommandOptions (str?): Arguments to the render command for batch rendering.  
                Properties: create
        showImage (bool?): Show progress of the current rendering job.  
                Properties: create
        status (str?): Status string for displaying the batch render status.  
                Properties: create
        useRemoteRender (bool?): If remote rendering is desired. Not available on Windows.  
                Properties: create
        useStandalone (bool?): Batch rendering is to be done by exporting the scene and rendering with a standalone renderer.  
                Properties: create
        verbosity (int?): Defines the verbosity level to report the batch rendering  
                status:  
                1. display only one start message, then one message when all  
                frames are rendered.  
                2. display only start and end frame messages.  
                3. display all messages (default).  
                Properties: create

    Returns:
        bool:

    Example:
    """

