from __future__ import annotations

from typing import *

Unknown = Any

def createMelWrapper(
    fn: Unknown,
    types: List[Any] = [],
    retType: str = "void",
    ignoreDefaultArgs: bool = True,
    returnCmd: bool = False,
    outDir: Unknown = None,
) -> Any: ...
def eval(*args: Unknown, **kwargs: Unknown) -> Any: ...
