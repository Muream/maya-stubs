from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def itemFilterRender(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., anyTextures: bool = ..., category: Multiuse[str] = ..., classification: str = ..., exists: bool = ..., exclusiveLights: bool = ..., lights: bool = ..., listBuiltInFilters: bool = ..., linkedLights: bool = ..., listOtherFilters: bool = ..., lightSets: bool = ..., listUserFilters: bool = ..., nodeClassification: Multiuse[str] = ..., negate: bool = ..., nonIlluminatingLights: bool = ..., nonExclusiveLights: bool = ..., parent: str = ..., postProcess: bool = ..., renderingNode: bool = ..., renderableObjectSets: bool = ..., renderUtilityNode: bool = ..., shaders: bool = ..., text: str = ..., textures2d: bool = ..., textures3d: bool = ..., texturesProcedural: bool = ...) -> None: ...
