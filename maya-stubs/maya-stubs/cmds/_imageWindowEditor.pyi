from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def imageWindowEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., autoResize: bool = ..., changeCommand: Tuple[str, str, str, str] = ..., clear: Tuple[int, int, float, float, float] = ..., control: bool = ..., drawAxis: bool = ..., doubleBuffer: bool = ..., displayImage: int = ..., displayStyle: str = ..., defineTemplate: str = ..., docTag: str = ..., exists: bool = ..., filter: str = ..., frameImage: bool = ..., forceMainConnection: str = ..., frameRegion: bool = ..., highlightConnection: str = ..., lockMainConnection: bool = ..., loadImage: str = ..., mainListConnection: str = ..., marquee: Tuple[float, float, float, float] = ..., nbImages: bool = ..., parent: str = ..., panel: str = ..., removeAllImages: bool = ..., refresh: bool = ..., removeImage: bool = ..., realSize: bool = ..., scaleBlue: float = ..., singleBuffer: bool = ..., scaleGreen: float = ..., saveImage: bool = ..., selectionConnection: str = ..., scaleRed: float = ..., showRegion: Tuple[int, int] = ..., stateString: bool = ..., toggle: bool = ..., unlockMainConnection: bool = ..., unParent: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ..., writeImage: str = ...) -> None: ...
