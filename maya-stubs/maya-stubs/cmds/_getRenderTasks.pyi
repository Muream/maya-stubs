from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getRenderTasks(arg0: str = ..., /, *, camera: str = ..., renderLayer: str = ...) -> List[str]:
    """Command to return render tasks to render an image source.  Image
    source can depend on upstream image sources that result from
    renderings of 3D scene, or 2D renderings (e.g. render targets).
    This command obtains the graph of image source render dependencies,
    and creates render tasks according to these dependencies.  A render
    task has context, which can be camera, render layer, and resolution,
    or other, renderer-specific context.  Because of image source
    overrides, the render task context depends on the path through the
    render dependency graph, with the most upstream override for a context
    item applied.  As there can be multiple paths through a render
    dependency graph to a render dependency, there can be multiple render
    tasks for a given render dependency.imageSource, render, task
    Args:
        camera (str?): Camera node to use in the render context for the image source render task.  
                Properties: create
        renderLayer (str?): Render layer to use in the render context for the image source render task.  
                Properties: create

    Returns:
        List[str]: Render tasks (one per string) for argument render target.

    Example:
    """

